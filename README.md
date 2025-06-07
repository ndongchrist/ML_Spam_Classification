# 📧 Email Spam Classifier

A machine learning project to classify emails as **spam** or **ham (not spam)** using natural language processing (NLP). The model uses techniques like TF-IDF vectorization and compares multiple classification algorithms including Logistic Regression, Naive Bayes, and Support Vector Machines (SVM).

---

## 🚀 Features

- Text preprocessing with TF-IDF
- Trained and validated on the `completespamassasin` dataset
- Compared multiple models: Logistic Regression, Naive Bayes, and SVM
- Best performance with **SVM** (98%+ accuracy)
- Save and reuse model for prediction
- CLI script to test your own email

---

## 🗂 Dataset

- Source: [Kaggle - arXiv Spam Dataset](https://www.kaggle.com/datasets/Cornell-University/arxiv)
- File used: `completespamassasin.csv`
- Columns:
  - `Body`: The content of the email
  - `Label`: 0 = Ham, 1 = Spam

---

## 🛠️ Setup

### 📦 Prerequisites

- Python 3.8+
- Virtual environment (optional but recommended)

### 🔧 Install dependencies

```bash
pip install -r requirements.txt
