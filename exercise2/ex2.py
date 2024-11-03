import tkinter as tk #Importing tkinter and giving it an alias tk
import random  #Importing the random module from the library

def load_jokes(filename="randomJokes.txt"): #Using the load jokes function to import the file
    try:
        with open(filename, 'r') as file: #Opening the file in read mode using ('r')
            jokes = [line.strip() for line in file if '?' in line] #Removing whitespaces and naming the file jokes
        return jokes #Opening the filtered jokes file
    except FileNotFoundError:
        return ["Error: randomJokes.txt not found."] #Used try and except functions so if the file isn't found the code still runs instead of giving an error

def show_joke():
    joke = random.choice(jokes) #choosing a random joke from the file using the random module
    setup, punchline = joke.split('?') #Splitting the joke into two parts
    setup_label.config(text=setup + "?") #Adding a question mark to the first part of the joke
    punchline_label.config(text="") #Hiding the puncline initially
    show_punchline_button.config(state="normal", command=lambda: punchline_label.config(text=punchline)) #Made a button to make the puncline visible chen clicked

def close_app():
    root.destroy() #closing the app

root = tk.Tk() #Starting window
root.title("Random Joke Teller") #Naming the window

jokes = load_jokes()  #Checking if the jokes loaded
if jokes == ["Error: randomJokes.txt not found."]:
    tk.Label(root, text=jokes[0]).pack() #If the jokes are not loaded showing an error
else:
    setup_label = tk.Label(root, text="", font=("Arial", 16), wraplength=400)
    setup_label.pack(pady=10) #Creating a label to show the first part of the joke (hidden at first)

    punchline_label = tk.Label(root, text="", font=("Arial", 16), fg="blue", wraplength=400)
    punchline_label.pack(pady=10) #Creating a label to show the second part of the joke (hidden at first)

    show_joke_button = tk.Button(root, text="Alexa, tell me a joke", command=show_joke)
    show_joke_button.pack(pady=5) #Creating a label that shows the first of the joke when pressed

    show_punchline_button = tk.Button(root, text="Show Punchline", state="disabled")
    show_punchline_button.pack(pady=5) #Creating a label that shows the punchline of the joke when pressed

    quit_button = tk.Button(root, text="Quit", command=close_app)
    quit_button.pack(pady=10) #Creating a quit button to close the window

show_joke() #This shows the first joke when the window opens 
root.mainloop()
