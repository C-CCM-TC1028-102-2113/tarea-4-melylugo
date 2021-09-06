

def main():
    #Escribe tu código debajo de esta línea
    
    num=int(input("Escribe un numero : "))
    acum=1

    while (acum**2)<=num:
        acum=acum+1
    print (acum)

    pass

if __name__=='__main__':
    main()
