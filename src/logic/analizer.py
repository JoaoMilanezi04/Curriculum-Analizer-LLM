import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()  # Carrega do arquivo api.env

api_key = os.getenv('GOOGLE_API_KEY')
if api_key is None:
    raise ValueError("A variável de ambiente 'GOOGLE_API_KEY' não está definida. Por favor, verifique o arquivo api.env.")

curriculum_example = """
João Silva
Desenvolvedor de Software
Email: joao.silva@example.com
Telefone: (11) 99999-9999
Resumo Profissional:
Desenvolvedor de software com 5 anos de experiência em desenvolvimento web e mobile. Habilidades em Python, JavaScript, React e Node.js.
Experiência Profissional:
Empresa XYZ - Desenvolvedor Full Stack (2019 - Presente)
- Desenvolvimento de aplicações web utilizando React e Node.js.
- Implementação de APIs RESTful.
- Colaboração com equipes de design e produto para criar interfaces intuitivas.
Empresa ABC - Desenvolvedor Frontend (2017 - 2019)
- Criação de interfaces de usuário responsivas com HTML, CSS e JavaScript.
- Otimização de performance de aplicações web.
Educação:
Bacharel em Ciência da Computação - Universidade Federal (2013 - 2017)
Habilidades Técnicas:
- Linguagens: Python, JavaScript, Java
- Frameworks: React, Node.js, Django
- Banco de Dados: MySQL, MongoDB
- Ferramentas: Git, Docker, AWS
"""

job_description_example = """
Vaga: Desenvolvedor Full Stack
Responsabilidades:
- Desenvolvimento de aplicações web utilizando React e Node.js.
- Implementação de APIs RESTful.
- Colaboração com equipes de design e produto para criar interfaces intuitivas.
Requisitos:
- Experiência com React, Node.js e bancos de dados relacionais.
- Conhecimento em Docker e AWS.
- Boa comunicação e trabalho em equipe.
requisitos_desejaveis:
- Experiência com TypeScript.
- Conhecimento em GraphQL.
- Familiaridade com metodologias ágeis.
"""

llm = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash", temperature=0.2)

summary_template = """
aja como um especialista em recrutamento e análise de currículos.
Analise o seguinte currículo e forneça um resumo das principais habilidades, nível de experiência e pontos fortes.

Currículo: {curriculum}

resumo do candidato:
"""

summary_prompt = PromptTemplate(input_variables=["curriculum"], template=summary_template)

score_prompt = """
aja como um especialista em recrutamento e análise de currículos.
Compare o seguinte currículo com a descrição da vaga e forneça uma pontuação de 0 a 100 com base na adequação do candidato à vaga.
1.  **Pontos Fortes:** Principais competências do candidato que batem com a vaga.
2.  **Pontos de Melhoria:** Competências exigidas na vaga que não estão claras ou ausentes no currículo.
3.  **Veredito:** Uma recomendação final em uma frase.

Currículo: {curriculum}
Descrição da Vaga: {job_description}
Pontuação e análise:
"""
score_prompt = PromptTemplate(input_variables=["curriculum", "job_description"], template=score_prompt)

questions_template = """
Aja como um gerente de contratação para a área de tecnologia.
Com base no currículo do candidato e na descrição da vaga, gere 5 perguntas de entrevista relevantes.
As perguntas devem ser uma mistura de técnicas (sobre as tecnologias citadas) e comportamentais
(sobre as experiências descritas).
Currículo: {curriculum}
Descrição da Vaga: {job_description}
Perguntas:
1.
2.
3.
4.
5.
"""
questions_prompt = PromptTemplate(input_variables=["curriculum", "job_description"], template=questions_template)


# Usando sintaxe moderna do LangChain
summary_chain = summary_prompt | llm
score_chain = score_prompt | llm
questions_chain = questions_prompt | llm


print("--- Analisador de Currículos Iniciado ---")

print("--resumo do candidato--")
summary = summary_chain.invoke({"curriculum": curriculum_example})
print(summary.content)

print("--pontuação do candidato--")
score = score_chain.invoke({"curriculum": curriculum_example, "job_description": job_description_example})
print(score.content)

print("--perguntas para o candidato--")
questions = questions_chain.invoke({"curriculum": curriculum_example, "job_description": job_description_example})
print(questions.content)

print("--- Analisador de Currículos Finalizado ---")
