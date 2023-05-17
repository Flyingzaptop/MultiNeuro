import openai
import time

# Set up ayour OpenAI API key
openai.api_key = "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"

# Set up the OpenAI API endpoint
endpoint = "https://api.openai.com/v1/"

# Set up the ChatGPT model ID
model = "text-davinci-002"

# Define a function that calls the OpenAI API to generate text
def generate_text(prompt):
    # Call the OpenAI API to generate text
    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    
    # Wait for the API to generate a response
    while "choices" not in response:
        response = openai.Completion.retrieve(response["id"])
        time.sleep(1)
    
    # Extract the generated text from the API response
    text = response["choices"][0]["text"]
    
    return text

# Prompt the user for input and generate a response using ChatGPT
while True:
    prompt = input("You: ")
    response = generate_text(prompt)
    print("ChatGPT:", response)
