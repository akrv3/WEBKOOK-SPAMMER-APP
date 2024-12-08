import customtkinter
from customtkinter import *
import requests

def webhookspamm():
    webhook = entry1.get()
    msg = entry2.get()
    name = entry3.get()
    
    webhook_url = webhook  
    data = {
        "content": msg,
        "username": name  
        }
    while True:
        response = requests.post(webhook_url, json=data)


app = customtkinter.CTk()
app.geometry("500x500")
app.title("Webhook tool - akr") 
app.iconbitmap('IMG_4588.ico')

tabview = CTkTabview(master=app)
tabview.pack(padx=100, pady=100)

tabview.add("WEBHOOK SPAMMER")

entry1 = CTkEntry(master=tabview.tab("WEBHOOK SPAMMER"), placeholder_text="WEBHOOK")
entry1.pack(padx=20, pady=20)

entry2 = CTkEntry(master=tabview.tab("WEBHOOK SPAMMER"), placeholder_text="MESSAGE")
entry2.pack(padx=20, pady=20)

entry3 = CTkEntry(master=tabview.tab("WEBHOOK SPAMMER"), placeholder_text="WEBHOOK NAME")
entry3.pack(padx=20, pady=20)


button3 = CTkButton(
    master=tabview.tab("WEBHOOK SPAMMER"), 
    text="START", 
    command=webhookspamm, 
    width=60, 
    height=30, 
    fg_color="darkred", 
)
button3.pack(padx=5, pady=5)

app.mainloop()
