# src/logic/analyzer.py

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

from utils.file_handler import load_prompt

load_dotenv()

def executar_analise(curriculo: str, vaga: str) -> dict:
    """
    Executa a análise completa de um currículo contra uma vaga.

    Args:
        curriculo (str): O texto do currículo.
        vaga (str): O texto da descrição da vaga.

    Returns:
        dict: Um dicionário contendo o resumo, a pontuação e as perguntas.
    """
    try:
        llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.3)
    except Exception as e:

        return {"erro": f"Falha ao inicializar o modelo de linguagem: {e}"}

    summary_template_str = load_prompt("summary.txt")
    score_template_str = load_prompt("scoring.txt")
    questions_template_str = load_prompt("questions.txt")

    summary_prompt = PromptTemplate.from_template(summary_template_str)
    score_prompt = PromptTemplate.from_template(score_template_str)
    questions_prompt = PromptTemplate.from_template(questions_template_str)
    
    summary_chain = LLMChain(llm=llm, prompt=summary_prompt)
    score_chain = LLMChain(llm=llm, prompt=score_prompt)
    questions_chain = LLMChain(llm=llm, prompt=questions_prompt)

    try:
        resumo_result = summary_chain.invoke({"curriculum": curriculo})
        pontuacao_result = score_chain.invoke({"curriculum": curriculo, "job_description": vaga})
        perguntas_result = questions_chain.invoke({"curriculum": curriculo, "job_description": vaga})

        return {
            "resumo": resumo_result['text'],
            "pontuacao": pontuacao_result['text'],
            "perguntas": perguntas_result['text']
        }
    except Exception as e:
        return {"erro": f"Ocorreu um erro durante a análise da IA: {e}"}