from getpass import getpass

username = input("Digite seu nome: ")

while len(username) < 5:
    print("Seu por favor digite o nome maior")
    username = input("Digite seu nome: ")

passwd = getpass("Digite sua senha: ")

while len(passwd) < 8:
    print("Seu por favor digite uma senha maior")
    passwd = getpass("Digite sua senha: ")

print(f"Seu usuário criado é {username} e senha {passwd}")