# MLOps_Major_Assignment
Name: Abhishek Anand Jaiswal
Roll Number: G25AI1002

## Project Overview

This project demonstrates an end-to-end MLOps pipeline using the Olivetti Faces dataset and a Decision Tree Classifier. The objective was to automate model training, testing, deployment, and orchestration using modern MLOps tools and practices.

The project includes:

* Model training using Scikit-Learn
* Model testing and evaluation
* CI/CD using GitHub Actions
* Flask web application for prediction
* Docker containerization
* Docker Hub image repository
* Kubernetes deployment with 3 replicas
* NodePort service exposure
* Pod auto-recovery demonstration

## Dataset

Dataset Used: **Olivetti Faces Dataset**

Source:

python
from sklearn.datasets import fetch_olivetti_faces


Dataset Details:

* 400 grayscale face images
* 40 classes
* 10 images per class
* Image size: 64 × 64


## Branch Structure

### main

Initial repository setup.

### dev

Contains:

* train.py
* test.py
* requirements.txt
* GitHub Actions workflow

### docker_cicd

Contains:

* Flask application
* Dockerfile
* Kubernetes deployment files


## Project Structure

MLOps_Major_Assignment
│
├── .github/workflows/ci.yml
├── templates/index.html
├── app.py
├── train.py
├── test.py
├── requirements.txt
├── Dockerfile
├── deployment.yaml
├── service.yaml
├── savedmodel.pth
└── README.md
```

---

## Model Training

To train the model:

```bash
python train.py
```

Output:

```text
Model saved successfully
```

---

## Model Testing

To test the model:

```bash
python test.py
```

Output:

```text
Test Accuracy: 0.5333
```

---

## GitHub Actions

A CI pipeline has been configured using GitHub Actions.

The workflow automatically:

1. Installs dependencies
2. Trains the model
3. Runs testing

Workflow File:

```text
.github/workflows/ci.yml
```

---

## Flask Application

Run the application:

```bash
python app.py
```

Access:

```text
http://localhost:5000
```

The application loads the trained model and displays the predicted class.

---

## Docker

Build Docker Image:

```bash
docker build -t olivetti-app .
```

Run Container:

```bash
docker run -p 5000:5000 olivetti-app
```

Docker Hub Repository:

```text
abhishekjais/olivetti-app
```

---

## Kubernetes

Deploy Application:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

Verify Deployment:

```bash
kubectl get deployments
kubectl get pods
kubectl get svc
```

Features:

* 3 replicas
* NodePort service
* Automatic pod recovery

---

## Conclusion

This project successfully demonstrates the implementation of an end-to-end MLOps workflow. The model was trained and tested successfully, automated using GitHub Actions, containerized with Docker, and deployed on Kubernetes with fault tolerance and scalability features.
