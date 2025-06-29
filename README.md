# 🏠 House Price Prediction & Iris Classification - MLOps Projects

This repository contains **two integrated MLOps projects** that demonstrate the end-to-end machine learning lifecycle — from training and logging a model using MLflow to deploying it via Flask and Kubernetes using Minikube.

---

## 📁 Project Structure

```
.
├── train_iris.py           # Trains a RandomForest on the Iris dataset and logs to MLflow
├── app.py                  # Flask API to serve house price prediction model
├── model.pkl               # Trained & serialized model (with scaler)
├── deployment.yaml         # Kubernetes deployment spec
├── service.yaml            # Kubernetes service spec
├── Dockerfile              # Docker setup for the Flask app
├── mlops.log               # Log file generated during training
└── requirements.txt        # Python dependencies
```

---

## 📌 Project 1: Iris Classification with MLflow

### ✅ Description

* Trains a `RandomForestClassifier` on the classic Iris dataset.
* Uses **MLflow** to track experiments and log metrics (accuracy).
* Logs are saved in `mlops.log`.

### 🚀 How to Run

```bash
python train_iris.py
```

### 🔎 MLflow Logs

```text
accuracy: 0.9667
```

---

## 📌 Project 2: House Price Prediction API with Flask & Kubernetes

### ✅ Description

* Serves a trained house price prediction model via a Flask API.
* Expects a list of input features like median income, house age, etc.
* Can be containerized with Docker and deployed on **Kubernetes using Minikube**.

### 🐳 Docker Build (within Minikube)

```bash
minikube start
& minikube -p minikube docker-env | Invoke-Expression
docker build -t ml-model:latest .
```

### 🚀 Kubernetes Deployment

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
minikube service ml-model-service --url
```

### 📮 Sample Prediction Request (via `curl`)

```bash
curl -X POST http://127.0.0.1:<your-port>/predict \
  -H "Content-Type: application/json" \
  -d "{\"features\": [8.3252, 41, 6.984, 1.023, 322, 2.555, 37.88, -122.23]}"
```

---
Iris Classification

![ml](https://github.com/user-attachments/assets/de42e4ec-2695-499c-8fb1-65452e345e32)
---

House price prediction

![1](https://github.com/user-attachments/assets/519bc353-1c1a-42ee-ad6c-15c7bec3abd6)
![2](https://github.com/user-attachments/assets/b3239f07-309c-43db-979d-e347c9f2e326)
![3](https://github.com/user-attachments/assets/be10f324-a31d-446d-ab90-010c0ecac529)
---

## 💡 Tech Stack

* Python 🐍
* Flask
* Scikit-learn
* MLflow 📊
* Kubernetes (via Minikube) ☸️
* Docker 🐳

---

## 📝 License

This project is for educational purposes as part of the LLM MLOps coursework.
