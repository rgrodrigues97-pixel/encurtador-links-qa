import httpx
import os


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

def test_ct05_encurtar_link_pela_interface(page):
        # 1. Encontra o caminho exato do index.html no seu computador
        caminho_html = f"file://{os.path.abspath('index.html')}"

        # 2. O robô abre a página
        page.goto(caminho_html)

        # 3. Digita a URL no campo de texto (usando o ID da caixa)
        page.fill("#link-original", "https://github.com/rgrodrigues97-pixel")

        # 4. Clica no botão "Encurtar"
        page.click("button")

        # 5. Espera a API responder e o link azul (<a>) aparecer na tela
        page.wait_for_selector("#resultado a")

        # 6. Validação do QA: Garante que a mensagem de sucesso está visível
        texto_resultado = page.inner_text("#resultado")
        assert "Link gerado:" in texto_resultado
        assert "http://127.0.0.1:8000/" in texto_resultado