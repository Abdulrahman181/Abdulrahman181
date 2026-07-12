<!-- HEADER SECTION -->
<div align="center">

# ⚡ Abdulrahman Ahmed

### **AI Engineer | Machine Learning Engineer | Data Scientist**

*I turn messy, imbalanced, real-world data into models that ship — with the numbers to prove it and the honesty to defend every one of them in a room.*

📍 Benha, Egypt &nbsp;|&nbsp; 💻 Open to Remote & Global Opportunities

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

<br>

## 📊 Verified Results

*Every number below comes from an executed notebook or a measured run — not a projection.*

<table width="100%">
  <tr>
    <td align="center" width="25%">
      <b>95.2%</b><br>
      <sub>Test ROC-AUC — Fraud Detection Ensemble<br>(96.6% Train, 1.45% gap)</sub>
    </td>
    <td align="center" width="25%">
      <b>98.3%</b><br>
      <sub>mAP@50 — Multi-Class Pest Detection (YOLOv8)</sub>
    </td>
    <td align="center" width="25%">
      <b>95.1%</b><br>
      <sub>mAP@50 — Weed Detection (YOLOv8)</sub>
    </td>
    <td align="center" width="25%">
      <b>6.3M+</b><br>
      <sub>Transaction Records Processed</sub>
    </td>
  </tr>
</table>

<p align="center"><sub>Full methodology and threshold trade-offs for each result are documented in the project write-ups below.</sub></p>

---

## 🛠️ Core Expertise

<table width="100%">
<tr>
<td valign="top" width="50%">

**Computer Vision**
Object Detection · Image Classification · Semantic Segmentation · Transfer Learning
`PyTorch` `TensorFlow` `YOLOv8` `OpenCV` `Albumentations`

**Machine Learning & Ensembles**
Gradient Boosting · Class-Imbalance Handling · Hyperparameter Tuning · Cross-Validation
`XGBoost` `LightGBM` `CatBoost` `Scikit-learn`

</td>
<td valign="top" width="50%">

**NLP & Generative AI**
Retrieval-Augmented Generation · Semantic Search · Dense Embeddings · Tool-Calling Agents
`SentenceTransformers` `FAISS` `OpenAI API` `BERT`

**Data Engineering & MLOps**
Distributed Processing · Workflow Orchestration · Containerized Deployment
`Apache Spark` `Airflow` `Docker` `FastAPI` `MLflow` `GitHub Actions`

</td>
</tr>
</table>

---

## 🏆 Featured Projects

### 💳 Financial Fraud Detection — Weighted Ensemble on 6.3M Transactions
**Problem:** Catch fraudulent transactions inside a ~0.13% fraud rate without drowning analysts in false alarms.

- Engineered behavioral, temporal, and destination-risk features from raw transaction logs
- Handled extreme imbalance via majority-class downsampling + `scale_pos_weight` / `auto_class_weights`
- Built a weighted ensemble (XGBoost 30% · LightGBM 30% · CatBoost 40%) with three selectable risk thresholds (aggressive / balanced / conservative)
- Shipped a Gradio demo for live inference

**Result:** **95.2% Test ROC-AUC**, 1.45% train/test gap. At the balanced threshold: **60.8% precision / 36.4% recall** — a deliberate trade-off, tunable per business risk appetite rather than a single inflated headline number.

`Python` `Pandas` `Scikit-learn` `XGBoost` `LightGBM` `CatBoost` `Gradio`

---

### 🌾 Napta — Full-Stack Agricultural AI Platform *(Graduation Project, Team of 6, Grade: A+)*
**Problem:** Give farmers one platform to identify crop diseases, pests, and weeds from field images, plus a conversational assistant for follow-up questions — combining four separate ML/AI subsystems into one served product.

**System components:**
- **Disease Classification** (CNN, multi-class): **99.7% test accuracy** across 15,000+ held-out images spanning dozens of crop/disease categories
- **Pest Detection** (YOLOv8, 5 classes): **98.3% mAP@50**, 98.7% precision, 95.6% recall
- **Weed Detection** (YOLOv8): **95.1% mAP@50**, 96.1% precision, 91.1% recall — GPU inference measured at 4.4–9.9ms/image (Tesla P100; not yet benchmarked on an edge device)
- **Conversational Assistant** (RAG-based chatbot for farmer Q&A) — built by the team alongside the vision models

**My role — model integration & serving:** Owned the **FastAPI serving layer**. Received the trained CV and chatbot models from teammates after their training runs, validated their outputs against held-out data, tuned inference behavior (thresholds, batching, error handling), and wired them into the backend that a separate teammate had scaffolded.

**Result:** Overall graduation grade **Excellent (A+)**. Per-model accuracy above is independently verified from training run outputs; the FastAPI integration and edge-latency claims are scoped to what I directly built and tested, not the full team's frontend/backend stack.

`PyTorch` `TensorFlow` `YOLOv8` `OpenCV` `FastAPI` `Docker`

---

### 🏢 RAG-Based Document Intelligence
**Problem:** Answer questions over policy/knowledge-base documents without pulling in a heavyweight orchestration framework.

- Built custom chunking + sliding-window segmentation for dense documents
- Dense retrieval via SentenceTransformers embeddings + local FAISS index
- Structured tool-calling against the OpenAI SDK to keep answers grounded in retrieved context only

**Result:** A lightweight, containerized document Q&A assistant with deterministic, source-constrained responses.

`Python` `SentenceTransformers` `FAISS` `OpenAI SDK` `Streamlit` `Docker`

---

### 🏥 Healthcare Recommendation Engine *(Team Project, 4 members)*
**Problem:** Generate multi-specialty clinical recommendations from large, heterogeneous patient histories.

- **My role:** distributed ingestion design (Apache Spark 3.5) and distributed storage (Hadoop HDFS)
- Contributed to hybrid collaborative + content-based recommendation logic (LightGBM/XGBoost)
- Workflows automated end-to-end via Apache Airflow DAGs

**Scale:** 500k+ patient profiles processed through the pipeline.

`Apache Spark` `Hadoop HDFS` `LightGBM` `XGBoost` `Airflow` `ClickHouse`

---

## 💼 Experience

**Data Science Lead Trainer** — AXIS Tech Community · *May 2025 – Present*
Designed and delivered ML/Data Science curriculum to 100+ students (regression, classification, SQL, validation methodology).

**Data Science Intern** — Pure Soft · *Dec 2025 – Feb 2026*
Built EDA and feature-engineering pipelines on 100k+ customer records; fine-tuned tree-based models; deployed via containerized FastAPI.

**AI Intern** — Aitronix · *Sep 2025 – Nov 2025*
Centralized model lifecycle management on Azure ML with tracked artifacts via Azure Blob Storage.

---

## 🎓 Education

**B.Sc. Computer Science & Artificial Intelligence** — Benha University *(July 2025)*
Graduation Project: *Napta — Agricultural Vision Suite*, Grade: **Excellent (A+)**

**Training Tracks:** Data Science & Analytics · Machine Learning Engineering · Deep Learning & Computer Vision · Big Data Engineering (Spark/Hadoop/Airflow)

---

## 🧰 Stack

<p align="center">
<img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,docker,fastapi,git,github,postgres,mysql,linux,vscode" />
</p>

---

## 🚀 Currently

- Building production-grade AI applications with honest, defensible benchmarks
- Deepening MLOps practice: reproducible pipelines, containerized serving, CI/CD
- Open to AI Engineer / Data Scientist roles across Egypt, Saudi Arabia, and the UAE
