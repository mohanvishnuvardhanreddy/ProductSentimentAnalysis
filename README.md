# Product Sentiment Analysis Pipeline 🧠🚀

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=flat-square&logo=python)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/mohanvishnuvardhanreddy/ProductSentimentAnalysis?style=flat-square&logo=github)](https://github.com/mohanvishnuvardhanreddy/ProductSentimentAnalysis)
[![GitHub Issues](https://img.shields.io/github/issues/mohanvishnuvardhanreddy/ProductSentimentAnalysis?style=flat-square)](https://github.com/mohanvishnuvardhanreddy/ProductSentimentAnalysis/issues)
[![GitHub Forks](https://img.shields.io/github/forks/mohanvishnuvardhanreddy/ProductSentimentAnalysis?style=flat-square&logo=github)](https://github.com/mohanvishnuvardhanreddy/ProductSentimentAnalysis)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg?style=flat-square)](https://github.com/psf/black)

A lightweight, automated Natural Language Processing (NLP) pipeline built with Python that processes unstructured consumer reviews and accurately categorizes user sentiment into **Positive**, **Negative**, and **Neutral** categories.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

This project automates the process of analyzing product reviews by leveraging VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis. It's designed to handle large volumes of unstructured text data and provide actionable sentiment insights with minimal configuration.

**Use Cases:**
- Monitor customer satisfaction trends
- Identify product improvement areas
- Track brand sentiment over time
- Generate sentiment reports for stakeholders

---

## ✨ Features

- **Automated Pipeline:** End-to-end sentiment analysis from raw reviews to categorized output
- **VADER Sentiment Analysis:** Industry-proven lexicon-based approach optimized for social media and reviews
- **Data Preprocessing:** Automatic handling of missing values, text normalization, and cleaning
- **Modular Architecture:** Clean separation of concerns for easy maintenance and extension
- **Batch Processing:** Efficiently processes large datasets through CSV files
- **Confidence Scores:** Provides sentiment confidence metrics for each review

---

## 🛠️ Tech Stack & Library Frameworks

| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.10+ |
| **Data Processing** | Pandas |
| **NLP Framework** | NLTK (Natural Language Toolkit) |
| **Sentiment Engine** | VADER Lexicon (Valence Aware Dictionary and sEntiment Reasoner) |

---

## 📂 Project Structure

```
ProductSentimentAnalysis/
│
├── data/
│   ├── reviews.csv               # 📥 Input: Raw consumer reviews dataset
│   └── analyzed_reviews.csv      # 📤 Output: Processed reviews with sentiment labels
│
├── src/
│   ├── preprocess.py             # Data cleaning & normalization
│   ├── analyzer.py               # Sentiment analysis engine (VADER)
│   └── main.py                   # Pipeline orchestrator
│
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git configuration
└── README.md                     # This file
```

### File Descriptions

| File | Purpose |
|------|---------|
| `preprocess.py` | Handles text sanitization, missing values, and data normalization |
| `analyzer.py` | Implements VADER sentiment analysis and score computation |
| `main.py` | Coordinates the entire pipeline workflow |

---

## 📦 Installation

### Prerequisites
- Python 3.10 or higher
- pip (Python package manager)

### Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/mohanvishnuvardhanreddy/ProductSentimentAnalysis.git
   cd ProductSentimentAnalysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

### Quick Start

1. **Prepare your data**
   - Place your reviews in `data/reviews.csv`
   - Format: CSV file with a `review` column containing the text to analyze

2. **Run the pipeline**
   ```bash
   python src/main.py
   ```

3. **Check results**
   - Output saved to `data/analyzed_reviews.csv`
   - Contains original reviews plus sentiment labels and confidence scores

### Example Input Format

```csv
review
"This product is amazing! Best purchase ever."
"Terrible quality, very disappointed."
"It's okay, nothing special."
```

### Example Output Format

```csv
review,sentiment,confidence
"This product is amazing! Best purchase ever.",Positive,0.92
"Terrible quality, very disappointed.",Negative,0.88
"It's okay, nothing special.",Neutral,0.71
```

---

## 🔍 How It Works

### Pipeline Flow

```
Raw Reviews (CSV)
      ↓
[Preprocessing]
  - Clean text
  - Handle missing values
  - Normalize formatting
      ↓
[VADER Sentiment Analysis]
  - Tokenize text
  - Calculate sentiment scores
  - Determine polarity
      ↓
[Classification]
  - Map scores to sentiment
  - Assign confidence metrics
      ↓
Output (CSV with labels)
```

### Sentiment Classification

- **Positive:** Compound score > 0.05
- **Negative:** Compound score < -0.05
- **Neutral:** -0.05 ≤ Compound score ≤ 0.05

---

## 📊 Output

The pipeline generates an enriched CSV file with:

- **review:** Original review text
- **sentiment:** Classification (Positive/Negative/Neutral)
- **confidence:** Score indicating certainty (0.0 - 1.0)
- **positive_score:** Proportion of positive sentiment
- **negative_score:** Proportion of negative sentiment
- **neutral_score:** Proportion of neutral sentiment

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes
4. Commit with clear messages (`git commit -m 'Add feature: description'`)
5. Push to your branch (`git push origin feature/improvement`)
6. Open a Pull Request

### Areas for Enhancement
- Support for additional languages
- Custom sentiment lexicons
- Integration with machine learning models
- Web API wrapper
- Visualization dashboard

---

## 📝 License

This project is open source and available under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙋 Support

For issues, questions, or suggestions, please open an issue on the [GitHub repository](https://github.com/mohanvishnuvardhanreddy/ProductSentimentAnalysis).

---

**Happy Analyzing! 📈**
