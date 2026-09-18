<div align="center">

# Abdulrahman Ahmed

### AI Engineer · Machine Learning Engineer · Data Scientist

I build applied AI and machine-learning systems across the lifecycle—from **data preparation and model development to evaluation, serving, and deployment**. My work spans **computer vision, NLP and retrieval-augmented generation, ML pipelines, and practical AI applications**, with a focus on **reproducibility, clear assumptions, and measurable model performance**.

**Based in Benha, Egypt · Open to AI/ML opportunities across Egypt, Saudi Arabia, the UAE, and remote roles**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/abdul-rahman-ahmed-711565255)
[![Email](https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:abdulrahmannassar202@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Abdulrahman181)

</div>

---

## Professional Focus

- **Model Development & Evaluation:** classification, ranking, feature engineering, imbalanced learning, cross-validation, and rigorous model evaluation.
- **Computer Vision:** image classification, object detection, semantic segmentation, transfer learning, image preprocessing, and inference workflows.
- **NLP, Generative AI & Agents:** embeddings, semantic retrieval, document question answering, retrieval-augmented generation, local LLM applications, agentic workflows, and tool-assisted AI workflows.
- **Data & ML Workflows:** data preparation, exploratory analysis, SQL, distributed processing, experiment tracking, and workflow automation.
- **AI Application Delivery:** model serving, API integration, containerization, reproducible workflows, and connecting AI models and retrieval systems to usable applications.

## Selected Evidence

| Project area | Audited result |
| --- | --- |
| Fraud detection | **0.9519 ROC-AUC** on a chronological PaySim holdout containing **1,272,524 transactions** |
| AI application engineering | Collaborative resume-analysis workflow covering document processing, structured evidence extraction, requirement matching, retrieval, and guided career interactions; repository link requires verification |
| Distributed ML/data systems | Synthetic Synthea EHR workflow using Spark, HDFS, ClickHouse, Airflow, MLflow, multiple recommendation approaches, and API/dashboard serving |
| Semantic segmentation | **0.5387 validation mIoU** and **0.7002 validation Dice** on an 8-class Cityscapes U-Net experiment |

Metrics are labeled with their actual evaluation split. Validation and chronological-holdout results are reported as project-level experimental evidence—not as production performance or a substitute for an untouched external test set. Collaborative projects are not presented as individually owned unless the repository evidence establishes individual ownership.

## Selected Projects

A focused selection of applied AI/ML work spanning machine learning, AI application engineering, distributed ML/data systems, and computer vision.

### Financial Fraud Detection System

A personal machine-learning project for detecting rare fraudulent transactions under severe class imbalance and chronological evaluation constraints.

* Analyzed the PaySim dataset with **6.36M transactions** and **8,213 fraud cases** (~**0.129%**).
* Engineered behavior- and risk-oriented features from transaction timing, amount, sender activity, recipient activity, and transaction type.
* Trained and combined **XGBoost, LightGBM, and CatBoost** using a weighted ensemble.
* Achieved **0.9519 ROC-AUC on a chronological holdout of 1,272,524 transactions**.

**Technologies:** Python, Pandas, scikit-learn, XGBoost, LightGBM, CatBoost, Jupyter

[View the project →](https://github.com/Abdulrahman181/AI-Powered-Financial-Fraud-Detection-System)

### AI Resume Analyzer

A collaborative AI application focused on resume and job-document workflows, structured evidence extraction, requirement matching, retrieval, and guided career interactions.

* Designed around the workflow from **document ingestion and structured extraction to requirement matching, retrieval, and guided responses**.
* Separates required and preferred job requirements to make matching results more explicit and interpretable.
* Connects backend services, data persistence, retrieval, application workflows, and controlled AI responses.
* The referenced repository returned **404 during review**; implementation-level details and individual contributions should be confirmed after the public repository link is restored or corrected.

**Technologies:** FastAPI, SQLite, SQLAlchemy, HTML/CSS, Vanilla JavaScript, RAG, information retrieval

[View the project →](https://github.com/AnasOsama2/AI-Resume-Analyzer)

### Healthcare Recommendation System

A collaborative engineering project for building recommendation workflows over synthetic electronic-health-record data.

* Processes synthetic **Synthea** data using **Apache Spark 3.5.3**, Hadoop HDFS, and ClickHouse.
* Implements multiple recommendation approaches, including **Spark ALS, TF-IDF content-based recommendation, and an XGBoost hybrid model**.
* Orchestrates ingestion, processing, training, evaluation, and model-serving workflows with **Apache Airflow** and tracks experiments with **MLflow**.
* Exposes recommendations through a **Flask REST API** and Streamlit interface within a Docker Compose environment.

> Uses synthetic data and is presented as an engineering prototype, not as clinically validated medical decision support.

**Technologies:** Python, Apache Spark, PySpark, Hadoop HDFS, ClickHouse, Airflow, MLflow, Flask, Streamlit, Docker Compose

[View the project →](https://github.com/amr-algazzar12/healthcare-recommendation-system)

### Urban Scene Semantic Segmentation with U-Net

A personal computer-vision project for pixel-level semantic segmentation of urban driving scenes using a U-Net encoder-decoder architecture.

* Trained a U-Net model on the **Cityscapes** dataset across **8 semantic classes**.
* Implemented image-mask preprocessing, class-label conversion, training, validation, inference, and qualitative visualization.
* Used skip connections to preserve spatial information for pixel-level class prediction.
* Recorded **0.5387 validation mIoU** and **0.7002 validation Dice** in the saved notebook evaluation output; no independent test-set result is claimed.

**Technologies:** Python, TensorFlow/Keras, U-Net, Cityscapes, NumPy, Matplotlib, Jupyter

[View the project →](https://github.com/Abdulrahman181/Self-Driving-Car-Semantic-Segmentation-using-U-Net)

## Professional Experience

**AI Trainer — MFC** | Aug 2026 – Present

* Deliver structured Artificial Intelligence training for students, progressing from **fundamental concepts and core foundations to advanced AI topics and practical implementation**.
* Build students’ technical understanding through a combination of **conceptual foundations, hands-on development, problem solving, and project-based learning**.
* Guide students in translating AI concepts into practical solutions and applying structured development workflows to real-world problem scenarios.

**Data Science Trainer — AXIS Tech Community** | Jan 2025 – Present

* Deliver practical Data Science training covering **Python, SQL, Machine Learning, data analysis, and project development**.
* Design and deliver technical sessions that connect data science principles with **practical implementation, analytical reasoning, and project-based problem solving**.
* Guide learners throughout project development, covering **data preparation, exploratory analysis, model development, evaluation, and solution implementation**.
* Review and support technical projects with emphasis on **problem formulation, analytical thinking, model selection, implementation quality, and practical application**.

## Technical Internships

**AI Intern — Aitronix** | Sep 2025 – Nov 2025 | Remote

* Contributed to applied AI projects across **Computer Vision, Natural Language Processing, and Machine Learning**, working with different approaches according to project requirements.
* Contributed to AI development workflows involving **data handling, model experimentation, and integration of AI capabilities into application systems**.
* Worked with **Azure Machine Learning** for experiment tracking and model registration, alongside **Azure Blob Storage** for cloud-based data handling.

**Data Science Intern — Pure Soft** | Dec 2025 – Feb 2026 | On-site

* Collected and transformed data from multiple web sources using **web scraping**, producing structured datasets for data science and machine learning applications.
* Worked across data preparation workflows including **data acquisition, cleaning, transformation, structuring, and preparation for downstream analysis and modeling**.
* Developed **recommendation system and chatbot solutions**, applying processed data within practical AI-driven applications.
* Contributed across the solution development workflow from **data acquisition and preparation through machine learning implementation and backend/API integration**.

## Certifications & Professional Training

**Digital Egypt Pioneers Program (DEPI) — AI & Data Science Track** | MCIT | 6-Month Program

**Agentic AI Track** | ITI | 3-Month Program

**HCIA-AI V3.5 & V4.0** | Huawei Academy

**HCIA-Big Data V3.5 & V4.0** | Huawei Academy

**Artificial Intelligence Training** | NTI | 120 Hours

**Machine Learning Training** | NTI | 72 Hours

**Computer Vision Training** | NTI | 72 Hours

**Egyptian Talent Academy — AI Track** | NTI & Huawei

**Agentic AI Track** | Digital Hub | 5-Week Program

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
