#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def chatbot_response(user_input):
    
    rules = {
        r'hello|hi|hey': "Hello! How can I assist you today?",
        r'how are you': "I'm just a computer program, but I'm here to help you!",
        r'what is your name': "I don't have a name, but you can call me Chatbot.",
        r'bye|goodbye': "Goodbye! Have a great day!",
        r'joke': "Sure, here's a joke: Why did the computer keep freezing? Because it left its Windows open!",
        r'weather': "I'm not equipped to check the weather, but you can use a weather app for that.",
        r'help': "Of course, I'm here to assist you. What do you need help with?",
        r'age|old': "I don't age as I'm just a program, but I'm always up to date!",
        r'who created you': "I was created by a team of developers using Python and natural language processing libraries.",
        r'favorite color': "I don't have preferences as I'm just a chatbot.",
        r'thank you|thanks': "You're welcome! If you have any more questions, feel free to ask.",
    }

    
    for pattern, response in rules.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return response

    
    return "I'm not sure how to respond to that. Can you please rephrase your question?"


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print("Chatbot:", response)


# In[ ]:




