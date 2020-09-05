import sys

class Estacionamento:

  def mostra_vagas_livres(self):
    count=0
    with open('vagas.txt', 'r') as f:
        texto = f.readlines()
        for posicao, i in enumerate(texto):
            if 'livre' in texto[posicao]:
                i = i.rsplit()
                print(i)
            elif 'ocupada' in texto[posicao]:
                count += 1
        if count == 20:
            print("Todas as vagas estão ocupadas.")

  def estaciona_carro(self):
    vaga = int(input("Informe o número de uma vaga: "))
    with open('vagas.txt', 'r') as a:
        texto = a.readlines()
    with open('vagas.txt', 'w') as a:
        for posicao, i in enumerate(texto):
            if posicao == vaga and 'livre' in texto[posicao]:
                temp = i.split('livre')
                i = 'ocupada'.join(temp)
                a.write(i)
            elif posicao == vaga and 'ocupada' in texto[posicao]:
                a.write(i)
                print('Vaga já ocupada.')
            else:
                a.write(i)
        if vaga > 19:
            print("Número de vaga não existe.")

  def remove_carro(self):
    vaga = int(input("Informe o número da vaga para ser liberada: "))
    with open('vagas.txt', 'r') as a:
        texto = a.readlines()
    with open('vagas.txt', 'w') as a:
        for posicao, i in enumerate(texto):
            if posicao == vaga and 'ocupada' in texto[posicao]:
                temp = i.split('ocupada')
                i = 'livre'.join(temp)
                a.write(i)
            elif posicao == vaga and 'livre' in texto[posicao]:
                a.write(i)
                print('Vaga já está livre.')
            else:
                a.write(i)
    if vaga > 19:
        print("Número de vaga não existe.")

  def mostra_atualizado(self):
    l = 0
    o = 0
    with open('vagas.txt', 'r') as f:
        texto = f.readlines()
        for posicao, i in enumerate(texto):
            if 'livre' in texto[posicao]:
                l += 1
            elif 'ocupada' in texto[posicao]:
                o += 1
    print("Resumo do estacionamento")
    print("-----------------------------")
    print(" %d vagas livres e %d vagas ocupadas" % (l, o))

  def sair(self):
    sys.exit()