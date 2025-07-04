def criar_pessoa(nome, idade):
    return {'nome': nome, 'idade': idade}

grupo = []
grupo.append(criar_pessoa('Frederico', 35))
grupo.append(criar_pessoa('Ana', 23))
grupo.append(criar_pessoa('Paulo', 42))

print(grupo)

print(grupo[0]['nome'])
print(grupo[2]['idade'])
print(grupo[1]['nome'])
print(grupo[1]['idade'])

for pessoa in grupo:
    print(f"O nome da pessoa é {pessoa['nome']}")
    print(f"A idade é {pessoa['idade']}")