import tkinter as tk
from tkinter import font as tkfont
from tkinter import PhotoImage
import os

class TelaAcoes:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None
        self.fonte = tkfont.Font(family="Helvetica", size=14)
        self.logo_img = None  # manter a imagem como atributo para não ser coletada pelo GC
        
    def mostrar(self):
        self._configurar_janela()
        self._criar_widgets()
        
    def _configurar_janela(self):
        self.root.title("Agência de Turismo")
        self.root.configure(bg="#E9F1F7")
        self.root.attributes('-fullscreen', True)
        
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_widgets(self):
        if self.frame:
            self.frame.destroy()
            
        self.frame = tk.Frame(self.root, bg="#E9F1F7")
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

        # Carrega a imagem LOGO.png da raiz do projeto
        try:
            logo_path = os.path.join(os.path.dirname(__file__), "..", "LOGO.png")
            self.logo_img = PhotoImage(file=logo_path)
            logo_label = tk.Label(self.frame, image=self.logo_img, bg="#E9F1F7")
            logo_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))
        except Exception as e:
            print("Erro ao carregar LOGO.png:", e)

        titulo = tk.Label(
            self.frame,
            text="OrdenaTOTUR",
            font=("Helvetica", 32, "bold"),
            bg="#E9F1F7",
            fg="#2C3E50"
        )
        titulo.grid(row=1, column=0, columnspan=2, pady=(0, 30))

        botoes = [
            ("Cadastrar Turista - F1", self.controller.abrir_cadastro_turista, "#28A745", "F1"),
            ("Cadastrar Atrativo Turístico - F2", self.controller.abrir_cadastro_atrativo_turistico, "#F39C12", "F2"),
            ("Cadastrar Pacote - F3", self.controller.abrir_cadastro_pacote, "#3498DB", "F3"),
            ("Nossos Pacotes - F4", lambda: print("Nossos Pacotes"), "#F1C40F", "F4"),
            ("Sair - F5", self.controller.sair, "#E74C3C", "F4")
        ]
        
        for i, (texto, comando, cor, tecla) in enumerate(botoes):
            button = tk.Button(
                self.frame,
                text=texto,
                width=30,
                font=self.fonte,
                command=comando,
                bg=cor,
                fg="white",
                relief=tk.RAISED,
                borderwidth=3,
                padx=20,
                pady=10
            )
            button.grid(row=i + 2, column=0, columnspan=2, pady=10, sticky="ew")
            self.root.bind(f"<{tecla}>", lambda event, comando=comando: comando())

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)