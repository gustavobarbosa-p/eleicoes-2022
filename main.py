from tkinter import *
import json
import requests

def buscar_resultados():

    data = requests.get('https://resultados.tse.jus.br/oficial/ele2022/545/dados-simplificados/br/br-c0001-e000545-r.json')
    json_data = json.loads(data.content)

    candidato1 = []
    candidato2 = []

    # Busca e anexa as informações dos candidatos
    for informacoes in json_data['cand']:
        if informacoes['seq'] in ['1']:
            candidato1.append(informacoes['nm'])
            candidato1.append(informacoes['vap'])
            candidato1.append(informacoes['pvap'])
            candidato1.append(informacoes['st'])
        if informacoes['seq'] in ['2']:
            candidato2.append(informacoes['nm'])
            candidato2.append(informacoes['vap'])
            candidato2.append(informacoes['pvap'])
            candidato1.append(informacoes['st'])

    # pega as informações e coloca na string
    texto = f'''
    {candidato1[0]}: {candidato1[2]+'% '} {'|  ' + candidato1[1] + ' votos'}
    -----------------------------------------------------------------------
    {candidato2[0]}: {candidato2[2]+'% '} {'|  ' + candidato2[1] + ' votos'}'''

    # edita o parâmetro "text" da variável "exibe"
    exibe['text'] = texto

def run():
    buscar_resultados()
    window.after(1000, run)
    window.update()

window = Tk()
window.title('Apuração eleições 2022')

txt_orientacao = Label(window, text="Clique no botão a para atualizar os resultados")
txt_orientacao.grid(column=0, row=0, padx=10, pady=10)

botao = Button(window, text = "Atualizar Resultados", font=('Arial', 10), command=run)
botao.grid(column=0, row=1, padx=10, pady=10)

exibe = Label(window, text='indisponível', bg='#f2f2f2')
exibe.grid(column=0, row=2, padx=10, pady=20)

window.mainloop()
