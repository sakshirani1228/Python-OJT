import streamlit as st
from pypdf import PdfReader
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
st.title("C.V Analyzer")
st.success("User CV")
f1=st.file_uploader("Upload User CV")
reader=PdfReader(f1)
cv="".join(page.extract_text() for page in reader.pages)
st.write(cv)
st.success("Job Description")
f2=st.file_uploader("Upload Job Description")
reader1=PdfReader(f2)
jd="".join(page.extract_text() for page in reader1.pages)
st.write(jd)
x=CountVectorizer()
matrix=x.fit_transform([jd,cv])
similarity_matrix=cosine_similarity(matrix)
st.write(similarity_matrix)
st.write(str(similarity_matrix[1][0]*100)+'%')
                    
