from estacionamento import Estacionamento 
from arquivoEstacionamento import Arquivo 

arquivo = open('vagas.txt')
class Menu:

  def menu(self):
    print("Selecione uma opção: ")
    print("1. Mostrar todas as vagas: ")
    print("2. Mostrar vagas livres: ")
    print("3. Estacionar carro: ")
    print("4. Remover carro: ")
    print("5. Mostrar vagas atualizadas: ")
    print("0. Sair. ")
    opcao = input("> ")

    while opcao == "1":
        a.imprime_tudo(arquivo)
        a.rewind(arquivo)
        self.menu()
    while opcao == "2":
        e.mostra_vagas_livres()
        a.rewind(arquivo)
        self.menu()
    while opcao == "3":
        e.estaciona_carro()
        self.menu()
    while opcao == "4":
        e.remove_carro()
        self.menu()
    while opcao == "5":
        e.mostra_atualizado()
        a.rewind(arquivo)
        self.menu()
    while opcao == "0":
        a.rewind(arquivo)
        a.fechar(arquivo)
        e.sair()
    if opcao > "5" or opcao < "0":
        print("Opção inválida.")

a = Arquivo()
e = Estacionamento()