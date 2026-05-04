usuario_correto = "arthur123"
senha_correta = "senha123"

usuario = input("digite o usuario:")
senha = input("digite a senha:")

if usuario == usuario_correto and senha == senha_correta:
    print("Login efetuado com sucesso")
else:
    print("Erro de login")
