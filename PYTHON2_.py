#lambda fonksiyonları
 #ismi olmayan fonksiyonlar oluşturmamızı sağlar.
kareal=lambda x: x*x     # parametre: fonksiyon döndüreceği değer.
print(kareal(5))

kupal= lambda x:x^3
print(kupal)  # fonk oldu içine değer yazarız.

# 2 parametre alan fonksiyonlara bakalım.

toplam=lambda x,y: x+y
print(toplam(5,7))
geneltoplam = lambda *args:sum(args)
print(geneltoplam(4,5,6,2))

print((lambda x,y,z:x*y+z)) # fonksiyondur

print((lambda *args:sum(args)/len(args))(2,3,4,5,6)) # fonksiyon
# lambda tek satırda halletmemizi ve kullanıp atacaksak lambdayla yapmam mantıklı.ki boşuna yer kaplamasın. projede   tekrar tekrar kullanılacaksa lambda kullanılmaz

#parametre olarak fonk alan fonksiyonlarda kullanılır

liste=[("ali",20),("veli",19),("emel",30),("hakan",24)]
liste.sort()#değer geri döndürmez sıralama yapar
print(liste)  # isme göre sıraladı
# peki  biz bunu isimlere göre değil , yaşlara göre sıralamak istiyorsak?
#LAMBDA KULLANIRIZ.

liste.sort(key=lambda x : x[1])  # liste.sort içinde key ifadesi yanına fonk alır. biz de o fonksiyonu lambda ile oluştururuz.
print(liste)  #yaşlara göre sıralandı.
liste2=[{"ad":"ahmet","soyad":"caliskan","yas":20},{"ad":"mehmet","soyad":"veli","yas":25}]
liste2.sort(key=lambda x: ["soyad"])   # soyadlara göre kıyaslama yapacak.
print(liste2)
liste2.sort(key=lambda x: ["yas"])  # sözlükte yas keyine denk gelen valuelara göre sıralama yapacak.
print(liste2)


#özetle:
#tek kullanımlıklarda
# parametre olarak fonksiyon alan fonksiyonlarda
#LAMBDA KULLANMAK FAYDALI.


#MAP FONKSİYONU:  # paremetre alarak fonksiyon,liste gireriz.
# bir listedeki elemanların hepsine aynnı işlemi yapar.
# listedeki elemanların karelerinden oluşan yeni bir liste oluşturalım.
liste=[1,2,3,4]
def kareal(x):
    return x*x

liste2=[]
for i in liste:     # normalde bu şekilde yapardık
    liste2.append(kareal(i))

# aynı işlemi map ile yapalım:
liste3=list(map(kareal,liste))  # mapin object type ını liste cast ettik.
print(liste3)  #object tir.
# ama biz neye istiyorsak ona döndürebiliriz

liste=[1,2,3,6,7,9]
liste2=   list(map((lambda x: x*x),liste))  #tek satırda hallettik. MAP ve LAMBDA ile
print(liste2)

# yani mapte fonksiyonu lambda ile de gönderebiliriz. işimiz kolaylaşır
#
# liste3=list(map(lambda x:x^3),liste)
# print(liste3)

# bir fonksiyon ve 2 liste olsun:
liste1 =[1,3,4,7,8]
liste2=[3,5,9,0,1]

# sıralı indisleri toplamından yeni bir liste oluşturalım.


liste3=list(map(lambda x,y:x+y,liste1,liste2))
print(liste3)

#kaç liste gönderiyorsak o kadar parametre alacak


#ORNEK:

urunler=[["ayakkabı",150],["pantalon",120],["gomlek",100],["ceket",200]]
#hepsine %20 indirim uygulanmış haliyle yeni liste oluştur

def indirimyap(x):
    urun,fiyat=x[0],x[1]
    fiyat= fiyat*80/100
    return [urun,fiyat]

sonuc=list(map(indirimyap,urunler))
print(sonuc)

isimler=["AhMeT","aYşE","oNur","hÜseyiN"]
# HEPSİNİ BÜYÜK HARF YAPMAK İSTİYORUM.
isimler2= list(map(lambda x:x.upper(),isimler))
print(isimler2)

# dikkat upper yanında() var.
# normalde parametre olarak göndersiğim fonksiyoun yanında parantez yokken lower ve upper da var. Neden?
# çümkü çağırılan fonksiyon lambda ,upper değil. ama mesela 1 üstünde çağırılan fonksiyon direkt olarak indirim yap fonk olduğu için parantezsiz.



#FİLTER FONKSİYONU:

# listeyi belirli koşullara göre filtrememizi sağlar. parametre olarak fonksiyon ve liste alır.
#ANCAK BURADAKİ FONKSİYONUM PARAMETRE OLARAK TRUE VEYA FALSE GÖNDEREN FONKSİYONDUR.

# istediğmiz koşulu sağlayanlarla yeni liste oluşturur.

liste=[1,2,3,5,7,88,9,8,65,4,0]
#çift sayilari istiyorum.

ciftler=list(filter(lambda x:x%2==0,liste))
print(ciftler)
#iki basamaklıları istiyorum.

ikibasamak=list(filter(lambda x :x>9 and x <100,liste))
print(ikibasamak)

kelimeler=["ayna","ahmet","ana","kalem","defter","kazak","son"]

#sadece a ile başlayablar:

kelimeler2= list(filter(lambda x:x.startswith("a"),kelimeler))
print(kelimeler2)

#içinde a geçenler

kelimeler3=list(filter(lambda x: "a"in x,kelimeler))
print(kelimeler3)


palindromlar=list(filter(lambda kelime:kelime == kelime[::-1],kelimeler))  # baştan sona eşit mi sondan başa
print(palindromlar)

liste=[1,2,(1,2,3),True,"string","örnek",{1,2,4}]
# ben buradaki stringleri istiyorum.

stringler= list(filter(lambda x: isinstance(x,str),liste))# x nesnesi str classından mı
print(stringler)

# int leri arasaydım true false da gelir . 1 ve 0 dan

# sözlük kullanarak örnek yapalım.
liste=[{"ad":"ahmet","yas":20},{"ad":"banu","yas":22},{"ad":"can","yas":18},{"ad":"anıl","yas":28}]

ailebaslayanlar=list(filter(lambda x:x["ad"].startswith("a"),liste))
print(ailebaslayanlar)




#REDUCE FONKSİYOU: parametre olarak fonksiyon,liste alır.
#map ve filter fonksiyonlarından farkı:reduce fonk bize liste göndermez. 1 tane değer gönderir
from functools import reduce
#reduce fonk functools modülü içinde olduğundan import etmem lazım

liste=[2,4,6,9]
# sonuc1= reduce(lambda x,y:x+y,liste)
# print(sonuc1)
# sonuc2=reduce(lambda x,y:x*y,liste)
# print(sonuc2)

#listedeki sayılarımın ekokunu bulmak istiyorum. pythonda ebob fonk var ama ekok fonk yok .öncelikle ebob fonksiyonunu import edip ebob ile ekok arasındaki ilişkiden ekok için tanımlama oluşturuyorum.
from math import gcd # ebob fonksiyonu iport ettim.
liste=[2,4,6,9,10]# ebob(a,b)*ekok(a,b)=a*b   o zaman ekok(a,b)=a*b/ebob(a,b)

def ekok(x,y):
    return int((x*y)/gcd(x,y))
print(ekok(6,8))

ekok2=reduce(ekok,liste)
print(ekok2)


# taş kağıt maakas oynayan bir kod:
def tasmakas(x,y):
    kume={x,y}
    if x==y:
        return x
    if kume=={"taş","makas"}:
        return "taş"
    if kume=={"taş","kağıt"}:
        return "kağıt"
    if kume=={"kağıt","makas"}:
        return "makas"

liste=["taş","kağıt","taş","makas","kağıt","makas","taş"]
sonuc=reduce(tasmakas,liste
             )
print(sonuc)   # taş kazandı



#ZİP FONKSİYONU:    # FERMUAR GİBİ DİŞLER ARASI EŞLEŞME YAPTI.
# 2 tane listenin elemanlarını birbirleriyle eşleştirip bize geri döndürür. biz neye istersek ona cast ederiz.
liste1=[1,2,3,4]
liste2=["a","b","c","d"]
liste3=list(zip(liste1,liste2))  # iterator (map gibi) object derken kastımız iterator idi . cast edicez.
print(liste3)

# 2 den fazla listeyle de kulalnılabilir.
liste1=list("python")
liste2=[1,2,3,4]
liste3=["A","B","C"]
liste4= list(zip(liste1,liste2,liste3))  # minimum sayodaki eleman sayısı kadar eşleşme yaptı.
print(liste4)

# zip fonk parametre olarak iterable olan(for döngüsüyle kullanabildiğimiz her şeyi alabilir.



#LOCAL ,ENCLOSİNG,GLOBAL,BUİLT-İN VARİABLES


# değişkenler önce tanımlandırılır sonra yazdırılır. (yukardan aşağı okuyor)

def fonk():
    print(x)

x=5  # buraya x i tanımlayınca hata gitmiş olabilir ama sorun tamamen ortadan kalkmadı. 5 yazmaz. tanımlandıktan sonra çalışma ihtimali olduğu için hata ortadan kalkar

fonk()#x'i tanımladıktan sonra fonksiyonu çağırınca 5 yazdı . x i tanımlamadan önce fonksiyonu çağırsaydım tekrar x tanımlı değildir hatası alıdım.


#GLOBAL VE LOCAL

x="global x"  #global değişken. tanımlandığından itibaren programın her yerinden erişilebilir.(üstteki kısımlar hariç tabiki)

# local: fnk içinde tanımlanan ve sadece o döngü veya fonk. içinde geçerli olan değişkenlerdir.

def fonk():
    #y="local y"
    print(x) # üstteki global çalışır. çünkü erişilebilir.

fonk()
#print(y) y local olduğundan dışardan erişilmez.


#ENCLOSİNG

def outer():
    x="enclosing x"  # iç içe fonksiyonlar var ise: En içteki LOCAL olur. onun bir üstü ENCLOSİNG olur.onun bir üstü de GLOBAL olur.
    print(x)
    def inner():
       # x="local x"
        print(x)# üsttekini yorum satırı yaptığımızda print ifadesi önce kendi scope una bakacak ve x göremicek. ve bi üstteki enclosing x i yazacak.
    inner()
outer()
print(x)
#enclosing x
#local x
#global x


x="global x"
#
# def fonk():  # ben bu fonksiyon içerisinden global x i değiştirmek istiyorum. ne yapmalıyım?
#     global x # yeni bir x değeri değil,global olarak tanımlanmış x değerini kullanmak istiyorum demek.sonu. 5 gelir
#     # bu şekilde global değişken değerini 5 olarak değiştirdik.
#
#     x=5

# içiçe fonk varsa enclosing variable ı da benzer yöntemle kullanabilirim.

def outer(x):
    x="enclosing x"
    print(x)
    def inner():
        nonlocal  x  # local değil bir önceki basamakta kullanılan x değeri demek.
        x=5
    inner()
    print(x) # nonlocal var iken 5, yok iken bu da enclosing x yazdırır. nonlocal olmadığı sürece kendi seviyesindekiyle ilgilenir. nonlocal yokken içerdeki x farklı ve yerel bir değişken olarak tanımlanır. ve iç fonk da print olmadığı için o değer yazdırılmaz sadece çağrılır.nonlocal varken ise x in güncel değeri 5 olarak değiştirilir. ve iç fonk da print olmasa da öyle kabul edilip öyle yazdırılır.

outer()
# fonk()
# print(x)




# built-in variables:  pythonda kullanmamamız gereken özel isimler

#sum,max,len,lambda bunlar değişken ismi olarak kullanılmaz. _ vs ekleyerek kullan.


