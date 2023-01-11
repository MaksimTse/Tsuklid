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
        a = (abs(int(input("Sisestage täisarv => ")))) #lisatud 2 sulgu
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
    c=b=a #eemaldatud võrdub
    paaris =0 #eemaldatud võrdub
    paaritu = 0 #eemaldatud võrdub
    while b > 0: #muutis käärsoole
        if b % 2==0: #lisatud võrdsed
            paaris += 1 #eemaldatud tühikud / TAB ja vahetatud + kohtades
        else:
            paaritu += 1 #eemaldatud tühikud / TAB ja vahetatud + kohtades
        b = b // 10 #eemaldas tühik
    print("Paaris arvude kogus:",paaris) #lisas koma
    print("Paaritu on:",paaritu) #lisas koma
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("*Tagurda* sisestatud number")
    print()
    b=0
    while a > 0: #lisas :
        number = a % 10
        a = a // 10
        b = b * 10
        b += number #eemaldas ruumi ja vahetatud + kohtades
    print("*Ümberpööratud* number", b)
    print()
#''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    print("Syracuse hüpoteesi testimine") #eemaldatud sulg
    print()
    if c % 2==0: #lisatud võrdsed
        print("с - paarisarv. Jagame 2-ga.")
    else:
        print("с - paaritu number. Korrutage 3-ga, lisage 1 ja jagage 2-ga.")
    while c != 1:
            if c % 2==0: #lisatud võrdsed
                    c=c / 2 #eemaldatud võrdub
            else:
                    c=(3*c + 1) / 2 #eemaldatud võrdub
            print(round(c), end=" ") #lisatud juttumärgid ja lisage ümardamine
    print()
    print("Hüpotees on õige") #juttumärgid vahetatud
