import tkinter as tk

class TelaAcoes:
    def __init__(self, controller):
        self.controller = controller
        self.root = controller.root
        self.frame = tk.Frame(self.root, bg="#DCE6F1")

        self.root.configure(bg="#DCE6F1")
        self.root.attributes('-fullscreen', True)

    def mostrar(self):
        self.root.title("Agência")
        self.frame.pack(padx=20, pady=20)


        tk.Button(self.frame, text="Cadastrar Turista", width=30).pack(pady=5)
        tk.Button(self.frame, text="Reservar", width=30).pack(pady=5)
        tk.Button(self.frame, text="Reservar", width=30).pack(pady=5)
        tk.Button(self.frame, text="Reservar", width=30).pack(pady=5)
        tk.Button(self.frame, text="Sair", width=30, comand=self.root.quit).pack(pady=5)