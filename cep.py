import requests
try:
    while True:
        
        cep = input('Informe o CEP: ')
        cep = cep.replace("-", "").replace(".", "").replace(" ", "")

        if len(cep) == 8:
            link = f'https://viacep.com.br/ws/{cep}/json/'
            request = requests.get(link)
            dic_request = request.json()
            logradouro = dic_request['logradouro']
            bairro = dic_request['bairro']
            uf = dic_request['uf']
            print(logradouro, bairro, uf)
        else:
            print('CEP Inválido.')
        opcao = input('Deseja informar outro CEP? (s/n): ')
        if opcao == 'n':
            break
except Exception as error:
    print(f'Erro localizado: ', error)
