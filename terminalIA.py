import os
import requests
import tkinter as tk
from tkinter import scrolledtext

# Substitua pela sua chave da Groq
GROQ_API_KEY = "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"
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

def query_groq(messages):
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-8b-8192",  # Modelo a ser utilizado
        "messages": messages
    }
    
    response = requests.post(GROQ_API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Erro: {response.status_code} - {response.text}"

def send_message():
    user_input = entry.get()
    if user_input:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"{user_name}: {user_input}\n\n")  # Adiciona linha em branco
        chat_area.config(state=tk.DISABLED)
        
        messages.append({"role": "user", "content": user_input})
        
        response = query_groq(messages)
        
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Cael-ia: {response}\n\n")  # Adiciona linha em branco
        chat_area.config(state=tk.DISABLED)
        
        messages.append({"role": "assistant", "content": response})
        entry.delete(0, tk.END)

def set_user_name():
    global user_name
    user_name = name_entry.get()
    if user_name:
        chat_area.config(state=tk.NORMAL)
        chat_area.insert(tk.END, f"Cael-ia: Olá, {user_name}! Eu sou uma inteligencia artificial criada por Cael P. Alves. ainda estou em desenvolvimento. Como posso ajudar você hoje?\n\n")  # Adiciona linha em branco
        chat_area.config(state=tk.DISABLED)
        name_frame.pack_forget()  # Ocultar o frame de entrada do nome

# Inicializar a lista de mensagens e o nome do usuário
messages = []
user_name = ""

# Configuração da janela principal
root = tk.Tk()
root.title("Chatbot Interface")

# Frame para entrada do nome
name_frame = tk.Frame(root)
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="Antes de começarmos, por favor me diga seu nome:")
name_label.pack()

name_entry = tk.Entry(name_frame)
name_entry.pack(pady=5)

name_button = tk.Button(name_frame, text="Enviar", command=set_user_name)
name_button.pack(pady=5)

# Área de texto para exibir o chat
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED)
chat_area.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# Campo de entrada para o usuário (ajustado para ser mais largo)
entry = tk.Entry(root, width=120)  # Aumente a largura para 120
entry.pack(pady=10, padx=10)

# Botão para enviar a mensagem
send_button = tk.Button(root, text="Enviar", command=send_message)
send_button.pack(pady=10)

# Iniciar a interface
root.mainloop()
