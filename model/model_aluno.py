import pymysql
class ModelAluno:
    def __init__(self):
        self.conexao = pymysql.connect(
            host="localhost",
            user="root",
            password="@Cursos21",
            database="serpro",
            cursorclass = pymysql.cursors.DictCursor
        )
    def criarAluno (self, nome, idade, peso):
        try: 
         with self.conexao.cursor() as cursor:
            criandoAluno = "INSERT INTO tb_alunos (nome, idade, peso) VALUES (%s, %s, %s)"
            valores = (nome, idade, peso)
            cursor.execute(criandoAluno, valores)
            self.conexao.commit()
        finally:
           self.conexao.close()