# Syntax Viewer (Streamlit App)

Interactive demo for Session 3: compares classical **dependency parsing** (spaCy) with the **attention mechanism** of a Transformer (BERT).

## Run locally

```bash
pip install -r requirements.txt
streamlit run syntax_viewer.py
```

The spaCy model (`en_core_web_sm`) is installed automatically via `requirements.txt`.

## Run in Google Colab

Colab cannot serve a Streamlit app directly, so write the script to a file and expose it through a tunnel (e.g. localtunnel):

```python
# Cell 1: install dependencies
!pip install -q streamlit spacy transformers torch pandas numpy
!python -m spacy download en_core_web_sm -q

# Cell 2: write the app file (paste the contents of syntax_viewer.py below the magic)
%%writefile syntax_viewer.py
# ... contents of syntax_viewer.py ...
```

```python
# Cell 3: launch Streamlit and open a tunnel
!streamlit run syntax_viewer.py &>/content/logs.txt &
!npx localtunnel --port 8501
```

Open the URL printed by localtunnel. If asked for a tunnel password, it is your public IP (`!curl ipv4.icanhazip.com`).
