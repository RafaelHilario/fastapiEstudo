# Gerenciador de Usuários com FastAPI

Este é um projeto simples de gerenciamento de usuários utilizando FastAPI, onde os dados são armazenados em um arquivo JSON.

## Tecnologias Utilizadas
- Python 3
- FastAPI
- Pydantic

## Instalação e Execução
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Crie e ative um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```
3. Instale as dependências:
   ```bash
   pip install fastapi pydantic uvicorn
   ```
4. Execute o servidor:
   ```bash
   uvicorn main:app --reload
   ```
5. Acesse a documentação interativa:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Endpoints Disponíveis

### Criar um usuário
- **Rota:** `POST /usuarios/`
- **Corpo da requisição:**
  ```json
  {
    "email": "usuario@email.com",
    "senha": "123456",
    "nome": "Usuário Teste"
  }
  ```
- **Resposta:**
  ```json
  {
    "mensagem": "Usuário criado com sucesso.",
    "usuario": {
      "email": "usuario@email.com",
      "senha": "123456",
      "nome": "Usuário Teste"
    }
  }
  ```

### Obter um usuário pelo email e senha
- **Rota:** `GET /usuarios/`
- **Parâmetros:** `email`, `senha`
- **Exemplo:** `GET /usuarios/?email=usuario@email.com&senha=123456`
- **Resposta:**
  ```json
  {
    "mensagem": "Usuário encontrado",
    "usuario": {
      "email": "usuario@email.com",
      "senha": "123456",
      "nome": "Usuário Teste"
    }
  }
  ```

### Obter um usuário pelo email
- **Rota:** `GET /usuariosComemail/`
- **Parâmetro:** `email`
- **Exemplo:** `GET /usuariosComemail/?email=usuario@email.com`

### Obter um usuário pelo nome
- **Rota:** `GET /usuariosComnome/`
- **Parâmetro:** `nome`
- **Exemplo:** `GET /usuariosComnome/?nome=Usuário Teste`

### Deletar um usuário
- **Rota:** `DELETE /usuarios/`
- **Parâmetro:** `email`
- **Exemplo:** `DELETE /usuarios/?email=usuario@email.com`
- **Resposta:**
  ```json
  {
    "mensagem": "Usuário deletado com sucesso."
  }
  ```

## Autor
Desenvolvido por Rafael Hilário.

## Licença
Este projeto está sob a licença MIT. Sinta-se à vontade para utilizar e modificar conforme necessário.

