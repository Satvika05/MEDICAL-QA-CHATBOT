import streamlit as st
from vector_store import load_data, build_index, retrieve_top_k
from qa_model import get_answer
from ner import extract_entities

st.set_page_config(page_title="Medical Q&A Chatbot", layout="wide")
st.title("🩺 Medical Q&A Chatbot using MedQuAD")

@st.cache_resource
def init():
    data = load_data()
    index, data = build_index(data)
    return index, data

index, data = init()

question = st.text_input("Ask your medical question here:")

if question:
    top_data = retrieve_top_k(index, data, question, k=1)[0]
    context = top_data["context"]
    answer = get_answer(question, context)
    ents = extract_entities(question)

    st.subheader("🧠 Answer:")
    st.success(answer)

    st.subheader("🔬 Detected Medical Entities:")
    if ents:
        for ent, label in ents:
            st.write(f"🔹 {ent} ({label})")
    else:
        st.write("No entities found.")
