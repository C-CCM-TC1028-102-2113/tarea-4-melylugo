def main():
    #escribe tu código abajo de esta línea
    valor=int(input())
    cont=0
    while valor%2!=0:
        print("1"+"-#")
        for valor in range (1,valor,2):
            cont=cont+2
            valor=valor+1
            print (str(valor)+"-%")
            while cont>=valor:
                valor=valor+1
                print (str(valor)+"-#")
        break
    else:
        for valor in range (1,valor,2):
            print (str(valor)+"-#")
            valor=valor+1
            print (str(valor)+"-%")
    pass

if __name__=='__main__':   
    main()
