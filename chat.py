import re
import tkinter as tk
from tkinter import scrolledtext

# Define patterns and responses
patterns_responses = [
    (r'I want to find a book about (.*)', 'What genre of book about {0} are you interested in?'),
    (r'Tell me about (.*)', 'Are you asking about a book or an author named {0}?'),
    (r'I need help with (.*)', 'What kind of help with {0} do you need?'),
    (r'Where can I find (.*)', 'I can help you find {0}. Are you looking for it in our catalog or in a specific section?'),
    (r'Who is (.*)', 'Are you interested in a book by {0} or information about their work?'),
]

def generate_response(user_input):
    for pattern, response in patterns_responses:
        match = re.match(pattern, user_input, re.IGNORECASE)
        if match:
            return response.format(match.group(1))
    return "I'm not sure how to help with that. Could you ask something else about books or authors?"

class ChatBotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Chatbot")

        # Create chat history text box
        self.chat_history = scrolledtext.ScrolledText(root, state='disabled', wrap='word', height=20, width=60)
        self.chat_history.pack(padx=10, pady=10)

        # Create user input text box
        self.user_input = tk.Entry(root, width=60)
        self.user_input.pack(padx=10, pady=10)
        self.user_input.bind("<Return>", self.send_message)

        # Create send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(padx=10, pady=10)

    def send_message(self, event=None):
        user_text = self.user_input.get()
        if user_text.strip() == "":
            return

        # Display user message in chat history
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"You: {user_text}\n")
        self.chat_history.config(state='disabled')

        # Generate and display bot response
        bot_response = generate_response(user_text)
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"Bot: {bot_response}\n")
        self.chat_history.config(state='disabled')

        # Clear user input
        self.user_input.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatBotApp(root)
    root.mainloop()