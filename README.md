<div align="center">

# Abdulrahman Ahmed

### AI Engineer · Machine Learning Engineer · Data Scientist

**Generative AI · RAG · Agentic AI · Computer Vision**

I develop AI and machine-learning systems across **data preparation, model development, evaluation, and application integration**. My work spans **machine learning, computer vision, NLP, retrieval-augmented generation, and AI application workflows**.

**Based in Benha, Egypt · Open to AI/ML opportunities in Egypt, across the Gulf, and remotely**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

---

## Professional Focus

- **Machine Learning:** model development, feature engineering, imbalanced learning, model selection, validation, and evaluation.
- **Computer Vision:** object detection, semantic segmentation, image preprocessing, augmentation, and inference.
- **Generative AI & Retrieval:** embeddings, semantic retrieval, RAG, document question answering, and LLM applications.
- **Agentic AI:** agent workflows, task decomposition, tool calling, context retrieval, and multi-step execution.
- **AI Engineering:** model integration, API development, model serving, application integration, and containerization.

## Selected Evidence

| Project Area | Evidence |
| --- | --- |
| Fraud detection | **0.9519 ROC-AUC** on a chronological PaySim holdout containing **1,272,524 transactions** |
| Agricultural AI | Three computer-vision models for plant disease, harmful weeds, and agricultural pests, with database-backed agricultural information and a RAG-based application layer |
| AI application engineering | Collaborative resume-analysis workflow combining document processing, structured extraction, requirement matching, retrieval, and guided career interactions |
| Distributed ML/data systems | Synthetic Synthea EHR workflow using **Spark, HDFS, ClickHouse, Airflow, and MLflow**, with multiple recommendation approaches and API/dashboard serving |
| Semantic segmentation | **0.5387 validation mIoU** and **0.7002 validation Dice** from an 8-class Cityscapes U-Net evaluation |

> Reported metrics reflect the stated evaluation split and should not be interpreted as production performance.

## Selected Projects

A selection of applied AI projects covering computer vision, machine learning, retrieval-based applications, and data-intensive recommendation systems.

### Napta Agricultural AI Platform

A collaborative agricultural AI platform where I led the **AI development workstream**, combining three computer-vision models, database-backed agricultural knowledge, and a RAG-based application layer.

- Led the AI workstream of the graduation project, translating agricultural requirements into three computer-vision models and the supporting AI application workflow.
- Developed a plant-disease detection model covering **12 crop disease profiles**, with its outputs connected to a database containing related agricultural information and treatment guidance.
- Developed a harmful-weed detection and classification model, connected to a database containing the corresponding weed information.
- Developed an agricultural-pest detection and classification model, connected to a database containing the corresponding pest information.
- Evaluated YOLO model variants from **v5 through v12** across the computer-vision models, comparing training configurations, validation results, inference behavior, and model stability.
- Expanded the training data through additional collection, preprocessing, and augmentation, followed by iterative retraining and evaluation.
- Used deployment and inference testing to compare candidate configurations under application runtime conditions before integration.
- Integrated the models with **OpenCV, Albumentations, FastAPI, and Docker**, and connected their database-backed outputs to the project's **RAG layer** for contextual agricultural assistance.

**Technologies:** Python, PyTorch, YOLO, OpenCV, Albumentations, FastAPI, Docker, RAG

### Financial Fraud Detection System

A personal machine-learning project for detecting rare fraudulent transactions under severe class imbalance and chronological evaluation constraints.

- Analyzed **6.36M PaySim transactions**, including **8,213 fraud cases** (~**0.129%**).
- Engineered features from transaction timing, amounts, user activity, recipient activity, and transaction types.
- Addressed class imbalance through downsampling and model-specific class-weighting strategies.
- Trained **XGBoost, LightGBM, and CatBoost** models and combined them through a weighted ensemble.
- Achieved **0.9519 ROC-AUC** on a chronological holdout containing **1,272,524 transactions**.

**Technologies:** Python, Pandas, scikit-learn, XGBoost, LightGBM, CatBoost, Jupyter

[View the project →](https://github.com/Abdulrahman181/AI-Powered-Financial-Fraud-Detection-System)

### AI Resume Analyzer

A collaborative AI application for resume analysis, job matching, retrieval, and career assistance.

- Contributed to a workflow combining **document processing, structured extraction, deterministic requirement matching, retrieval, and AI-generated responses**.
- Helped structure job requirements into **required and preferred criteria** to support explicit matching and skill-gap analysis.
- Worked across **FastAPI services, SQLite persistence, retrieval components, and AI-driven application workflows**.
- Contributed to separating **resume evidence, job requirements, and retrieved guidance** into distinct sources of context.

**Technologies:** FastAPI, SQLite, SQLAlchemy, HTML/CSS, Vanilla JavaScript, RAG, Information Retrieval

[View the project →](https://github.com/AnasOsama2/AI-Resume-Analyzer)

### Healthcare Recommendation System

A collaborative engineering project for recommendation workflows over synthetic electronic-health-record data.

- Processed synthetic **Synthea** data using **Apache Spark 3.5.3, Hadoop HDFS, and ClickHouse**.
- Implemented three recommendation approaches: **ALS collaborative filtering, TF-IDF content-based recommendation, and an XGBoost hybrid approach**.
- Integrated **Apache Airflow** for workflow orchestration and **MLflow** for experiment tracking and model lifecycle management.
- Exposed recommendation results through a **Flask REST API and Streamlit dashboard** within a Docker Compose environment.

> Uses synthetic data and is presented as an engineering prototype, not clinically validated medical decision support.

**Technologies:** Apache Spark, PySpark, Hadoop HDFS, ClickHouse, Airflow, MLflow, Flask, Streamlit, Docker Compose

[View the project →](https://github.com/amr-algazzar12/healthcare-recommendation-system)

### Urban Scene Semantic Segmentation with U-Net

A personal computer-vision project for pixel-level semantic segmentation of urban driving scenes using a U-Net encoder-decoder architecture.

- Trained a U-Net model on the **Cityscapes** dataset across **8 semantic classes**.
- Implemented image-mask preprocessing, class-label conversion, training, validation, inference, and qualitative result visualization.
- Used U-Net skip connections to preserve spatial information for pixel-level prediction.
- Recorded **0.5387 validation mIoU** and **0.7002 validation Dice** in the saved notebook evaluation output; no independent test-set result is claimed.

**Technologies:** Python, TensorFlow/Keras, U-Net, Cityscapes, NumPy, Matplotlib, Jupyter

[View the project →](https://github.com/Abdulrahman181/Self-Driving-Car-Semantic-Segmentation-using-U-Net)

## Professional Experience

**AI Trainer — MFC** | Aug 2026 – Present

- Deliver structured Artificial Intelligence training from foundational concepts through advanced topics, combining technical instruction with hands-on implementation.
- Lead practical exercises and project-based development, helping learners translate AI concepts into working solutions.
- Guide learners through AI development workflows, from experimentation and problem solving to implementation in practical projects.

**Data Science Trainer — AXIS Tech Community** | Jan 2025 – Present

- Deliver practical Data Science training covering **data analysis, SQL, Machine Learning, and project development**.
- Guide learners through analytical problem solving and hands-on implementation across structured projects.
- Support projects across **data preparation, exploratory analysis, model development, evaluation, and implementation**.

## Technical Internships

**AI Intern — Aitronix** | Sep 2025 – Nov 2025 | Remote

- Contributed to AI projects across **Computer Vision, Natural Language Processing, and Machine Learning**, supporting data preparation, model experimentation, and application integration.
- Used **Azure Machine Learning** for experiment tracking and model registration, alongside **Azure Blob Storage** for cloud-based data handling.

**Data Science Intern — Pure Soft** | Dec 2025 – Feb 2026 | On-site

- Collected, cleaned, transformed, and structured data from multiple web sources using **web scraping** for analysis and machine-learning workflows.
- Contributed to **recommendation-system and chatbot solutions**, including backend and API integration.
- Supported the workflow from data acquisition and preparation through model development and application integration.

## Certifications & Professional Training

**Digital Egypt Pioneers Program (DEPI) — AI & Data Science Track** | MCIT | 6-Month Program

**HCIA-AI V3.5 & V4.0** | Huawei Academy

**HCIA-Big Data V3.5 & V4.0** | Huawei Academy

**Agentic AI Track** | ITI | 3-Month Program

**Artificial Intelligence Training** | NTI | 120 Hours

**Machine Learning Training** | NTI | 72 Hours

**Computer Vision Training** | NTI | 72 Hours

**Agentic AI Track** | Digital Hub | 5-Week Program

**Egyptian Talent Academy — AI Track** | NTI & Huawei

## Technical Capabilities

### Machine Learning & Data Science

`Data Analysis` · `SQL` · `Model Development` · `Feature Engineering` · `Model Selection` · `Ensemble Learning` · `Imbalanced Learning` · `Cross-validation` · `Hyperparameter Optimization` · `Error Analysis`

### Deep Learning & Computer Vision

`Neural Network Modeling` · `CNN Architectures` · `Transfer Learning` · `Object Detection` · `Image Classification` · `Semantic Segmentation` · `Inference Pipelines`

### NLP, Generative AI & Retrieval

`Text Representation` · `Embeddings` · `Semantic Retrieval` · `Vector Search` · `RAG Systems` · `Document Question Answering` · `LLM Applications`

### Agentic AI

`Agent Workflows` · `Task Decomposition` · `Tool Calling` · `Context & Retrieval` · `Multi-step Execution`

### AI Engineering

`AI System Design` · `Model & Retrieval Integration` · `API Engineering` · `Model Serving` · `Document Processing` · `Containerized AI Systems`

### Data, MLOps & Cloud

`Data Pipeline Engineering` · `Distributed Data Processing` · `Workflow Orchestration` · `Analytical Data Systems` · `Experiment Tracking` · `Model Lifecycle Management` · `Cloud ML Workflows`

## Education

**B.Sc. in Computer Science and Artificial Intelligence — Benha University**<br>
*July 2025 · Graduation Project: Napta Agricultural AI Platform*

## Currently Focused On

- Building practical AI systems that connect **models, retrieval, APIs, and deployment**.
- Advancing **Generative AI, RAG, and Agentic AI** through application-level workflows and tool interaction.
- Strengthening **MLOps and AI delivery** through reproducible workflows, experiment tracking, and containerized serving.

---

<div align="center">

**Open to collaborating on practical AI, machine learning, Generative AI, and computer-vision projects.**

</div>
