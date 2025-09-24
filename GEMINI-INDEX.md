# Gemini Project Index

This document provides an overview of the project structure and the purpose of each file and directory. This will help you (and me!) navigate the codebase and understand how everything fits together.

## Project Structure

```
/
├── src/                           # Main source code directory
│   ├── __init__.py                # Makes the src directory a Python package
│   ├── data_processing.py         # Functions for preparing your data
│   ├── fine_tuning.py             # Functions for fine-tuning models
│   ├── evaluation.py              # Functions for evaluating models
│   └── models.py                  # Functions for interacting with different models
├── scripts/                       # Scripts to run different parts of the project
│   ├── run_finetuning.py          # Script to run the fine-tuning process
│   └── query_model.py             # Script to query a fine-tuned model
├── tests/                         # Directory for your tests
│   ├── __init__.py                # Makes the tests directory a Python package
│   ├── test_data_processing.py    # Tests for the data processing functions
│   └── test_fine_tuning.py        # Tests for the fine-tuning functions
├── data/                          # Directory for your training data
│   └── Q-A-DATASET.jsonl          # Your training data in JSONL format
├── docs/                          # Directory for documentation
│   └── MISTRAL-MAIN-FUNCS.md      # Quick reference for Mistral AI client functions
├── reference-text/                # Directory for human-readable reference material
│   ├── CUMULATIVE-BRC-RESEARCH.md # The original research summary
│   ├── EXAMPLE-QUESTIONS.md       # A list of example questions
│   ├── PAPERS-TO-PRECIS.md        # A prioritized list of papers to summarize
│   └── Q-A-DRAFT.md               # A human-readable draft of the Q&A dataset
├── requirements.txt               # A list of the Python dependencies for the project
├── convert_to_jsonl.py            # Script to convert the Q&A draft to JSONL format
├── AFTER-FINETUNE-1.md            # Guide on what to do after your first fine-tune
├── README.md                      # A general overview of the project
├── GEMINI.md                      # Gemini-specific project information
└── TUTORIAL.md                    # A tutorial on how to use the project
```