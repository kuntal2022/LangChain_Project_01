import pandas as pd, streamlit as st, tiktoken, os, tempfile
import pymupdf4llm
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
import matplotlib.pyplot as plt, seaborn as sns

st.header("Document Chunking : Stats")
st.write(f"To do a Small eda of your documnet is Good idea to understand the distribution of the chunks, tokens, words and characters in your document. This can help you to understand the structure of your document and to identify any potential issues with the chunking process. By visualizing the stats, you can easily identify any outliers or patterns in the data that may need further investigation.")


pdf_path = st.file_uploader("Upload a PDF file", type=["pdf"])
button = st.button("Process PDF")

if button and pdf_path:
  if not pdf_path.name.lower().endswith(".pdf"):
    st.error("Please upload a valid PDF file.")
  else:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
      tmp.write(pdf_path.read())
      tmp_path = tmp.name


  md_text =pymupdf4llm.to_markdown(tmp_path)
  os.unlink(tmp_path)
  docs = [Document(page_content=md_text, metadata={"source": pdf_path.name})]
  splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50,
  )
  chunks = splitter.split_documents(docs)
  enc = tiktoken.encoding_for_model("gpt-3.5-turbo")

  stats=[]
  for i, chunk in enumerate(chunks):
    text = chunk.page_content
    token_count = len(enc.encode(text))
    word_count  = len(text.split())
    char_count  = len(text)

    stats.append({
      "chunk"  : i + 1,
      "tokens" : token_count,
      "words"  : word_count,
      "chars"  : char_count,
    })  

  st.write("###📊 Chunking Stats")
  st.write()  
  df=pd.DataFrame(stats)
  st.write(f"Now you know which model will be good base on the context size of your chunks. You can also identify any potential issues with the chunking process, such as chunks that are too large or too small. By visualizing the stats, you can easily identify any outliers or patterns in the data that may need further investigation.")



  ds=df.describe()
  st.write(ds)  

  fig, ax1 = plt.subplots()
  sns.barplot(data=ds, x=ds.index, y="tokens", ax=ax1, color="r")
  ax1.set_title("Token Stats per Chunk")
  ax1.set_xlabel("Statistic")
  st.pyplot(fig)



  fig, ax1 = plt.subplots()
  sns.barplot(data=ds, x=ds.index, y="chunk", ax=ax1, color="g")
  ax1.set_title("Chunk Stats per Chunk")
  ax1.set_xlabel("Statistic")
  st.pyplot(fig)

  fig, ax2 = plt.subplots()
  sns.barplot(data=ds, x=ds.index, y="words", ax=ax2, color="skyblue")
  ax2.set_title("Word Stats per Chunk")
  ax2.set_xlabel("Statistic")
  st.pyplot(fig)


  fig, ax = plt.subplots()
  sns.barplot(data=ds, x=ds.index, y="chars", ax=ax, color="navy")
  ax.set_title("Character Stats per Chunk")
  ax.set_xlabel("Statistic")
  st.pyplot(fig)



