# Início Academia

Projeto inicial de gerenciamento de academia, desenvolvido com Django.

## Requisitos

- Python 3.12 ou superior
- pip

## Configuração no Windows (PowerShell)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Abra http://127.0.0.1:8000/ no navegador.

Para criar uma conta de administração:

```powershell
python manage.py createsuperuser
```

O painel administrativo fica em http://127.0.0.1:8000/admin/.

## Variáveis de ambiente

`DJANGO_SECRET_KEY`, `DJANGO_DEBUG` e `DJANGO_ALLOWED_HOSTS` podem ser definidos
no ambiente. Sem `DJANGO_SECRET_KEY`, o projeto usa uma chave apenas para
desenvolvimento local; em produção, a aplicação exige uma chave forte e
exclusiva. Em produção, defina `DJANGO_DEBUG=False` e informe os hosts permitidos
em `DJANGO_ALLOWED_HOSTS`, separados por vírgula.

## Estrutura inicial

- `config/`: configurações, URLs e pontos de entrada WSGI/ASGI.
- `core/`: app inicial da aplicação, com a página de boas-vindas.
- `db.sqlite3`: banco SQLite local, criado ao executar as migrações (não versionado).

## Testes

```powershell
python manage.py test
```
