import tkinter as tk
from tkinter import font as tkfont

class TelaAcoes:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame = None
        self.fonte = tkfont.Font(family="Helvetica", size=12)
        
    def mostrar(self):
        self._configurar_janela()
        self._criar_widgets()
        
    def _configurar_janela(self):
        self.root.title("Agência de Turismo")
        self.root.configure(bg="#DCE6F1")
        self.root.attributes('-fullscreen', True)
        
        # Centralizar conteúdo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_widgets(self):
        if self.frame:
            self.frame.destroy()
            
        self.frame = tk.Frame(self.root, bg="#DCE6F1")
        self.frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        
        tk.Label(self.frame, 
                text="OrdenaTOTUR",
                font=("Helvetica", 16, "bold"),
                bg="#DCE6F1").pack(pady=(0, 20))
        
        botoes = [
            ("Cadastrar Turista", self.controller.abrir_cadastro_turista),
            ("Cadastrar Atrativo Turistico", self.controller.abrir_cadastro_atrativo_turistico),
            ("Cadastrar Pacote", self.controller.abrir_cadastro_pacote),
            ("Gerenciar Reservas", lambda: print("Gerencias Reservas")),
            ("Avaliações", lambda: print("Avaliações")),
            ("Sair", self.controller.sair)
        ]
        
        for texto, comando in botoes:
            tk.Button(
                self.frame,
                text=texto,
                width=25,
                font=self.fonte,
                command=comando,
                bg="#4BACC6",
                fg="white",
                relief=tk.RAISED,
                borderwidth=2
            ).pack(pady=5, ipady=5)