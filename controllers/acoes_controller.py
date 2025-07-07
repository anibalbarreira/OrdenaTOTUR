from views.acoes_view import TelaAcoes
from controllers.turista_controller import TuristaController
from controllers.pacote_controller import CadastroPacoteController
from controllers.atrativo_turistico_controller import CadastroAtrativoturisticoController
import tkinter as tk

class AcoesController:
    def __init__(self, root):
        self.root = root
        self.pacote_controller = CadastroPacoteController(self.root)
        self.view = TelaAcoes(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
    
    def abrir_cadastro_turista(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        TuristaController(cadastro_window).iniciar_tela()

    def abrir_cadastro_atrativo_turistico(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        CadastroAtrativoturisticoController(cadastro_window).iniciar_tela()
    
    def abrir_cadastro_pacote(self):
        cadastro_window = tk.Toplevel(self.root)
        cadastro_window.attributes('-fullscreen', True)
        CadastroPacoteController(cadastro_window).iniciar_tela()
        
    def abrir_lista_pacotes(self):
        # Criar a janela de listagem de pacotes
        lista_window = tk.Toplevel(self.root)
        lista_window.title("Lista de Pacotes")
        lista_window.configure(bg="#E9F1F7")
        lista_window.attributes('-fullscreen', True)

        
        # Título da tela
        titulo = tk.Label(
            lista_window,
            text="Lista de Pacotes",
            font=("Helvetica", 30, "bold"),
            bg="#E9F1F7",
            fg="#2C3E50"
        )
        titulo.grid(row=1, column=0, columnspan=2, pady=(20, 50), sticky="n")

        # Obter pacotes da controller
        pacotes = self.pacote_controller.listar_pacote()

        # Criar o Treeview para exibir os pacotes
        tree = tk.Treeview(lista_window, columns=("ID", "Nome", "Descrição", "Preço"), show="headings")
        tree.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

        # Definir os cabeçalhos das colunas
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Descrição", text="Descrição")
        tree.heading("Preço", text="Preço")

        # Preencher o Treeview com os pacotes
        for pacote in pacotes:
            tree.insert("", "end", values=(pacote.id, pacote.Nome, pacote.Descricao, pacote.Preco_total))

        # Ajustar largura das colunas
        tree.column("ID", width=50, anchor="center")
        tree.column("Nome", width=200, anchor="w")
        tree.column("Descrição", width=250, anchor="w")
        tree.column("Preço", width=100, anchor="e")

        # Adicionar botão de fechar
        button_fechar = tk.Button(
            lista_window,
            text="Fechar",
            command=lista_window.destroy,  # Fechar a janela
            bg="#E74C3C",
            fg="white",
            relief=tk.RAISED,
            borderwidth=3,
            padx=20,
            pady=10
        )
        button_fechar.grid(row=3, column=0, columnspan=2, pady=20)

    def sair(self):
        self.root.quit()