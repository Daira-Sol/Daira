from transformers import pipeline

def load_model(model_name="gpt2", task="text-generation"):
    """
    Load a Hugging Face model and pipeline.
    :param model_name: The name of the model on Hugging Face (e.g., "microsoft/DialoGPT-large").
    :param task: The type of task for the pipeline (e.g., "text-generation", "sentiment-analysis").
    :return: A Hugging Face pipeline object.
    """
    print(f"Loading model: {model_name} for task: {task}...")
    model_pipeline = pipeline(task, model=model_name)
    print("Model loaded successfully!")
    return model_pipeline
