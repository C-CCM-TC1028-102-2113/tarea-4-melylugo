def main():
    #escribe tu código abajo de esta línea

    num=int(input())

    num=int(input())

    valor=num

    for valor in range (1,valor,2):
            print (str(valor)+"-#")
            valor=valor+1
            print (str(valor)+"-%")
    if num%2!=0:
        print (str(num)+"-#")


    pass

if __name__=='__main__':   
    main()
