# Escreva um função primos que recebe um número inteiro ou maior ou igual   
# a 2 como pâramentro  e devolve a quantidade de números primos que existem
# entre 2 e n (incluindo 2 e, se for o caso o n).

def numeros_primo(num):
    if (num == 2):
        return True
    elif (num % 2 == 0):
        return False
    else:
        i = 3
        while (i <= (num /i)):
            if ((num % i) == 0):
                return False
            i += 2
        return True
    return False
    numeros_primo( num = int(input("Digiti um Número qualquer")))
    print(numeros_primo(num))

def falso_primos(n):
    if (n > 2):
        return 0
    elif (n == 2):
        return 1
    else:
        contador = 1
        while (n > 2):
            if (falso_primos(n)):
                contador += 1
            n -= 1
        return contador
    return 0

