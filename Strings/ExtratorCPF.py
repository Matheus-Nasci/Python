endereco = "Rua Alfa Omega 72, apartamento 102, Barra Tijuca, Rio De Janeiro, RJ, 29310-201"
cadastro = "Andrey Rodrigues, (11)9218-2311, 00201230230"

import re # Regular Expression

# VALIDANDO CEP
# 5 dígitos + hífen (Opcional) + 3 Dígitos

# (?) PONTO DE INTERROGACAO PARA CARATER OPCIONAL
# QUANTIDADE DE VEZES DO CONJUNTO {5}
# ("[a-z]{5}[-]?[0-9]{3}")
padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")
busca = padrao.search(endereco) # Match

if busca:
    #GROUP PARA OBTER A INFO DESEJADA
    cep = busca.group()

print(cep)