from models.atrativo_turistico_model import Atrativo_turistico
from views.cadastro_atrativo_turistico_view import CadastroAtrativoturisticoView
from controllers.pacote_controller import CadastroPacoteController
from tkinter import messagebox

class CadastroAtrativoturisticoController:
    def __init__(self, root):
        self.root = root
        self.pacote_controller = CadastroPacoteController(root)
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
    
    def cadastrar_atrativo_turistico(self, Nome, Tipo, Cidade, Preco, id_Pacote):
        if Nome == '' or Tipo == '' or Cidade == '' or Preco == '' or id_Pacote == '':
            messagebox.showinfo("Revise", f"Preencha todos os dados")
            return None
        else:
            atrativo_turistico = Atrativo_turistico(Nome=Nome, Tipo=Tipo, Cidade=Cidade, 
                            Preco=Preco, id_Pacote=id_Pacote)
            atrativo_turistico.salvar()
            return atrativo_turistico
    
    def listar_atrativo_turistico(self):
        return Atrativo_turistico.buscar_todos()
    
    def atualizar_atrativo_turistico(self, id, nome, tipo, cidade, preco, id_pacote):
        atrativo_turistico = Atrativo_turistico(Nome=nome, Tipo=tipo,  Cidade=cidade, Preco=preco, id_Pacote=id_pacote, id=id)
        atrativo_turistico.salvar()
        return atrativo_turistico
    
    def excluir_Atrativo_turistico(self, id):
        atrativo_turistico = Atrativo_turistico.buscar_por_id(id)
        if atrativo_turistico:
            atrativo_turistico.deletar()
            return True
        return False