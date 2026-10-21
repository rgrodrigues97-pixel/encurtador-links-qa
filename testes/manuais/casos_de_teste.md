# Casos de Teste - API Encurtador de Links

## CT01: Gerar link curto com sucesso (Caminho Feliz)
**Objetivo:** Validar se a API cria um link curto e salva no banco de dados quando recebe uma URL válida.
**Pré-condições:** O servidor da API deve estar rodando localmente (porta 8000).

*   **Passo 1:** Abrir o Postman e criar uma nova requisição com o método `POST`.
*   **Passo 2:** Inserir a URL `http://127.0.0.1:8000/encurtar`.
*   **Passo 3:** Na aba Body, selecionar `raw` e `JSON`.
*   **Passo 4:** Inserir o payload: `{ "url_original": "https://www.google.com" }`
*   **Passo 5:** Clicar em "Send".

**Resultado Esperado:** 
A API deve retornar o HTTP Status `200 OK`. O corpo da resposta deve conter o `id_no_banco`, a `url_original`, a `url_curta` gerada e o `codigo`.

---

## CT02: Bloquear requisição com formato de dados incorreto (Teste Negativo)
**Objetivo:** Validar se a API aplica a regra de validação do Pydantic e recusa pacotes que não contenham o campo obrigatório `url_original`.
**Pré-condições:** O servidor da API deve estar rodando localmente.

*   **Passo 1:** No Postman, criar uma requisição `POST` para `http://127.0.0.1:8000/encurtar`.
*   **Passo 2:** Configurar o Body como `raw` e `JSON`.
*   **Passo 3:** Inserir um payload incorreto propositalmente: `{ "site_errado": "https://www.google.com" }`
*   **Passo 4:** Clicar em "Send".

**Resultado Esperado:**
A API deve barrar a criação e retornar o HTTP Status `422 Unprocessable Entity`. A resposta deve conter o detalhamento do erro indicando a falta do campo `url_original`.

---

## CT03: Redirecionamento de código inexistente (Tratamento de Exceção)
**Objetivo:** Garantir que o sistema não quebre (Erro 500) ao buscar um código que não está no banco de dados.
**Pré-condições:** O servidor da API deve estar rodando localmente.

*   **Passo 1:** No Postman (ou navegador), criar uma requisição `GET`.
*   **Passo 2:** Inserir a URL com um código inválido: `http://127.0.0.1:8000/codigoFalso123`
*   **Passo 3:** Executar a requisição.

**Resultado Esperado:**
A API deve retornar o HTTP Status `404 Not Found` com a mensagem "Link curto não encontrado".