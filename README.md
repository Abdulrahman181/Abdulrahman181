<div align="center">

# Abdulrahman Ahmed

### AI Engineer · Machine Learning Engineer

**Generative AI · RAG · Agentic AI · Computer Vision**

I build AI systems across **model development, evaluation, retrieval, and application integration**. My work spans **machine learning, computer vision, NLP, Generative AI, RAG, and agentic workflows**, with a focus on turning experiments into **usable AI applications**.

**Based in Benha, Egypt · Open to AI/ML opportunities in Egypt, across the Gulf, and remotely**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

---

## Professional Focus

I work across the AI/ML lifecycle, from **data preparation and model development to evaluation, retrieval, and application integration**.

### Core Areas

- **Machine Learning** — supervised learning, ensemble methods, feature engineering, model evaluation, and imbalanced-data workflows
- **Computer Vision** — image classification, object detection, and semantic segmentation
- **NLP & Generative AI** — LLM applications, embeddings, semantic retrieval, RAG, and retrieval-grounded generation
- **Agentic AI** — agent workflows, task routing, tool use, multi-step execution, and workflow orchestration
- **AI Engineering** — API-based AI applications, modular architectures, testing, containerization, and deployment-oriented development
- **Data & MLOps** — data pipelines, experiment tracking, reproducible workflows, and cloud ML workflows

## Selected Evidence

| Project Area | Evidence |
| --- | --- |
| Fraud detection | **0.9519 ROC-AUC** on a chronological PaySim holdout containing **1,272,524 transactions** |
| Agentic AI & RAG | Multi-agent HR and IT assistant using **LangGraph**, with a supervisor routing queries between specialized agents |
| AI application engineering | Collaborative resume-analysis application combining **document processing, structured extraction, requirement matching, retrieval, and AI-assisted workflows** |
| Distributed ML & data systems | Synthetic Synthea EHR workflow using **Spark, HDFS, ClickHouse, Airflow, and MLflow**, with multiple recommendation approaches and API/dashboard serving |
| Semantic segmentation | **0.5387 validation mIoU** and **0.7002 validation Dice** from an 8-class Cityscapes U-Net evaluation |

> Reported metrics reflect the stated evaluation split and should not be interpreted as production performance.

## Selected Projects

A selection of applied AI projects covering computer vision, machine learning, retrieval-based applications, and data-intensive recommendation systems.

### Napta Agricultural AI Platform

A collaborative graduation project applying **computer vision and retrieval-augmented AI** to practical agricultural problems.

- Led the **AI development workstream**, owning the computer-vision solutions and their integration into the wider AI application.
- Developed and evaluated workflows for **plant disease detection, agricultural pest detection and classification, and harmful weed detection/classification**.
- Built a plant-disease detection workflow covering **12 crop disease profiles**, with predictions connected to database-backed agricultural knowledge.
- Prepared and augmented image data, implemented preprocessing and inference workflows, and iterated across model configurations and YOLO variants.
- Integrated the vision components with **OpenCV, Albumentations, FastAPI, and Docker** for application-level inference.
- Connected model predictions to the project's agricultural knowledge and **RAG-based assistance workflow**, enabling contextual user-facing responses.

**Technologies:** Python · PyTorch · YOLO · OpenCV · Albumentations · FastAPI · Docker · RAG

### Financial Fraud Detection System

A personal machine-learning project focused on detecting rare fraudulent transactions under severe class imbalance and chronological evaluation constraints.

- Analyzed **6.36M PaySim transactions**, including **8,213 fraud cases** (~**0.129%** of all transactions).
- Engineered features from **transaction timing, amounts, user activity, recipient activity, and transaction types**.
- Addressed severe class imbalance using **downsampling and model-specific class-weighting strategies**.
- Trained and compared **XGBoost, LightGBM, and CatBoost** models for fraud detection.
- Combined the individual models into a **weighted ensemble** to improve predictive performance.
- Evaluated the final ensemble on a **chronological holdout containing 1,272,524 transactions**, achieving **0.9519 ROC-AUC**.

**Technologies:** Python, Pandas, scikit-learn, XGBoost, LightGBM, CatBoost, Jupyter

[View the project →](https://github.com/Abdulrahman181/AI-Powered-Financial-Fraud-Detection-System)

### AI Resume Analyzer

A collaborative AI application for resume analysis, job matching, retrieval, and career assistance.

- Contributed to a workflow combining **document processing, structured extraction, deterministic requirement matching, retrieval, and AI-assisted responses**.
- Helped structure job requirements into **required and preferred criteria** to support explicit matching and skill-gap analysis.
- Worked across **FastAPI services, SQLite persistence, retrieval components, and AI-driven application workflows**.
- Contributed to separating **resume evidence, job requirements, and retrieved guidance** into distinct sources of context.

**Technologies:** FastAPI, SQLite, SQLAlchemy, HTML/CSS, Vanilla JavaScript, RAG, Information Retrieval

[View the project →](https://github.com/Abdulrahman181/AI-Resume-Analyzer-development)

### Healthcare Recommendation System

A collaborative engineering project for recommendation workflows over synthetic electronic health record data.

- Processed synthetic **Synthea** electronic health record data using **Apache Spark 3.5.3, Hadoop HDFS, and ClickHouse**.
- Implemented and evaluated three recommendation approaches: **ALS collaborative filtering, TF-IDF content-based recommendation, and an XGBoost hybrid approach**.
- Integrated **Apache Airflow** for workflow orchestration and **MLflow** for experiment tracking and model lifecycle management.
- Exposed recommendation results through a **Flask REST API and Streamlit dashboard**.
- Containerized the application workflow using **Docker Compose** for reproducible local execution.

> Uses synthetic data and is presented as an engineering prototype, not clinically validated medical decision support.

**Technologies:** Apache Spark · PySpark · Hadoop HDFS · ClickHouse · Airflow · MLflow · Flask · Streamlit · Docker Compose

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

`Data Analysis` · `SQL` · `Model Development` · `Feature Engineering` · `Model Selection` · `Ensemble Learning` · `Imbalanced Learning` · `Model Validation` · `Hyperparameter Optimization` · `Model Evaluation`

### Deep Learning & Computer Vision

`Neural Network Modeling` · `CNN Architectures` · `Object Detection` · `Image Classification` · `Semantic Segmentation` · `Image Preprocessing` · `Data Augmentation` · `Inference Pipelines`

### NLP, Generative AI & Retrieval

`Text Representation` · `Embeddings` · `Semantic Retrieval` · `Vector Search` · `RAG Systems` · `Document Question Answering` · `LLM Applications`

### Agentic AI

`Agent Workflows` · `Task Decomposition` · `Tool Calling` · `Context & Retrieval` · `Multi-step Execution`

### AI Engineering

`AI Application Integration` · `Model & Retrieval Integration` · `API Development` · `Model Serving` · `Document Processing` · `Containerized AI Systems`

### Data, MLOps & Cloud

`Data Pipeline Engineering` · `Distributed Data Processing` · `Workflow Orchestration` · `Data Processing & Analytical Systems` · `Experiment Tracking` · `Model Registration` · `Cloud ML Workflows` · `Containerized ML Workflows`

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
