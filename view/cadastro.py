class cadastro:
    @staticmethod
    def pega_dados_alunos():
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        peso = float(input("Digite seu peso:" ))
        return nome,idade,peso
    
    @staticmethod
    def mostrar_messagem(messagem):
        print(messagem)