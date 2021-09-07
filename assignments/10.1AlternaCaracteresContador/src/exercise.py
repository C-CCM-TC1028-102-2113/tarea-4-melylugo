def main():
    #escribe tu código abajo de esta línea
    num=int(input())
    cont=0
    valor=1

    while num%2==0:
        print (str(valor)+"-#")
        cont=cont+1
        valor=valor+1
        print (str(valor)+"-%")
        cont=cont+1
        valor=valor+1
        if cont>=num:
            break
    while num%2!=0:
        print (str(valor)+"-#")
        cont=cont+1
        valor=valor+1
        if cont>=num:
            break
        print (str(valor)+"-%")
        cont=cont+1
        valor=valor+1


    pass

if __name__=='__main__':   
    main()
