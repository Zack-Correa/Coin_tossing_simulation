import plotly.graph_objects as go
import random

chance = 0.5
rounds = 0
nCoins = 0
normal_distribution = {}


def coin_tossing(rounds, nCoins):
    coins_tossed = []
    for i in range(rounds):
        head = 0
        tails = 0
        for j in range(nCoins):
            if random.random() < chance:
                head += 1
            else:
                tails += 1
        try:
            normal_distribution[head] += 1
        except:
            normal_distribution[head] = 1


class TossedCoins:
    def __init__(self, head_num, tails_num):
        self.head_Num = head_num
        self.tails_Num = tails_num


try:
    rounds = int(
        input('Digite a quantidade de vezes que as moedas serão jogadas: '))
    nCoins = int(
        input('\n\rDigite a quantidade de moedas que serão jogadas: '))
except:
    print('Entrada em formato incorreto!')


coin_tossing(rounds, nCoins)


list_keys = [k for k in normal_distribution]
list_values = [k for k in normal_distribution.values()]

layout = go.Layout(title="Simulação de jogada de moedas", xaxis={
                   'title': 'Número de moedas'}, yaxis={'title': 'Quantidade de jogadas'})
fig = go.Figure(data=go.Bar(x=list_keys, y=list_values), layout=layout)
fig.write_html('first_figure.html', auto_open=True)
