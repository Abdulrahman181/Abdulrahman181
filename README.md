<div align="center">

# Abdulrahman Ahmed

### AI Engineer · Machine Learning Engineer · Data Scientist

I design and build applied AI systems that connect **data engineering, machine learning, model evaluation, and deployment**. My focus is turning experimental models into understandable, testable, and usable software—with clear assumptions and metrics that can be defended in a technical interview.

**Based in Benha, Egypt · Open to AI/ML opportunities in Egypt, Saudi Arabia, the UAE, and remote teams**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

---

## Professional Focus

- **Applied Machine Learning:** classification, ranking, imbalanced learning, feature engineering, model evaluation, and cross-validation.
- **Computer Vision:** image classification and object detection with PyTorch, TensorFlow, OpenCV, and YOLOv8.
- **Data & MLOps:** distributed processing, workflow orchestration, experiment tracking, containerized services, and reproducible pipelines.
- **NLP & Generative AI:** embeddings, semantic search, retrieval-augmented generation, local LLM inference, and source-aware responses.
- **Production Thinking:** designing around data quality, split strategy, leakage prevention, threshold trade-offs, latency, and maintainability.

## Selected Evidence

| Project area | Audited result |
| --- | --- |
| Fraud detection | **0.9519 ROC-AUC** on a chronological PaySim holdout containing **1,272,524 transactions** |
| Pest detection | **0.9834 mAP@50** on a **3,000-image validation split** |
| Weed detection | **0.9512 mAP@50** on a **1,655-image validation split** |
| Plant-disease classification | **0.9963 validation accuracy** on **15,231 images across 33 classes** |
| Healthcare data pipeline | **11,679 patient rows** and millions of related synthetic clinical-event rows processed through a distributed pipeline |

> Metrics are labeled with their actual split. Validation and holdout results are not presented as production performance or as a substitute for an untouched external test set.

## Featured Projects

### Financial Fraud Detection

An imbalanced-learning system built on the PaySim dataset to identify fraudulent transactions while making the precision/recall trade-off explicit.

- Audited dataset size: **6,362,620 transactions**, including **8,213 fraud cases** (**0.129082%**).
- Verified **0 duplicate rows** and no missing values in the loaded dataset.
- Used a chronological, step-ordered split rather than a random split.
- Engineered time, amount, transaction-type, user-history, and destination features using training-derived statistics where applicable.
- Trained XGBoost, LightGBM, and CatBoost models.
- Combined model probabilities with explicit weights: XGBoost **30%**, LightGBM **30%**, CatBoost **40%**.
- Achieved **0.951918 ROC-AUC** on the chronological holdout and **0.966423 ROC-AUC** on the training sample.
- The train/holdout gap was **0.014505 AUC**, equivalent to **1.45 percentage points**.

At the notebook’s F1-selected threshold of **0.981419**, the holdout produced **60.8% precision** and **36.4% recall**. Because the threshold was selected on that holdout in the current notebook, these operating-point metrics are reported transparently and should not be interpreted as an untouched final estimate.

`Python` `Pandas` `Scikit-learn` `XGBoost` `LightGBM` `CatBoost` `Gradio`

[View the project →](https://github.com/Abdulrahman181/AI-Powered-Financial-Fraud-Detection-System)

### Healthcare Recommendation System

A distributed, synthetic-EHR recommendation-pipeline prototype built with Synthea data. The system is designed as an engineering project—not as clinically validated medical decision support.

- Generates reproducible synthetic data with Synthea using a fixed seed and a configured population of **10,000 patients**.
- The committed exploration notebook reports **11,679 patient rows** plus millions of related rows across conditions, medications, observations, encounters, and procedures.
- Ingests data into **Hadoop HDFS** and **ClickHouse**.
- Uses **Apache Spark 3.5.3** for cleaning and feature engineering.
- Orchestrates stages with **Apache Airflow** and tracks experiments with **MLflow**.
- Implements Spark ALS collaborative filtering, TF-IDF content-based recommendation, and an XGBoost hybrid model.
- Exposes recommendation services through Flask and Streamlit within a Docker Compose environment.

`Apache Spark 3.5.3` `Hadoop HDFS` `ClickHouse` `Airflow` `MLflow` `XGBoost` `Docker` `Flask` `Streamlit`

[View the project →](https://github.com/amr-algazzar12/healthcare-recommendation-system)

### Napta — Agricultural AI Platform

A graduation project developed by a six-person team to support agricultural image analysis and farmer-oriented assistance.

The available public evidence supports describing Napta as a team project involving agricultural computer vision and an assistant. Detailed claims about my individual FastAPI ownership and the project’s full model metrics are intentionally not presented here until the corresponding project repository or direct implementation artifacts are publicly available for verification.

`Computer Vision` `Deep Learning` `FastAPI` `Agricultural AI`

### Pest Detection

A YOLOv8 object-detection experiment evaluated on a validation split of **3,000 images** and **5,929 labeled instances**.

- **98.34% mAP@50**
- **98.75% precision**
- **95.63% recall**
- **86.35% mAP@50:95**

`Python` `Ultralytics` `YOLOv8` `PyTorch` `OpenCV`

[View the project →](https://github.com/Abdulrahman181/pest-detection)

### Weed Detection

A YOLOv8 object-detection experiment evaluated on a validation split of **1,655 images** and **4,250 labeled instances**.

- **95.12% mAP@50**
- **96.06% precision**
- **91.06% recall**
- **81.14% mAP@50:95**
- A recorded single-image run reported **9.9 ms inference** at 640×640 on a Tesla P100 environment; this is not an edge-device benchmark.

`Python` `Ultralytics` `YOLOv8` `PyTorch` `OpenCV`

[View the project →](https://github.com/Abdulrahman181/weed-detection)

### Plant-Disease Classification

A PlantVillage image-classification experiment using a 33-class validation setup.

- **99.63% validation accuracy** on **15,231 images**.
- The result is explicitly labeled as validation accuracy; it is not presented as untouched test accuracy.
- Dataset and experiment variants are kept separate because another notebook in the same project uses a different 39-class, 7,800-image split and reports a materially different result.

`Python` `TensorFlow` `Keras` `CNN` `OpenCV` `Scikit-learn`

[View the project →](https://github.com/Abdulrahman181/Classification-of-plant-diseases)

### Smart Document Assistant

A local document question-answering application that combines retrieval with local LLM inference.

- Uses SentenceTransformers embeddings and a local FAISS index.
- Retrieves the top three relevant documents for a question.
- Uses a local Llama-based model through CTransformers.
- Displays source-document references in the Streamlit interface.
- Uses a context-constrained prompt that instructs the assistant to answer only from retrieved context.

The implementation supports a **source-aware RAG design**. No unsupported claim is made that the system eliminates hallucinations, and no numerical answer-quality benchmark is claimed.

`Python` `SentenceTransformers` `FAISS` `CTransformers` `Llama` `Streamlit` `LangChain`

[View the project →](https://github.com/Abdulrahman181/Smart-Document-Assistant)

## Experience

**Data Science Lead Trainer — AXIS Tech Community**<br>
*May 2025 – Present*

Design and deliver practical machine-learning and data-science training for **100+ students**, covering regression, classification, SQL, feature engineering, and model validation.

**Data Science Intern — Pure Soft**<br>
*Dec 2025 – Feb 2026*

Built EDA and feature-engineering pipelines for **100K+ customer records**, fine-tuned tree-based models, and deployed inference through containerized FastAPI services.

**AI Intern — Aitronix**<br>
*Sep 2025 – Nov 2025*

Worked with Azure ML to organize model-lifecycle workflows and track artifacts through Azure Blob Storage.

## Technical Stack

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,pytorch,tensorflow,sklearn,docker,fastapi,git,github,postgres,mysql,linux,vscode" alt="Technical stack icons" />
</p>

**Machine Learning:** Scikit-learn · XGBoost · LightGBM · CatBoost · Model evaluation · Imbalanced learning · Ranking metrics · Cross-validation<br>
**Computer Vision:** PyTorch · TensorFlow · Keras · YOLOv8 · OpenCV · Albumentations · Transfer learning<br>
**NLP & GenAI:** SentenceTransformers · FAISS · RAG · Embeddings · Local LLM inference · LangChain<br>
**Data Engineering:** Pandas · Apache Spark · Hadoop HDFS · ClickHouse · SQL<br>
**MLOps & Delivery:** Airflow · MLflow · Docker · FastAPI · Flask · Streamlit · GitHub Actions · Azure ML<br>
**Databases & Tools:** PostgreSQL · MySQL · Linux · Git · GitHub

## Education

**B.Sc. in Computer Science and Artificial Intelligence — Benha University**<br>
*July 2025 · Graduation Project: Napta Agricultural AI Platform · Grade: Excellent (A+)*

Additional training in Data Science and Analytics, Machine Learning Engineering, Deep Learning and Computer Vision, and Big Data Engineering.

## Engineering Principles

- **Measure the right thing:** choose metrics that match the problem, especially under class imbalance.
- **Respect the split:** distinguish training, validation, holdout, and test data clearly.
- **Make claims traceable:** connect public results to code, outputs, and reproducible experiments.
- **Build for use:** treat serving, error handling, monitoring, and maintainability as part of the ML system.
- **Communicate trade-offs:** explain what a model does well, where it can fail, and what remains unverified.

## Currently Focused On

- Building reliable AI applications from data preparation through deployment.
- Improving MLOps practices with reproducible pipelines, experiment tracking, CI/CD, and containerized serving.
- Strengthening system design for scalable machine-learning products.
- Developing evaluation protocols that separate model quality from optimistic experimentation.

---

<div align="center">

**Open to collaborating on applied AI, machine learning, computer vision, data engineering, and MLOps projects.**

</div>
