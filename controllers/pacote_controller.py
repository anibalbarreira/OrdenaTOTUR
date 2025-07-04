from models.pacote_model import Pacote
from views.pacote_view import CadastroPacoteView
from tkinter import messagebox

class CadastroPacoteController:
    def __init__(self, root):
        self.root = root
        self.view = CadastroPacoteView(self.root, self)
        
    def iniciar_tela(self):
        self.view.mostrar()
        self._centralizar_formulario()
    
    def _centralizar_formulario(self):
        # Força a centralização do conteúdo
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')
    
    def cadastrar_pacote(self, Nome, Descricao, Preco_total):
        if Nome == '' or Descricao == '' or Preco_total == '' :
            messagebox.showinfo("Revise", f"Preencha todos os dados")
            return None
        else:
            pacote = Pacote(Nome=Nome, Descricao=Descricao,  
                            Preco_total=Preco_total)
            pacote.salvar()
            return pacote
    
    def listar_pacote(self):
        return Pacote.buscar_todos()
    
    def atualizar_pacote(self, id, nome, descricao, preco_total):
        Pacote = Pacote(Nome=nome, Descricao=descricao, Preco_total=preco_total, id=id)
        Pacote.salvar()
        return Pacote
    
    def excluir_Pacote(self, id):
        Pacote = Pacote.buscar_por_id(id)
        if Pacote:
           Pacote.deletar()
           return True
        return False