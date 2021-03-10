#GLOBAL AI HUB
#İbrahim Utku USLUCAN
#Homework 2

cv1 = { "Name: ":"Furkan",
        "Surname: ":"Kaya",
        "Date of Birth: ":"01.05.1993",
        "Nationality: ":"TC",
        "Place of Birth: ":"İstanbul",
        "Job Title: ":"Bilgisayar Mühendisi"}

cv2 = cv1.copy()
cv3 = cv1.copy()
cv4 = cv1.copy()
cv5 = cv1.copy()

cv2["Name: "] = "Burcu"
cv2["Surname: "] = "Yılmaz"
cv2["Date of Birth: "] = "13.08.1995"
cv2["Nationality: "] = "TC"
cv2["Place of Birth: "] = "Ankara"
cv2["Job Title: "] = "Muhasebeci"

cv3["Name: "] = "Ahsen"
cv3["Surname: "] = "Korkut"
cv3["Date of Birth: "] = "21.06.1990"
cv3["Nationality: "] = "TC"
cv3["Place of Birth: "] = "Van"
cv3["Job Title: "] = "Yazılım Mühendisi"

cv4["Name: "] = "İbrahim Utku"
cv4["Surname: "] = "Uslucan"
cv4["Date of Birth: "] = "23.01.1999"
cv4["Nationality: "] = "TC"
cv4["Place of Birth: "] = "Ankara"
cv4["Job Title: "] = "Öğrenci"

cv5["Name: "] = "Ömer"
cv5["Surname: "] = "Aktaş"
cv5["Date of Birth: "] = "25.12.1984"
cv5["Nationality: "] = "TC"
cv5["Place of Birth: "] = "İstanbul"
cv5["Job Title: "] = "Avukat"


def printCv():
    for a,b in cv1.items():
        print(a,b)
    print("\n")
    for a,b in cv2.items():
        print(a,b)
    print("\n")
    for a,b in cv3.items():
        print(a,b)
    print("\n")
    for a,b in cv4.items():
        print(a,b)
    print("\n")
    for a,b in cv5.items():
        print(a,b)


printCv()
