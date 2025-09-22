# Crie um programa em Python que simule um sistema de login. 
# O programa deve permitir ao usuário três tentativas para acertar o nome de usuário e a senha corretos. 
# Caso o usuário erre as credenciais, o programa deve fornecer uma mensagem informando quantas tentativas restam. 
# Se o usuário acertar, uma mensagem de boas-vindas deve ser exibida, e o programa deve terminar imediatamente.
# Se todas as três tentativas falharem, o programa deve usar um loop for para exibir uma mensagem de "Acesso bloqueado" repetida três vezes.

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "1234"

for tentativas_restantes in range(3, 0, -1):
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
        print("Bem-vindo!")
        break
    else:
        if tentativas_restantes - 1 > 0:
            print(f"Credenciais incorretas. Restam {tentativas_restantes - 1} tentativa(s).")
else:
    for _ in range(3):
        print("Acesso bloqueado")