def greeting(user_input):
    wlc_txt = ["hello", "hi", "hola", "namaste"]
    return any(greeting in user_input.lower() for greeting  in wlc_txt)

def name(user_input):
    name_list = ["tejas", "rahul", "nitin"];
    return any(name in user_input.lower() for name in name_list)

def farewell(user_input):
    farew_txt = ["bye", "goodbye", "farewell", "see you later"]
    return any(farewell in user_input.lower() for farewell in farew_txt)

def chatbot(user_input):
    # if "hello" in user_input.lower():
    #     return "Hello! How can I help you today?"

    if greeting(user_input):
        return user_input.capitalize()+"! What is your name?"
    elif name(user_input):
        return f"Nice to meet you {user_input.capitalize()}! How can I assit you today?"
    elif farewell(user_input):  
        return "Goodbye!"
    else:
        return "Didn't understand that, Please try again."
           
while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Have a great day...!")
        break

    response = chatbot(user_input);
    print("Chatbot: ", response)