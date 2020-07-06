from time import sleep
from respostas import Respostas

respostas = Respostas()


class DecidaPorMim():
    def Menu(self):
        print('* Seja muito bem-vindo ao programa "Decida por mim". *')
        print()
        print('************ Menu **************')
        print('********************************')
        print('* i : Iniciar                  *')
        print('* c : Cadastrar nova resposta  *')
        print('* l : Listar frases existentes *')
        print('* e : Editar frase             *')
        print('* d : Deletar alguma frase     *')
        print('* s : Sair                     *')
        print('********************************')

        self.inicio = input(
            "Digite o atalho referente a atividade que deseja fazer: ")

        if self.inicio not in ['i', 'c', 'e', 'd', 's', 'l']:
            print("Operação inválida!")
            exit()

        if self.inicio == 'i':
            self.Iniciar()

        if self.inicio == 'c':
            respostas.inserirNovaResposta(
                input("Favor, digite a nova frase:\n"))
            sleep(1)
            self.DesejaContinuar()

        if self.inicio == 'l':
            respostas.mostrarRespostasCadastradas()
            sleep(1)
            self.DesejaContinuar()

        if self.inicio == 'e':
            respostas.editarResposta(int(input(
                "Insira o ID da resposta que será editada: ")),
                input("Edite como quiser:\n"))
            sleep(1)
            self.DesejaContinuar()

        if self.inicio == 'd':
            respostas.excluirResposta(
                int(input("Digite o ID da frase que deseja deletar:\n")))
            sleep(1)
            self.DesejaContinuar()

        if self.inicio == 's':
            print("Até breve!")
            exit()

    def Iniciar(self):
        self.DuvidaDoUsuario()
        print('Pensando...')
        sleep(3)
        respostas.respostaAleatoria()
        sleep(2)
        self.DesejaContinuar()

    def DesejaContinuar(self):
        self.deseja_continuar = input(
            'Deseja fazer mais alguma ação?(s/n) ').lower()

        if self.deseja_continuar == 's':
            self.Menu()
        elif self.deseja_continuar == 'n':
            print('Até mais!')
            while True:
                break
        else:
            print('Por favor, digite "s" para sim ou "n" para não.')
            self.DesejaContinuar()

    def DuvidaDoUsuario(self):
        self.duvida = input("Faça-me uma pergunta: ")


start = DecidaPorMim()
start.Menu()
