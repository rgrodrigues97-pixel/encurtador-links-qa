import httpx


def test_ct04_redirecionamento_no_navegador(page):
    # 1. Simula o Postman criando um link curto válido
    resposta = httpx.post(
        "http://127.0.0.1:8000/encurtar",
        json={"url_original": "https://pt.wikipedia.org"}
    )
    url_curta = resposta.json()["url_curta"]

    # 2. O robô do Playwright assume o controle e acessa a URL curta
    page.goto(url_curta)

    # 3. Validação: Garante que a página final carregada é a da Wikipedia
    assert "wikipedia.org" in page.url