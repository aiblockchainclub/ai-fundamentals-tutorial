from transformers import pipeline

# Load GPT-2 model for text generation
generator = pipeline("text-generation", model="gpt2")
result = generator("Once upon a time in AI,", max_length=50)
print(result[0]["generated_text"])
