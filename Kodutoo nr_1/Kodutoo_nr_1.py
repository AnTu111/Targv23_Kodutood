from math import *

#ülesanne 1
name = str(input("pls tell me you name: "))
print("hello! , " + name)

#ülesanne 2
calculate = float(3+8/(4-2)*4)
print(calculate)

#ülesanne 2.1
r=int(3)
d=r*r
ruudupindala = d*d
ruuduumbermõõt = 4*d
π=3.14 
ringipindala = round(π*d)
ringiumbermoot = round(2*π*r)
print(d + ruudupindala + ruuduumbermõõt + ringipindala +ringiumbermoot) 
print(d)
print(ruudupindala)
print(ruuduumbermõõt)
print(ringipindala)
print(ringiumbermoot) 

#ülesanne 2.2
maaraadius = float(6378000) # või 6378 km
müntiraadius = float(0.02575) # või 27,75 mm
π = 3.14 
ümbermõõt = 2*π*maaraadius
print("длина окружности")
print(ümbermõõt/1000,"km")
print(round((ümbermõõt/müntiraadius)/1000),"km")

#ülesanne 3
text1=str("kill")
text2=str("koll")
text3=str("killadi")
print(text1 + "-" + text2+" "+text1 + "-" + text2+" "+text3+"-"+text2+" "+text1 + "-" + text2+" "+text1 + "-" + text2+" "+text3+"-"+text2+" "+
text1 + "-" + text2)

#ülesanne 4
number=(print("rong see sõitis tsuhh tsuhh tsuhh\npiilupart oli rongijuht.\nrattad tegid rat tat taa,\nrat tat taa ja tat tat taa.\naga seal rongi peal,\nkas sa tead, kes olid seal?"))




#ülesanne 5
a=float(input("sisetage ristküliku lähiskülgede pikkused a"))
b=float(input("ristküliku lähiskülgede pikkused b"))
pindala=float(2*(a+b))
ümbermõõdu=float(a*b)
print("pindala on", pindala)
print("ümbermõõt on ", ümbermõõdu)

ülesanne 6
kütusekulu arvutamine

kutus = (float(input("sisestage tangitud kütuse liitrid ")))
km = (float(input("sisestage läbitud km  ")))
kutusekulu = kutus/km*100
print(f"teie keskmine kutusekulu on {round(kutusekulu,2)}")

ülesanne 7
rulluisutajad

    rulluisutaja keskmine kiirus on 29,9km/h
    kui kaugele jõuab m minutiga

v = 29,9 #km/h
v = (100/3600)*29.9 #m/s
s = 60 * v # 60 sec * kiirus
print(f"rulluisuatjad jõuavad minutiga {round(s,0)} meetrid")


ülesanne 8
ajateisendus

    kasutaja sisestab aja minutites
    sinu valem leiab ja väljastab tunnid ja minutid
    näiteks: sisestus 72, vastus 1:12
t = int(input("sisestage aja minutites "))
t1 = t // 60
t2 =t % 60
print(t1,t2,sep =":")

