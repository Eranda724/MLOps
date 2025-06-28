# Train script placeholder 
import mlflow
import logging
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("mlops.log"),
        logging.StreamHandler()
        ]
    )

logging.info("Starting the training process...")

logging.info("Loading..")
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)

logging.info("Training the model...")

with mlflow.start_run():
    logging.info("MLflow run started.")
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    logging.info("Model training completed.")
    
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    mlflow.log_metric("accuracy", accuracy)
    logging.info(f"Model accuracy: {accuracy}")