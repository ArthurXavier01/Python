(NOTES AVERAGE)

note1 = float (input("Enter one note: "))
note2 = float (input("Enter another note: "))
note3 = float (input("Enter another note: "))
average = (note1 + note2 + note3) / 3
if average >= 5 :
 print ("Approved")
else:
 print ("Disapproved")

----------------------------------------------------------------
(PASSWORD RELEASED, DENIED)


password = int(input("Enter your password:"))
if password == 123456 :
 print ("Access released")
else :
 print ("Acess denied")

------------------------------------------------------------------
(Letters Value Comparation)

A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))
C = int(input("Enter the value of C:"))
if (A + B) < C :
 print ("A + B is less then C")
else :
 print ("A + B is equal to or bigger than C")

-----------------------------------------------------------------
(SALARY INCREASE)

salary = float (input("Enter the salary:"))
if salary <= 300 :
 increase1 = salary * 1.35
 print("Your new salary is: ", increase1)
else :
 increase2 = salary * 1.15
 print("Your new salary is: ", increase2)
  
 ------------------------------------------------------------------
(BIGGER NUMBER)

A = int(input("Enter the value of A:"))
B = int(input("Enter the value of B:"))
C = int(input("Enter the value of C:"))
if A == B == C :
 print ("Equal numbers")
elif A > B and A > C :
 print ("A is bigger")
elif B > A and B > C :
 print("B is bigger")
else :
 print("C is bigger")
--------------------------------------------------------------------
(Brazil Localization States)

state = input("Enter the state(PB, PE, RJ, SP): ").lower()
if state == "pb" or state == "pe" :
 print ("Belongs to the Northeast")
elif state == "rj" or state == "sp" :
 print ("Belongs to the Southeast")
else :
 print ("North or Center")

-----------------------------------------------------------------------

# matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

#     for lista in range(3):
#         for numeros in range(3):
#           matriz[lista][numeros] = int(input("Digite o número: "))
#           if(lista == numero):
#             matriz[lista][numero] =  matriz[lista][numero] *5
    


# //


# cidades = ([0,0], [0,0], [0,0])

# for cidade in range(3):
#     cidadeNome = input("Digite o nome da cidade: ")
#     cidades[cidade][0] = int(input("Digite o valor da pitu desta cidade: "))
#     cidades[cidade][1] = int(input("Digite o valor da 51 desta cidade: "))
# print(cidades)

// 



# precos = [[0,0], [0,0], [0,0]]
# cidadeNome = ["", "", ""]
# for cidade in range(3):
#     cidadeNome[cidade] = input("Digite o nome da cidade: ")
#     for valor in range(2): 
#         precos[cidade][valor] = int(input("Digite o valor das Bebidas respectivamente Pitu e 51 : "))
# print(cidadeNome)
# print(precos)

//


# precos = [[0,0], [0,0], [0,0]]
# cidadeNome = ["", "", ""]
# for cidade in range(3):
#      cidadeNome[cidade] = input("Digite o nome da cidade: ")
#      for valor in range(2): 
#          precos[cidade][valor] = int(input("Digite o valor das Bebidas respectivamente Pitu e 51 : "))
# print(cidadeNome)
# print(precos)
# print(" o valor da pitu em", cidadeNome[0], "é", precos[0][0])
# print(" o valor da pitu em", cidadeNome[1], "é", precos[1][0])
# print(" o valor da pitu em", cidadeNome[2], "é", precos[2][0])
# print(" o valor da 51 em", cidadeNome[0], "é", precos[0][1])
# print(" o valor da 51 em", cidadeNome[1], "é", precos[1][1])
# print(" o valor da 51 em", cidadeNome[2], "é", precos[2][1])

//

precos = [[0,0], [0,0], [0,0]]
cidadeNome = ["", "", ""]
for cidade in range(3):
     cidadeNome[cidade] = input("Digite o nome da cidade: ")
     for valor in range(2): 
         precos[cidade][valor] = int(input("Digite o valor das Bebidas respectivamente Pitu e 51 : "))
bebida = input("Voce deseja saber o valor de qual bebida: \n 1. Pitu \n 2. 51")
local = input("Qual cidade: \n 1.", cidadeNome[0], "\n 2.", cidadeNome[1],"\n 3." cidadeNome[2])
if bebida == 1 and local == 1:
    print("Valor da pitu: ", precos[0][0])
elif bebida == 2 and local == 1:
    print("Valor da 51: ", precos[0][1])
elif bebida == 1 and local == 2:
    print("Valor da pitu: ", precos[1][0])
elif bebida == 2 and local == 2:
    print("Valor da 51: ", precos[1][1])
elif bebida == 1 and local == 3:
    print("Valor da pitu: ", precos[2][0])
elif bebida == 2 and local == 3:
    print("Valor da 51: ", precos[2][1])


