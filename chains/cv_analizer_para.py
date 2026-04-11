import os
import io
import streamlit as st
from pypdf import PdfReader
from docx import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableParallel, RunnableLambda
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.title("CV - Analysis")
st.write("#### Author - Kuntal")

# ✅ JD text area
jd = st.text_area("Give me The JD here")

# ✅ CV file upload
uploaded_file = st.file_uploader(
    "Upload your CV", 
    type=["pdf", "docx", "png"]
)

button = st.button("Analyze")

# ✅ File read karne ka function
def read_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(uploaded_file.read()))
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text

    elif uploaded_file.name.endswith(".docx"):
        doc = Document(io.BytesIO(uploaded_file.read()))
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text

# ✅ Sab sahi hai tab chalao
if button and uploaded_file and jd:
    cv = read_file(uploaded_file)  # file se text nikalo
    st.success("CV Successfully Read! ✅")

    with st.spinner("Analyzing...."):

        cv_prompt_skills = ChatPromptTemplate.from_messages([
            ('system', "Analyze skills only from CV: {cv}")
        ])
        cv_prompt_project = ChatPromptTemplate.from_messages([
            ('system', "Analyze projects only from CV: {cv}")
        ])
        cv_prompt_others = ChatPromptTemplate.from_messages([
            ('system', "Analyze everything except projects & skills from CV: {cv}")
        ])
        combined_cv_prompt = ChatPromptTemplate.from_messages([
            ('system', """
            Skills: {skills}
            Projects: {projects}
            Others: {others}
            JD: {jd}
            Compare and give genuine feedback with matching_score from 1% to 100% strictly with 1 decimal point.
            
            -Rules:
             - Give the matching score in the begining 
             - Give bullet points in a comapirsion table of Jd vs Skill 
            -Format 
             [-Matching Score: x.x%,
             -Tabluer compair]
            """)
        ])

        llm_cv = ChatOpenAI(model='gpt-4o-mini', max_tokens=500)
        llm_compare = ChatOpenAI(model='gpt-4o', max_tokens=1000)
        parser = StrOutputParser()

        parachain = RunnableParallel({
            'skills'  : cv_prompt_skills | llm_cv | parser,
            'projects': cv_prompt_project | llm_cv | parser,
            'others'  : cv_prompt_others | llm_cv | parser,
            'jd'      : RunnableLambda(lambda x: x['jd'])
        })

        cv_jd_chain = parachain | combined_cv_prompt | llm_compare | parser

        response = cv_jd_chain.invoke({"cv": cv, "jd": jd})
        st.write(response)
        st.write("😎 Hope this is cool")