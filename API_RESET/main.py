import requests
print('######################################################')
print('#################### CONSULTA CEP ####################')
print('######################################################')
print()
## o input é para colocar o cep
cep_input =  input('DIGITE SEU CEP')
## o if é para caso der erro sair da programação
if len(cep_input) != 8:
    print('ERRO')
    exit()
## font request https://postmon.com.br/
request = requests.get(f'https://api.postmon.com.br/v1/cep/{cep_input}')


### abaixo linha de código para caso tenha que testar o request antes de fazer o resto do código
### print(request.json())
### result : com o teste cpf 13054205
# {'bairro': 'Dic II (Conj Habitacional Doutor Antônio Mendonça 
# de Barros)','cidade': 'Campinas', 'logradouro': 'Rua Aguinaldo José Antoniolli', 
# 'estado_info': {'area_km2': '248.221,996', 'codigo_ibge': '35', 'nome': 
# 'São Paulo'}, 'cep': '13054205', 'cidade_info': {'area_km2': '794,571', 
# 'codigo_ibge': '3509502'}, 'estado': 'SP'}

address_data = request.json()
if 'erro' not in address_data:
## Se caso não der erro
    print('====> DEU CERTO DE ENCONTRAR O CEP <====')
## Aqui é necessário os parametros para o inpuit das informaçoes pedidas
    print('CEP: {}'.format(address_data['cep']))
    print('CIDADE: {}'.format(address_data['cidade']))
    print('RUA: {}'.format(address_data['logradouro']))
    print('BAIRRO: {}'.format(address_data['bairro']))
else:
## Caso cpf invalido
    print('CEP invalido')

