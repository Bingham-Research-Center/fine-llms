# Fine-Tuning LLMs for Research

This project provides a framework for fine-tuning Large Language Models (LLMs) on your own research data. The goal is to create a knowledgeable AI assistant that can help your team with its research.

## Data Preparation

This guide provides a detailed breakdown of how to prepare your research data for fine-tuning a Large Language Model.

### Breaking Down the Data Preparation Process

Here is a more detailed breakdown of how to prepare your research data:

**Step 1.1: Gather Your Raw Materials**

First, gather all the documents you want your AI Research Assistant to learn from. This can include:

*   Research papers (PDFs, Word documents, etc.)
*   Lab notes
*   Presentations
*   Grant proposals
*   Any other documents that contain relevant information

**Step 1.2: Extract the Text**

Next, you need to extract the raw text from these documents. This is a good candidate for automation. You can use Python libraries to extract text from different file formats:

*   **PDFs:** `PyPDF2` or `pdfplumber`
*   **Word Documents:** `python-docx`

**Step 1.3: Curate and Clean the Data**

This is the most important step, and it requires manual curation. Raw text extracted from documents can be messy. You need to clean it up and format it in a way that is easy for the model to understand.

**Step 1.4: Create Your Training Data**

Now it's time to create your `research_data.jsonl` file. It's a good idea to use a mix of different data formats, such as summaries and question-answer pairs.

## Running the Fine-Tuning Process

1.  **Install Dependencies:** Make sure you have all the required packages installed:

    ```bash
    pip install -r requirements.txt
    ```

2.  **Prepare Your Data:** Make sure your `reference-text/Q-A-DRAFT.md` file is up-to-date with your human-vetted Q&A pairs.

3.  **Convert Your Data:** Run the `convert_to_jsonl.py` script to convert your Markdown Q&A pairs to the required JSONL format:

    ```bash
    python convert_to_jsonl.py
    ```

4.  **Run the Fine-Tuning Script:** Run the `fine_tune.py` script to upload your data and create the fine-tuning job:

    ```bash
    python scripts/fine_tune.py
    ```

5.  **Start the Job:** The script will create the job but will not start it automatically. You will need to go to the Mistral website to review the job and manually start the training process.
