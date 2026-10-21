# 🇧🇷 Encurtador de Links - Portfólio de Quality Assurance 🚀

Este projeto é uma API de encurtamento de URLs desenvolvida em Python para demonstrar habilidades práticas em Quality Assurance (QA). O repositório contém a aplicação completa (Backend e Frontend básico) e uma suíte de testes ponta a ponta (E2E) e de integração.

## 🛠️ Tecnologias Utilizadas
* **Backend:** Python, FastAPI, SQLModel (SQLite).
* **Frontend:** HTML, CSS, JavaScript (Vanilla).
* **Testes Automatizados:** Pytest, HTTPX (API) e Playwright (Web E2E).
* **Documentação:** Plano de Testes e Casos de Teste (Markdown).

## 📂 Estrutura de Qualidade (QA)
A estratégia de qualidade do projeto foi dividida em três frentes:
1. **Documentação:** Criação de Plano de Testes com definição de escopo e critérios de aceite (`docs/plano_de_testes.md`).
2. **Testes Manuais:** Casos de teste estruturados para validação de caminho feliz e testes negativos (`testes/manuais/casos_de_teste.md`).
3. **Testes Automatizados:**
   * **API:** Scripts para validar Status Code (200, 404, 422) e payloads utilizando `pytest`.
   * **Web:** Robôs em `Playwright` para validar a interface gráfica e o redirecionamento dinâmico.

## 💻 Como rodar o projeto na sua máquina

**1. Clone o repositório e acesse a pasta:**
```bash
git clone [https://github.com/SEU_USUARIO/encurtador-links-qa.git](https://github.com/SEU_USUARIO/encurtador-links-qa.git)
cd encurtador-links-qa
```

**2. Crie e ative o ambiente virtual:**
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
```

**3. Instale as dependências e o navegador de testes:**
```bash
pip install fastapi uvicorn sqlmodel pytest httpx pytest-playwright
playwright install
```

**4. Inicie o servidor da API:**
```bash
uvicorn app.main:app --reload
```
*Após iniciar o servidor, abra o arquivo `index.html` no seu navegador para utilizar a interface.*

## 🧪 Como executar os testes automatizados
Com o servidor rodando em um terminal, abra um segundo terminal, ative o `venv` e rode:
* Para testar a API: `pytest testes/api/`
* Para testar a Interface Visual: `pytest testes/web/ --headed`



---

# 🇺🇸 Link Shortener - Quality Assurance Portfolio 🚀

This project is a URL shortening API developed in Python to demonstrate practical skills in Quality Assurance (QA). The repository contains the complete application (Backend and basic Frontend) and a suite of end-to-end (E2E) and integration tests.

## 🛠️ Technologies Used
* **Backend:** Python, FastAPI, SQLModel (SQLite).
* **Frontend:** HTML, CSS, JavaScript (Vanilla).
* **Automated Tests:** Pytest, HTTPX (API), and Playwright (Web E2E).
* **Documentation:** Test Plan and Test Cases (Markdown).

## 📂 Quality Assurance (QA) Structure
The quality strategy of the project was divided into three fronts:
1. **Documentation:** Creation of a Test Plan defining scope and acceptance criteria (`docs/plano_de_testes.md`).
2. **Manual Tests:** Structured test cases for happy path and negative testing (`testes/manuais/casos_de_teste.md`).
3. **Automated Tests:**
   * **API:** Scripts to validate Status Codes (200, 404, 422) and payloads using `pytest`.
   * **Web:** `Playwright` robots to validate the graphical interface and dynamic redirection.

## 💻 How to run the project locally

**1. Clone the repository and access the folder:**
```bash
git clone [https://github.com/SEU_USUARIO/encurtador-links-qa.git](https://github.com/SEU_USUARIO/encurtador-links-qa.git)
cd encurtador-links-qa
```

**2. Create and activate the virtual environment:**
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/Mac: source venv/bin/activate
```

**3. Install dependencies and the test browser:**
```bash
pip install fastapi uvicorn sqlmodel pytest httpx pytest-playwright
playwright install
```

**4. Start the API server:**
```bash
uvicorn app.main:app --reload
```
*After starting the server, open the `index.html` file in your browser to use the interface.*

## 🧪 How to execute the automated tests
With the server running in one terminal, open a second terminal, activate the `venv` and run:
* To test the API: `pytest testes/api/`
* To test the Visual Interface: `pytest testes/web/ --headed`