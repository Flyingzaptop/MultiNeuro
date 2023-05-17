import openai
openai.api_key ="API_KEY"
while True:
    user_input = input("User: ")
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": user_input}])
    print("ChatGPT: "+(completion.choices[0].message.content))
