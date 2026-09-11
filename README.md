<div align="center">

# Abdulrahman Ahmed

### AI Engineer · Machine Learning Engineer · Data Scientist

I build practical AI systems—from data pipelines and model training to reliable API serving and deployment. My work focuses on **computer vision, applied machine learning, NLP, and MLOps**, with an emphasis on measurable results and reproducible engineering.

**Based in Benha, Egypt · Open to AI/ML opportunities in Egypt, Saudi Arabia, the UAE, and remote teams**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

---

## What I Do

- Design and train machine-learning models for structured and unstructured data.
- Build computer-vision solutions for classification, detection, and segmentation.
- Develop retrieval-augmented applications and grounded document assistants.
- Turn models into usable services through **FastAPI, Docker, CI/CD, and experiment tracking**.
- Work with distributed data systems and automated workflows using **Spark, Hadoop, Airflow, and ClickHouse**.

## Selected Results

| Area | Result |
| --- | --- |
| Fraud detection | **95.2% test ROC-AUC** on a weighted ensemble trained on **6.3M+ transactions** |
| Pest detection | **98.3% mAP@50** with YOLOv8 |
| Weed detection | **95.1% mAP@50** with YOLOv8 |
| Disease classification | **99.7% test accuracy** across **15,000+ held-out images** |

> Metrics are reported from the corresponding project experiments. For production decisions, I also consider class imbalance, threshold selection, recall/precision trade-offs, latency, and reproducibility—not just a single headline score.

## Featured Projects

### Financial Fraud Detection

A weighted ensemble for highly imbalanced transaction data, where fraudulent cases represent approximately **0.13%** of the dataset.

- Processed and engineered behavioral, temporal, and destination-risk features from **6.3M+ records**.
- Combined XGBoost, LightGBM, and CatBoost with configurable risk thresholds.
- Reached **95.2% test ROC-AUC** with a **1.45% train/test gap**.
- At the balanced threshold: **60.8% precision** and **36.4% recall**.
- Built a Gradio interface for live inference and threshold experimentation.

`Python` `Pandas` `Scikit-learn` `XGBoost` `LightGBM` `CatBoost` `Gradio`

### Napta — Agricultural AI Platform

Graduation project developed by a six-person team to help identify crop diseases, pests, and weeds from field images and support farmers through a conversational assistant.

- **Disease classification:** 99.7% test accuracy across 15,000+ held-out images.
- **Pest detection:** 98.3% mAP@50, 98.7% precision, and 95.6% recall.
- **Weed detection:** 95.1% mAP@50, 96.1% precision, and 91.1% recall.
- **My contribution:** owned the FastAPI model-serving layer, validated model outputs, tuned inference behavior, and implemented batching and error handling.
- Graduation project awarded **Excellent (A+)**.

`PyTorch` `TensorFlow` `YOLOv8` `OpenCV` `FastAPI` `Docker`

### RAG-Based Document Intelligence

A lightweight document question-answering assistant designed to provide source-constrained responses without relying on a heavyweight orchestration framework.

- Implemented custom chunking and sliding-window segmentation.
- Generated dense embeddings with SentenceTransformers and indexed them with FAISS.
- Used structured tool calling through the OpenAI SDK to ground responses in retrieved context.
- Packaged the application with Docker and exposed it through a Streamlit interface.

`Python` `SentenceTransformers` `FAISS` `OpenAI SDK` `Streamlit` `Docker`

### Healthcare Recommendation Pipeline

Team project for processing heterogeneous patient histories and generating multi-specialty recommendations.

- Designed distributed ingestion and storage using Apache Spark 3.5 and Hadoop HDFS.
- Contributed to hybrid collaborative and content-based recommendation logic.
- Automated workflows with Apache Airflow and processed **500K+ patient profiles**.

`Apache Spark` `Hadoop HDFS` `LightGBM` `XGBoost` `Airflow` `ClickHouse`

## Experience

**Data Science Lead Trainer — AXIS Tech Community**<br>
*May 2025 – Present*<br>
Design and deliver practical machine-learning and data-science training for **100+ students**, covering regression, classification, SQL, feature engineering, and model validation.

**Data Science Intern — Pure Soft**<br>
*Dec 2025 – Feb 2026*<br>
Built EDA and feature-engineering pipelines for **100K+ customer records**, fine-tuned tree-based models, and deployed inference through containerized FastAPI services.

**AI Intern — Aitronix**<br>
*Sep 2025 – Nov 2025*<br>
Worked with Azure ML to organize model-lifecycle workflows and tracked artifacts through Azure Blob Storage.

## Technical Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,docker,fastapi,git,github,postgres,mysql,linux,vscode" alt="Technical stack icons" />
</p>

**Machine Learning:** Scikit-learn · XGBoost · LightGBM · CatBoost · Model evaluation · Imbalanced learning · Cross-validation<br>
**Computer Vision:** PyTorch · TensorFlow · YOLOv8 · OpenCV · Albumentations · Transfer learning<br>
**NLP & GenAI:** SentenceTransformers · FAISS · RAG · Embeddings · OpenAI SDK · Tool calling<br>
**Data & MLOps:** Pandas · Apache Spark · Hadoop HDFS · Airflow · MLflow · Docker · FastAPI · GitHub Actions<br>
**Databases & Tools:** PostgreSQL · MySQL · ClickHouse · Linux · Git · GitHub

## Education

**B.Sc. in Computer Science and Artificial Intelligence — Benha University**<br>
*July 2025 · Graduation Project: Napta Agricultural AI Platform · Grade: Excellent (A+)*

Additional training in Data Science and Analytics, Machine Learning Engineering, Deep Learning and Computer Vision, and Big Data Engineering.

## Currently Focused On

- Building production-ready AI applications with clear evaluation and reliable inference.
- Improving MLOps practices: reproducible pipelines, containerized serving, experiment tracking, and CI/CD.
- Strengthening system design for scalable machine-learning products.

---

<div align="center">

**Open to collaborating on applied AI, machine learning, computer vision, and data products.**

</div>
