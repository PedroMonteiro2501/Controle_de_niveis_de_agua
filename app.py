from colorama import Fore, Style

nivel = [1, 2, 3, 4, 5]

print("nivel:")
for numero in nivel:
    print(numero)

nivel = int(input("Qual o nível da água?: "))    

if nivel == 1:
    print(Fore.RED + "Muito baixo (Crítico)!")
elif nivel == 2:
    print(Fore.YELLOW + "Baixo")
elif nivel == 3:
    print(Fore.GREEN + "Médio")
elif nivel == 4:
    print(Fore.CYAN + "Alto")
elif nivel == 5:
    print(Fore.BLUE + "Muito alto (Alerta)")

print(Style.RESET_ALL)