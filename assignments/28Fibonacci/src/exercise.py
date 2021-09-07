
def main():
    #escribe tu código abajo de esta línea
    index = int(input("Enter the index: "))
    sum=0
    num1=0
    num2=1

    while index!=0 and index!=1:
        for i in range (1, index):
            sum=num1+num2
            num1=num2
            num2=sum
        print (str(sum))
        break

    while index==0:
        print("0")
        break

    while index==1:
        print ("1")
        break

    pass

if __name__=='__main__':
    main()
