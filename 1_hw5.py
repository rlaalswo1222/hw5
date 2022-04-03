##김민재2021041070
def base2(num):
    if num>0 :
        base2(num//2)
        print(num%2,end=" ")

def base8(num):
    if num>0:
        base8(num//8)
        print(num%8,end=" ")
    
def base16(num):
    if num>0:
        base16(num//16)
        renum=num%16
        if(renum<10):
            print(renum,end=" ")
        else:
            if renum==10: print('A',end=" ")
            elif renum==11: print('B',end=" ")
            elif renum==12: print('C',end=" ")
            elif renum==13: print('D',end=" ")
            elif renum==14: print('E',end=" ")
            elif renum==15: print('F',end=" ")

a = int(input("10진수 입력 --> "))
base2(a)
print("\n")
base8(a)
print("\n")
base16(a)
