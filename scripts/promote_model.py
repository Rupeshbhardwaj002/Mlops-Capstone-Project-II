# promote model

import os
import mlflow


def promote_model():
    # Set up DagsHub credentials for MLflow tracking
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "vikashdas770"
    repo_name = "YT-Capstone-Project"

    # Set up MLflow tracking URI
    mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

    client = mlflow.MlflowClient()

    model_name = "my_model"

    # -----------------------------------------
    # Get ALL versions of the registered model
    # -----------------------------------------
    versions = list(client.search_model_versions(f"name='{model_name}'"))

    if not versions:
        raise ValueError(f"No versions found for model: {model_name}")

    # Pick the latest version
    latest_version = max(versions, key=lambda mv: int(mv.version)).version

    # -----------------------------------------
    # Archive current production versions
    # -----------------------------------------
    prod_versions = client.search_model_versions(
        f"name='{model_name}' and current_stage='Production'"
    )

    for version in prod_versions:
        client.transition_model_version_stage(
            name=model_name,
            version=version.version,
            stage="Archived"
        )

    # -----------------------------------------
    # Promote latest model to Production
    # -----------------------------------------
    client.transition_model_version_stage(
        name=model_name,
        version=latest_version,
        stage="Production"
    )

    print(f"Model version {latest_version} promoted to Production")


if __name__ == "__main__":
    promote_model()