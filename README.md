# 🤖 Automação de Coleta de Dados com RPA

Projeto desenvolvido em Python com foco em **RPA (Robotic Process Automation)** para automatizar a coleta, organização e exportação de informações provenientes de pesquisas no Google.

---

## 📌 Descrição

A aplicação realiza automaticamente uma busca no Google e extrai os **N primeiros resultados**, coletando informações relevantes como:

- 📰 Título da página  
- 🔗 Link  
- 🧾 Descrição (snippet)  
- 📅 Data de publicação (quando disponível)  
- 🏢 Fonte  

Após a coleta, os dados são estruturados e exportados em múltiplos formatos, permitindo fácil análise e compartilhamento.

Todo o fluxo — da busca até a geração dos arquivos finais — é **100% automatizado**.

---

## 🚀 Funcionalidades

- 🔎 Automação de buscas no Google  
- 📊 Extração estruturada de dados  
- 📁 Exportação em múltiplos formatos:
  - CSV  
  - Excel (.xlsx)  
  - PDF  
  - TXT  
- ⚙️ Organização modular do código  
- 🧠 Manipulação e tratamento de dados automatizados  

---

## 🏗️ Estrutura do Projeto

```
Automacao/
│
├── main.py            # Arquivo principal (orquestra o fluxo)
├── navegador.py       # Automação de navegação (RPA / scraping)
│
├── CSV.py             # Geração de arquivos CSV
├── EXCEL.py           # Geração de arquivos Excel
├── PDF.py             # Geração de arquivos PDF
├── TXT.py             # Geração de arquivos TXT
│
├── Resultados/        # Saídas geradas automaticamente
│   ├── resultados.csv
│   ├── resultados.xlsx
│   ├── resultados.pdf
│   └── resultados.txt
│
├── LICENSE
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

- Python 3.x  
- Automação Web (Selenium)   
- Manipulação de dados  
- Geração de relatórios  

---

## ▶️ Como Executar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Automacao.git
cd Automacao
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

> Caso não exista um `requirements.txt`, instale manualmente as bibliotecas utilizadas no projeto.

### 3. Execute o projeto

```bash
python main.py
```

---

## ⚙️ Configuração

Você pode ajustar parâmetros como:

- Quantidade de resultados coletados (N)  
- Termo de busca  
- Formatos de saída desejados  

---

## 📈 Exemplo de Uso

1. O sistema realiza uma busca automática  
2. Coleta os primeiros resultados  
3. Extrai os dados relevantes  
4. Gera arquivos organizados na pasta `/Resultados`  

---

## 🎯 Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de:

- Explorar conceitos de **RPA com Python**  
- Praticar **web scraping e automação**  
- Trabalhar com **estruturação de dados**  
- Gerar **relatórios automatizados**  
- Simular aplicações reais de automação no mercado  

---

## 📌 Possíveis Melhorias

- Interface gráfica (GUI)  
- Integração com APIs de busca  
- Agendamento automático (cron jobs)  
- Armazenamento em banco de dados  
- Deploy como serviço  

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.

---

## 👨‍💻 Autor

Desenvolvido por **Victor Speorin**
