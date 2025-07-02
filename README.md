# Diário de Saúde

## 1. Membros do Grupo

- Fernanda Vieira Pagano
- Júlio Guerra Domingues
- Marcos Felipe Cavalieri

## 2. Sobre o Sistema

O **Diário de Saúde** é um sistema web para registro e acompanhamento de sintomas e tratamentos de saúde.  
O usuário pode cadastrar sintomas informando nome, descrição, data e horário, além de cadastrar tratamentos realizados com nome, descrição, data de início e fim.  
Na página inicial, o sistema exibe os sintomas e tratamentos mais recentes, facilitando o acompanhamento da saúde ao longo do tempo.  
O sistema possui interface simples, navegação intuitiva e validações para garantir a consistência dos dados.

### Funcionalidades

- Cadastro, edição e remoção de sintomas
- Cadastro, edição e remoção de tratamentos
- Listagem de sintomas e tratamentos
- Página inicial com sintomas e tratamentos recentes

## 3. Tecnologias Utilizadas

- **Python 3.x**
- **Django 4.x**
- **Pytest** para testes automatizados
- **Coverage.py** para análise de cobertura de código (inclusive cobertura de branches)
- **GitHub Actions** para integração contínua (CI/CD)

---

### Como rodar o sistema

1. Instale as dependências:

   ```sh
   pip install -r requirements.txt
   ```

2. Aplique as migrações do banco de dados:

   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Inicie o servidor de desenvolvimento:

   ```sh
   python manage.py runserver
   ```

4. Acesse o sistema em [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

### Como rodar os testes

```sh
pytest
```

### Como medir a cobertura de testes

Cobertura padrão:

```sh
coverage run --source=diario,DiarioDeSaude -m pytest
coverage report -m
```

Cobertura de branches:

```sh
coverage run --branch --source=diario,DiarioDeSaude -m pytest
coverage report -m
```

Para relatório visual:

```sh
coverage html
# Abra o arquivo htmlcov/index.html no navegador
```
