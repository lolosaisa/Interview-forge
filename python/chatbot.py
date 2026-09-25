bot_name: str = 'Lolo'
print(f"Hello! My name is {bot_name}.  How can I assist you today?")

while True:
    user_input = input("You: ").lower()
    # Python is case sensitive, so we convert the input to lowercase for easier matching.

    if user_input in ['hello', 'hi', 'hey']:
        print(f"{bot_name}: Hello there! How can I help you?")

    elif user_input in ['how are you', 'how are you doing']:
        print(f"{bot_name}: I'm just a bot, but I'm doing great! How about you?")

    elif user_input in ['bye', 'exit', 'quit']:
        print(f"{bot_name}: Goodbye! Have a great day!")
        break

    elif user_input in ['-', 'substract', 'subtract']:
                        print(f"{bot_name}: Sure! Please provide two numbers to subtract Lt u try substraction. Please provide two numbers.")
                        try:
                                num1 = float(input("Enter the first number: "))
                                num2 = float(input("Enter the second number: "))
                                result = num1 - num2
                                print(f"{bot_name}: The result of {num1} - {num2} is {result}.")

                        except ValueError: 
                                print(f"{bot_name}: Sorry! That doesn't seem to be a valid number. Please try again.")

    else:
                                print(f"{bot_name}: I'm sorry, I didn't understand that. Could you please rephrase or ask something else?")
                                