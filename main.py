from tkinter import *
import json
import requests

def buscar_resultados():

    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
    json_data = json.loads(data.content)

    candidato1 = ['']
    candidato2 = ['']
    secoesApuradas = []
    
    for informacoes in json_data['cand']: # Busca e anexa as informações dos candidatos
        if informacoes['seq'] in ['1']:
            candidato1[0] = (informacoes['st'])
            candidato1.append(informacoes['nm'])
            candidato1.append(informacoes['vap'])
            candidato1.append(informacoes['pvap'])
        if informacoes['seq'] in ['2']:
            candidato2[0] = (informacoes['st'])
            candidato2.append(informacoes['nm'])
            candidato2.append(informacoes['vap'])
            candidato2.append(informacoes['pvap'])
    
    # Busca e anexa a porcentagem de seções apuradas
    secoesApuradas.append(json_data['psa'])
    pctSecoesApuradas['text'] = f'{secoesApuradas[0]}%'

    # pega as informações e coloca na string
    texto1 = f'''
    {'1° - ' + candidato1[1]}: {candidato1[3]+'% '} {'|  ' + candidato1[2] + ' votos'}'''
    exibeCandidato1['text'] = texto1

    texto2 = f'''
    {'2° - ' + candidato2[1]}: {candidato2[3]+'% '} {'|  ' + candidato2[2] + ' votos'}'''
    exibeCandidato2['text'] = texto2

    if candidato1[0] == 'Eleito':
        exibeCandidato1['bg'] == '#1aff1a'
    if candidato2[0] == 'Eleito':
        exibeCandidato2['bg'] == '#1aff1a'

def run():
    buscar_resultados()
    window.after(1000, run)
    window.update()

window = Tk()
window.title('Apuração eleições 2022')

txt_orientacao = Label(window, text="Clique no botão a para atualizar os resultados")
txt_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(window, text = "Atualizar Resultados", font=('Arial', 8), command=run)
botao.grid(column=0, row=1, padx=10, pady=10)

exibeCandidato1 = Label(window, text='indisponível', bg='#f2f2f2')
exibeCandidato1.grid(column=0, row=2, padx=10)

exibeCandidato2 = Label(window, text='indisponível', bg='#f2f2f2')
exibeCandidato2.grid(column=0, row=3, padx=10)

pctSecoesApuradas = Label(window, text='', bg='#f2f2f2')
pctSecoesApuradas.grid(column=1, row=1, padx=10, pady=20)

window.mainloop()
