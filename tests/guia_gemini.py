"""
GUIA BÁSICO - Google Gemini API
===============================

A API do Google Gemini é muito simples! Você só precisa conhecer alguns comandos básicos:

1. CONFIGURAÇÃO INICIAL (fazer uma vez)
"""
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv('api.env')
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Criar o modelo (testando diferentes versões)
try:
    model = genai.GenerativeModel('gemini-pro')
except:
    try:
        model = genai.GenerativeModel('models/gemini-pro')
    except:
        model = genai.GenerativeModel('gemini-1.0-pro')

"""
2. COMANDOS BÁSICOS QUE VOCÊ VAI USAR:

A) Fazer uma pergunta simples:
"""
def pergunta_simples():
    response = model.generate_content("Explique o que é inteligência artificial")
    return response.text

"""
B) Analisar texto (como um currículo):
"""
def analisar_curriculo(texto_curriculo):
    prompt = f"""
    Analise este currículo e me diga:
    1. Principais habilidades
    2. Nível de experiência
    3. Pontos fortes
    
    Currículo: {texto_curriculo}
    """
    response = model.generate_content(prompt)
    return response.text

"""
C) Fazer perguntas com contexto:
"""
def pergunta_com_contexto(contexto, pergunta):
    prompt = f"""
    Contexto: {contexto}
    
    Pergunta: {pergunta}
    """
    response = model.generate_content(prompt)
    return response.text

"""
D) Comparar dois currículos:
"""
def comparar_curriculos(curriculo1, curriculo2):
    prompt = f"""
    Compare estes dois currículos e diga qual é melhor para uma vaga de desenvolvedor:
    
    Currículo 1: {curriculo1}
    
    Currículo 2: {curriculo2}
    """
    response = model.generate_content(prompt)
    return response.text

"""
ISSO É TUDO! 🎉

Os comandos principais são:
- model.generate_content("sua pergunta")
- response.text (para pegar a resposta)

Para seu projeto de análise de currículos, você vai usar principalmente:
1. Carregar o texto do currículo (PDF/Word)
2. Enviar para o Gemini com model.generate_content()
3. Receber a análise em response.text

Simples assim! 
"""

# Exemplo de uso prático para teste
if __name__ == "__main__":
    try:
        # Teste básico
        response = model.generate_content("Diga 'Olá' em 5 idiomas diferentes")
        print("✅ API funcionando!")
        print("Resposta:", response.text)
    except Exception as e:
        print(f"❌ Erro: {e}")
