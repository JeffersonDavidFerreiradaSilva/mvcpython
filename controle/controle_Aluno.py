from model.model_aluno import ModelAluno
from view.cadastro import cadastro

class controleAluno:
    def __init__(self):
        self.model = ModelAluno()
        self.view = cadastro()
    
    def salvando (self):
        nome,idade,peso = self.view.pega_dados_alunos()
        self.model.criarAluno(nome,idade,peso)
        self.view.mostrar_messagem("Aluno Cadastrado com sucesso!")