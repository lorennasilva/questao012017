x=float(input("Digite o valor de x:"))
y=float(input("Digite o valor de y:"))
print(x,y)
soma=0;
cont=0;
soma1=0;
cont1=0;
if (x==0)and(y==0):
    print("nao existem pontos")
while (x!=0) and (y!=0):
    soma+=x
    cont+=1
    soma1+=y
    cont1+=1
    x=float(input("Digite o valor de x:"))
    y=float(input("Digite o valor de y:"))
    print(x,y)
media=soma/cont
media1=soma1/cont1
print("%.2f" %media, "%.2f" %media1)
