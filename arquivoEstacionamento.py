class Arquivo:

  try:
    arquivo = open('vagas.txt')
  except FileNotFoundError:
    print('Não foi possível encontrar o arquivo vagas.txt')

  def rewind(self,f):
    f.seek(0)

  def imprime_tudo(self,f):
    print(f.read())

  def fechar(self,f):
    f.close()
