print('olá, mundo');
#Alo mundo!
print ('Alô mundo!');

#metros/centimetros
metros= int( input('Digite o valor em metros para ser convertido em centimetros :'));
conversao= metros*100;
print('O resultado é', conversao,'cm');

#area do circulo
a= 3.14;
raio= int( input('Digite o valor do raio do circulo para conhecer sua area, com pi valendo 3.14 :'));
area= a*raio*raio;
print('A area do circulo é de', area,'m^2');

#area do quadrado e o dobro do seu valor
lado= int( input('Digite o valor do lado do quadrado para saber o dobro de sua area :'));
area= lado*lado;
final= area*2;
print('O dobro da area do quadrado de lado', lado, 'é', final);

#fahrenheit para celsius
F= int( input('Digite a temperatura em fahrenheit para ser convertida em graus Celsius :'));
C= ((F-32)/9)*5;
print('A temperatura em graus Celsius é de ',C);

#Celsius para fahrenheit
C= int( input('Digite a temperatura em Celsius para ser convertida em graus Fahrenheit :'));
F=((C*9/5)+32);
print('A temperatura em graus Fahrenheit é de ',F);
 
#'Peso ideal'
altura = float( input('Para saber seu peso ideal digite sua altura em cm :'));
peso = float((72.7*altura)-58);
print('Para a altura de', altura,'é recomendado o peso de ',peso,'Kg');