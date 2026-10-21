from fastapi.testclient import TestClient
from app.main import app

# Cria o nosso "Postman virtual"
client = TestClient(app)

def test_ct01_gerar_link_curto_com_sucesso():
    # Configuração do Payload (o pacote JSON que vai no Body)
    payload = {"url_original": "https://www.google.com"}

    # Simula o clique no botão "Send" do Postman usando o método POST
    resposta = client.post("/encurtar", json=payload)

    # --- VALIDAÇÕES DO QA (O que seria conferido com os olhos, agora é automático) ---

    # 1. Verifica se o Status é 200 OK
    assert resposta.status_code == 200

    # Extrai a resposta da API
    dados = resposta.json()

    # 2. Verifica se a API devolveu as informações corretas
    assert "id_no_banco" in dados
    assert "codigo" in dados
    assert dados["url_original"] == "https://www.google.com"

def test_ct02_bloquear_requisicao_com_formato_incorreto():
        # Payload com o nome do campo errado de propósito
        payload = {"site_errado": "https://www.google.com"}

        resposta = client.post("/encurtar", json=payload)

        # 1. Garante que a API barrou a requisição (Erro 422)
        assert resposta.status_code == 422

        # 2. Garante que o detalhe do erro aponta exatamente a falta do campo "url_original"
        dados = resposta.json()
        assert dados["detail"][0]["loc"] == ["body", "url_original"]

def test_ct03_redirecionamento_de_codigo_inexistente():
        # Tenta fazer um GET para uma rota que não existe no banco
        resposta = client.get("/codigoFalso123")

        # 1. Garante que o sistema tratou a exceção e devolveu 404 Not Found
        assert resposta.status_code == 404

        # 2. Garante que a mensagem amigável que escrevemos está correta
        assert resposta.json() == {"detail": "Link curto não encontrado"}