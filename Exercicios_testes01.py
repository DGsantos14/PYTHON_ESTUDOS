def maior(x,y): #Aqui esta a definição do Maximo, essa função é uma função de x e y
    if x > y: # omparação do do x e y verificando se x é maior que y
        return x
    else: # Caso contrário, retornamos o valor y
        return y

x = int(input("Informe o primeiro Número:  ")) # Recebendo o valor das variáveis 
y = int(input("Informe o segundo Número:  ")) # Recebendo o valor das variáveis

print("O maior valor é: ", maior(x, y)) # imprimindo o resultado
