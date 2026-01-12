from fastapi import APIRouter, Depends, HTTPException
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from dependencies import pegar_sessao
from models import Usuario
from main import bcrypt_context

auth_router = APIRouter(prefix="/auth", tags=["auth"])



def criar_token(id_usuario):
    token = f"A65FGUfy5r5ytf7i7edf3w2{id_usuario}"
    return token

def autenticar_usuario(email, senha, session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()

    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario



@auth_router.post("/criar_usuario")
async def criar_usuario(usuario_schema : UsuarioSchema, session : Session = Depends(pegar_sessao)):
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code = 400, detail="Ja existe um usuario com este email")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return{"mensagem": f"Usuario criado com sucesso: {usuario_schema.email}"}
    

@auth_router.post("/login")
async def login(login_schema : LoginSchema, session : Session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=400, detail="Usuario nao encontrado ou senha incorreta")
    else:
        access_token = criar_token(usuario.id)
        return{
            "access_token": access_token,
            "token_type": "Bearer"
        }
