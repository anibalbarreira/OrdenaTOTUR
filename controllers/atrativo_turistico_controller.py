from models.atrativo_turistico_model import Atrativo_turistico
from views.cadastro_atrativo_turistico_view import CadastroAtrativoturisticoView
from tkinter import messagebox

class CadastroAtrativoturisticoController:
    def __init__(self, root):
        self.root = root
        self.view = CadastroAtrativoturisticoView(self.root, self)
        
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
    
    def cadastrar_atrativo_turistico(self, Nome, Cidade, Tipo, Preco):
        if Nome == '' or Cidade == '' or Tipo == '' or Preco == '':
            messagebox.showinfo("Revise", f"Preencha todos os dados")
            return None
        else:
            Atrativo_turistico = Atrativo_turistico(Nome=Nome, Cidade=Cidade, Tipo=Tipo, 
                            Preco=Preco)
            Atrativo_turistico.salvar()
            return Atrativo_turistico
    
    def listar_atrativo_turistico(self):
        return Atrativo_turistico.buscar_todos()
    
    def atualizar_atrativo_turistico(self, id, nome, cidade, tipo, preco):
        Atrativo_turistico = Atrativo_turistico(nome=nome, Cidade=cidade, Tipo=tipo, Preco=preco, id=id)
        Atrativo_turistico.salvar()
        return Atrativo_turistico
    
    def excluir_Atrativo_turistico(self, id):
        Atrativo_turistico = Atrativo_turistico.buscar_por_id(id)
        if Atrativo_turistico:
            Atrativo_turistico.deletar()
            return True
        return False