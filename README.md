# Curriculum Analyzer LLM

🤖 **Analisador de Currículos com Google Gemini e Streamlit**

Uma aplicação web inteligente que utiliza a API do Google Gemini para analisar currículos, fornecendo:
- Resumo detalhado das competências do candidato.
- Pontuação de adequação para uma vaga específica.
- Perguntas personalizadas para a fase de entrevista.

## 🚀 Funcionalidades

- **Interface Web Interativa**: Front-end amigável construído com Streamlit.
- **Análise Inteligente**: Avalia currículos usando o poder do Gemini 2.5-Flash.
- **Pontuação Automática**: Gera um score de 0 a 100 baseado na compatibilidade com a vaga.
- **Perguntas para Entrevista**: Cria perguntas técnicas e comportamentais relevantes.
- **Comparação com Vagas**: Identifica pontos fortes e áreas de melhoria do candidato.

## 🛠️ Tecnologias

- **Python** - Linguagem principal
- **Streamlit** - Framework para a interface web
- **Google Gemini 2.5-Flash** - Modelo de IA generativa
- **LangChain** - Framework para desenvolvimento com LLMs
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## ⚙️ Configuração

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/JoaoMilanezi04/Curriculum-Analizer-LLM.git
    cd Curriculum-Analizer-LLM
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Mac/Linux
    # venv\Scripts\activate   # No Windows
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave API:**
    Crie um arquivo chamado `.env` na raiz do projeto e adicione sua chave:
    ```
    GOOGLE_API_KEY="sua_chave_secreta_aqui"
    ```

## 🎯 Como Executar

1.  Verifique se o ambiente virtual está ativado.
2.  Execute o aplicativo Streamlit pelo terminal:
    ```bash
    streamlit run src/app.py
    ```
3.  Abra o navegador no endereço local fornecido (geralmente `http://localhost:8501`).

## 📁 Estrutura do Projeto

```
Curriculum-Analizer-LLM/
├── .env                     # Arquivo para chaves de API (não versionado)
├── .gitignore               # Arquivos ignorados pelo Git
├── README.md                # Documentação do projeto
├── requirements.txt         # Dependências do Python
├── prompts/                 # Arquivos de texto com os prompts para a IA
│   ├── questions.txt
│   ├── scoring.txt
│   └── summary.txt
└── src/                     # Código-fonte da aplicação
    ├── app.py               # Interface do usuário com Streamlit
    └── logic/
        └── analyzer.py      # Lógica de análise com LangChain e Gemini
    └── utils/
        └── file_handler.py  # Utilitário para carregar arquivos
```

## 🔐 Segurança

- O arquivo `.env` que contém a chave da API é ignorado pelo Git (`.gitignore`) para evitar que segredos sejam expostos.
- **Nunca** suba suas chaves de API ou outros dados sensíveis para repositórios públicos.

---

⚡ **Desenvolvido com Google Gemini AI e Streamlit**
