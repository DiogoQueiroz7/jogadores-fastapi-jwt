# jogadores-fastapi-jwt

Atividade da matéria do professor Rogério, onde fiz uma API usando FastAPI para cadastrar jogadores do Palmeiras.

Os jogadores ficam salvos no SQLite. Qualquer pessoa pode consultar o elenco. Para cadastrar, editar ou excluir um jogador, precisa fazer login.

## Integrantes

- Diogo Queiroz

## Como rodar

Precisa ter Python instalado.

Abra o terminal na pasta onde quer baixar o projeto e execute os passos:

1. Clonar: git clone https://github.com/DiogoQueiroz7/jogadores-fastapi-jwt.git

2. Entrar na pasta: cd jogadores-fastapi-jwt

3. Criar o ambiente virtual: python -m venv .venv

4. Ativar no Windows PowerShell: `.\.venv\Scripts\Activate.ps1`
   - Linux/Mac: `source .venv/bin/activate`

5. Instalar as dependências: python -m pip install -r requirements.txt

6. Criar as tabelas: alembic upgrade head

7. Criar um usuário: python criar_usuario.py

8. Gerar a chave do JWT no Windows PowerShell: $env:CHAVE_JWT = python -c "import secrets; print(secrets.token_hex(32))"
   - Linux/Mac: export CHAVE_JWT=$(python -c "import secrets; print(secrets.token_hex(32))")

9. Rodar a API no mesmo terminal: fastapi dev main.py

## Como testar o login

Acesse http://127.0.0.1:8000/docs para testar pelo Swagger.

Primeiro, teste o GET /jogadores/. se o banco estiver vazio, ele retorna uma lista vazia. se tentar cadastrar um jogador pelo POST /jogadores/ sem fazer login, a API retorna 401

Clique em Authorize e coloque o email que cadastrou no campo username. digite a senha no campo password, clique em Authorize e depois em close

Tente cadastrar o jogador de novo. agora a API deve retornar 200 com os dados do jogador

## Rotas

- GET /jogadores/ - Lista os jogadores.
- GET /jogadores/{jogador_id} - Busca pelo ID.
- POST /jogadores/ - Cadastra um jogador.
- PUT /jogadores/{jogador_id} - Edita um jogador.
- DELETE /jogadores/{jogador_id} - Exclui um jogador.
- POST /token - Faz o login e retorna o token JWT.

Também dá pra filtrar pela posição: /jogadores/?posicao=goleiro