import sqlite3


class Banco():
    def __init__(self):
        self.conexao = sqlite3.connect('decida_por_mim.db')
        self.createTable()

    def createTable(self):
        conn = self.conexao.cursor()

        conn.execute("""
        CREATE TABLE IF NOT EXISTS respostas (
            idresposta integer primary key autoincrement,
            resposta text
        )""")

        self.conexao.commit()
        conn.close()


Banco()
