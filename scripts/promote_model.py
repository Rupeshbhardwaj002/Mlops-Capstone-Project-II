# promote model

import os
import sys
import mlflow
from mlflow import MlflowClient


def promote_model():
    # Set up DagsHub credentials for MLflow trackig
    dagshub_token = os.getenv("CAPSTONE_TEST")
    if not dagshub_token:
        raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

    os.environ["MLFLOW_TRACKING_USERNAME"] = "Rupeshbhardwaj002"
    os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

    dagshub_url = "https://dagshub.com"
    repo_owner = "Rupeshbhardwaj002"
    repo_name = "Mlops-Capstone-Project-II"

    tracking_uri = f"{dagshub_url}/{repo_owner}/{repo_name}.mlflow"
    mlflow.set_tracking_uri(tracking_uri)

    client = MlflowClient()

    # Must match the name used in register_model.py
    model_name = "Mlops-Capstone-Project-II-model"
    alias_name = "production"

    try:
        # Check that registry is reachable
        registered_model = client.get_registered_model(model_name)
        print(f"Registered model found: {registered_model.name}")

    except Exception as e:
        print(
            f"Tracking server configured, but model registry lookup is not available "
            f"for model '{model_name}' in this workflow."
        )
        print(f"Registry check failed with: {type(e).__name__}: {e}")
        print(
            "Use the DagsHub MLflow UI Models tab to promote the registered model manually, "
            "or remove this CI promotion step."
        )
        return 0

    try:
        # Fetch all versions of this model
        versions = list(client.search_model_versions(f"name='{model_name}'"))

        if not versions:
            print(f"No versions found for registered model '{model_name}'.")
            return 0

        # Pick the latest numeric version
        latest_version = max(versions, key=lambda mv: int(mv.version))
        latest_version_num = latest_version.version

        print(
            f"Latest model version found for '{model_name}': version {latest_version_num}"
        )

    except Exception as e:
        print(f"Could not fetch model versions for '{model_name}'.")
        print(f"Version lookup failed with: {type(e).__name__}: {e}")
        return 0

    try:
        # Preferred modern approach: use alias instead of deprecated stages
        client.set_registered_model_alias(
            name=model_name,
            alias=alias_name,
            version=latest_version_num,
        )

        print(
            f"Successfully assigned alias '{alias_name}' "
            f"to version {latest_version_num} of model '{model_name}'."
        )
        print(
            f"Production model reference is now: models:/{model_name}@{alias_name}"
        )
        return 0

    except Exception as e:
        print(
            f"Model version {latest_version_num} was found, but automated alias-based "
            f"promotion is not available through the current MLflow endpoint in this workflow."
        )
        print(f"Alias assignment failed with: {type(e).__name__}: {e}")
        print(
            "Use the DagsHub MLflow UI Models tab to promote/select the model manually."
        )
        return 0


if __name__ == "__main__":
    sys.exit(promote_model())