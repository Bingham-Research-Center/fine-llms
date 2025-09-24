# Mistral AI Client: Main Functions (Version 0.4.2)

This document provides a quick reference for the main functions and methods from the `mistralai` client version `0.4.2` that are relevant to this project.

## Client Initialization

| Method | Description |
| --- | --- |
| `MistralClient(api_key=...)` | Initializes the Mistral client. |

**Import:**

```python
from mistralai.client import MistralClient
```

## Fine-Tuning

| Method | Description |
| --- | --- |
| `client.files.create(file=...)` | Uploads a file to the Mistral API. The `file` parameter should be a tuple containing the filename and a file-like object. |
| `client.jobs.create(model=..., training_files=...)` | Creates a new fine-tuning job. |
| `client.jobs.retrieve(job_id=...)` | Retrieves the status of a fine-tuning job. |
| `client.jobs.start(job_id=...)` | Starts a fine-tuning job that was created but not started automatically. |

**Import:**

```python
from mistralai.client import MistralClient
```

## Chat Completion

| Method | Description |
| --- | --- |
| `client.chat(model=..., messages=...)` | Creates a chat completion. |

**Import:**

```python
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
```
