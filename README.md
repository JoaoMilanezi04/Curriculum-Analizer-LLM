# Curriculum Analyzer LLM

🤖 **Analisador de Currículos com Google Gemini**

Um sistema inteligente que utiliza a API do Google Gemini para analisar currículos automaticamente, fornecendo:
- Resumo detalhado das competências
- Pontuação de adequação para vagas específicas
- Perguntas de entrevista personalizadas

## 🚀 Funcionalidades

- **Análise Inteligente**: Avalia currículos usando IA avançada
- **Pontuação Automática**: Score de 0-100 baseado na vaga
- **Perguntas de Entrevista**: Gera perguntas técnicas e comportamentais
- **Comparação com Vagas**: Identifica pontos fortes e áreas de melhoria

## 🛠️ Tecnologias

- **Python** - Linguagem principal
- **Google Gemini 2.5-Flash** - Modelo de IA
- **LangChain** - Framework para LLM
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## ⚙️ Configuração

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Mac/Linux
   ```
3. Instale as dependências:
   ```bash
   pip install google-generativeai python-dotenv langchain langchain-google-genai
   ```
4. Configure sua chave API no arquivo `api.env`:
   ```
   GOOGLE_API_KEY=sua_chave_aqui
   ```

## 🎯 Uso

Execute o analisador:
```bash
python Backend/analizer.py
```

## 📁 Estrutura do Projeto

```
Curriculum-Analizer-LLM/
├── Backend/
│   └── analizer.py          # Código principal
├── src/
│   └── __init__.py
├── api.env                  # Configurações da API
├── .gitignore              # Arquivos ignorados
└── README.md               # Este arquivo
```

## 🔐 Segurança

- Arquivo `api.env` está no `.gitignore`
- Nunca commite suas chaves API
- Use variáveis de ambiente para dados sensíveis

## 📋 Exemplo de Saída

O sistema gera:
- **Resumo**: Análise completa das competências
- **Pontuação**: Score de adequação à vaga
- **Perguntas**: Questões para entrevista técnica

---

⚡ **Desenvolvido com Google Gemini AI**
