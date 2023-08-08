import tkinter as tk
from ttkbootstrap import Style
from templates.jocke_app import JokeGetter

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Joke")
        self.root.geometry("700x400")
        style = Style(theme="flatly")
        self.root.style = style

        self.joke_label = tk.Label(text="Click the button to get a random joke!",
                                  font=("TkDefaultFont", 20))
        self.joke_label.place(relx=0.5, rely=0.5, anchor="center")

        self.get_joke_button = tk.Button(text="Get Joke", command=self.update_joke)
        self.get_joke_button.pack(pady=20)

        self.joke_getter = JokeGetter()

    def update_joke(self):
        setup, punchline = self.joke_getter.get_joke()
        self.joke_label.configure(text=f"{setup}\n\n {punchline}")

def main():
    window = tk.Tk()
    app = GUI(window)
    window.mainloop()

if __name__ == "__main__":
    main()