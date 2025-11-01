import tkinter as tk
from tkinter import scrolledtext
from openai import OpenAI

# --- Initialize ChatGPT client ---
client = OpenAI(api_key="")  # Replace with your API key

# --- Function to get response from ChatGPT ---
def get_response(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful chatbot."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# --- Function to send message ---
def send_message():
    user_input = user_entry.get()
    if user_input.strip() == "":
        return
    chat_window.config(state=tk.NORMAL)
    chat_window.insert(tk.END, f"You: {user_input}\n", "user")
    chat_window.insert(tk.END, "Bot: Thinking...\n", "bot")
    chat_window.config(state=tk.DISABLED)
    root.update()

    # Get bot response
    response = get_response(user_input)

    chat_window.config(state=tk.NORMAL)
    chat_window.delete("end-2l", "end-1l")  # Remove "Thinking..."
    chat_window.insert(tk.END, f"Bot: {response}\n\n", "bot")
    chat_window.config(state=tk.DISABLED)
    chat_window.yview(tk.END)
    user_entry.delete(0, tk.END)

# --- GUI Setup ---
root = tk.Tk()
root.title("Simple AI Chatbot")
root.geometry("500x600")
root.config(bg="#1e1e1e")

# Chat display area
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, bg="#2d2d2d", fg="white", font=("Arial", 12))
chat_window.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_window.config(state=tk.DISABLED)

# Input field
user_entry = tk.Entry(root, font=("Arial", 14), bg="#3c3c3c", fg="white")
user_entry.pack(padx=10, pady=10, fill=tk.X)
user_entry.bind("<Return>", lambda event: send_message())

# Send button
send_button = tk.Button(root, text="Send", font=("Arial", 12, "bold"), bg="#0078D7", fg="white", command=send_message)
send_button.pack(pady=5)

# Style tags
chat_window.tag_config("user", foreground="#00ffcc")
chat_window.tag_config("bot", foreground="#ffffff")

root.mainloop()
