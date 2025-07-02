from django.test import TestCase, Client
from django.urls import reverse
from diario.models import Sintoma, Tratamento
from datetime import date, time, timedelta

class SystemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.sintoma = Sintoma.objects.create(
            nome="Dor de cabeça",
            descricao="leve",
            data=date.today(),
            horario=time(10, 0)
        )
        self.tratamento = Tratamento.objects.create(
            nome="Dipirona",
            descricao="500mg",
            data_inicio=date.today(),
            data_fim=date.today()
        )

    def test_homepage_mostra_informacoes(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dor de cabeça")
        self.assertContains(response, "Dipirona")

    def test_criar_sintoma(self):
        response = self.client.post(reverse('sintoma_create'), {
            'nome': 'Febre',
            'descricao': 'alta',
            'data': date.today(),
            'horario': '15:00',
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Febre')
        self.assertTrue(Sintoma.objects.filter(nome="Febre").exists())

    def test_criar_tratamento(self):
        response = self.client.post(reverse('tratamento_create'), {
            'nome': 'Ibuprofeno',
            'descricao': '200mg',
            'data_inicio': date.today(),
            'data_fim': date.today(),
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Ibuprofeno')
        self.assertTrue(Tratamento.objects.filter(nome="Ibuprofeno").exists())

    def test_editar_nome_sintoma(self):
        response = self.client.post(reverse('sintoma_edit', args=[self.sintoma.pk]), {
            'nome': 'Dor intensa',
            'descricao': self.sintoma.descricao,
            'data': self.sintoma.data,
            'horario': self.sintoma.horario,
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Dor intensa')
        self.assertFalse(Sintoma.objects.filter(nome='Dor de cabeça').exists())

    def test_deletar_tratamento(self):
        response = self.client.post(reverse('tratamento_delete', args=[self.tratamento.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(Tratamento.objects.filter(pk=self.tratamento.pk).exists())

    def test_retorna_lista_sintomas(self):
        response = self.client.get(reverse('sintomas_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.sintoma.nome)

    def test_retorna_lista_tratamentos(self):
        response = self.client.get(reverse('tratamentos_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.tratamento.nome)

    def test_tratamento_data_invalida(self):
        response = self.client.post(reverse('tratamento_create'), {
            'nome': 'Test Fail',
            'descricao': 'bad date',
            'data_inicio': date.today(),
            'data_fim': date.today() - timedelta(days=1),
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIn('data_fim', form.errors)
        self.assertIn('A data final não pode ser anterior à data inicial.', form.errors['data_fim'])


    def test_criar_sintoma_sem_nome(self):
        response = self.client.post(reverse('sintoma_create'), {
            'nome': '',
            'descricao': 'descrição',
            'data': date.today(),
            'horario': '12:00',
        })
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIn('nome', form.errors)
        self.assertIn('Este campo é obrigatório.', form.errors['nome'])


    def test_sintoma_form_valores_padrao(self):
        response = self.client.get(reverse('sintoma_create'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'type="date"')
        self.assertContains(response, 'type="time"')
