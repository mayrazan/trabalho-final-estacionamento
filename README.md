Trabalho final do curso de Python da UNOESC.

                                Vaga de Estacionamento

Implementar em Python um programa para controlar 20 vagas de um estacionamento particular. Monte
um menu de opções conforme o exemplo abaixo e implemente as funções para que cada opção do menu
funcione corretamente:

                                        MENU:

1 - Mostrar todas as vagas, exemplo: Vaga 0: Ocupada, Vaga 1: Ocupada, Vaga ….

2 - Mostrar vagas livres, exemplo: Vaga 2 Livre, Vaga 4 Livre, Vaga 8...

3 - Estacionar carro: Informar o número de uma vaga livre e marcar a vaga como ocupada, caso a vaga estiver
ocupada avisar o usuário

4 - Remover carro: Informar o número de uma vaga ocupada e fazer a remoção do veículo, caso a vaga estiver
livre avisar o usuário

5 - Resumo do estacionamento, exemplo: 3 vagas livres, 7 vagas ocupados

Observações: O programa deve iniciar com todas as vagas livres e a opção 0 para sair do programa, ou seja,
depois de escolher qualquer opção deve sempre voltar ao menu. Deve gravar as vagas livre e ocupadas em um
arquivo, assim ao finalizar o programa não será perdido as informações.

O código deve utilizar o paradigma de orientação a objetos. Sendo que, deve ter pelo menos três classes:

• Estacionamento: Onde deve conter a lógica de remover, adicionar, listar veículos/vagas, ou seja,
implementado a lógica das opções selecionadas no menu principal.

• MenuPrincipal: Deve conter a implementação do menu e a leitura e tratamento das opções de usuário.

• ArquivoEstacionamento: Deve ser responsável por gravar e ler os dados salvos em arquivo txt.

