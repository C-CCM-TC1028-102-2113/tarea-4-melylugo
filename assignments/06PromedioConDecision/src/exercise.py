def main():
    #escribe tu código abajo de esta línea
    cont=0
    sum=0
    
    n=float(input())
    while n>=0:
        sum=sum+n
        cont=cont+1
        n=float(input())
    prom=sum/cont
    print(prom)

    pass
if __name__=='__main__':
    main()
