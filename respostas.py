from banco import Banco
import random


class Respostas(object):
    def inserirNovaResposta(self, respostas):
        banco = Banco()

        conn = banco.conexao.cursor()

        conn.execute(f"""
            INSERT INTO respostas (resposta)
            VALUES ('{respostas}')
        """)

        banco.conexao.commit()
        conn.close()

        print("Nova resposta cadastrada com sucesso!")

    def editarResposta(self, idresposta, respostas):
        banco = Banco()

        conn = banco.conexao.cursor()

        conn.execute(f"""
            UPDATE respostas SET resposta = '{respostas}'
            WHERE idresposta = '{idresposta}'
        """)

        banco.conexao.commit()
        conn.close()

        print('Resposta alterada com sucesso!')

    def excluirResposta(self, idresposta):
        banco = Banco()

        conn = banco.conexao.cursor()

        conn.execute(f"""
            DELETE FROM respostas WHERE idresposta = '{idresposta}'
        """)

        banco.conexao.commit()
        conn.close()

        print('Resposta excluída com sucesso')

    def mostrarRespostasCadastradas(self):
        banco = Banco()

        conn = banco.conexao.cursor()

        conn.execute("""
            SELECT idresposta, resposta FROM respostas
        """)

        for i in conn.fetchall():
            print(i)

        conn.close()

    def respostaAleatoria(self):
        banco = Banco()

        conn = banco.conexao.cursor()

        conn.execute("""
            SELECT resposta FROM respostas ORDER BY RANDOM() limit 1;
        """)

        self.respostas_aleatorias = [list(i) for i in conn.fetchall()]

        return random.choice(self.respostas_aleatorias)
