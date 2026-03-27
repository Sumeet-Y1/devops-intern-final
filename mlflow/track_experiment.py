"""
MLflow Tracking - Extra Credit
Logs a dummy experiment with metrics and parameters.
"""

import mlflow
import mlflow.sklearn
import random

# Set the tracking URI (local directory)
mlflow.set_tracking_uri("./mlruns")
mlflow.set_experiment("devops-intern-demo")

with mlflow.start_run(run_name="dummy-experiment"):
    # Log some dummy parameters
    mlflow.log_param("model_type", "demo")
    mlflow.log_param("learning_rate", 0.01)
    mlflow.log_param("epochs", 10)

    # Log some dummy metrics
    for epoch in range(1, 11):
        loss = round(1.0 / epoch + random.uniform(0, 0.05), 4)
        accuracy = round(0.5 + epoch * 0.04 + random.uniform(0, 0.02), 4)
        mlflow.log_metric("loss", loss, step=epoch)
        mlflow.log_metric("accuracy", accuracy, step=epoch)
        print(f"Epoch {epoch:02d} | Loss: {loss:.4f} | Accuracy: {accuracy:.4f}")

    # Log a simple artifact (a text file)
    with open("model_summary.txt", "w") as f:
        f.write("Model: DummyClassifier\n")
        f.write("Task: DevOps intern assessment demo\n")
        f.write("Result: Experiment tracked successfully!\n")

    mlflow.log_artifact("model_summary.txt")

    print("\n✅ MLflow experiment logged successfully!")
    print("Run: mlflow ui  →  open http://localhost:5000 to view")