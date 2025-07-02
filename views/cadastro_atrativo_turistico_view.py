import tkinter as tk
from tkinter import messagebox, ttk

class CadastroAtrativoturisticoView:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.frame_principal = None
        self._configurar_estilos()
        
    def _configurar_estilos(self):
        self.style = ttk.Style()
        self.style.configure('TFrame', background='#DCE6F1')
        self.style.configure('TLabel', background='#DCE6F1', font=('Helvetica', 12))
        self.style.configure('TButton', font=('Helvetica', 12), padding=5)
        self.style.configure('TEntry', font=('Helvetica', 12), padding=5)

    def mostrar(self):
        self._configurar_janela()
        self._criar_formulario()
        
    def _configurar_janela(self):
        self.root.title("Cadastro de Atrativo Turistico - Agência de Turismo")
        self.root.configure(bg='#DCE6F1')
        
        # Centraliza o conteúdo
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
    def _criar_formulario(self):
        if self.frame_principal:
            self.frame_principal.destroy()
            
        self.frame_principal = ttk.Frame(self.root, padding=20)
        self.frame_principal.grid(row=0, column=0, sticky='nsew')
        
        frame_form = ttk.Frame(self.frame_principal)
        frame_form.pack(pady=50)
        
        ttk.Label(frame_form, 
                 text="Cadastro de Atrativo Turistico",
                 font=('Helvetica', 16, 'bold')).grid(row=0, column=0, columnspan=2, pady=20)
        
        # Variáveis para os campos
        self.var_nome = tk.StringVar()
        self.var_cidade = tk.StringVar()
        self.var_tipo = tk.StringVar()
        self.var_preco = tk.StringVar()
                
        # Campos do formulário
        campos = [
            ("Nome:", self.var_nome),
            ("Cidade:", self.var_cidade),
            ("Tipo:", self.var_tipo),
            ("Preço:", self.var_preco),
        ]
        
        for i, (label, var) in enumerate(campos, start=1):
            ttk.Label(frame_form, text=label).grid(row=i, column=0, sticky='e', padx=5, pady=5)
            ttk.Entry(frame_form, textvariable=var, width=40).grid(row=i, column=1, padx=5, pady=5)
        
        # Frame dos botões
        frame_botoes = ttk.Frame(self.frame_principal)
        frame_botoes.pack(pady=20)
        
        ttk.Button(frame_botoes, text="Salvar", command=self._salvar).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes, text="Limpar", command=self._limpar).pack(side=tk.LEFT, padx=10)
        ttk.Button(frame_botoes, text="Voltar", command=self._fechar).pack(side=tk.LEFT, padx=10)

    def _salvar(self):
        try:
            dados = {
                'Nome': self.var_nome.get(),
                'Cidade': self.var_cidade.get(),
                'Tipo': self.var_tipo.get(),
                'Preco': self.var_preco.get(),
            }
            
            # Chama o controller para cadastrar
            atrativoturistico = self.controller.cadastrar_atrativoturistico(**dados)
            messagebox.showinfo("Sucesso", f"Atrativoturistico {atrativoturistico.Nome} cadastrado com sucesso!")
            self._limpar()
            
        except Exception as e:
            messagebox.showerror("Erro", f"Falha ao cadastrar: {str(e)}")
    
    def _limpar(self):
        self.var_nome.set("")
        self.var_cidade.set("")
        self.var_tipo.set("")
        self.var_preco.set("")
            
    def _fechar(self):
        self.root.destroy()