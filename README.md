# Product Sentiment Analysis Pipeline 🧠🚀

A lightweight, automated Natural Language Processing (NLP) pipeline built with Python that processes unstructured consumer reviews and accurately categorizes user sentiment into **Positive**, **Negative**, or **Neutral** metrics.

---

## 🛠️ Tech Stack & Library Frameworks
* **Language:** Python 3.10+
* **Data Ingestion:** Pandas
* **Natural Language Processing:** NLTK (Natural Language Toolkit)
* **Sentiment Modeling Engine:** VADER Lexicon (Valence Aware Dictionary and sEntiment Reasoner)

---

## 📂 File System & Project Architecture
The project maintains a decoupled modular layout dividing core extraction steps from clean runtime configs:

```text
ProductSentimentAnalysis/
│
├── data/
│   ├── reviews.csv          # Input: Consumer raw dataset
│   └── analyzed_reviews.csv # Output: Categorized text files
│
├── src/
│   ├── preprocess.py        # String sanitization & missing value handling
│   ├── analyzer.py          # NLTK VADER analytical computation logic
│   └── main.py              # Central pipeline workflow orchestrator
│
├── .gitignore               # Keeps massive dataset files out of source control
└── requirements.txt         # Project software prerequisites

