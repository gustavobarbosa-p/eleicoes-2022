import requests
import json
from tkinter import *

def resultado_eleicoes():

    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
    json_data = json.loads(data.content)

    candidato1 = []
    candidato2 = []

    # Busca e anexa as informações dos candidatos
    for informacoes in json_data['cand']:
        if informacoes['seq'] in ['1']:
            candidato1.append(informacoes['nm'])
            candidato1.append(informacoes['vap'])
            candidato1.append(informacoes['pvap'])
        if informacoes['seq'] in ['2']:
            candidato2.append(informacoes['nm'])
            candidato2.append(informacoes['vap'])
            candidato2.append(informacoes['pvap'])

    # pega as informações e coloca na string
    texto = f'''
    {candidato1[0]}: {candidato1[2]+'% '} {'|  ' + candidato1[1] + ' votos'}
    -----------------------------------------------------------------------
    {candidato2[0]}: {candidato2[2]+'% '} {'|  ' + candidato2[1] + ' votos'}'''

    # edita o parâmetro "text" da variável "exibe"
    exibe['text'] = texto

#------------------------JANELA------------------------#
window = Tk()
window.title('Segundo Turno 2022')

txt_orientacao = Label(window, text="Clique no botão a para atualizar os resultados")
txt_orientacao.grid(column = 0, row = 0, padx = 10, pady = 10)

botao = Button(window, text = "Atualizar Resultados", command = resultado_eleicoes)
botao.grid(column = 0, row = 1, padx = 10, pady = 10)

exibe = Label(window, text = 'indisponível')
exibe.grid(column = 0, row = 2, padx = 20, pady = 20)

window.mainloop()