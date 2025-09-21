import google.generativeai as genai

API_KEY = "AIzaSyDdmnvWXaWo_IgGwuYxqEJ2rhoWAM9mKp0"
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

print("Chat with Gemini (type 'exit' to quit)")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    try:
        response = model.generate_content(user_input)  # <-- direct call
        print("Gemini:", response.text)
    except Exception as e:
        print("Error:", str(e))
