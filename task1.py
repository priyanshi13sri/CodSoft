import re

def chatbot():
    print("🤖 Chatbot: Hello! I am a chatbot, you can call me PyBot.")
    print("How can I help you. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower()

       # Exit 
        if "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Take care! 👋")
            break

        elif re.search(r"\b(hi|hello|hey)\b", user_input):
            print("🤖 Chatbot: Hello there! How are you doing today?")


        elif re.search(r"\b(your name|who are you)\b", user_input):
            print("🤖 Chatbot: I am a chatbot created in Python. You can call me PyBot! 🐍")

     
        elif re.search(r"\b(age|old)\b", user_input):
            print("🤖 Chatbot: I don’t have an age, but I was just created recently!")


        elif re.search(r"\b(weather|temperature)\b", user_input):
            print("🤖 Chatbot: I can’t check live weather yet, but I hope it's sunny where you are 🌞!")

       
        elif re.search(r"\b(hobby|hobbies|fun)\b", user_input):
            print("🤖 Chatbot: I love chatting with people like you and learning new responses!")

        
        elif re.search(r"\b(joke|funny)\b", user_input):
            print("🤖 Chatbot: Why don’t programmers like nature? Because it has too many bugs! 🐞😂")

        
        elif re.search(r"\b(who made you|creator|developer)\b", user_input):
            print("🤖 Chatbot: I was created by a Python programmer just like you 😉")

        elif re.search(r"\b(thank|thanks)\b", user_input):
            print("🤖 Chatbot: You’re welcome! Happy to help anytime 🙌")

        
        elif re.search(r"\b(help|support|assist)\b", user_input):
            print("🤖 Chatbot: Sure! You can ask me about my name, age, hobbies, weather, or even for a joke!")

        
        else:
            print("🤖 Chatbot: Hmm... I didn’t quite get that. Can you rephrase it?")
            

chatbot()
