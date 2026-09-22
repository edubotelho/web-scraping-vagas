# Web Scraping de Vagas com Python

Projeto simples criado para estudar web scraping em Python, com foco em aprender sobre requisições HTTP e extração de dados de páginas HTML.

## Sobre o projeto

O script acessa uma página de vagas de emprego (site de teste), coleta título, empresa, localização e link de cada vaga, entra em cada uma delas para buscar a descrição completa, e salva tudo organizado em um arquivo CSV.

Desenvolvido a partir de um desafio do [roadmap.sh](https://roadmap.sh/), estudando diretamente a documentação oficial das bibliotecas.

## Tecnologias utilizadas

- Python
- Requests
- BeautifulSoup4
- CSV (biblioteca padrão)

## Como funciona

1. Faz a requisição da página principal com `requests`
2. Usa `BeautifulSoup` para localizar os elementos com título, empresa e localização de cada vaga
3. Para cada vaga, acessa o link individual e extrai a descrição completa
4. Salva todos os dados coletados em um arquivo `vagas.csv`

## Como rodar

\`\`\`bash
pip install requests beautifulsoup4
python index.py
\`\`\`

## Aprendizados

Esse projeto ajudou a fixar conceitos de requisições HTTP, navegação em HTML/CSS selectors e estruturação de dados coletados. Sigo estudando e construindo outros projetos.
