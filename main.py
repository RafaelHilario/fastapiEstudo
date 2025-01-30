from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
import json
import os

app = FastAPI()

USERS_FILE = "usuarios.json"

# Modelo de dados para o usuário
class Usuario(BaseModel):
    email: EmailStr
    senha: str
    nome: str

def carregar_usuarios():
    if not os.path.exists(USERS_FILE):
        # Cria o arquivo com uma lista vazia se não existir
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []
    
    # Tenta carregar os usuários
    try:
        with open(USERS_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        with open(USERS_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, ensure_ascii=False, indent=4)
        return []

def salvar_usuarios(usuarios):
    with open(USERS_FILE, "w", encoding="utf-8") as file:
        json.dump(usuarios, file, ensure_ascii=False, indent=4)

@app.get("/usuarios/")
def obter_usuario(email: EmailStr, senha: str):
    usuarios = carregar_usuarios() # Carrega os usuários
    for usuario in usuarios:
        if usuario["email"] == email and usuario["senha"] == senha:
            return {"mensagem": "Usuário encontrado", "usuario": usuario}
    raise HTTPException(status_code=404, detail="Usuário não encontrado ou credenciais inválidas.")

@app.post("/usuarios/")
def criar_usuario(usuario: Usuario):
    usuarios = carregar_usuarios()
    for u in usuarios:
        if u["email"] == usuario.email:
            raise HTTPException(status_code=400, detail="Email já cadastrado.")
    usuarios.append(usuario.dict())
    salvar_usuarios(usuarios) # Salva os usuários
    return {"mensagem": "Usuário criado com sucesso.", "usuario": usuario}

# Rota para deletar um usuário por email
@app.delete("/usuarios/")
def deletar_usuario(email: EmailStr):
    usuarios = carregar_usuarios()
    usuarios_filtrados = [u for u in usuarios if u["email"] != email]
    if len(usuarios) == len(usuarios_filtrados):
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    salvar_usuarios(usuarios_filtrados)
    return {"mensagem": "Usuário deletado com sucesso."}


@app.get("/usuariosComemail/")
def usuarioEmail(email: EmailStr):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["email"] == email:
            return {"mensagem": "Usuário encontrado", "usuario": usuario}
    raise HTTPException(status_code=404, detail="Usuário não encontrado ou credenciais inválidas.")

@app.get("/usuariosComnome/")
def usuarioNome(nome: str):
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario["nome"] == nome:
            return {"mensagem": "Usuário encontrado", "usuario": usuario}
    raise HTTPException(status_code=404, detail="Usuário não encontrado ou credenciais inválidas.")