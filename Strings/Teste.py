json = "{min_position: 8,has_more_items: false,items_html: Bike,new_latent_count: 1,data: {length: 30,text: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

# PEGANDO TEXTO JSON
index_texto = json.find("text:")
tamanho_json = len(json)
texto = json[index_texto + 6: tamanho_json]
# print(texto)

index = len("items_html:")
posicao_item = json.find("items_html")
item = json[posicao_item + index: json.find(",new")]
print(item)
