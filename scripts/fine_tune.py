import os
from mistralai.client import MistralClient

def main():
    """
    This script uploads a training file to Mistral and creates a fine-tuning job.
    """

    # Get API key from environment variable
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not set")

    client = MistralClient(api_key=api_key)

    # 1. Upload your training data
    try:
        with open("data/Q-A-DATASET.jsonl", "rb") as f:
            training_file = client.files.create(file=("Q-A-DATASET.jsonl", f))
        print(f"Successfully uploaded training data. File ID: {training_file.id}")
    except FileNotFoundError:
        print("Error: data/Q-A-DATASET.jsonl not found. Please run the convert_to_jsonl.py script first.")
        return
    except Exception as e:
        print(f"Error uploading file: {e}")
        return

    # 2. Create a fine-tuning job
    try:
        job = client.jobs.create(
            model="open-mistral-7b",
            training_files=[training_file.id],
        )
        print(f"Fine-tuning job created with ID: {job.id}")
        print("The job has been created. Please review the job on the Mistral website.")

    except Exception as e:
        print(f"Error creating fine-tuning job: {e}")
        return

if __name__ == "__main__":
    main()
