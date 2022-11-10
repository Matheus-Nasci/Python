
# String em formato JSON
data_JSON = """
{
	"size": "Medium",
	"price": 15.67,
	"toppings": ["Mushrooms", "Extra Cheese", "Pepperoni", "Basil"],
	"client": {
		"name": "Andrey Rodrigues",
		"phone": "11 92344-2234",
		"email": "andrey@email.com",
	}
}
"""


class ExtratorDado:

    def __init__(self, parametro):
        self.parametro = parametro

    def get_parametro(self):
        tamanho_parametro = len(self.parametro)
        indice_parametro = data_JSON.find(self.parametro) + tamanho_parametro + 4
        return indice_parametro

    def get_valor(self):
        indice_virgula = data_JSON.find(",", self.get_parametro()) - 1
        return data_JSON[self.get_parametro() : indice_virgula]


# TESTE
extrairNome = ExtratorDado("name")
extrairTelefone = ExtratorDado("phone")
extrairEmail = ExtratorDado("email")

print(f" Nome: {extrairNome.get_valor()}")
print(f" Telefone: {extrairTelefone.get_valor()}")
print(f" E-mail: {extrairEmail.get_valor()}")
