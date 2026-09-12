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

- **Model Development & Evaluation:** classification, ranking, feature engineering, imbalanced learning, cross-validation, and rigorous evaluation.
- **Computer Vision:** image classification, object detection, transfer learning, image preprocessing, and inference workflows.
- **NLP & Retrieval:** embeddings, semantic search, document question answering, retrieval-augmented generation, and local language-model applications.
- **Data & ML Workflows:** data preparation, exploratory analysis, SQL, distributed processing, experiment tracking, and workflow automation.
- **AI Application Delivery:** model serving, API integration, containerization, reproducible workflows, and connecting trained models to usable applications.

## Selected Evidence

| Project area | Audited result |
| --- | --- |
| Fraud detection | **0.9519 ROC-AUC** on a chronological PaySim holdout containing **1,272,524 transactions** |
| Pest detection | **0.9834 mAP@50** on a **3,000-image validation split** |
| Weed detection | **0.9512 mAP@50** on a **1,655-image validation split** |
| Plant-disease classification | **0.9963 validation accuracy** on **15,231 images across 33 classes** |
| Healthcare data pipeline | **11,679 patient rows** and millions of related synthetic clinical-event rows processed through a distributed pipeline |

> Metrics are labeled with their actual evaluation split. Validation and chronological-holdout results are reported as project-level experimental evidence—not as production performance or a substitute for an untouched external test set.

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
