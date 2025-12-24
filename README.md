# 🛡️ ScamGuard AI – Intelligent Scam Detection Assistant

## 📌 Overview
ScamGuard AI is an intelligent scam detection system designed to analyze messages, emails, and online content to identify potential scams and fraudulent patterns. The application helps users detect phishing attempts, financial fraud, and social engineering attacks using AI-driven classification and contextual analysis.

This project focuses on solving a real-world cybersecurity problem by combining machine learning, prompt-based AI logic, and structured evaluation workflows to deliver reliable scam detection insights.

---

## 🚨 Problem Statement
With the rapid growth of digital communication, users are increasingly exposed to scam messages such as:
- Phishing emails and SMS
- Fake job offers and lottery scams
- Bank and payment fraud messages
- Social engineering attacks

Most users struggle to differentiate legitimate messages from scams, leading to financial loss, identity theft, and security breaches. Manual verification is unreliable and time-consuming.

---

## 💡 Solution
ScamGuard AI provides an automated solution that analyzes suspicious messages and determines whether they are:
- **Scam**
- **Not a Scam**
- **Uncertain**

The system evaluates message content, intent, language patterns, and contextual cues to generate an informed classification along with reasoning. This assists users in making safer decisions before responding or taking action.

---

## ✨ Key Features
- AI-powered scam message classification  
- Detection of phishing and fraud patterns  
- Context-aware analysis of user-provided text  
- Confidence-based output (Scam / Not Scam / Uncertain)  
- Modular architecture for easy extension  
- Evaluation and testing pipeline for model validation  

---

## 🧠 How It Works
1. The user inputs a message or text content.
2. The system preprocesses and structures the input.
3. AI-driven classification logic analyzes the message.
4. Scam indicators and contextual signals are evaluated.
5. The system returns a clear verdict with reasoning.

This design ensures transparency, scalability, and reliability in scam detection.

---

## 🏗️ System Architecture
ScamGuard AI follows a modular pipeline-based architecture:
- **Input Layer** – Accepts user-provided messages
- **Preprocessing Layer** – Cleans and structures data
- **Classification Engine** – Detects scam patterns
- **Evaluation Module** – Measures performance
- **Output Layer** – Returns final classification

Each component is independently maintainable and testable.

---

## 🛠 Tech Stack
- **Python** – Core application logic  
- **AI / LLM-based classification**  
- **Prompt-driven analysis**  
- **Dataset-based evaluation**  
- **Environment-based configuration**  
- **Streamlit / CLI-ready architecture**

---

## 📂 Project Structure
ScamGuard-AI/
│
├── app.py # Application entry point
├── scam_classifier.py # Core scam classification logic
├── scam_news.py # Scam-related news/context handling
├── dataset_loader.py # Dataset loading and preprocessing
├── evaluation.py # Model evaluation logic
├── run_evaluation.py # Evaluation execution script
├── test_evaluation.py # Testing and validation
├── schema.py # Output and data schema definitions
├── prompt.py # Prompt templates for AI analysis
├── dataset.xlsx # Sample dataset for testing
├── requirements.txt # Project dependencies
├── .env.example # Environment variable template
├── README.md # Project documentation


---

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of Python and virtual environments

### Installation
```bash
pip install -r requirements.txt
