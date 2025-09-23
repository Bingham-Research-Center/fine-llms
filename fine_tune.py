import os
from mistralai.client import MistralClient

def main():
    """
    This script uploads a training file to Mistral, creates a fine-tuning job,
    and monitors the job until it is complete.
    """

    # Get API key from environment variable
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not set")

    client = MistralClient(api_key=api_key)

    # 1. Upload your training data
    try:
        with open("research_data.jsonl", "rb") as f:
            training_data = client.files.create(file=("research_data.jsonl", f))
        print(f"Successfully uploaded training data. File ID: {training_data.id}")
    except FileNotFoundError:
        print("Error: research_data.jsonl not found. Please create this file and add your training data.")
        return
    except Exception as e:
        print(f"Error uploading file: {e}")
        return

    # 2. Create a fine-tuning job
    try:
        job = client.jobs.create(
            model="open-mistral-7b",
            training_files=[training_data.id],
            # You can add hyperparameters here, for example:
            # hyperparameters={
            #     "training_steps": 100,
            #     "learning_rate": 1e-4,
            # }
        )
        print(f"Fine-tuning job created with ID: {job.id}")
    except Exception as e:
        print(f"Error creating fine-tuning job: {e}")
        return

    # 3. Monitor the job status
    try:
        while True:
            job_status = client.jobs.retrieve(job.id)
            print(f"Job status: {job_status.status}")
            if job_status.status in ["SUCCEEDED", "FAILED"]:
                if job_status.status == "SUCCEEDED":
                    print(f"Fine-tuning successful! Model ID: {job_status.fine_tuned_model}")
                else:
                    print("Fine-tuning failed.")
                break
            # Wait for 60 seconds before checking the status again
            import time
            time.sleep(60)
    except Exception as e:
        print(f"Error monitoring job: {e}")

if __name__ == "__main__":
    main()
