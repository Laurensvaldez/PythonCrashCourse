# You can store your prompt in a variable and pass that variable to the input() function.
# This allows you to build your prompt over several lines, then write a clean input() statement.

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")