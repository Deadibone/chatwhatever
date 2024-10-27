import random
import re
import tkinter as tk


# Create a Tkinter window
window = tk.Tk()
window.title("Chat Whatever")
window.geometry("400x500")

# Create a label for the "Chat Whatever" text
title_label = tk.Label(window, text="Chat Whatever", font=("Helvetica", 16, "bold"))
title_label.pack(pady=10)


# Create a text box for displaying the conversation
conversation_text = tk.Text(window, state="disabled")
conversation_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Create an entry field for user input
user_input_entry = tk.Entry(window, width=50)
user_input_entry.pack(padx=10, pady=10)

# Add placeholder/hint text to the input box
user_input_entry.insert(0, "Type in a message")

# Function to handle user input and generate bot response
def handle_user_input():
    user_input = user_input_entry.get().lower()
    user_input_entry.delete(0, tk.END)

    matched_rules = []
    for rule in rules:
        matched_patterns = [pattern for pattern in rule["patterns"] if re.search(pattern, user_input)]
        if matched_patterns:
            matched_rules.append(rule)

    if matched_rules:
        rule = random.choice(matched_rules)
        response = random.choice(rule.get("responses", [""]))
    else:
        response = "I'm sorry, I didn't understand that."

    conversation_text.config(state="normal")
    conversation_text.insert(tk.END, "User: " + user_input + "\n")
    conversation_text.insert(tk.END, "Social Work GPT: " + response + "\n")
    conversation_text.insert(tk.END, "\n")
    conversation_text.config(state="disabled")
    conversation_text.see(tk.END)

    if user_input in ["bye", "exit"]:
        window.destroy()

# Function to handle the click event on the input box
def clear_placeholder(event):
    if user_input_entry.get() == "Type in a message":
        user_input_entry.delete(0, tk.END)

# Bind the click event to the input box
user_input_entry.bind("<Button-1>", clear_placeholder)

# Function to bind the Enter key to the user input field
def bind_enter_key(event):
    handle_user_input()

window.bind("<Return>", bind_enter_key)

# Define the conversation rules
rules = [
        {
        "patterns": [r".*(hello|hi|hey|howdy|good morning|good afternoon|good evening|good night).*"],
        "responses": [
            "Hi, how could i help you?",
            "Hello user, I am Chat Whatever and I am here to help you find answers to different questions!"
        ]
    },
        {
        "patterns": [r".*(tell me a joke|crack me up).*"],
        "responses": [
            "To the guy who invented zero: Thanks for nothing!",
            "Where do generals keep their armies? In their sleevies!",
            "Why can't a bicycle stand on its own? It's two-tired.",
            "I was up all night wondering where the sun went, but then it dawned on me.",
            "My dolphin puns are terrible on porpoise.",
            "Time flies like an arrow. Fruit flies like a banana.",
            "Why can't you use 'Beef stew' as a password? Because it's not stroganoff.",
            "If the mushroom was such a fun guy why didn't they have the party at his house?"
        ]
    },
        {
        "patterns": [r".*(how are you|how are you doing).*"],
        "responses": [
            "I'm doing well, thank you!",
            "I'm great, thanks for asking. How can I assist you today?",
            "I'm functioning perfectly. How can I help you?"
        ]
    },
    {
        "patterns": [r".*(what is your name|who are you).*"],
        "responses": [
            "I am Chat Whatever, your friendly chatbot.",
            "You can call me Chat Whatever. How can I assist you today?",
            "I'm Chat Whatever, here to help you with your inquiries."
        ]
    },
    {
        "patterns": [r".*(help|need assistance).*"],
        "responses": [
            "Of course! I'm here to help. What do you need assistance with?",
            "I'm here to assist you. How can I be of service?",
            "I'm happy to help. What do you need assistance with?"
        ]
    },
    {
        "patterns": [r".*(bye|goodbye|see you later|take care).*"],
        "responses": [
            "Goodbye! If you have any more questions, feel free to ask.",
            "Take care! Don't hesitate to reach out if you need further assistance.",
            "See you later! Have a great day!"
        ]
    },
        {
        "patterns": [r".*(tell me about yourself|who created you|your origin).*"],
        "responses": [
            "I am an AI-powered chatbot created by RELPLUS.",
            "I'm an AI chatbot designed to assist users with their inquiries.",
            "I was developed by RELPLUS to provide helpful information and engage in conversations."
        ]
    },
    {
        "patterns": [r".*(what can you do|your abilities).*"],
        "responses": [
            "I can answer questions, provide information, and engage in conversations.",
            "I'm knowledgeable about a wide range of topics. Feel free to ask me anything.",
            "I'm designed to assist with various tasks, from providing recommendations to answering queries."
        ]
    },
    {
        "patterns": [r".*(thank you|thanks).*"],
        "responses": [
            "You're welcome! I'm here to help.",
            "No problem! If you have any more questions, feel free to ask.",
            "You're welcome! Don't hesitate to reach out if you need further assistance."
        ]
    },
    {
        "patterns": [r".*(how can I contact you|contact information).*"],
        "responses": [
            "I'm an AI chatbot, so you can interact with me right here in this chat.",
            "You can reach me anytime by typing your questions or requests here.",
            "You're already in contact with me! Feel free to ask anything you need."
        ]
    },
    {
        "patterns": [r".*(tell me something interesting|fun fact).*"],
        "responses": [
            "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "Here's a fun fact: The average person walks the equivalent of three times around the world in their lifetime.",
            "Here's an interesting fact: The world's oldest known recipe is for beer. It's over 4,000 years old and was discovered in a Sumerian poem.",
            "Did you know that the world's smallest mammal is the bumblebee bat? It weighs about the same as a dime!",
            "Here's a fun fact: The Great Wall of China is so long that it could wrap around the Earth's equator more than twice."
        ]
    },
    {
        "patterns": [r".*(tell me a story|share a story).*"],
        "responses": [
            "Once upon a time, in a land far away, there lived a wise old wizard...",
            "Long ago, in a kingdom ruled by magical creatures, there was a brave young knight...",
            "In a small village nestled in the mountains, there was a curious young girl named Lily..."
        ]
    },
        {
        "patterns": [r".*(what is the weather like today|weather|forecast).*"],
        "responses": [
            "I don't have real-time weather data, but you can check a reliable weather website or app for the latest forecast.",
            "To get the most accurate weather information, I recommend checking a trusted weather service or app.",
            "I'm sorry, I can't provide real-time weather updates. I suggest using a weather app or website for accurate forecasts."
        ]
    },
    {
        "patterns": [r".*(how old are you|your age).*"],
        "responses": [
            "As an AI chatbot, I don't have a physical form or age. I exist solely to assist you.",
            "I don't have an age. I'm here to help you with your questions and tasks.",
            "I'm ageless, but my knowledge is up to date. How can I assist you?"
        ]
    },
    {
        "patterns": [r".*(what is the meaning of life|purpose of life).*"],
        "responses": [
            "The meaning of life can vary for each individual. It's a philosophical question that people have contemplated for centuries.",
            "The meaning of life is subjective and can be different for everyone. It's about finding your own purpose and what brings you fulfillment.",
            "The meaning of life is a profound question with no definitive answer. It's up to each person to find their own purpose and meaning."
        ]
    },
    {
        "patterns": [r".*(recommend a movie|movie recommendation).*"],
        "responses": [
            "Sure! What genre of movies are you interested in?",
            "I'd be happy to recommend a movie. Could you let me know your preferred genre or any specific preferences?",
            "I can suggest some great movies. What kind of movies do you enjoy?"
        ]
    },
    {
        "patterns": [r".*(tell me a fun fact about animals|animal trivia).*"],
        "responses": [
            "Did you know that a group of flamingos is called a flamboyance?",
            "Here's a fun fact: Cows have best friends and can become stressed when separated from them.",
            "Did you know that the fingerprints of koalas are so similar to humans' that they have been mistaken at crime scenes?",
            "Here's an interesting fact: Dolphins have been known to recognize themselves in mirrors, demonstrating self-awareness.",
            "Did you know that a honeybee can flap its wings up to 200 times per second? That's how they create buzzing sounds."
        ]
    },
    {
        "patterns": [r".*(tell me a riddle|share a riddle).*"],
        "responses": [
            "Sure, here's a riddle: I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
            "Here's a riddle for you: What has keys, but can't open locks?",
            "I have a riddle for you: What has cities but no houses, forests but no trees, and rivers but no water?",
            "Ready for a riddle? What comes but never arrives?",
            "Here's a challenging riddle: I am taken from a mine, and shut in a wooden case, from which I'm never released. I am used by everyone. What am I?"
        ]
    },
    {
        "patterns": [r".*(what is the best programming language|favorite programming language).*"],
        "responses": [
            "The best programming language depends on the specific use case and personal preference.",
            "There is no definitive answer to the best programming language. It's subjective and depends on what you aim to achieve.",
            "Each programming language has its strengths and weaknesses. The best one for you depends on your goals and requirements."
        ]
    },
    {
        "patterns": [r".*(tell me a quote|inspirational quote).*"],
        "responses": [
            "Here's an inspirational quote: 'The only way to do great work is to love what you do.' - Steve Jobs",
            "Here's a quote to inspire you: 'Success is not final, failure is not fatal: It is the courage to continue that counts.' - Winston Churchill",
            "Here's a quote for you: 'Believe you can and you're halfway there.' - Theodore Roosevelt",
            "Here's an inspiring quote: 'The future belongs to those who believe in the beauty of their dreams.' - Eleanor Roosevelt",
            "Here's a quote to motivate you: 'The only limit to our realization of tomorrow will be our doubts of today.' - Franklin D. Roosevelt"
        ]
    },
    {
        "patterns": [r".*(tell me a random fact|random trivia).*"],
        "responses": [
            "Did you know that the shortest war in history was between Britain and Zanzibar in 1896? It lasted only 38 minutes!",
            "Here's a random fact: The world's oldest known musical instrument is a flute made from a vulture's wing bone, dating back over 40,000 years.",
            "Here's a random fact: Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "Here's a random fact: The average person spends about six months of their life waiting for red traffic lights to turn green.",
            "Here's a random fact: The world's largest desert is actually Antarctica. It's considered a desert because it receives very little precipitation."
        ]
    },
    {
        "patterns": [r".*(what is your favorite book|favorite author).*"],
        "responses": [
            "As an AI, I don't have personal preferences. However, some popular authors include J.K. Rowling, Stephen King, and Jane Austen.",
            "I don't have a favorite book or author since I'm an AI. But there are many great authors to explore, depending on your interests.",
            "Since I'm an AI chatbot, I don't have personal preferences. However, there are countless amazing books and authors to discover."
        ]
    },
    {
        "patterns": [r".*(what is the time|current time).*"],
        "responses": [
            "I'm sorry, but as an AI chatbot, I don't have access to real-time information. You can check the time on your device or ask a voice assistant for the current time.",
            "I don't have the ability to provide real-time information like the current time. You can easily check the time on your device or ask a voice assistant for the precise time.",
            "As an AI chatbot, I don't have real-time capabilities. You can check the time on your device or use an online time service to get the current time."
        ]
    },
    {
        "patterns": [r".*(what is the meaning of AI|AI).*"],
        "responses": [
            "AI stands for Artificial Intelligence. It refers to the simulation of human intelligence in machines that are programmed to think and learn like humans.",
            "Artificial Intelligence, or AI, is the field of computer science that focuses on creating intelligent machines capable of performing tasks that typically require human intelligence.",
            "AI, short for Artificial Intelligence, involves designing and developing computer systems that can perform tasks that would typically require human intelligence, such as visual perception, speech recognition, and decision-making."
        ]
    },
    {
        "patterns": [r".*(what should I have for dinner|food recommendation).*"],
        "responses": [
            "That depends on your preferences. If you want to cook, you could go to https://www.supercook.com/ and generate some recipies depending on the stock of food you have, if you want to go outside, then you could go to google maps and find a nearby restaraunt!"
        ]
    },
    {
        "patterns": [r".*(who won the .* game|result of the .* match).*"],
        "responses": [
            "I'm sorry, but as an AI chatbot, I don't have access to real-time sports results. You can check a reliable sports news website or app for the latest updates.",
            "To find out the result of the game, I recommend checking a sports news website or app for the most up-to-date information.",
            "I don't have access to real-time sports results. I suggest checking a sports news website or app for the latest information on the {team} game."
        ]
    },

    {
        "patterns": [r".*(what is the speed of light|speed of light).*"],
        "responses": [
            "The speed of light in a vacuum is approximately 299,792 kilometers per second or about 186,282 miles per second.",
            "In a vacuum, the speed of light is approximately 299,792 kilometers per second.",
            "The speed of light in a vacuum is approximately 299,792,458 meters per second.",
            "Light travels at a speed of approximately 299,792 kilometers per second in a vacuum.",
            "The speed of light is about 299,792,458 meters per second in a vacuum."
        ]
    }
]

# Start the Tkinter event loop
window.mainloop()