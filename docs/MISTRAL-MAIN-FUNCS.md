# Mistral AI Client: Main Functions

The following examples use the modern `mistralai` client API.

## Client Initialization

```python
import os
from mistralai import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))
```

## File Uploading

To fine-tune a model, you first need to upload your training data in JSONL format.

```python
from mistralai import Mistral
from mistralai.models import File

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

with open("data/Q-A-DATASET-instruct.jsonl", "rb") as f:
    file_obj = File(file_name="Q-A-DATASET-instruct.jsonl", content=f.read())
    training_file = client.files.upload(file=file_obj)

print(f"File ID: {training_file.id}")
```

## Fine-Tuning

Once you have your file ID, you can create a fine-tuning job.

```python
from mistralai import Mistral
from mistralai.models import File, CompletionTrainingParametersIn, TrainingFile

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

# Assumes training_file.id is available from the file upload step
job = client.fine_tuning.jobs.create(
    model="open-mistral-7b",
    training_files=[TrainingFile(file_id=training_file.id)],
    hyperparameters=CompletionTrainingParametersIn(
        epochs=1, # Adjust based on your dataset size
    )
)

print(f"Fine-tuning job created with ID: {job.id}")
```

### Understanding the 'Too Many Epochs' Error

You may encounter an error message like this when creating a fine-tuning job:

> The estimated number of epochs (...) from the given training files and training steps is too high. Reduce the number of training steps or increase the size of your dataset so that your job doesn't exceed 100 epochs.

This error occurs when the number of `training_steps` you have set is too high for the size of your dataset, causing the fine-tuning job to exceed Mistral's limit of 100 epochs.

**Why it happens:**

*   **Epoch:** An epoch represents one full pass through your entire training dataset.
*   **Training Steps:** This is the total number of times the model will update its weights.
*   **The Calculation:** The total number of epochs is calculated by dividing your total `training_steps` by the number of steps it takes to complete one epoch. If you have a small dataset and a large number of training steps, you'll be repeating the data too many times, leading to a high number of epochs.

**Risks:**

*   **High Costs:** While this specific error stops the job before it starts, setting inappropriately high training steps on a larger dataset could lead to unexpectedly long and expensive training runs.
*   **Overfitting:** Training for too many epochs can cause the model to "memorize" your training data instead of learning general patterns. This results in a model that performs poorly on new, unseen data.

**How to Avoid It:**

*   **Set `training_steps` wisely:** A good rule of thumb is to set `training_steps` to be roughly equal to the number of examples in your dataset. This will result in approximately one epoch of training. You can find the number of lines in your JSONL file using `wc -l <your_file>.jsonl`.
*   **Increase dataset size:** If you need to train for more steps to improve your model, it's best to add more high-quality training examples to your dataset.
*   **Iterate:** Start with a smaller number of training steps (e.g., for one epoch), evaluate your model's performance, and then decide if further training with more steps is necessary.

## Chat Completion

```python
from mistralai import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

response = client.chat.complete(
    model="mistral-large-latest",
    messages=[
        {"role": "user", "content": "What is the best French cheese?"}
    ]
)

print(response.choices[0].message.content)
```

## Embeddings

```python
from mistralai import Mistral

client = Mistral(api_key=os.environ.get("MISTRAL_API_KEY"))

response = client.embeddings.create(
    model="mistral-embed",
    input=["Embed this sentence.", "As well as this one."]
)

print(response)
```
