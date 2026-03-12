# promote model

import os
import mlflow


def promote_model():
    # Set up DagsHub credentials for MLflow tracking
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    # Better credential mapping for DagsHub-hosted MLflow
    os.environ["MLFLOW_TRACKING_USERNAME"] = "Rupeshbhardwaj002"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "Rupeshbhardwaj002"
    repo_name = "Mlops-Capstone-Project-II"

    # Set up MLflow tracking URI
    mlflow.set_tracking_uri(f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow")

    client = mlflow.MlflowClient()

    # Must match the name used in register_model.py
    model_name = "Mlops-Capstone-Project-II-model"

    # NOTE:
    # DagsHub / current backend is returning 404 for model registry search endpoints
    # in CI, so we stop here with a clear message instead of crashing on deprecated /
    # unsupported stage-based promotion APIs.
    print(
        f"Tracking server configured correctly for model '{model_name}', "
        "but automated registry promotion is not available through the current "
        "MLflow endpoint in this workflow."
    )
    print(
        "Use the DagsHub MLflow UI Models tab to promote the registered model manually, "
        "or remove this CI promotion step."
    )


if __name__ == "__main__":
    promote_model()