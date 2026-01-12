from fastapi import APIRouter, Depends
from models import Pedido
from schemas import PedidoSchema
from sqlalchemy.orm import Session
from dependencies import pegar_sessao

order_router = APIRouter(prefix="/order", tags=["order"])

@order_router.post("/pedido")
async def pedido(pedido_schema : PedidoSchema, session : Session = Depends(pegar_sessao)):
    novo_pedido = Pedido(pedido_schema.usuario)
    session.add(novo_pedido)
    session.commit()
    return{"mensagem": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}