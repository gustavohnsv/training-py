import requests
from tkinter import *

def buscar_cep():
    try:

        cep = txtbox_value.get()
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")

        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            request = requests.get(link)
            dic_request = request.json()
            logradouro = dic_request['logradouro']
            complemento = dic_request['complemento']
            bairro = dic_request['bairro']
            localidade = dic_request['localidade']
            uf = dic_request['uf']
            ddd = dic_request['ddd']

            txtbox_logradouro['text'] = logradouro
            txtbox_bairro['text'] = bairro
            txtbox_uf['text'] = uf

            print(logradouro, complemento, bairro, localidade, uf, ddd)
        else:
            print('CEP Inválido.')
    except Exception as error:
        print(f'Erro localizado: ', error)

janela = Tk()
janela.title('API de Busca de CEP')
janela.geometry('300x200')
# janela.configure(background='')

lbl_info = Label(janela, text='Informe seu CEP abaixo:')
lbl_info.grid(column=0, row=0, padx=4, pady=4)

txtbox_value = Entry(janela)
txtbox_value.grid(column=0, row=1, padx=4, pady=4)

btn_enviar = Button(janela, text='Enviar', command=buscar_cep)
btn_enviar.grid(column=0, row=2, padx=4, pady=4)

txtbox_logradouro = Label(janela, state=DISABLED, text='')
txtbox_logradouro.grid(column=3, row=0)

txtbox_bairro = Label(janela, state=DISABLED, text='')
txtbox_bairro.grid(column=3, row=1)

txtbox_uf = Label(janela, state=DISABLED, text='')
txtbox_uf.grid(column=3, row=2)

janela.mainloop()

