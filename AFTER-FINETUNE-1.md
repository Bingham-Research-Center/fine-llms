# After Your First Fine-Tune: What to Do Next

Congratulations on completing your first fine-tuning job! You now have a custom model that is trained on your research data. This document will guide you on what to do next to start "playing" with your new model.

## 1. Get Your Fine-Tuned Model ID

Once your fine-tuning job has successfully completed, you will get a new model ID for your fine-tuned model. You can find this model ID in the output of the `fine_tune.py` script, or by retrieving the job details from the Mistral API.

For example, your fine-tuned model ID is: `ft:open-mistral-7b:2a790761:20250924:0550e55a`

If you need to retrieve the job details again, you can use the following command, replacing `your_job_id` with the ID of your fine-tuning job:

```bash
python -c "from mistralai import Mistral; import os; client = Mistral(api_key=os.environ.get('MISTRAL_API_KEY')); print(client.fine_tuning.jobs.get('your_job_id'))"
```

Look for the `fine_tuned_model` field in the output.

## 2. Update the Query Script

Now that you have your new model ID, you need to update the `scripts/query_model.py` script to use it. Open the `scripts/query_model.py` file and replace `"your_fine_tuned_model_id"` with your new model ID.

## 3. "Play" with Your Model

You are now ready to start interacting with your new model! Run the `scripts/query_model.py` script to start a conversation with your AI Research Assistant:

```bash
python scripts/query_model.py
```

Here are some things you can do to "play" with your model and evaluate its performance:

*   **Ask it questions from your test set:** If you created a separate test set of questions, ask your model those questions and see how it performs.
*   **Ask it open-ended questions:** Ask your model open-ended questions that require it to synthesize information from different parts of your research.
*   **Try to trick it:** Ask your model tricky questions or questions that are outside the scope of its training data to see how it responds.
*   **Get feedback from your team:** Ask your team members to interact with the model and provide feedback. This will help you identify areas where the model needs improvement.

## Next Steps

Based on the performance of your model, you can then decide on the next steps. This could include:

*   **Refining your training data:** You may need to add more data, improve the quality of your existing data, or try a different data format.
*   **Experimenting with hyperparameters:** You can experiment with different hyperparameters, such as the learning rate and the number of training steps, to improve the performance of your model.
*   **Trying a different model:** You can try fine-tuning a different base model to see if it gives you better results.

Fine-tuning is an iterative process. Don't be discouraged if your first model isn't perfect. Keep experimenting and refining your approach, and you will eventually create a powerful and helpful AI Research Assistant.