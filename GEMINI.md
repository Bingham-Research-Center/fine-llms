# Gemini Project: Fine-Tuning LLMs

## Project Overview

This project is dedicated to learning and experimenting with fine-tuning Large Language Models (LLMs), with a primary focus on Mistral models. The goal is to create a lightweight and accessible framework for a small research team with varying levels of technical expertise to train, test, and deploy fine-tuned models. The initial project will be to fine-tune a model on the team's cumulative research, making it a knowledgeable assistant for the research group.

## Development Environment Setup

This project is set up to be developed locally, with the understanding that team members may be using different development environments and tools.

### Local Development with Gemini

As the main developer, you will be using Gemini as your AI assistant. To ensure a smooth workflow, please follow these guidelines:

*   **API Keys:** Never commit API keys or other sensitive information to the git repository. Store them as environment variables. For the Mistral API, use:
    ```bash
    export MISTRAL_API_KEY='your_api_key'
    ```
*   **Virtual Environment:** It is highly recommended to use a Python virtual environment to manage project dependencies. The `.venv` directory in this project is set up for this purpose.
    ```bash
    # To activate the virtual environment
    source .venv/bin/activate
    ```
*   **Dependencies:** Project dependencies will be managed in a `requirements.txt` file. To install them, run:
    ```bash
    pip install -r requirements.txt
    ```

### Compatibility with Other Tools

To ensure compatibility with team members who are not using Gemini, we will adhere to the following conventions:

*   **Clear Documentation:** All code will be well-documented, and the `START-HERE.md` file will serve as the primary entry point for new team members.
*   **Jupyter Notebooks:** For experimentation and tutorials, we will use Jupyter notebooks, which can be easily shared and run by all team members.
*   **Standard File Formats:** We will use standard file formats for data and documents (e.g., `.jsonl`, `.md`, `.ipynb`) to ensure they can be opened and edited with any tool.

## Development and Testing Guidelines

Given the varying skill levels of the team, we will start with a simple and clear set of guidelines for development and testing.

### Development

*   **Keep it simple:** We will prioritize simple, readable, and well-documented code over complex and opaque solutions.
*   **Modular design:** We will break down the project into smaller, manageable modules to make it easier to understand and maintain.
*   **Code reviews:** All code will be reviewed by at least one other team member before being merged into the main branch.

### Testing

Since the team is new to testing, we will start with a basic testing framework and gradually introduce more advanced techniques.

*   **Manual testing:** All new features will be manually tested before being committed.
*   **Unit tests:** We will start by writing simple unit tests for individual functions to ensure they are working correctly.
*   **Test-Driven Development (TDD):** As the team becomes more comfortable with testing, we will explore Test-Driven Development, where tests are written before the code.

## Cost Management

To prevent accidental high costs, we will implement the following safeguards:

*   **Budget limits:** We will set budget limits for all fine-tuning jobs on the Mistral platform.
*   **Cost estimates:** We will get cost estimates before starting any fine-tuning job.
*   **Monitoring:** We will regularly monitor our API usage and costs.

This `GEMINI.md` file will be updated as the project evolves. Please feel free to suggest any changes or additions.