# Importar o módulo
import re
import json

# String em formato JSON
data_JSON = """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Jane Doe",
		"phone": "455-344-234",
		"email": "janedoe@email.com"
	}
}
"""

# Converter a string em JSON em um dicionário
data_convert_str = json.loads(data_JSON)

parametro = "name"

def buscar_valor():
    tamanho_parametro = len(parametro)
    indice_parametro = data_convert_str.find(parametro)
    indice_valor = indice_parametro + tamanho_parametro
    return indice_valor

# def get_parametros(self):
#    index_valor_parametro = data_convert_str.find(parametro)
#    index_valor = index_valor_parametro + len(parametro) + 2
#    return index_valor

seila = buscar_valor()
print(seila.find())
