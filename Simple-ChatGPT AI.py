import tkinter as tk
from tkinter import messagebox
import openai

# Set up OpenAI API credentials
openai.api_key = "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"  # Replace with your actual OpenAI API key

# Function to generate chatbot response using GPT-3
def generate_response(prompt):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=prompt,
        temperature=0.6,
        max_tokens=100,
        n=1,
        stop=None
    )
    return response.choices[0].text.strip()

# Function to handle user's message
def send_message():
    user_input = user_entry.get()
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_input + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    # Generate chatbot response
    bot_response = generate_response("User: " + user_input + "\nChatbot:")
    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "Chatbot: " + bot_response + "\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)
    user_entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Chatbot")

# Create chat box
chat_box = tk.Text(root, state=tk.DISABLED)
chat_box.pack(pady=10, padx=10)
chat_box.config(state=tk.NORMAL)
chat_box.insert(tk.END, "Chatbot: " + "Hello, I am your chatbot!" + "\n")
chat_box.config(state=tk.DISABLED)

# Create user input entry
user_entry = tk.Entry(root)
user_entry.pack(pady=10, padx=10)
user_entry.focus()

# Create send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

# Function to handle closing of the window
def close_window():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", close_window)
root.mainloop()
