import os
os.system('clear') or None

x = int(input("Digite a largura da peça: \n"))
y = int(input("Digite o comprimento da peça: \n"))

if (x > 0) and (x < 40):
    espacadorX = 1
if (x > 40) and (x < 80):
    espacadorX = 2
if (x > 80) and (x < 120):
    espacadorX = 3

if (y > 0) and (y < 40):
    espacadorY = 1
if (y > 40) and (y < 80):
    espacadorY = 2 
if (y > 80) and (y < 120):
    espacadorY = 3

espacador = espacadorY + espacadorX
m2 =  float(input("Digite a M²: \n"))

m2real = (x / 100) * (y/ 100)

total = (m2 / m2real) * espacador  
print("O total de espaçadores é: {:.0f} " .format(total))
print("\n")








