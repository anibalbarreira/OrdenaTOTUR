from models.turista_model import Turista
from views.cadastro_turista_view import CadastroTuristaView
from tkinter import messagebox

class TuristaController:
    def __init__(self, root):
        self.root = root
        self.view = CadastroTuristaView(self.root, self)
        
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
    
    def cadastrar_turista(self, Nome, Email, Telefone, Cidade, Nacionalidade):
        if Nome == '' or Email == '' or Telefone == '' or Cidade == '' or Nacionalidade == '':
            messagebox.showinfo("Revise", f"Preencha todos os dados")
            return None
        else:
            turista = Turista(Nome=Nome, Email=Email, Telefone=Telefone, 
                            Cidade=Cidade, Nacionalidade=Nacionalidade)
            turista.salvar()
            return turista
    
    def listar_turista(self):
        return Turista.buscar_todos()
    
    def atualizar_turista(self, id, nome, email, telefone, cidade, nacionalidade):
        turista = Turista(nome=nome, email=email, telefone=telefone, Cidade=cidade, Nacionalidade=nacionalidade, id=id)
        turista.salvar()
        return turista
    
    def excluir_turista(self, id):
        turista = Turista.buscar_por_id(id)
        if turista:
            turista.deletar()
            return True
        return False