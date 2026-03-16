# Adicione os comandos que presentão as ordem solicitadas 
comandos = {
    "listar arquivos": "ls",
    "criar nova pasta": "mkdir",
    "remover arquivo": "rm",
    "mostrar conteudo": "cat"
}

descricao = input().strip().lower()

comando_encontrado = "comando desconhecido"
for chave, comando in comandos.items():
    if chave in descricao:
        comando_encontrado = comando
        break  # Encontrou o comando, não precisa continuar

print(comando_encontrado)