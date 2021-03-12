#GLOBAL AI HUB
#İbrahim Utku USLUCAN
#Homework 3

stuOne = input("Öğrencinin adını giriniz: ")
stuOneMidterm = int(input("Ara sınav notunu giriniz: "))
stuOneProject = int(input("Proje puanını giriniz: "))
stuOneFinal = int(input("Final sınavı puanını giriniz: "))
print(stuOne, "adlı öğrencinin kaydı başarılı!\n")

stuTwo = input("Öğrencinin adını giriniz: ")
stuTwoMidterm = int(input("Ara sınav notunu giriniz: "))
stuTwoProject = int(input("Proje puanını giriniz: "))
stuTwoFinal = int(input("Final sınavı puanını giriniz: "))
print(stuTwo, "adlı öğrencinin kaydı başarılı!\n")

stuTheree = input("Öğrencinin adını giriniz: ")
stuThereeMidterm = int(input("Ara sınav notunu giriniz: "))
stuThereeProject = int(input("Proje puanını giriniz: "))
stuThereeFinal = int(input("Final sınavı puanını giriniz: "))
print(stuTheree, "adlı öğrencinin kaydı başarılı!\n")

stuFour = input("Öğrencinin adını giriniz: ")
stuFourMidterm = int(input("Ara sınav notunu giriniz: "))
stuFourProject = int(input("Proje puanını giriniz: "))
stuFourFinal = int(input("Final sınavı puanını giriniz: "))
print(stuFour, "adlı öğrencinin kaydı başarılı!\n")

stuFive = input("Öğrencinin adını giriniz: ")
stuFiveMidterm = int(input("Ara sınav notunu giriniz: "))
stuFiveProject = int(input("Proje puanını giriniz: "))
stuFiveFinal = int(input("Final sınavı puanını giriniz: "))
print(stuFive, "adlı öğrencinin kaydı başarılı!\n")

stuOnePG = float(stuOneMidterm * (0.3) + stuOneProject * (0.3) + stuOneFinal * (0.4))
stuTwoPG = float(stuTwoMidterm * (0.3) + stuTwoProject * (0.3) + stuTwoFinal * (0.4))
stuThereePG = float(stuThereeMidterm * (0.3) + stuThereeProject * (0.3) + stuThereeFinal * (0.4))
stuFourPG = float(stuFourMidterm * (0.3) + stuFourProject * (0.3) + stuFourFinal * (0.4))
stuFivePG = float(stuFiveMidterm * (0.3) + stuFiveProject * (0.3) + stuFiveFinal * (0.4))

stuOneL = { "İsim: " : stuOne, "Ara Sınav Notu: " : stuOneMidterm, "Proje Notu: " : stuOneProject, "Final Sınavı Notu: " : stuOneFinal, "Ortalama Not: " : stuOnePG}
stuTwoL = { "İsim: " : stuTwo, "Ara Sınav Notu: " : stuTwoMidterm, "Proje Notu: " : stuTwoProject, "Final Sınavı Notu: " : stuTwoFinal, "Ortalama Not: " : stuTwoPG}
stuThereeL = { "İsim: " : stuTheree, "Ara Sınav Notu: " : stuThereeMidterm, "Proje Notu: " : stuThereeProject, "Final Sınavı Notu: " : stuThereeFinal, "Ortalama Not: " : stuThereePG}
stuFourL = { "İsim: " : stuFour, "Ara Sınav Notu: " : stuFourMidterm, "Proje Notu: " : stuFourProject, "Final Sınavı Notu: " : stuFourFinal, "Ortalama Not: " : stuFourPG}
stuFiveL = { "İsim: " : stuFive, "Ara Sınav Notu: " : stuFiveMidterm, "Proje Notu: " : stuFiveProject, "Final Sınavı Notu: " : stuFiveFinal, "Ortalama Not: " : stuFivePG}

passingGrade = [(stuOneL.get("Ortalama Not: ")), 
                (stuTwoL.get("Ortalama Not: ")),
                (stuThereeL.get("Ortalama Not: ")),
                (stuFourL.get("Ortalama Not: ")),
                (stuFiveL.get("Ortalama Not: "))]
passingGrade.sort(reverse=True)

print("\n")
print(passingGrade)
