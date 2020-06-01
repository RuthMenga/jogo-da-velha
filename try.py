import random
def imprimeCampo(campo):
    # print(campo, 'salve')
    for c in range(3):
        print(campo[c * 3 + 0], campo[c * 3 + 1], campo[c * 3 + 2])


def ganhou(simbolo, campo):
    if campo[0] == simbolo and campo[1] == simbolo and campo[2] == simbolo:
        return 1

    if campo[3] == simbolo and campo[4] == simbolo and campo[5] == simbolo:
        return 1

    if campo[6] == simbolo and campo[7] == simbolo and campo[8] == simbolo:
        return 1

    if campo[0] == simbolo and campo[3] == simbolo and campo[6] == simbolo:
        return 1

    if campo[1] == simbolo and campo[4] == simbolo and campo[7] == simbolo:
        return 1

    if campo[2] == simbolo and campo[5] == simbolo and campo[8] == simbolo:
        return 1

    if campo[0] == simbolo and campo[4] == simbolo and campo[8] == simbolo:
        return 1

    if campo[2] == simbolo and campo[4] == simbolo and campo[6] == simbolo:
        return 1


def velha(campo):
    if '_' not in campo:
        return 1


campo = [
    '_', '_', '_',
    '_', '_', '_',
    '_', '_', '_'
]

jogador = random.choice((0, 1))

if jogador == 1:
    sVC = 'X'
    sPC = 'O'
else:
    sPC = 'X'
    sVC = 'O'

print(f"Você é {sVC}")
print(f"O Pc é {sPC}")

while 1:
    if velha(campo):
        imprimeCampo(campo)
        print("VELHA")
        break
    if jogador:
        imprimeCampo(campo)

        while 1:
            vc = int(input())

            if campo[vc] == '_':
                break

        campo[vc] = sVC

        jogador = 0

        if ganhou(sVC, campo):
            imprimeCampo(campo)
            print("VC GANHOU")
            break

    else:
        imprimeCampo(campo)
        while 1:
            pc = random.randint(0, 8)

            if campo[pc] == '_':
                break

        campo[pc] = sPC

        jogador = 1

        if ganhou(sPC, campo):
            imprimeCampo(campo)
            print("PC GANHOU")
            break
