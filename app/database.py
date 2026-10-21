from sqlmodel import SQLModel, create_engine, Session

# Define que o banco será um arquivo local chamado banco_dados.db
sqlite_url = "sqlite:///banco_dados.db"

# O engine é o motor que vai executar as ações no banco
engine = create_engine(sqlite_url, echo=True)

def criar_banco_e_tabelas():
    SQLModel.metadata.create_all(engine)

def obter_sessao():
    with Session(engine) as session:
        yield session