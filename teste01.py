"""
print("Hello World!");


print("Olá mundo python!");

name = input("Digite seu nome: ");
age = input("Digite sua idade aqui pfvr: ");

print("Olá " + name + "! Você tem " , age , " anos de idade.");


integer_number = int(input("write an integer number: "));
float_number = float(input("write a float number: "));



print("The integer number is: " , integer_number);
print("The float number is: " , float_number , );

    

this_is = type(input("Digite um numero: "));

print("O tipo de dado é: " , this_is);




numb_01 = float(input("Digite um numero: "));
numb_02 = float(input("Digite outro numero: "));

result =[numb_01 + numb_02, numb_01 / numb_02, numb_01 * numb_02, numb_01 - numb_02]

print("A soma dos numeros é:" , (numb_01 + numb_02), "a divisão é: " , (numb_01 / numb_02), "a multiplicação é: " , (numb_01 * numb_02), "e a subtração é: " , (numb_01 - numb_02));

print("A soma dos numeros é:" , result[0], "a divisão é: " , result[1], "a multiplicação é: " , result[2], "e a subtração é: " , result[3]);



lista_frutas = ["banana", "maçã", "laranja", "uva", "abacaxi"];
print("A lista de frutas é: " , lista_frutas);


lista_de_compras = ["arroz", "feijão", "macarrão", "carne", "frango", "leite", "pão", "queijo", "manteiga", "ovo"];
print(f'A lista de compras é:   {lista_de_compras[0]}, {lista_de_compras[7:9]}');



lista_de_carros = ["Fusca", "Gol", "Civic", "Corolla", "Onix", "HB20", "Fiesta", "Palio", "Uno", "Sandero"];
lista_de_carros.insert(0, "Chevete");
lista_de_carros.remove("Onix");
lista_de_carros[2]= "Civiczão";
lista_de_carros
print(f'A lista de carros é: {lista_de_carros}');



lista_linguagens = ["Python", "Java", "C#", "C++", "JavaScript", "PHP", "Ruby", "Swift", "Kotlin", "Go"];

for i in range(lista_linguagens.__len__()):
    print(f'A linguagem de programação é: {lista_linguagens[i]}');



for i in range(1,10):
    print(f'Número: {i}');


for i in range(0,11,5):
    print(f'Número: {i}');


frutas = ["banana", "maçã", "laranja"]; 

for i in frutas:
    for j in frutas:
        print(f'Fruta: {i} e Fruta: {j}');



frutas = ["banana", "maçã", "laranja"];
vegetais = ["cenoura", "batata", "alface"];

for i in frutas:
    for j in vegetais:
        print(f'Fruta: {i} e Vegetal: {j}');


contador = 0 

while contador < 10:
    contador += 1
    print(f'Contador: {contador}')
else: print("FINALIZOU FI VEZES")


for i in range(1,10):
    if i == 5:
        print(f'parei familia parei.......');
        break
    print(f'Número: {i}');

for i in range(1,10):
    if i == 5:
        continue
    print(f'Número: {i}');

"""

lista_montar_pc = ["placa mãe", "processador", "memória ram", "fonte", "ssd", "hd", "gabinete", "fonte"];
contador = 0

for peça in lista_montar_pc:
    if peça == "fonte":
        contador += 1

print(f'A quantidade de peças "fonte" na lista é: {contador}');


"""   --------------- APENAS TESTE PRA RELEMBRAR UM POUCO DE PYTHON -----------------   """