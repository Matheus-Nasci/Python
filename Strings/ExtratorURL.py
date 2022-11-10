import re
class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    # Sanitização da URL
    # url = url.replace(" ", "")
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    # VALIDANDO URL
    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vázia.")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)

        if not match:
            raise ValueError("A URL não é válida.")

    # SEPARA BASE E OS PARAMETROS
    def get_url_base(self):
        indice_interrogacao = self.url.find("?")
        url_base = self.url[:indice_interrogacao]
        return url_base

    # BUSCAR VALOR NOS PARAMETROS
    def get_url_parametros(self):
        indice_interrogacao = self.url.find("?")
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find("&", indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __eq__(self, other):
        return self.url == other.url

    #String
    def __str__(self):
        return f"URL: {self.url} \nBase: {self.get_url_base()} \nParâmetros: {self.get_url_parametros()} \ntamanho URL: {len(extrator_url)}"

# extrator_url = ExtratorURL("http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100")
url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
extrator_url = ExtratorURL(url)
extrator_url.valida_url()
print(extrator_url)