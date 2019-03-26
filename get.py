#!/usr/bin/python3
import requests

cep = input('Digite o cep: ')

url = 'http://viacep.com.br/ws/{cep}/json/'.format(cep)
#url = f'http://viacep.com.br/ws/{cep}/json/'
response = requests.get(url)
if response.status_code == 200:
	print(response.json())
