url = "http://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
tamanho_url = len(url)
print(f"URL: {url} Total Caracter: {tamanho_url}")

#Sanitização da URL
#url = url.replace(" ", "")
url.strip()

# VALIDANDO URL
if url == "":
    raise ValueError("A URL está vázia.")

# SEPARA BASE E OS PARAMETROS
indice_interrogacao = url.find("?")
url_base = url[:indice_interrogacao]
print(f"URL BASE: {url_base}")

# BUSCAR VALOR NOS PARAMETROS
url_parametro = url[indice_interrogacao + 1:]
print(f"PARAMETROS URL: {url_parametro}")

parametro_busca = "moedaDestino"
indice_parametro = url_parametro.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametro.find("&", indice_valor)

if indice_e_comercial == -1:
    valor = url_parametro[indice_valor:]
else:
    valor = url_parametro[indice_valor:indice_e_comercial]

print(f"VALOR: {valor}")
