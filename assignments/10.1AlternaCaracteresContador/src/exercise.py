def main():
    #escribe tu código abajo de esta línea

    valor=int(input())

    for valor in range (1,valor+1,2):
        print (str(valor)+"-#")
        valor=valor+1
        print (str(valor)+"-%")
    pass

if __name__=='__main__':   
    main()
