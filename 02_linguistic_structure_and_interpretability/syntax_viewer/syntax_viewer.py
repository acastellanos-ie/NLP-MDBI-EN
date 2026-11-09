import streamlit as st
import spacy
from spacy import displacy
from transformers import AutoTokenizer, AutoModel
import torch
import pandas as pd
import numpy as np

# Configuración
st.set_page_config(page_title="Session 3: Syntax & Attention", layout="wide")
st.title("🧠 Linguistic Structure: Trees vs. Attention")

# Cargar recursos (Cacheado)
@st.cache_resource
def load_spacy():
    return spacy.load("en_core_web_sm")

@st.cache_resource
def load_model():
    model_name = "bert-base-uncased"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name, output_attentions=True)
    return tokenizer, model

nlp = load_spacy()
tokenizer, model = load_model()

# Input
text = st.text_input("Escribe una frase compleja (en inglés para este modelo):", "The quick brown fox jumps over the lazy dog.")

if text:
    # PESTAÑA 1: SPACY
    st.header("1. La Visión Clásica: Dependency Parsing")
    doc = nlp(text)
    html = displacy.render(doc, style="dep", options={"compact": True, "distance": 100, "bg": "#ffffff"})
    st.write(html, unsafe_allow_html=True)

    # PESTAÑA 2: BERT
    st.divider()
    st.header("2. La Visión Moderna: Attention Mechanism (BERT)")

    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
    attention = outputs.attentions

    c1, c2 = st.columns(2)
    layer = c1.slider("Capa (Layer):", 0, 11, 9)
    head = c2.slider("Cabeza (Head):", 0, 11, 8)

    att_matrix = attention[layer][0, head].detach().numpy()
    tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

    df_att = pd.DataFrame(att_matrix, index=tokens, columns=tokens)
    st.dataframe(df_att.style.background_gradient(cmap="Blues", axis=None).format("{:.2f}"), width="stretch")
