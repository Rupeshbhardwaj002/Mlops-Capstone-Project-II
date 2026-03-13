# register model

import json
import mlflow
from src.logger import logging
import os
import dagshub

import warnings
warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings("ignore")

# Below code block is for production use
# -------------------------------------------------------------------------------------
# Set up DagsHub credentials for MLflow tracking

dagshub_token = os.getenv("CAPSTONE_TEST")
if not dagshub_token:
    raise EnvironmentError("CAPSTONE_TEST environment variable is not set")

os.environ["MLFLOW_TRACKING_USERNAME"] = dagshub_token
os.environ["MLFLOW_TRACKING_PASSWORD"] = dagshub_token

dagshub_url = "https://dagshub.com"
repo_owner = "Rupeshbhardwaj002"
repo_name = "Mlops-Capstone-Project-II"

# Set up MLflow tracking URI
mlflow.set_tracking_uri(f'{dagshub_url}/{repo_owner}/{repo_name}.mlflow')

# # -------------------------------------------------------------------------------------


# Below code block is for local use
# -------------------------------------------------------------------------------------
# register model
import time  # Add this import
import json
# ... other imports ...


# Wait 5 seconds to let DagsHub connection reset
print("Waiting for DagsHub connection to stabilize...")
time.sleep(5)

# Then do the init

# mlflow.set_tracking_uri('https://dagshub.com/Rupeshbhardwaj002/Mlops-Capstone-Project-II.mlflow')
# dagshub.init(repo_owner='Rupeshbhardwaj002', repo_name='Mlops-Capstone-Project-II', mlflow=True)

# -------------------------------------------------------------------------------------


def load_model_info(file_path: str) -> dict:
    """Load the model info from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            model_info = json.load(file)
        logging.info('Model info loaded from %s', file_path)
        return model_info
    except FileNotFoundError:
        logging.error('File not found: %s', file_path)
        raise
    except Exception as e:
        logging.error('Unexpected error occurred while loading the model info: %s', e)
        raise


def register_model(model_name: str, model_info: dict):
    """Register the model to the MLflow Model Registry."""
    try:
        # Use the exact model URI returned by mlflow.sklearn.log_model()
        model_uri = model_info['model_uri']
        logging.info('Registering model from URI: %s', model_uri)

        # Register the model
        model_version = mlflow.register_model(model_uri=model_uri, name=model_name)

        # Transition the model to "Staging" stage
        client = mlflow.tracking.MlflowClient()
        client.transition_model_version_stage(
            name=model_name,
            version=model_version.version,
            stage="Staging"
        )

        logging.info(
            'Model %s version %s registered and transitioned to Staging.',
            model_name,
            model_version.version
        )
    except Exception as e:
        logging.error('Error during model registration: %s', e)
        raise


def main():
    import time
    max_retries = 3

    for attempt in range(max_retries):
        try:
            model_info_path = 'reports/experiment_info.json'
            model_info = load_model_info(model_info_path)

            model_name = "my_model"
            register_model(model_name, model_info)
            print("Model registered successfully.")
            break  # Success! Exit the loop

        except Exception as e:
            logging.error(f'Attempt {attempt + 1} failed: {e}')
            if attempt < max_retries - 1:
                time.sleep(5)  # Wait 5 seconds before trying again
            else:
                print(f"Error: Failed after {max_retries} attempts.")


if __name__ == '__main__':
    main()