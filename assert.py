
def testing(min, max, x):
    condicao = x < max and x > min
    mensagem = 'x não está entre o min e o max'

    #o assert verifica se uma condiçao é verdadeira
    #caso for, ele fica em 'silêncio', caso não ele
    #dispara uma mensagem de erro
    assert condicao, mensagem

min = 10
max = 20
x = int(input('X: '))

testing(min, max, x)