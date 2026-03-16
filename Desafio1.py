# Adicione no dicionário com comandos Linux e suas descrições
comandos = {
    "ls": "lista arquivos e diretorios",
    "cd": "altera o diretorio atual",
    "pwd": "mostra o caminho do diretorio atual",
    "mkdir": "comando invalido"
}

# Lê o comando digitado pelo usuário
entrada = input().strip()

# Busca a descrição do comando ou informa se é inválido
descricao = comandos.get(entrada, "comando invalido")
print(descricao)