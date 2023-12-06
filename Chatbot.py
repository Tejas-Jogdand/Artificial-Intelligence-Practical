def greeting(user_input):
    grt_txt = ["hello", "hi", "hola", "namaste"]
    return any(greet in user_input.lower() for greet in grt_txt)

def farewell(user_input):
    fr_txt = ["bye", "sayonara", "ttyl"]
    return any(far in user_input.lower() for far in fr_txt)

def name(user_input):
    name_list = ["tejas", "sid", "manish"]
    return any(nam in user_input.lower() for nam in name_list)

def chatbot(user_input):
    if greeting(user_input) :
        return user_input.capitalize()+"! What is your name?"
    elif name(user_input):
        return "Nice to meet you, "+user_input.capitalize()
    elif farewell(user_input):
        return "Goodbye!"
    else:
        return "Sorry, Didn't uderstand that. Please try again."
    

while True:
    user_input = input("You : ")
    if user_input.lower() == 'exit':
        print("Chatbot : Have a good day....!")
        break
    response = chatbot(user_input)
    print("Chatbot: ",response)