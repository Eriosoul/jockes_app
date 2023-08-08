from templates.interface import main

if __name__ == "__main__":
    main()

# import requests
# import tkinter as tk
# from tkinter import ttk
# from ttkbootstrap import Style
#
# def get_joke():
#     # request to api
#     resource = requests.get("https://official-joke-api.appspot.com/random_joke")
#     # Get json data
#     data = resource.json()
#     setup = data["setup"]
#     punchline = data["punchline"]
#     # set the text in label
#     joke_label.configure(text=f"{setup}\n\n {punchline}")
#
#
#
# window = tk.Tk()
# window.title("Random Jocke")
# window.geometry("700x400")
# style = Style(theme="flatly")
# window.style = style
#
# joke_label = tk.Label(text="Clic the button to get a random joke!",
#                        font=("TkDefaultFont", 20))
# joke_label.place(relx=0.5, rely=0.5, anchor="center")
#
# get_joke_button = tk.Button(text="Get Joke", command=get_joke)
# get_joke_button.pack(pady=20)
#
# window.mainloop()
