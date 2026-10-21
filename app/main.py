from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Field, Session
import random
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from sqlmodel import select
import string

# Importa as configurações do banco que você acabou de criar
from app.database import engine, criar_banco_e_tabelas, obter_sessao


# 1. Definir a Tabela no Banco de Dados
class Link(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    url_original: str
    codigo: str = Field(unique=True, index=True)


# 2. Modelo de entrada (o que o usuário envia via Postman)
class LinkRequisicao(SQLModel):
    url_original: str


app = FastAPI()


# 3. Criar o banco de dados assim que a API ligar
@app.on_event("startup")
def ao_iniciar():
    criar_banco_e_tabelas()


@app.get("/")
def read_root():
    return {"mensagem": "API do Encurtador de Links rodando!"}


@app.post("/encurtar")
def criar_link_curto(link_req: LinkRequisicao, sessao: Session = Depends(obter_sessao)):
    # Gera o código aleatório
    caracteres = string.ascii_letters + string.digits
    codigo_aleatorio = "".join(random.choices(caracteres, k=6))

    # 4. Prepara o novo registro com os dados
    novo_link = Link(url_original=link_req.url_original, codigo=codigo_aleatorio)

    # 5. Salva de fato no banco de dados
    sessao.add(novo_link)
    sessao.commit()
    sessao.refresh(novo_link)  # Atualiza a variável com os dados gerados pelo banco (como o ID)

    return {
        "id_no_banco": novo_link.id,
        "url_original": novo_link.url_original,
        "url_curta": f"http://127.0.0.1:8000/{novo_link.codigo}",
        "codigo": novo_link.codigo
    }


@app.get("/{codigo}")
def redirecionar(codigo: str, sessao: Session = Depends(obter_sessao)):
    # 1. Cria a instrução para buscar o código no banco
    busca = select(Link).where(Link.codigo == codigo)
    link_encontrado = sessao.exec(busca).first()

    # 2. Se o código não existir, devolve um erro 404
    if not link_encontrado:
        raise HTTPException(status_code=404, detail="Link curto não encontrado")

    # 3. Se existir, redireciona o navegador para o site original
    return RedirectResponse(url=link_encontrado.url_original)