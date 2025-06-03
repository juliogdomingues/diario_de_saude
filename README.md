# Diário de Saúde

## 1. Membros do Grupo
- Fernanda Vieira Pagano
- Júlio Guerra Domingues 
- Marcos Felipe Cavalieri

## 2. Sobre o Sistema

O **Diário de Saúde** é um sistema web simples para registro de sintomas e tratamentos. O usuário pode cadastrar sintomas informando nome, descrição, data e horário, além de cadastrar tratamentos realizados. Na página inicial, o sistema exibe um calendário agrupando os sintomas registrados por dia, facilitando o acompanhamento da saúde ao longo do tempo.

## 3. Tecnologias Utilizadas

- Python 3.x
- Django 4.x
- Pytest, Coverage.py
- GitHub Actions para CI/CD

## 4. Como rodar o sistema

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

4. Acesse o sistema em http://127.0.0.1:8000/

5. Para rodar os testes:
    ```sh
    pytest
    ```

6. Para medir a cobertura de testes:
   ```sh
    coverage run -m pytest
    coverage report
    ```
