from transformers import pipeline

# Prepare the input messages
messages = [
    {"role": "user", "content": "Who are you?"},
]

# Load the DialoGPT model
pipe = pipeline("text-generation", model="microsoft/DialoGPT-large")

# Generate a response
for message in messages:
    response = pipe(message["content"], max_length=50)
    print(response[0]["generated_text"])
