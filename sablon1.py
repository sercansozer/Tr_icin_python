# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#########################(istikrarla programlamaya başla)#################33



###############################################################################
#######################  20.01.2020 TARİHLİ ÇALIŞMALAR #######################
###############################################################################

'''

######  if kullanımı  #########################################################
if name == 'Mary':
    print('Hello Mary')
if password == 'swordfish':
    print('Access granted.')
else:
    print('Wrong password.')

###############################################################################
'''


'''
########################### matematiksel operatörler   ########################




###############################################################################
#######################  DİKKAT EDİLMESİ GEREKEN NOTLAR #######################
###############################################################################




**   Exponent 2 ** 3 ------>8  (**,ifadesi üslü sayı anlamında kullanılır.)

%    Modulus/remainder 22 % 8------> 6 (%, ifadesi bölümünden kalan anlamına gelmektedir.

//   Integer division/floored quotient 22 // 8------> 2 (// ifadesi bölüm ifadesi kaçtırı bulur. )

/    Division 22 / 8 ------->2.75  ( / , ifadesi bölme işlemidir.)

*    Multiplication 3 * 5 --------->15 (*, ifadesi 3 ile 5 in çarpımıdır.)

-    Subtraction 5 - 2------> 3 (- ,ifadesi 5 ve 2 nin çıkarılması anlamına gelir.)

+    Addition 2 + 2---------> 4  (+,ifadesi toplama işlemi anlamına gelir.)

###############################################################################

'''
'''
###############################################################################
#######################  DİKKAT EDİLMESİ GEREKEN NOTLAR #######################
###############################################################################

Data                          type Examples
Integers                     -2, -1, 0, 1, 2, 3, 4, 5
Floating-point numbers       -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25
Strings                      'a', 'aa', 'aaa', 'Hello!', '11 cats'

'''
###############################################################################
#######################  ÖRNEKLERLE ÖĞRENMEYE DEVAM  ##########################
###############################################################################

tip=type('sercan sözer')
print( " ' sercan sözer' ifadesi tipi:",tip,"tipidir")
tip1=type(5)
print( " 5 ifadesi tipi:",tip1,"tipidir")
tip2=type(5.0)
print( " 5.0 ifadesi tipi:",tip2,"tipidir") 
print('alice'*5+'   '+'Buradaki olay alice ifadesini int bir ifadeyle çarparak o çarpılan sayı kadar tekrar ettirebiliriz ') 


"""
eğer int ile bir sayı yazılır ve bu sayı float değerde ise .0  kısmı alınmaz.
eğer string değer içerisine bir sayı değeri yazılırsa bu sayı değeri strin ifadeye dönüştürülür.
"""
#### örneklerle öğrenmeye devam ediyoruz.

str_deger=str(12)
int_deger=int(12.5)
float_deger=float(10)
print(int_deger,str_deger,float_deger,'str_deger değişkeninin sınıfı=',type(str_deger))

"""
tamam bunlar arasındaki ilişkiyide çözdük adım adım gidiyoruz zafereeeeee
seninle çok işim var daha bu sayfayı yazabildiğim kadar kod yazıp dert tasamıda bu .py uzantılı python dosyasına kaydedeceğim
 bundan sonra bu dosya benim günlüğümdür
"""

# Boolean veri tipi nedir ?7
"""


boolean veri tipinde sadece 2 tane değer vardır.
True and False;
sadece bu iki değeri alabilir boolean veri tipi alacak değişken sadece bu iki değiri alabilir.

"""

import time
girdi=str(input("evet mi hayrı mı sorusunun cevabını arıyorum.'Evet' mi 'Hayır' mı ? ="))


if girdi=='Evet':
    giris=True
    
    
elif girdi=='Hayır':
     giris=False
    
else:
    print("girdiğin değerin bir anlamı yok")
    
    
if giris ==True:
    print("bakayım doğrumu")
    time.sleep(5)
    print( "gerçekten evet çıktı bizde ikna olduk ")

elif giris==False:
        print("bakayım yanlışmı")
        time.sleep(5)
        print('gerçekten hayrı çıktı bizde ikna olduk :)')
else:
         print("giris değeri çok alakasız birşey çıktı şakınız")
    
    






















'Alice'+'BoB' # ifadesi iki string değeri birleştirir.
# fakat aradaki değer e ' ' eklemesi yapılırsa bışluk ta atılmış olur

calısır='Alice'+' '+'Bob'
print(calısır)

#fakat string ile int float vs değerler toplanamaz 
#   Eror='Alice'+5  // can only concatenate str (not "int") to str hatası verir
###############################################################################
#######################  DİKKAT EDİLMESİ GEREKEN NOTLAR #######################
###############################################################################


##### karambole bir oyun kodlaması yazayım dedim yaratıcı olmakta fayda var ##########


import time

print("Sisteme giriş yapıyorsunuz hazırlanın:")
print("F5 girişi tespit edildi.Şuan sen yandın.")
i=0
sayıcı=0
for i in range (11):
    print("yükleniyor %",sayıcı)
    
    sayıcı=sayıcı+1
    time.sleep(0.1)
    if i==9:
        print("yükleme tamamlansın mı? 'yes' / 'no' cevabı olarak yaz ")
        cevap=str(input("cevabını şimdi verebilirsin seni dinliyorum:"))
        if cevap=='yes':
            
            print("bir sonraki aşamaya geçmeyi hak kazandın.iyi insana benziyordun")
            time.sleep(1)
            i=10
        else:
            i=11
if  i == 10:
    print("Yükleme Tamamlandı.")
    print("                                         ")
    
    time.sleep(1)
    play=[
            " #######################################             "+
          "        ###########################################           "+
          "      #######_^^^^^^^^_       _^^^^^^^^_#############          "+
          "      #######_________#######__________##############           "+
          "     #################################################             "+
          "     #################################################             "+
           "    ###############################################             "+
          "      ###############(             )###############             "+
          "        #########################################               "+
          "           ####################################                 " + 
          "             ###############################                    "
          
          ]
    
    print("sen benimle uğraşmak istemezsin şimdi sana gerçek yüzümü göstericem")
    time.sleep(1)
    print("hazırmısın")
    
    oylama=input("hazırsan 'Evet' için 1 e bas .Hazır değilsen çıkmak için 0 a bas=")
    oylama=str(oylama)
    if oylama =='1':
        print(play)
        print("                         ")
        print ("Büyüyünce daha korkutucu olacağım şimdilik böyle idare et :DDD")
    elif oylama =='0':
        print ("Doğru kararı verdin uslu çocuk ol sütünü iç yat ")
    else:
        print ("sana iki seçeneketen başka birşey sunmadım ' " +oylama+ " ' ifadesi seni kurtaramaz hahahaha")
        
else: 
    print("Yükleme Tamamlanamadı başarız oldun. tekrar dene pes etme!!!")
    



###############################################################################
#######################  DİKKAT EDİLMESİ GEREKEN NOTLAR #######################
###############################################################################
"""
Bu len komutu sayı saydırmaya yarıyor.
bunun kıymetini bilmek lazım

"""
dizi=['sercan1','sercan2','sercan3']
a=len(dizi)
"""
yukarıdaki görülen dizin için len komutu uygulanırsa 
bu dizin içerisinde kaç tane eleman var bu sayı alınır.

"""

ismim='sercan'
b=len(ismim)
"""
ismim değişkeni içerisinde bulunan strin ifadenin kaç harften oluştuğunu sayar.

"""



###############################################################################
#######################  21.0.1.2020 TARİHLİ ÇALIŞMALAR #######################
###############################################################################


"""
Bugün ki çalışmamız karşılaştırma operatörleridir.

Operator                   Meaning

==                         Equal to 'Eşittir '
!=                         Not equal to 'Eşit değildir'
<                          Less than 'küçüktür'
>                          Greater than 'büyüktür'
<=                         Less than or equal to 'küçük eşittir'
>=                         Greater than or equal to 'büyük eşittir'



"""



# not True ifadesinin çıktısı False olarak verilir.
print('not True ifadesi False ifadesine eşittir:(input:not True) -->output:',not True)


# 'Hello'== 'Hello' ifadesi True değeri verir çünkü bir sorgudur 
'Hello'=='Hello'
'hello'=='Hello'

#bu ifade eşittir True
print("'dog' ifadesi ile 'cat' ifadesi birbirine benziyormu ",'dog'!='cat',)

print('Hello'=='Hello')




#bunu şu şekildede kullana biliriz

                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################

import time

a=input("if you say hello to me ,I say this True and False:")
a=str(a)
b='Hello'

time.sleep(1)

if a==b:
    print ("hello Dear Sercan,you put on to your head, you will do this software")
else:
    print("you don't say hello to me ,ı broken to you")
    

                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################

####düzeltilecek çalışma ####
import time

gırıs=type(int)
gırıs=int(input("bir sayı gir bakalım ve bu sayıyı bul="))
i='basadön'
while type(gırıs)==int:
         
    if i=='basadön':
    
             if gırıs <50:
                  print ("girdiğin değer küçük bulamadın.")
                  i='basadön'
             elif gırıs>50:
                  print("benim bulduğum değerden fazlasını buldun")
                  i='basadön'
             elif gırıs==50:
                  print("tamam benim tahminimi buldun.")
                  i='çıkış yap'
                  
    
    else:
        print("çıkış yapılıyor")
        
time.sleep(1)
print("Oyun sona erdi.")
 

                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################

(4 < 5) and (5 < 6)
True
(4 < 5) and (9 < 6)
False
(1 == 2) or (2 == 2)

print((1==2)or(2==2))
#output:True


print(2 + 2 == 4 and not 2 + 2 == 5 and 2 * 2 == 2 + 2)
      
      
      
  
                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################    
parola=1234

kullanıcı_adı=str(input('kullanıcı adı giriniz:'))
if kullanıcı_adı=='Sercan19035':
    print("kullanıcı adı doğru onaylandı")
    parola=int(input("parolayı giriniz:"))
    if parola==1234:
        print("parola doğru")
    else:
        print("parola yanlış")
else:
    print("kullanıcı adı yanlış")
        
    
    

                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################
      
      
while True:
          print('lütfen isminizi giriniz=')
          name = input()
          if name == 'sercan':
              break
print('Thank you!')
      
      

"""

continue ifadesi döngü başlangıcından devam et demektir.
while x:
    ...............
    ...............
    continue         kodlama burada döngü başına döner
    
"""



                #######################################################
                ################      while döngüsü      ##############
                ################     continue ifadesi    ##############
                #######################################################
      
        """
        bu örnekte while değerine true değeri vererek sonsuz döngü oluşturduk.
        döngüye girdikten sonra print komutu ile ilk başta karşımıza çıkan ifade 
        Who are you?
        bu ifadeden sonra name değişkeni içerisine input () komutu ile klavyeden ifade çekiyoruyuz 
        eğer isim Joe değilse durmadan isim soracak olacak şekilde bir döngü oluşturuyoruz.
        continue komutu burda bu işe yarıyor .
        name !='Joe'   demek name değişkeni içerisine yazılı olan değer eğer Joe değeri değilse 
        burada döngüyü başa çekiyoruz demektir.
        eğer isim Joe ise döngüden çıkarır.
        continue satırı sonrasına geçiş yapar.
        password sonrasında eğer doğru bilinmiş ise break komutu kullanılarak.
        while içerisinden çıkış yapılır.
        eğer password yanlış olasydı bu sefer döngüye yeniden dönüyoruz.
        """
    
    

                #######################################################
                #######################  ÖRNEK  #######################
                #######################################################  
                
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        break
print('Access granted.')
      


                #######################################################
                ######  for Loops and the range() Function ############
                #######################################################
                ###### for döngüsü ve range fonksiyonu     ############
                #######################################################
    
    
#######################################################
###############          ÖRNEK      ###################
####################################################### 
                
              #  For ile yapılan örnek 
print('My name is')
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

               # While ile yapılan örnek

print('My name is')
i = 0
while i < 5:
        print('Jimmy Five Times (' + str(i) + ')')
        i = i + 1



total = 0
for num in range(101):
         total = total + num
         print(total)




#######################################################
######       range () komutu kullanımı     ############
#######################################################
#######################################################


"""

eğer iki değer yazarsak bu değerler arasında (a,b)
a  dahil a dan b ye 1 er 1 er say 

5 sayısından -1 e kadar -1 azalarak ilerle demek 
5 sayısından 50 sayısına kadar 5 er 5 er arttır.

"""


for i in range(12, 16):
    print(i)


for i in range(5,50 , 5):
    print(i)



#######################################################
######       random modülü                 ############
#######################################################
#######################################################
"""
import random  ile random kütüphanesi çağırıldı.


tekli olarak tahmini bir şekilde kullanılada bilir.


for döngüsünde range komutu ile i=0 da iken 5 e kadar saydırma işlemi yapıldı loop başlatıldı 
her loop döngüsünde 1 den 10 a kadar olan sayılar  arasında bu sayılarda dahil olacak şekilde 
random integer değer tahminleri random kütüphanesinde randint komutu kullanarak elde edildi.



"""


import random

print(random.randint(10,30))


for i in range(5):
    print(random.randint(1, 10))



#######################################################
#########    sys.exit() kullanarak          ###########
#########  bir programı erken sonlandırmak  ###########
#######################################################
#######################################################
    
    
    
#######################################################
###############          ÖRNEK      ###################
####################################################### 
    
import sys
while True:
    print('Type exist to exit.')
    response=input()
    if response =='exit':
        sys.exit()
    print('You type'+response+'.')





#######################################################
#########  ÖNEMLİ BİR KONU FONKSİYONLAR     ###########
#######################################################
#######################################################
"""
def fonksiyonu kullanımı:
    
def fonksiyon(icerik)

şeklinde bir formatı vardır.

def fonksiyon(x):          |bu fonksiyonda bir formül var ve bu formül dışarıdan çağırılacak sonra 
    y=a* (x**2) +b*x       |bir değer bu formül içerisine atılacak foksiyon işlemlerini yaptıktan 
                           |sonra fonksiyon geri cevap verir.
b=fonksiyon(34)            |
print(b)
    
"""            
def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')


a=hello()
print(a)



def isim(name):
    print('İsmini fonksiyona aldım isminiz:  '+name)
    
print(isim('Sercan'))





#######################################################
###############          ÖRNEK      ###################
####################################################### 

"""
random sayı ürettirildi.
def fonksiyonu olarak getAnswer olarak fonksiyon tanımlandı.
fonksiyonu çağırmak için getAnswer() çağırmasını kullanacağız.
 fonksiyon oluşturuldu.
 
 -r sayısını random olarak üretiyoruz. (1,9) arasında değişkenlik gösteren bir sayıdır.
 getAnswer() fonksiyonu içerisine r değişkeni içerisindeki değer katılarak 
 getAnswer() nasıl cevap vereceği öğreniliyor
 çıkan değer 
 fortune=getAnswer(r)  ifadesi ile alınan cevap fortune değişkeni içerisine atılıyor.
 ve print (fortune)
ifadesiyle bastırılıyor.

"""



#######################################################
###############          ÖRNEK      ###################
####################################################### 
import random
def getAnswer(answerNumber):
         if answerNumber == 1:
             return 'It is certain'
         elif answerNumber == 2:
             return 'It is decidedly so'
         elif answerNumber == 3:
             return 'Yes'
         elif answerNumber == 4:
             return 'Reply hazy try again'
         elif answerNumber == 5:
             return 'Ask again later'
         elif answerNumber == 6:
             return 'Concentrate and ask again'
         elif answerNumber == 7:
             return 'My reply is no'
         elif answerNumber == 8:
             return 'Outlook not so good'
         elif answerNumber == 9:
             return 'Very doubtful'
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)








#######################################################
#########    Keyword Arguments and print()  ###########
#########   anahtarkelimeler ve print()     ###########
#######################################################
#######################################################
########       print() fonksiyonu kullanımı   #########

#aynı satıra ekleme yapma 
print('Hello', end='')
print('World',end='')
print('daha bitmedi bu satır işlem hala devam ediyor ki :)')

"""
eğer print içerisine end='' ifadesi konulursa
bu şu anlama gelir basma işlemi daha bitmedi
ekleme yapılacak bir  daha sonra gelen print 
işelemi içerisindeki değer ile içerinde bbirleştirme yapar .
"""


#print fonksiyonu içerisindeki değerler arasına ekleme yapmak
print(sep=',') #bu fonksiyon içerisindeki parametre bu işe yarar.
print('cats','dogs','monkey','rabbit',sep=',*(^_^)*,')


#######################################################
###############  Local ve Global scope ################
####################################################### 

"""
Local Variables Cannot Be Used in the Global Scope
yerel değişkenler global alanda kullanılamaz.

spam() fonksiyonundan eggs değeri çekilemedi
"""
#######################################################
###############          ÖRNEK      ###################
####################################################### 
def spam():
    eggs = 31337
spam()
print(eggs)


"""
Local Scopes Cannot Use Variables in Other Local Scopes
yerel alan diğer yerel alanlar içindeki değişkenleri kullanamaz.
"""
#######################################################
###############          ÖRNEK      ###################
####################################################### 
def spam():
    eggs = 99
    bacon()
    print(eggs)
    
def bacon():
        ham = 101
        eggs = 0
spam()


"""
Local and Global Variables with the Same Name
aynı isimli local ve global değişkenler
"""
#######################################################
###############          ÖRNEK      ###################
####################################################### 
def spam():
        eggs = 'spam local'
        print(eggs) # prints 'spam local'
def bacon():
        eggs = 'bacon local'
        print(eggs) # prints 'bacon local'
        spam()
        print(eggs) # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) 
# bacon local
# spam local
# bacon local
# global
    
    
#######################################################
###############   Global beyan      ###################
#######################################################     
    
    
def spam():
    global eggs
    eggs='spam'

eggs='global'
spam()
print(eggs)







#######################################################
###############          ÖRNEK      ###################
####################################################### 

def spam():
    global eggs
    eggs = 'spam' # this is the global
def bacon():
    eggs = 'bacon' # this is a local
def ham():
    print(eggs) # this is the global
eggs = 42 # this is the global
spam()
print(eggs)
    
    

def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'
eggs = 'global'
spam()




#######################################################
###############    Try/Except     ###################
####################################################### 

"""
Hata Türleri
1)programcı hataları(Error)
2)Program kusurları(Bug)
3)istisnalar(Exception)

    
örneğin ;
print "merhaba dünya Python!"

yazıldı ve çalıştırıldı
out:
invalid syntax hatası verir
Söz dizimi hatasıdır:
    bu hatalar, programlama diline ilişkin bir özelliğin yanlış kullanımından 
    veya en basit şekilde programcının yaptığı yazım hatalarından kaynaklanır.
    
    
    ValueError istenilen değer tipinde olmayan bir değer tipi ile işlem yapılıyorsa.
    ZeroDivisionError bir sayının 0 ile bölünmesi bu gibi hatalar birer istisnadır.
    hata(error ), kusur(bug), istisna (exception)
    
    
    
    






şimdi bir hata oluşması durumunda o hatayı bilinen 
bir sonuç olarak bilerek yaptıysak bu hata değeri makinaya
 anlamlı olarak bizim tarafımızdan ne anlama gelir bunu açıklayacağız
 
 mesela buna örnek olarak bir sayının sıfır ile bölümü makinanında
 bizimde bildiğimiz bir tanımsızlıktır .
 bu tanımsızlığın hata açıklamasını belirtebiliriz.
"""

# istisna işleme
#Exception Handling
#Divide-by-zero
#sıfır ile bölüm olarak bir örnek yapacağız.



"""
Bu örnekte 42 ilk önce 2 ile bölünüyor.
sonuç bulunuyor.
12 ile bölünüyor sonuç bulunuyor.
sıra 0 ile bölüme geliyor.
"""
#######################################################
###############          ÖRNEK      ###################
####################################################### 
def spam(divideBy):
    return 42 / divideBy
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1)) 

# output:  ZeroDivisionError: division by zero   # hata mesajı


def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
        
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

#hata vereceğini bildiğimiz kodları try içerisine alıyoruz.

#######################################################
###############          ÖRNEK      ###################
####################################################### 

ilk_sayı=input(" ilk sayı: ")
ikinci_sayı=input("ikinci sayı:")

try:
    sayı1=int(ilk_sayı)
    sayı2=int(ikinci_sayı)
    print(sayı1,"/",sayı2,"=",sayı1/sayı2)
except ValueError:
    print("Lütfen sadece sayı giriniz!")

"""

except ValueError:
    print("Lütfen sadece bir sayı giriniz!")

Buradaki kod python'a şu emri vermiş olduk.
Eğer try bloğu içinde belirtilen işlemler sırasında bir ValueError ile karşılaştırırsan
bunu görmezden gel ve normal şartlar altında kullanıcıya göstereceğin hata mesajını gösterme
onun yerine kullanıcıya lütfen sadece sayı girin' uyarısını göster.

#####################################################
try:
    hata verebileceğini bildiğimiz kodlar
except hataAdı:
    hata durumunda yapılacak işlem
####################################################
    
    detayları var şimdilik dursun
    
    
    
"""
import sys

print("This is the  Collatz sequence")
user= int(input("Enter a number: "))

def collatz(n):
    print(n)
    while n!=1:
        if n%2==0:
            n=n//2
            print(n)
        else:
            n=n*3+1
            print(n)
        sys.exit(input("çıkış için bir tuşa basınız"))
collatz(user)
#######################################################
###########   22.01.2020 tarihli çalışmalar  ##########
####################################################### 

#######################################################
###############         Listeler     ###################
####################################################### 

"""
Evet önemli bir konuya başlıyoruz listeler

1)listeler=[1,2,3,4,5,6]
 bu yapı bir dizindir.
 
liste içerisine 'cat' ,True,None,42.3.1415 gibi değerler yerleştirebiliriz.

2)şimdi bu liste içerisinden bir veri almak istersek nasıl alırız soru bu 
bu listeden veriyi nasıl çekeriz şöyle :
    
spam = ['cat', 'bat', 'rat', 'elephant']

liste içerisinde değerlerin index numaraları vardır ve ilk giriş yapan veri 0
değerine atanarak başlar.

name=spam[0]
print(name)
 out : cat olarak çıkış verir.
"""
#1)
spam = ['cat', 'bat', 'rat', 'elephant']
print(spam)

#2)
name=spam[0]
print(name)

name1=spam[1]
print(name1)


print('this is name '+ spam[0]+' dizinler içerisinden 0. indexten okundu.')

"""
dizin içerisinden veri çekme işlemi sadece int sayılarla yapılır.

spam[1.0]
bu arama hata verecektir 

veya 
spam[1000] değeri ile aratma yapılır ise 
IndexError:list index out of range  hatası verilrir.
indexin olmadığı anlamına gelir.

3) liste içerisinde liste de tanımlanabilir.

list=[['cat','dog'],[10,,20,30,40,50]]
list[0]

"""
# 3)
list=[['cat','dog'],[10,,20,30,40,50]]
list[0]


"""
4)listeler içerisindeki listeden değer almak için ne yapmamız lazım
"""


#4)
list=[['cat','dog'],[10,20,30,40,50]]
print(list[0][1])
print(list[1][3])

"""
5) liste içerisinde sorgu yaparken negatif değer ile sorgu nasıl yapılır.
"""
spam=['cat','bat','rat','elephant']
spam[-1]
spam[-3]

'The '+spam[-1]+' is afraid of the '+spam[-3]


"""
6) listeler içerisinden belirli aralık değerlerini almak
"""
#  Alt listeler için dilimleme yapar.

spam=['cat','bat','rat','elephant']
a=spam[0:4]
b=spam[1:3]
print(a)
print(b)

"""
7) len() ile bir listenin uzunluğunun tespiti
    listede kaç tane değer var
"""
spam=['cat','dog','moose']

len(spam)



"""
8) liste içerisindeki değerleri değiştirme 
değişkenleri birbirine eşitleme
"""
spam=['cat','bat','rat','elephant']
spam[1]='1.degerin_degismesi'
print(spam)
spam=['cat','bat','rat','elephant']
spam[1]=spam[2]
print(spam)
spam[-1]=12345
print(spam)


spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:-1]


"""
9)listeler arasında toplama yapmak
listelerdeki değerleri int bir değer ile 
çarpılması halinde liste aynı şekilde o sayı kadar tekrar eder
"""

a=[1,2,3]+['A','B','C']
print(a)

liste=['X','Y','Z']*3
print(liste)

liste=liste+['A'+'B'+'C']
print(liste)

liste=liste+['A','B','C']
print(liste)

"""
10) Listeden bir değer silmek 
"""


spam=['cat','bat','rat','elephant']
del spam[2]
print(spam)

#######################################################
###############          ÖRNEK      ###################
####################################################### 
catname1='Zophie'
catname2='Pooka'
catname3='Simon'
catname4='Lady Macbeth'
catname5='Fat-tail'
catname6='Miss Cleo'


print('Enter the name of cat 1:')
catName1 = input()
print('Enter the name of cat 2:')
catName2 = input()
print('Enter the name of cat 3:')
catName3 = input()
print('Enter the name of cat 4:')
catName4 = input()
print('Enter the name of cat 5:')
catName5 = input()
print('Enter the name of cat 6:')
catName6 = input()
print('The cat names are:')
print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' +
catName5 + ' ' + catName6)


"""
output:
    
Enter the name of cat 1:

Zoophie
Enter the name of cat 2:

Pooka
Enter the name of cat 3:

Simon
Enter the name of cat 4:

Lady Macbeth
Enter the name of cat 5:

Fat-tail
Enter the name of cat 6:

Mis Cleo
The cat names are:
Zoophie Pooka Simon Lady Macbeth Fat-tail Mis Cleo



"""
    
"""
listeye isim ekleme kodlaması
 
ilk başta catname adı altında bir dizin oluşturduk
daha sonra 
while True şeklinde bir döngü ortaya koyduk
bu döngü içerisinde bizi ilk karşılayan print fonksiyonu oldu.
print içerisinde 'Enter the name of cat'='kedinin adını gir ' yazmakta 
str(len(catNames)+1)ifadesi ile print ifadesinde liste içerisindeki
şuan kaçıncı kedi isminde olunduğu yazmakta d 
daha sonra if koşulu belirtilmiş input ile giriş alırken  girişi name değişkeni içerisine aktarılıyor.
eğer name içerisine boş bir ifade girecek olursa boşluk koyarak döngüyü çalıştırmak 
istersek program dönügden çıkıyor.
ama boş bir değer değilde bir giriş yaparsak bu girişimiz sisteme hala eklenmeye devam edecek
 ver her ekleme yapıldığında bu giriş CatNames değerinin içerisine
catNames = catNames + [name]  ifadesi sayesinde girdi yapılan değer listeye eklenir
daha sonra 

print('The cat names are:') 
çıkış olarak 
kedi isimleri : çıktısı verilir
daha sonra for döngüsü ile 
for name in catNames:
    ifadesi ile liste içerisindeki cat nameleri dödüre döndüre 
print(' ' + name) basılır




"""
#######################################################
###############          ÖRNEK      ###################
####################################################### 

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
          ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
    
    
""" output :
    
Enter the name of cat 1 (Or enter nothing to stop.): (Or enter nothing to stop.):

sercan
Enter the name of cat 2 (Or enter nothing to stop.): (Or enter nothing to stop.):

sözer
Enter the name of cat 3 (Or enter nothing to stop.): (Or enter nothing to stop.):

ben
Enter the name of cat 4 (Or enter nothing to stop.): (Or enter nothing to stop.):

program
Enter the name of cat 5 (Or enter nothing to stop.): (Or enter nothing to stop.):

yazmak
Enter the name of cat 6 (Or enter nothing to stop.): (Or enter nothing to stop.):

istiyorum
Enter the name of cat 7 (Or enter nothing to stop.): (Or enter nothing to stop.):

ondan 
Enter the name of cat 8 (Or enter nothing to stop.): (Or enter nothing to stop.):

bu 
Enter the name of cat 9 (Or enter nothing to stop.): (Or enter nothing to stop.):

programı 
Enter the name of cat 10 (Or enter nothing to stop.): (Or enter nothing to stop.):

yaptım
Enter the name of cat 11 (Or enter nothing to stop.): (Or enter nothing to stop.):


The cat names are:
 sercan
 sözer
 ben
 program
 yazmak
 istiyorum
 ondan 
 bu 
 programı 
 yaptım


"""


#######################################################
#######    listelerle for döngüsünün kullanımı      ###
####################################################### 


"""
1)
        
for döngüsünün kullanımını hatırlayalım:
"""
for i in range(4):
    print(i)
"""
output:
    
0
1
2
3
"""



"""
2)
        
for döngüsünün listelerde kullanımı 
""" 
for i in [0, 1, 2, 3]:
    print(i)
"""
output:
0
1
2
3

"""
    


"""
3)
        supplies adında bir değişken oluşturuyoruz.
        for döngüsüne diyoruz ki i sayısını 0 dan başlat supplies dizini içerisindeki
        eleman sayısı kadar dönen bir döngü oluştur.
        bu for döngüsü her döndüğünde içerisinden gelen mesaj ise şu şekildedir
        yaz   --> 'Index' + i her döndüğünde i sayısını str formatına dönüştür ve 'Index' yazısının
        yanına ekle 
        + 'in spplies is :' yukarıda şimdiye kadar yazdırdığımız yazının yanına 'in spplies is :'
        ifadesini ekle 
        + supplies[i] ifadesi
        i=0 iken ; 'pens' metninin bu metnin yanına ekle bas
        i=1 iken ,i=2 ve i= 3 iken bu sayıları devam ettir listler içerisinden eş değer gelen ifadeleri 
        yazdır 
        
        
"""
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])


"""
output:
Index 0 in supplies is: pens
Index 1 in supplies is: staplers
Index 2 in supplies is: flame-throwers
Index 3 in supplies is: binders
"""


#######################################################
#######    in ve not in operatörlerinin kullanımı  ###
####################################################### 


"""
1)
        
elimizde spam adlı bir liste var
bu listenin içerisinde 'howdy',değeri var mı yok   mu bunun sorgulanması yapılması için
cat değeri spam listesi içerisinde  -in- kullandık listede cat yoktu false çıktısı verdi
cat değeri spam lsitesi içerisinde -not in - kullandık listede yok dedik gerçekten listede yoktu ve 
True değeri bastırır.
 


"""

spam = ['hello', 'hi', 'howdy', 'heyas']

print('howdy'in ['hello', 'hi', 'howdy', 'heyas'])

#true
print ('cat' in spam)
#false
print('cat' not in spam)
#true



"""

in ,in not ifadeleri


"""


#######################################################
###############          ÖRNEK      ###################
####################################################### 

mypets=['köpek1','kedi1','kedi2','tavşan1']
Enter=str(input("evcil hayvan isminizi giriniz:"))
if Enter in mypets:
    print('ismini verdiğin '+Enter +' adlı hayvan senin')
else:
    print ('ismini verdiğin '+Enter+'evcil hayvanının senle alakası yok')


#######################################################
###############          ÖRNEK      ###################
####################################################### 

mypets=['köpek1','kedi1','kedi2','tavşan1']
Enter=str(input("evcil hayvan isminizi giriniz:"))
if Enter not in mypets:
    print ('ismini verdiğin '+Enter+'evcil hayvanının senle alakası yok')
else:
    
    print('ismini verdiğin '+Enter +' adlı hayvan senin')


#######################################################
############### Çoklu ifade tanımlama   ###############
####################################################### 


cat=['fat','black','loud']
size=cat[0]
color=cat[1]
dispositon=[2]

size,color,disposition=cat
,

Augmented Assignment Operators


#######################################################
#####   Augmented Assignment Operators  ###############
####################################################### 

"""
Augmented assignment statement Equivalent assignment statement
spam += 1                         spam = spam + 1
spam -= 1                         spam = spam - 1
spam *= 1                         spam = spam * 1
spam /= 1                         spam = spam / 1
spam %= 1                         spam = spam % 1


"""

#######################################################
###############          ÖRNEK      ###################
####################################################### 

spam=int(input('bir rakam giriniz:'))
for i in range(6) :
    
    spam+=1
    print(str(spam) +'spam ifadesi 1 sayı arttırılıyor')
    if i==5:
        print ('6 defa döngü yapıldı son değer '+str(spam))
        break
    


#######################################################
###############          ÖRNEK      ###################
####################################################### 

spam=int(input('bir rakam giriniz:'))
for i in range(6) :
    
    spam-=1
    print(str(spam) +'spam ifadesi 1 sayı azaltılıyor')
    if i==5:
        print ('6 defa döngü yapıldı son değer '+str(spam))
        break


#######################################################
###############          ÖRNEK      ###################
####################################################### 
spam=int(input('bir rakam giriniz:'))
for i in range(6) :
    
    spam*=2
    print(str(spam) +'spam ifadesi 2 ile çarpılıyor')
    if i==5:
        print ('6 defa döngü yapıldı son değer '+str(spam))
        break
#######################################################
###############          ÖRNEK      ###################
#######################################################     
spam=int(input('bir rakam giriniz:'))
for i in range(6) :
    
    spam/=2
    print(str(spam) +'spam ifadesi 2 sayısına bölünüyor.')
    if i==5:
        print ('6 defa döngü yapıldı son değer '+str(spam))
        break
#######################################################
###############          ÖRNEK      ###################
####################################################### 
spam=int(input('bir rakam giriniz:'))
for i in range(1) :
    
    spam%=2
    print(str(spam) +'spam ifadesinin 2 ile bölümünden kalandır')
    if i==5:
        print ('6 defa döngü yapıldı son değer '+str(spam))
        break
    
#######################################################
###############          ÖRNEK      ###################
#######################################################    
bacon = ['Zophie']
bacon *= 3
print(bacon)





"""
spam listesi içerisindeki 'hello' ifadesinin index değeri yani listedeki konumu nedir.

"""

spam = ['hello', 'hi', 'howdy', 'heyas']
      
spam.index('hello')


# output:0

"""
###############################################################################
#######  Listeye append() komutu ile değer ekleme          ####################
#######  ve insert() metodunun kullanımı                   ####################
############################################################################### 
"""

"""
append() komutu ile liste içerisine en sonuncu indeksten sonraki bir fazla olan 
index değerine komut içerisine girilen değer eklenir.

"""

spam = ['cat', 'dog', 'bat']
spam.append('moose')
print(spam)


"""
listenin sonunda bir değer eklemek iyi güzel ama ya istediğimiz bir indexe değer atamak istesek 
ne yapmamız gerekir.
işte burada devreye .insert()
komutu devreye giriyor



"""

spam = ['cat', 'dog', 'bat']
spam.insert(1,'1. indekse ekleme yaptım.')
print(spam)
spam.insert(2,'2. indekse ekleme yaptım.')
print(spam)



"""
###############################################################################
####### Listeden remove() ile değer kaldırma               ####################
###############################################################################
############################################################################### 
"""

"""
liste içerisindeki istediğimiz bir değeri listeden kaldıracağız.
aşağıdaki örnekte spam listesi içerisindeki 'cat' değerini 
spam listesi içerisindeki 'cat ' değerini kaldıracağız.

"""

spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('cat')
print(spam)



"""
###############################################################################
####### sort() metodu ile bir liste içerisindeki değerleri  ##################
####### küçükten büyüğe doğru sıralama                        #################
############################################################################### 
"""

"""
.sort() metodu ile liste içerisindeki sayısal değerlere en küçük değerden 
en büyük değere doğru sıralama yapılır.

"""

spam = [2, 5, 3.14, 1, -7]
print(spam)
spam.sort()
print(spam)


'''
strin yapılarda sıralama işlemi ise alfabetik sırayla yapılır
a dan ileriye doğru sıralar

'''


spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
print(spam)
spam.sort()
print(spam)



'''
peki bu liste içerisindeki string değerlerini alfabenin son harfinden başa doğru 
sıralama işlemi sitenirse ne yapacağız 
işte bu seferde 
.sort(reverse=True)
yaparak bu sıralama tipini tersine çeviririz.


'''

spam.sort(reverse=True)
print(spam)


'''
fakat liste içerisinde int ve str tipi karışık bulunuyorsa bu sıralama yapılamaz
hata verir

'''
spam = [1, 3, 2, 4, 'Alice', 'Bob']
spam.sort()
print(spam)




'''
bu halde iken sıralama yapılırsa 
büyük harfle başlayan değer ve küçük harflerle başlayan bir değerlerin karışık olarak 
tutulduğu bir liste varsa 
ve bu liste için .sort() metodu kullanılmak istenirse o zaman bu metodla çalışan
 listede sıralama ilk başta büyük harfler arasında sıralama be hemen arkasına küçük 
 harfler ile sıralama yaparak tamamlanır.
'''


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
print(spam)


'''

şuan yapılan sıralamada alfabetik sıralama yapılır.eğer 

'''

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.lower)
print(spam)


spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort(key=str.upper)
print(spam)


'''
#######################################################
###############          ÖRNEK      ###################
#######################################################   
'''


import random
messages = ['It is certain',
'It is decidedly so',
'Yes definitely',
'Reply hazy try again',
'Ask again later',
'Concentrate and ask again',
'My reply is no',
'Outlook not so good',
'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])



'''
#######################################################
###   Liste bezeri tipler: strings and Tuples     #####
#######################################################   
'''
name='Zophie'
name[0]
name[-2]
name[0:4]
'Zo' in name
'z' in name
'p' not in name

for i in name:
    print('  *' +i+ '  *')
    
    
    
'''
bıkamdan usamadan devam ediyoruz 
durmak yok 
motivasyon motivasyon motivasyon 
hergün daha ileri daha ileri 
ekleye ekleye devam ediyoruzzz

ek özellik 1


name içerisindeki 'Zophie a cat '

ifadesi içerisindeki str yapıyı lisst değer gibi düşünerek index
değerine göre atama yapa bileceğimiz düşüncesi yanlıştır.
bu şekilde str yapıya ekleme veya çıkarma yapamayız .

'''

name=' Zophie a cat'
#şimdi bu name  değişkeni içerisindeki string değer e atama yapmaya çalışalım
name[7]='the'
# hata mesajı veriyor 'str ' objesi öğe atamasını desteklemiyor diyor


name='Zophie a cat' 
neWName=name[0:7]+'the '+name[8:12]
print(name)
print(neWName)
#Zophie a cat
#Zophie the  cat





"""
###############################################################################
####### Tuple DATA TİPİ İLE ŞİLEMLER                         ##################
###############################################################################
############################################################################### 
"""

'''

tuple yapısına öğre eklenemez list yapısındaki append() metodu yoktur.
tuple yapısında öğre atılamaz:
    list yapısındaki remove() ve pop() metotları yoktur.
    tuple içinde bir öğe aranamaz list yapısındaki gibi index() metodu yoktur.
    Döngüler list yapısına göre tuple de daha hızlıdır.
    
    değişmeyecek veriler için tuple yapısı list yapısına göre daha uygun seçimdir.
    
    değişmezliği nedeniyle tuple ,dictionary yapısı için anahtar kelime olarak 
    kullanılabilir.
    
    tuple string dönüşümü için kullanılabilir.
    
    tupleda index() metodu yoktur ama tuple içerisindeki verilere ulaşım
    spam=('sercan','sözer','mekatronik','mühendisi')
    gibi elimizde bir tuple veri tipi varken 
    spam[2] değerini çağırmak istersek 
    'mekatronik' olarak çıkış verecektir.
'''



eggs = ('hello', 42, 0.5)
eggs[1] = 99
print(type(eggs[0]))
print(eggs)
print(type(eggs))
"""

egg[1] içerisine dışardan başka bir müdahele ile veri değişikliği yapamayız 
<class 'str'>
('hello', 42, 0.5)
<class 'tuple'>
"""



eggs = [ 42, 0.5,'hello']
eggs[1] = 99
print(type(eggs[0]))
print(eggs)
print(type(eggs))
"""
<class 'int'>
[42, 99, 'hello']
<class 'list'>
"""




tuple(['cat', 'dog', 5])
#('cat', 'dog', 5)
list(('cat', 'dog', 5))
#['cat', 'dog', 5]
list('hello')
#['h', 'e', 'l', 'l', 'o']

#######################################################
###########   23.01.2020 tarihli çalışmalar  ##########
####################################################### 

'''
#######################################################
###########           Referanslar            ##########
####################################################### 

'''




'''
bu konuda anlatılmak istenen 
örnek vererek anlatacak olursak ;
spam ve cheese adında iki tane değişken tanımlayalım.
bu değişkenler birer kutuya benzetilsin
ve spam kutusu içerisine bir liste girsin liste içerisindeki değerler [0, 1, 2, 3, 4, 5]
şekilinde olsun.

şimdi buradaki anlamamız gerek durum şu 
spam içerisine giren verinin bir referans değeri var ve spam bu veriye referans değerini bilerek 
ulaşıyor 
eğer cheese değişkeninede spam içerisindeki refesans değeri öğretilirse 
cheese değeride bu değere ulaşa bilir.
şuan elimizdeki [0, 1, 2, 3, 4, 5] değerine iki değişkenden de ulaşa biliyoruz.
o halde cheese değişkenini kullanarak ta bu [0, 1, 2, 3, 4, 5] listesinde değişiklikler yapa biliriz



'''

#######################################################
###########       ÖRNEK     ###########################
#######################################################

spam = [0, 1, 2, 3, 4, 5]
cheese = spam
print(cheese)
#[0, 1, 2, 3, 4, 5]
cheese[1] = 'Hello!'
spam
print (spam)
#[0, 'Hello!', 2, 3, 4, 5]



'''
#######################################################
###########  GEÇİŞ REFERANSLARI     ###################
###########  Passing References     ###################
#######################################################


Burada gene referans değerleriyle değişken değerini def fonk. ile nasıl kullanılıyor ona bakalım 
bir def tanımladık
isminide eggs koyduk
eggs ismindeki fonksiyonun değişken ismini someParameter koyalım
egss sınıfında someParameter değerimize ne yyapmak istersin diyecek şekilde bir kodlama yapıyoruz.
daha sonra def içerisindek çıkıyoruz.
spam adında bir liste oluşturuyoruz.
ve fonksiyon dışındaki kodumda eggs fonksiyonunu çağırıyoruz.
ve na diyoruz ki senin someParameter değerin artık spam değişkeni içerisindeki değerdir
fonksiyonda someParameter ile ne yapıyorsan artık spam değişkeni içerisindeki değer ile yapacaksın
daha sonra spam değerimizi print() ile basıyoruz.


'''
#######################################################
###########       ÖRNEK     ###########################
#######################################################
def eggs(someParameter):
    someParameter.append('Hello')
spam = [1, 2, 3]
eggs(spam)
print(spam)

'''
###################################################################
###########  Kopyalama fonksiyonları                ###############
###########  copy() ve deecopy() fonksiyonları      ###############
###################################################################

bir liste bir sözlük kopyalaması nasıl olacak şimdi bu konuya değinelim 
elimizde pythonda bu konuyla ilgili bir kütüphane var 
ilk önce pythona bu kodu çağırıyoruz.
kardeşim gel buraya sana kopyalama işi çıktı şunu hallet diyoruz 
 
import copy  / evet kütüphanemmizi çağırdık.
          
bir önceki konuda referans değerlerinden bahsetmiştik
bir değişken referans değeri ile ulaşması gerek değere ulaşıyor demiştik 
aslında 
spam=cheese değer bir kopyalama işlemidir.bunu gibi düşünmek lazım



spam değer içerindeki referans değerini kopyala ve cheese değerine yapıştır.

cheese=copy.copy(spam)




'''



'''
#######################################################
###########       ÖRNEK     ###########################
#######################################################
'''

import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
print(spam)
# ['A', 'B', 'C', 'D']


import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.deepcopy(spam)
cheese[1] = 42
print(cheese)
print(spam)
#['A', 42, 'C', 'D']
#['A', 'B', 'C', 'D']  




'''
#######################################################
#######    Sözlük veri tipi             ###############
#######    The Dictionary Data Type     ###############
#######################################################
'''

'''

Sözlük  için {}  parantezi kullanılır.
sözlük={'Sözlüğün_anahtarı':'anahtar_değeri'}

kişi_bilgileri ={
sözlüğe diyoruz ki boyu: 184 
kilosu:78
saç rengi :siyah 
}

sonra soruyoruz

kişi_bilgileri[boyu] --> kişinin boy bilgisini getir.
oda sözlük içerisindeki anahtarı boy olan değeri getirir
yani bir sandık gibi

sözlük  bir oda 
oda içerisinde sandıklar var boy,kilo,saç rengi vs  ve sandıkların içerisinde mektup var
bu mektupta ne yazılyor öğrenmek istiyoruz.
odaya girip hangi sandıktaysa onu açıyoruz ve değeri yani mektupu okuyoruz.




'''

'''
#######################################################
###########       ÖRNEK     ###########################
#######################################################
'''

myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size']


print('sözlükte kayıtlı olan kedinin ölçüsü : '+myCat['size']+' ,kedinin rengi: '+myCat['color']+',kedinin huyu/eğilimi:'+myCat['disposition'])



spam = {12345: 'Luggage Combination', 42: 'The Answer'}

type(spam)



'''
#######################################################
########### Dictionaries vs. Lists   ##################
#######################################################
'''


'''
sözlük ile liste arasındaki ayrımdan biri ise liste içerisindeki veriler 
index değerine göre ayrım yapar
sözlüklerde ise anahtar değerine bakar ve değeri bellidir.
bu yüzden aşağıdaki örnekteki gibi eğer 2 liste içerisindeki veriler aynı sırada 
ve aynı şekilde yazılı ise true değeri görürüz fakat 
herhangi bir sapma index ,verideki değişiklik bu koşulu Fasle yapar
ama kütüphanede sıralamanın önemi yoktur . içerik önemlidir.



'''

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}

print(eggs==ham)
#True değeri çıkışı veirir.


spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon
print(spam==bacon)
#false


'''
#######################################################
###########       ÖRNEK     ###########################
#######################################################
'''

'''
birthdays islimli bir sözlük oluşturuyoruz.
anahtarlar ve değerlerii sözlük içerisine girildi
while döngüsü ile sonsuz loop oluşturuluyor.
döngü içerisinde bir print ile isim değeri girişi isteniyor 
input ile name değişkeni içerisine bu girdi değerinin alıyoruz.
eğer boş giriş yapılırsa döngüden çıkılır.

eğer name içerisindeki değer birthdays içerisinde varsa
print ile baskı yapılacak bu baskı içerisinde birthdayssözlüğü içerisinden 
name için aldığımız girdiyi aratıyoruz.
anahtar değerini arattırdığımız  veri değerini bize verir.
daha sonra bu değeri 'in the birthday of' metini ile birleştiririz.
daha sonra + name ifadesi ile name içine aldığımız girdi değeri eklenir.
daha sonra bastırma işlemi biter 
if döngüsü name ifadesini sözlük içerisinde bulamazsa bunun içinde bir koşul oluşturuyoruz.
bu durum oluştuğunda bu isim için doğum günü bilgisine sahip değilim dememiz gerekiyor
             print('I do not have birthday information for ' + name)
burda bundan bahsediyoruz ve en son name girdisi ile mesajımıza ekleme yapıyoruz.

daha sonra bu isimde girdiğimiz kişinin ismini saorarark bu kişiyide sözlüğe ekleme yapacağız
bunu için bday= isimli bir değişken oluşturuyoruz ve input() metodu ile buyara girdi alıyoruz
birthdays[name]=bday
en son girdiğimiz isim için bir birthday değeri yoktu ve onu tanımladık sonrada bu name değerine 
değer ataması yaptık.

daha sonra bu atamanın yapıldığını program akışında problem olmadığını anlamak için print ile 
databse güncellemesi yapıldı gibi bir mesaj ekleyebiliriz
daha sonra program tekrar isim isteyecek ta ki boş değer girişi yapıp döngüyü kırma işlemi 
yapana dek



'''

birthdays={ 'Alice':'Apr 1','Bob':'Dec 12','Carol': 'Mar 4'}
while True:
         print("Enter a name: (blank to quit)")
         name = input()
         if name=='':
             break
         if name in birthdays:
             print(birthdays[name]+' in the birhtday of '+name)
         else:
             print('I do not have birthday information for ' + name)
             print('What is their birthday?')
             bday = input()
             birthdays[name] = bday
             print('Birthday database updated.')
            


'''
###################################################################
###########  keys() ,values() ve items() metotları  ###############
###################################################################
###################################################################

.values() değeri
sözlük içerisindeki değerler ile ilgili bilgi alır.

.keys()
sözlük içerisindeki anahtar değerleri ilgili bigiye ulaşmak için kullanılır.

.items()
sözlük içerisindeki bir tane itemi taşır ve bize getirir.

'''
spam = {'color': 'red', 'age': 42}
for v in spam.values():
    print(v)
#red
#42



spam = {'color': 'red', 'age': 42}
for k in spam.keys():
    print(k)

#color
#age



spam = {'color': 'red', 'age': 42}
for i in spam.items():
    print(i)
#('color', 'red')
#('age', 42)

'''
sözlük içerisindeki anahtar ve anahtarlara karşılık
gelen değerleri lsiteleme işlemi yapmak çok kolay
bu şekilde sözlükteki anahtarlar sözlükten çıkarılıp 
lsitelene biliyor bunu yaparken sözlük değişkeni etkilenmez.

print(spam.keys()) ifadesi çalıştırıldığından 

dict_keys(['color', 'age']) şeklinde çıktı veririr.

dict_keys( ) ifadesi ile içerideki anahtarları bir listeye alıp bu değerleri sözlük
anahtarları olduğu belirlilerek bir paranteze alınır.


'''

spam_list=list(spam.keys())
print(spam_list)

print(spam.keys())



'''
spam = {'color': 'red', 'age': 42} 
şimdi sözlük belirledik
key ve value olarak iki kısımlı itemlerden oluşuyor bu sözlük bilindiği gibi
bu sözlük içerisindeki her anahtar ve bu değere karşılık gelen değeri için
 bir döngü oluşturmak istiyoruz.
 
 for döngüsü ile döngü başlatacağız.
for  k,v in spam.item(): / spam sözlüğü içerisindeki key ve value değerleri için döngü oluştur.
her döngüde k,v değerleri için anaktar ve değerlerini k,v içerisine yansıtacak

bu değerler de print ile basıla bilir k değeri ile çağırılan key değerleri zaten str tipinde 
fakat value değerleri içerisinde int tiplerde bulunmakta bu yüzden bu değerleri str tipine 
dönüştürerek yazdıra bilirz.


''' 
spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))



'''
###################################################################
########### Checking Whether a Key or Value         ###############
###########     Exists in a Dictionary              ###############
###################################################################
###################################################################
sözlük içerisinde var olan anahtar ve değer kontrol edilmesi


'''




'''
#######################################################
###########       ÖRNEK     ###########################
#######################################################
'''
spam={'Anahtar1':'Veri1','Anahtar2':'Veri2','Anahtar3':'Veri3'}
a1='Anahtar1' in spam.keys()
a2='Veri1' in spam.values()
a3='veri4' not in spam.keys()
a4='tip1' in spam
print(a1)
print(a2)
print(a3)
print(a4)



'''
###################################################################
###################################################################
############    The get() Metodu                     ##############
###################################################################
###################################################################
sözlük içerisinde var olan anahtar ve değer kontrol edilmesi


bu örnekte sözlük içerisinde sorgu yapacağız

'''

picnic_items={ 'apples':5 ,'cups':2}
print('I am bringing '+str(picnic_items.get('cups',0))+' cups.')

print('I am bringing ' +str(picnic_items.get('eggs',0))+ ' eggs.')


ing_sözlük={'dil':'language',"bilgisayar":"computer","masa":"tabel"}

sorgu=input("Litfen anlamını öğrenmek istediğiniz kelimeyi yazınız: ")

print(ing_sözlük[sorgu])




'''
###################################################################
###################################################################
############    The setdefault() methodu             ##############
###################################################################
###################################################################
bu ifade bir sabitleme ifadesidir.
bir değişkenle bu set yapılırsa bir daha değiştirilemez.
bu değişkene yeni değer ataması yapılamaz.





'''

spam = {'name': 'Pooka', 'age': 5}
if 'color' not in spam:
    spam['color'] = 'black'
 

print(spam)





spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black')
spam
spam.setdefault('color', 'white')
spam
type(spam['color'])
'''
burada set edilen bir değer var 
o değerin değişmediğini görmüş olduk.
çünkü ilk başta bir set değeri oluşturduk sonraki aynı değere değer ataması 
yapmak istedik ama program zaten böyle bir değişken içerisinde set edilmiş
 bir değer var dedi
'''



massage='merhaba ben sercan sözer şuan sizlere setdefault() metodu için bir örnek yapacağım'
count={}
for character in massage:
    count.setdefault(character,0)
    count[character]=count[character]+1
    
print(count)


'''
burada bize massage içerindeki değerlerin sayısal karşılıklarını vermiş oldu her harfin 
default değeri aslında nasıl algılanıyor onu görmüş olduk
'''
    
    

import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
    
    
import pprint
Dictionary={'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}
someDictionaryValue=Dictionary.values()
print(someDictionaryValue)
pprint.pprint(someDictionaryValue,indent=0)
print(pprint.pformat(someDictionaryValue,compact=True))
    
    

    '''
    şimdi XOX oyunu oluşturalım
    bu oyunu kullanacağımız tabla nasıl olacak onu görelim
    
                          |         |
                  'top-L' | 'top-M' |'top-R'
                          |         |
                 ---------+---------+--------
                          |         |
                  'mid-L' | 'mid-M' | 'mid-R'
                          |         |
                 ---------+---------+--------
                          |         |
                  'low-l' | 'low-M' |'low-R'
                          |         |
                          
                          
        tabla içerisindeki alanlar için sözlük içerisine anahtarlar tanımlanır
        daha sonra bu ifadeler içerisine value değerleri aktarılacak
        
    '''
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ','mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ','low-L': ' ', 'low-M': ' ', 'low-R': ' '}
    
    
    
    
    def printBoard(board):
        print(board['top-L'] + ' | ' + board['top-M'] + ' | ' + board['top-R'])
        print('--+---+--')
        print(board['mid-L'] + ' | ' + board['mid-M'] + ' | ' + board['mid-R'])
        print('--+---+--')
        print(board['low-L'] + ' | ' + board['low-M'] + ' | ' + board['low-R'])
printBoard(theBoard)







'''
#######################################################
###########     ÖNEMLİ  ÖRNEK     ###########################
#######################################################


BU ÖRENĞİN AÇIKLAMASINI YAPALIM!!!

theBoard isimli bir sözlük oluşturuyoruz.
ve value değerlerini boş bırakıyoruz.
böylelikle aşağıdaki şekilde oluşturasağımız alanlar için tanımlamalar oluşturacağız
    
                          |         |
                  'top-L' | 'top-M' |'top-R'
                          |         |
                 ---------+---------+--------
                          |         |
                  'mid-L' | 'mid-M' | 'mid-R'
                          |         |
                 ---------+---------+--------
                          |         |
                  'low-l' | 'low-M' |'low-R'
                          |         |
                          
                          evet burada her alanın ismini oluşturduk.

#0 numaralı
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
                       
#1 numaralı
 printBoard isimli bir fonksiyon oluşturuyoruz
bu fonksiyon içerisinde 
#1.1 numaralı satırdan #1.5 numaralı satıra kadar olan satılarda 
oyun tahtamız şekilleniyor bu fonksiyon her şekillendiğinde ekleme yapılacaksa board olarak 
hangi değer verildiyse o değeri günceller.
ve oyun tahtasını günceller

daha sonra ana kodumuza dönüyoruz.
ve bir değişten tanımlıyoruz

turn='X'
değeri oluşturuldu
daha sonra bir for döngüsü oluşturuluyor.
dönü içerisinde i 0 dan başlayarak 9 a kadar bir dönüg oluşturulur
bu döngü içerisinde printBoard fonksiyonu çağırılır ve fonksiyondaki işlemlerini 
theBoard sözlüğü için çalıştır diyoruz.
ve daha sonra bir mesaj yollarız kullanıcıya 
diyoruz ki ;
Turn for -
X için döndür  
O için döndür diyeceğiz 
+ turn değişkenini yansıtacağız şuan için turnde X değeri var sırasıyla başlatıyoruz.
daha sonra soruyoruz X değişkenini hangi alana hareket ettireceksin.

print('Turn for ' + turn + '. Move on which space?') bu anlama gelir.


daha sonra move değişkeni tanımlarız ve input() metodu ile değişken içerine veri çekeceğiz
ve bu değişken içerisindeki alan theBoard sözlüğü içerisindeki bir değer olmalı 
sözlükte belirttiğimiz tahtada olan alanlardan birini yazıyoruz.

daha sonra bir if döngüsü oluşturuyoruz.
eğer buraya kadar ki işlem sırasında turn değeri X te ise ve O ya çeviririz 
sıra o ya geçer 
eğer O da  ise X değerine geçer


daha sonra hepsinden çıkarız
ve oyun tahtasını tekrar çağırırız biz işlemleri yaptık gel tahtayı bir daha oluştur 
diyeceğiz 
oyun bu şekilde oynanmış olacak.


'''



#0
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
#1
def printBoard(board):
    #1.1
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    #1.2
    print('-+-+-')
    #1.3
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    #1.4
    print('-+-+-')
    #1.5
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)

'''
 | | 

-+-+-
 | | 
-+-+-
 | | 
Turn for X. Move on which space?

top-L
X| | 
-+-+-
 | | 
-+-+-
 | | 
Turn for O. Move on which space?

top-M
X|O| 
-+-+-
 | | 
-+-+-
 | | 
Turn for X. Move on which space?

top-R
X|O|X
-+-+-
 | | 
-+-+-
 | | 
Turn for O. Move on which space?

Mid-M
X|O|X
-+-+-
 | | 
-+-+-
 | | 
Turn for X. Move on which space?


kodumuzun işleyişi bu şekildedir.

'''





###############################################################################
#######################  25.0.1.2020 TARİHLİ ÇALIŞMALAR #######################
###############################################################################


"""
Nested Dictionaries and Lists

iç içe sözlükler ve listeler

bu ifade ile öğrenebileceğimiz bilgi şu şekildedir.
totalBrought()
bir sözlük tanımladık
sözlüğümüz allGuests  isimli bir sözlük olsun
daha sonra bu sözlük içerisinde 
'Alice':adına tanımlanmış diğer sözlük bilgileri bulunsun.

sözlük={'Alice':{'apples:'5,'pretzels':12 } } bu değer iç içe geçmiş bir sözlüktür.

şimdi bu öreneği şu şekilde tanımlayalım 
bir piknik yapılacak.
ve herkes imkanlarına göre bazı şeyler hazırlamış gelmiş
bu pikniğe katılacakların her biri anahtar değerdir.
ve katılımcıların getirdiği yiyecekler anahtarı sözlük konumuna düşürerek
ne getirirlmiş ne kadar getirilmiş olarak bir sözlük daha oluşturuyor.
şimdi iç içe geççmiş iki tane sözlüğümüz var 
peki biz bu sözlük içerisindeki  yani piknik alanındaki yiyeceklerden toplam 
kaç tane var hangi yiyecekten kaçar tane getirilmiş bunu öğrenmek istiyoruz 
nasıl yapmamız gerekir

işte burada bize yardımcı olacak bir metod bulunuyor.
bu metod şu şekildedir.
 totalBrought()
 
burada kullanılma şeklinden bahsedelim 
totalBrought(ana_sözlük_adı,toplamı_bulunacak_anahtarın_adı)

totalBrought(sözlük,'apples') bu bilgi bize sözlük içerisinde 'apples' değerine eşit olan 
verilerin toplamını verir.


"""


allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
'Bob': {'ham sandwiches': 3, 'apples': 2},
'Carol': {'cups': 3, 'apple pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - Apples ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies ' + str(totalBrought(allGuests, 'apple pies')))





"""
kütüphane içerisinde key ve value değerleri çekmek için kullanılacak for döngüsü

spam = {'color': 'red', 'age': 42}
for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
"""





"""  şimdi güzel bir mmorpg oyunu için item toplama uygulaması yapacağız güzel bir uygulama
şimmdi burada iki tane fonksiyon tanımlayacağız
1.si envanterimizin gösterildiği bir fonksiyon tanımlıyoruz.
2.si bu envantere ekleme yapılması için kullanılacak bir fonksiyon yazıyoruz.
 
"""


'''
#######################################################
###########     ÖNEMLİ  ÖRNEK     #####################
#######################################################

bunu unutmammmmm
zamanımı aldı ama güzel oldu.

'''


sözlük1={'key1':5,'key2':15,'key3':20}
canta={'key1':10,'key2':36,'key3':68}
def sözlük(anahtar,değer):
     sözlük1
     for k,v in sözlük1.items():
         print(k+' anahtar değeridir. '+str(v)+' ifadesi değerdir.')
     print('şimdi kütüphaneye ekleme yapacağız.')
        


def ekle(anahtar1,değer1):
    
    print('eğer sözlük1 içerisindeki değerlere ekleme yapılacaksa buradan bakacağız')
    print('çanta bulduk.eklemek istiyormusun.')
    m=input("çantayı alacakmısın : ")
    
    if m=='Evet':
        
        print(sözlük1)
        
        for k1,v1 in sözlük1.items():
            
                sözlük1[k1]=sözlük1[k1]+canta[k1]
        sözlük(sözlük1.keys(),sözlük1.values())
                
         
    elif m=='Hayır':
        print('yola devam et')
        
        
    else: 
        print('çıkış yapılıyor')
        sys.exit('exit')    


neyapacaksın=input("çantadaki eşyaları alacakmısın?'Evet'/'Hayır' ")
if neyapacaksın=='Evet' :
    
    ekle(canta.keys(),canta.values())
elif neyapacaksın=='Hayır':
    sys.exit('exit')
else:
    print('yanlış bir tuşa bastın')
    neyapacaksın=input("çantadaki eşyaları alacakmısın?'Evet'/'Hayır' ")
 

        


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    