#o_vastus = 4*100-55
#k = 1
#print("Arvuta peast! ...4*100-55")
#while True:
#    vastus = int(input("Lahenda ülesanne ..."))
#    if vastus == o_vastus:
#        print("Õige vastus! Katsed oli ...", k)
#        break
#    else:
#        print("Viga! Sisesta Õige vastus on ...", o_vastus)
#    k += 1

#x = 0
#while True:
#    if x % 2 == 1:
#        print(x, end=" ")
#    x += 1
#    if x==30:
#        break

#for x in range(0,30,1):
#    if x % 2 == 1:
#        print(x, end=" ")


print("*** NUMBRIDEGA MÄNGUD ***")
print()
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
while 1:
    try:
        a = (abs(int(input("Sisestage täisarv => ")))) #dobavil 2 skobki
        break
    except ValueError:
         print("See ei ole täisarv")
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
if a==0:
    print("Nulliga pole mõtet midagi peale hakata")
else:
#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Määrake, kui palju paaris ja mitu paaritu numbrit on arvus")
    print()
    c=b=a #ubral ravno
    paaris =0 #ubral ravno
    paaritu = 0 #ubral ravno
    while b > 0: #izmenil dvoetochie eto ne js ili C# :)
        if b % 2==0: #dobavil ravno
            paaris += 1 #ubral probeli/TAB i + pomenjal mestami
        else:
            paaritu += 1 #ubral probeli/TAB i + pmenjal mestami
        b = b // 10 #ubral probel
    print("Paaris arvude kogus:",paaris) #dobavil zapjatuju
    print("Paaritu on:",paaritu) #dobavil zapjatuju
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0: #dobavil dvoetochie
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #ubral probel i pomenjal mestami +
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #ubral skobku
    print()
    if c % 2==0: #dobavil ravno
        print("с - paarisarv. Jagame 2-ga.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2==0: #dobavil ravno
                    c=c / 2 #ubral ravno
            else:
                    c=(3*c + 1) / 2 #ubral ravno
            print(round(c), end=" ") #dobavil kovichki
    print()
    print("Hüpotees on õige") #izmenil kovichki

