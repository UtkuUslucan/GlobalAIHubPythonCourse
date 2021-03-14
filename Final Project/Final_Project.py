#GLOBAL AI HUB
#İbrahim Utku USLUCAN
#Final Project

import time as tm

questions = ["1 - Türkiye'nin başkenti neresidir?",
             "2 - Kadınlara seçme ve seçilme hakkı tanıyan ilk ülke hangisidir ?",
             "3 - İnsan vücudu her gün kaç nefes alır?",
             "4 - Cumhurbaşkanı kaç yılda bir seçilir?",
             "5 - Pusulada (N) harfi hangi yönü ifade eder",
             "6 - İnternet üzerinde en fazla kullanılan arama motoru hangisidir ?",
             "7 - Basketbol karşılaşmasında bir takım maç süresince kaç adet mola kullanabilir",
             "8 - En geniş ormanlık alana sahip bölgemiz hangisidir ?",
             "9 - Hayvanları koruma günü hangi gündür ?",
             "10 - Pisagor teoremi hangi bilim dalıyla ilgilidir ?"]


def ask():
    puan = 0

    print("BİLGİ YARIŞMAMIZA HOŞGELDİNİZ\n")
    tm.sleep(0.5)
    guest = input("Adınız: ")
    tm.sleep(0.3)
    print("Hoşgeldin",guest.upper()+".")
    tm.sleep(1)
    print("Yarışmada başarılı olabilmek için 10 sorudan en az 6 soruyu doğru işaretleminiz gerekiyor. Aksi takdirde başarısız olacaksınız.")
    tm.sleep(0.5)
    input("Hazır olduğunda 'ENTER' tuşuna basarak yarışmayı başlatabilirsin.")
    print("Yarışmamız 3 saniye sonra başlıyor!")
    print("3..")
    tm.sleep(1)
    print("2..")
    tm.sleep(1)
    print("1..")
    tm.sleep(1)

    print("Soru", questions[0])
    answer1 = input("Cevap: ")
    if (answer1.lower() == "ankara"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Ankara")
    print("Puanınız: ",puan,"\n")


    print("Soru", questions[1])
    answer2 = input("Cevap: ")
    if (answer2.lower() == "türkiye"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Türkiye")
    print("Puanınız : ", puan,"\n")


    print("Soru", questions[2])
    answer3 = input("Cevap: ")
    if (answer3.lower() == "20000"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : 20000")
    print("Puanınız : ", puan,"\n")


    print("Soru", questions[3])
    answer4 = input("Cevap: ")
    if (answer4.lower() == "5"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : 5")
    print("Puanınız : ", puan,"\n")


    print("Soru", questions[4])
    answer5 = input("Cevap: ")
    if (answer5.lower() == "kuzey"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Kuzey")
    print("Puanınız : ", puan,"\n")


    print("Soru", questions[5])
    answer6 = input("Cevap: ")
    if (answer6.lower() == "google"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Google")
    print("Puanınız : ", puan,"\n")


    print("Soru:", questions[6])
    answer7 = input("Cevap: ")
    if (answer7.lower() == "5"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : 5")
    print("Puanınız : ", puan,"\n")


    print("Soru:", questions[7])
    answer8 = input("Cevap: ")
    if (answer8.lower() == "karadeniz"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Karadeniz")
    print("Puanınız : ", puan,"\n")


    print("Soru:", questions[8])
    answer9 = input("Cevap: ")
    if (answer9.lower() == "4 eylül" or "4eylül"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : 4 Eylül")
    print("Puanınız : ", puan,"\n")


    print("Soru:", questions[9])
    answer10 = input("Cevap: ")
    if (answer10.lower() == "matematik"):
        print("Doğru cevap!\n10 puan kazandınız.")
        puan += 10
    else:
        print("Yanlış cevap!\nDoğru cevap : Matematik")
    print("Puanınız : ", puan,"\n")

    print("YARIŞMADA BAŞARILI OLMAK İÇİN 50 PUAN ÜZERİ ALMANIZ GEREKMEKTEDİR.\n")
    if puan <= 50:
        print(puan, "puan ile başarısız oldunuz!\n",(100-puan),"puan daha almanız gerekiyordu.")
    elif puan == 100:
        print("TEBRİKLER BÜTÜN SORULARI DOĞRU CEVAPLAYARAK",puan,"PUAN İLE YARIŞMAYI TAMAMLADINIZ.")
    else:
        print("TEBRİKLER!\n",puan,"puan ile başarılı oldunuz!")         

ask()
