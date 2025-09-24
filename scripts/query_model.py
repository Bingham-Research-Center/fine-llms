from mistralai import Mistral
import os

def main():
    """
    This script queries a fine-tuned model.
    """

    # Get API key from environment variable
    api_key = os.environ.get("MISTRAL_API_KEY")
    if not api_key:
        raise ValueError("MISTRAL_API_KEY environment variable not set")

    client = Mistral(api_key=api_key)

    # Replace this with your fine-tuned model ID
    model_id = "ft:open-mistral-7b:2a790761:20250924:0550e55a"

    while True:
        prompt = input("Enter your prompt (or 'quit' to exit): ")
        if prompt.lower() == 'quit':
            break

        try:
            response = client.chat.complete(
                model=model_id,
                messages=[{"role": "user", "content": prompt}]
            )
            print("Model response:", response.choices[0].message.content)
        except Exception as e:
            print(f"Error querying model: {e}")


if __name__ == "__main__":
    main()