# Natural Language Processing — from tokens to a working AI system

Welcome. Over this course you won't just learn NLP techniques in isolation — **you will build one real system, piece by piece, across every session, and watch it come together at the end.**

The system is the **Helcon Support Copilot**. *Helcon* is a fictional software company whose support team is drowning in customer tickets. Week by week we build the AI that triages those tickets, answers them from the company's help center, and knows when to escalate. Every session adds a real component; the final session assembles all of them into a copilot you can run end to end.

## The journey

Each session is a standalone lesson *and* a step in the build. The running thread is the company (**Helcon**) and a shared dataset that grows with you.

| # | Session | What you learn | What you build for Helcon |
|---|---|---|---|
| 01 | [Introduction](01_introduction) | Meet the company and the data the whole course is built on. | A tour of Helcon's tickets, help center, and the hard cases to come. |
| 02 | [Linguistic structure & interpretability](03_linguistic_structure_and_interpretability) | How classical grammar parses language and why structure isn't meaning. How attention really works inside BERT. | A rule-based ticket reader… that breaks on real customer language ("my refund was *never* processed"). The motivation for everything next. |
| 03 | [Language modeling](05_language_modeling) | What "Generative AI" physically is: predicting the next token. Decoding, temperature, and why models hallucinate fluently. | A measure of which tickets *surprise* the model and the intuition for why a grounded system needs evidence, not fluency. |
| 04 | [Transfer learning & fine-tuning](06_transfer_learning_and_fine_tuning) | Classic baselines vs. fine-tuning vs. LoRA vs. zero-shot vs. prompting judged on one fair leaderboard (accuracy, cost, latency). | **Helcon's triage model**: a classifier that routes each ticket to the right queue. Shipped as a 3 MB LoRA adapter the rest of the course reuses. |
| 05 | [Information retrieval & RAG](07_rag) | How search engines rank (TF-IDF, BM25, dense), measured on a real benchmark. How Retrieval-Augmented Generation grounds an LLM in your documents. | **Helcon's retriever**: RAG over the help center, with citations and a live demo of *poisoning* the index to see why grounding ≠ truth. |

## How the pieces connect

The course ships a small shared "company data + tools" folder, [`system/`](system/), that every notebook loads through one helper (`system_io.py`):

- **the data** — Helcon's support tickets, help-center articles, and policies — so every session works on the *same* company, not a different toy dataset each week;
- **the artifacts** — the triage model from session 06, the retriever config from session 07 — so a component you build once is reused downstream, exactly like a real ML team's model registry.

## Running the notebooks

These labs are built for **Google Colab** (free tier). Click the **Open in Colab** badge at the top of any notebook, then run the first ("Setup") cell that installs the libraries, downloads the models, and pulls in the shared Helcon data. Sessions that train or run larger models will ask you to enable a **GPU runtime** (Runtime → Change runtime type → T4).

## About the data

*Helcon* is fictional and its data is **manufactured for teaching**. The tickets, help-center articles, and policies were written for this course (the support-ticket structure mirrors public customer-support datasets). It is free to use and reuse. Nothing here is a real company or real customer data.

---

*The best way to finish this course is to be able to say: "I built that — all of it."* See you in session 03.
