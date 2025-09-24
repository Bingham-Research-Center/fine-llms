from src.models import get_model
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import os

def main():
    """
    This script queries a fine-tuned model.
    """

    # Get API key from environment variable
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not set")

    client = MistralClient(api_key=api_key)

    # Replace this with your fine-tuned model ID
    model_id = "your_fine_tuned_model_id"

    while True:
        prompt = input("Enter your prompt (or 'quit' to exit): ")
        if prompt.lower() == 'quit':
            break

        try:
            response = client.chat(
                model=model_id,
                messages=[ChatMessage(role="user", content=prompt)]
            )
            print("Model response:", response.choices[0].message.content)
        except Exception as e:
            print(f"Error querying model: {e}")


if __name__ == "__main__":
    main()
