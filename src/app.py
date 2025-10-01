import streamlit as st
import logic.analyzer as analyzer

# config page

st.set_page_config(
    page_title="Analisador de Currículos",
    page_icon="📄",
    layout="wide"
)

# title

st.title("📄 Analisador de Currículos")
st.markdown("""
Este aplicativo utiliza um modelo de linguagem avançado para analisar currículos em relação a descrições de vagas de emprego.
Ele gera um resumo do candidato, uma pontuação de adequação à vaga e perguntas de entrevista relevantes.
""")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.header("currículo do candidato")
    curriculum_text = st.text_area("Cole seu currículo aqui", height=300, label_visibility="collapsed")
    
with col2:
    st.header("descrição da vaga")
    job_description_text = st.text_area("Cole a descrição da vaga aqui", height=300, label_visibility="collapsed")

if st.button("Analisar Candidato", type="primary", use_container_width=True):
    if curriculum_text and job_description_text:

        with st.spinner("Analisando o currículo..."):

            resultados = analyzer.executar_analise(curriculo=curriculum_text, vaga=job_description_text)

        st.divider()
        st.success("Análise concluída!")
        
        if "erro" in resultados:
            st.error(f"ocorreum um erro: {resultados['erro']}")
        else:
            st.subheader("Resumo do Candidato")
            st.markdown(resultados["resumo"])

            st.subheader("Pontuação do Candidato")
            st.markdown(resultados["pontuacao"])

            st.subheader("Perguntas para a Entrevista")
            st.markdown(resultados["perguntas"])
    else:
        st.warning("Por favor, insira tanto o currículo quanto a descrição da vaga para análise.")
        
    
        
