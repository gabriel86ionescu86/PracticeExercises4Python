# Gotham:
# Esti un ofiter de politie si primesti un raport de activitate criminala! O sa mergi sa te lupti singur sau sa chemi
# un supererou sa te ajute?Daca este mai mic ca 5 ai putea sa mergi singur daca este intre 5-10 ar trebui sa mergi impreuna cu Batman.
# Daca este peste 10 ar trebui sa il lasi pe Batman sa se descurce singur.
# Task:
# determina daca trebuie sa chemi ajutor sau poti sa te descurci singur si sa lupti.
#
# Input format:
# un numar intreg care reprezinta nivelul activitatii criminale
# Output:
# un string care zice: "Ma descurc" "Ajuta-ma Batman" "Noroc Batman, te descurci" in functie de scenariu
# Ex:
# 7
# Ajuta-ma Batman

# crime_level = int(input("Add the criminal activity level: "))
# if crime_level <=5:
#     print("I got this, Batman")
# elif crime_level>5 and crime_level<10:
#     print("Help me, Batman!")
# else:
#     print("Good luck Batman, you got this!")
#

## Same exercise, with range this time
# if crime_level in range(1,5):
#         print("I got this, Batman")
# elif crime_level in range(5,10):
#         print("Help me, Batman!")
# else:
#         print("Good luck Batman, you got this!")

# ------------------------------------------------------------------------------------------------------------------------
# Balconul:
# Vrei sa determini care dintre 2 apartamente are balconul cel mai mare.Amandou balcoane
# sunt dreptunghuri si au lungime si latime,dar tu ai nevoie de arie.
# Task:
# Evalueaza cele 2 arii ale balconului si determinca care este cel mai mare.
# Format input:
# intputurile vor fi 2 string-uri unde sunt introduse masuratorile pentru balcoane separate de o virgula.
# Primul reprezinta ap A iar al doilea ap B
# Output:
# Un string  care va spune ca apartamentul A sau B este mai mare:
#
# ex:
# Input:
# 5,5
# 2,10
# Output:
# Apartamentul A

# ap_A = input("Introdu lungimea,latimea pt ap A: ")
# ap_B = input("Introdu lungimea,latimea pt ap B: ")
# dimens_ap_A = ap_A.split(",")
# dimens_ap_B = ap_B.split(",")
# aria_ap_A = int(dimens_ap_A[0]) * int(dimens_ap_A[1])
# aria_ap_B = int(dimens_ap_B[0]) * int(dimens_ap_B[1])
# if aria_ap_A>aria_ap_B:
#     print("Apartamentul A este mai mare")
# elif aria_ap_A < aria_ap_B:
#     print("Apartamentul B este mai mare")
# else:
#     print("Apartamentele au aria egala")

# ------------------------------------------------------------------------------------------------------------------------
# In jungla:
# Esti cu cortul in jungla singur si auzi niste animale in intuneric prin apropiere
# Bazat pe sunete determina ce animale sunt
# Task:
# Ti se da sunetele facute de animalele din intuneric, evalueaza fiecare sunet pentru a determina ce animal este:
# Leii fac "Grr" , Tigri fac "Rawr", Serpii fac "Sss" iar pasarile fac "Cirip"
#
# Input:
# Un string ce reprezinta sunetele ce le auzi cu spatiu intre ele
# Output:
# Un string ce reprezinta animalele ce le auzi cu spatiu intre ele
# (nota sunetele se pot repeta)
#
# Ex:
# Rawr Cirip Sss
# Tigru Pasare Sarpe

# animale = {"Leu" : "Grr", "Tigru": "Rawr", "Sarpe" : "Sss", "Pasare" : "Cirip"}
#
# jungle_sounds = input("Insert animal sounds-> ")
# animal_sounds = jungle_sounds.split()
# animals = ""
# for sounds in animal_sounds:
#     if sounds == animale["Leu"]:
#         animals += "Leu "
#     elif sounds == animale["Tigru"]:
#         animals += "Tigru "
#     elif sounds == animale["Sarpe"]:
#         animals += "Sarpe "
#     elif sounds == animale["Pasare"]:
#         animals += "Pasare "
#     else:
#         animals += "Necunoscut "
# print(animals)

# ------------------------------------------------------------------------------------------------------------------------
# DejaVu:
# Intr-un sir de caractere aleatorii task-ul tau este sa aflii daca exista
# un carcater ce este repetat sau sunt doar caractere unice
# Input format: sir de caractere litere(nu vor fi numere sau alte caractere speciale)
#
# Ex:
# aaaghlj
# Output: Deja Vu
# Ex:
# aghlj
# Output: Sir Unic

# caractere = input("Introdu un sir de caractere:")
# sir_nou = []
# gasit = False
# for x in caractere:
#     if x not in sir_nou:
#         sir_nou.append(x)
#     else:
#         gasit = True
#         break
# if not gasit:
#     print("Sir Unic")
# else:
#     print("Deja Vu")
# ------------------------------------------------------------------------------------------------------------------------


# lista_cutii_valori = input(" Intordu o lista de obiecte cu virgula intre ele -> ")
# obiectul_cautat = input("Introdu obiectul cautat ->")
# timp = 0
# lista_cutii_valori = lista_cutii_valori.split(",")
# for incercare in lista_cutii_valori:
#     timp += 5
#     if incercare == obiectul_cautat:
#         break
# print(timp)

# ------------------------------------------------------------------------------------------------------------------------
#  Ai 2 prieteni ce vorbesc orca intre ei.Limba orca sunt aceleasi cuvinte
# ca in limba romana doar ca se ia prima litera a fiecarui
# cuvant si se pune la sfarsitul cuvantului in urma caruia se adauga un ay
# drum = rumday
# Input:
# Un string ce reprezinta o propozite in limba romana
# Output:
# Un string ce reprezinta traducerea in limba orca

# input_romana = input("Introdu propozitia in limba romana: ")
# def translate_orchish(word):
#     orc_word = ""
#     orc_word = word[1:] + word[0] + "ay "
#     return orc_word
# output = ""
# for word in input_romana.split():
#     output += translate_orchish(word)
# print(output)


# ------------------------------------------------------------------------------------------------------------------------
# Creati o functie ce verifica daca un sir de
# caractere este un palindrom sau nu
# ex:
# Input: ccabbacc
# Output: YES

# palindorm = input("introu un sir de caractere->")
#
# def checkPal(input_msg):
#     input_msg = input_msg.replace(" ", "")
#     isPal = False
#     front_list = 0
#     back_list = -1
#     jumatatea_listei = int(len(input_msg) / 2)
#     for x in range(jumatatea_listei):
#         if input_msg[front_list].lower() == input_msg[back_list].lower():
#             a = input_msg[front_list]
#             b = input_msg[back_list]
#             front_list += 1
#             back_list -= 1
#             isPal = True
#         else:
#             isPal = False
#     if isPal:
#         print(f" Textul '{input_msg}' este palindrom!")
#     else:
#         print(f" Textul '{input_msg}' nu este palindrom!")
#
# checkPal(palindorm)

# ------------------------------------------------------------------------------------------------------------------------


# Game of Thrones
# Dothraki plănuiesc să usurpe tronul Regelui Robert. Regele Robert aude de această conspirație de la un raven
# și plănuiește să încuie singura ușă prin care inamicul poate să pătrundă în regat lui.
#     Dar această ușă are nevoie de o cheie care este reprezentată
#     de către anagrama unui palindrom.
#     începe să caute în cutia lui de șiruri de caractere,
#     verificând pe fiecare în parte dacă poate fi rearanjat într-un palindrom.
# Cerință:
#     Pentru un șir de caractere,
#     să se tipărească pe ecran cuvântul DA sau NU
#     dacă acest șir poate fi rearanjat astfel încât să fie
#     un palindrom.
# Constrangeri:
# Poat fi folosite doar caractere
# din alfabetul latin cu litere mici
# Date de intrare:
#     Șirul de caractere.
# Exemplu:
# INPUT:
# aaabbbb
# OUTPUT:
# DA
# Șirul poate fi permutat astfel: bbaaabb
# ------------------------------------------------------------------------------------------------------------------------
# if at least 2 chars:
#     if at most 1 char is par
#     then
#         lista 0 = 1 impar char
#         lista 1 si -1 = impar char
#
# aaaabbbbccccddd
#
sir_caractere = input("Please add a password: ").lower()
sir_caractere = sir_caractere.replace(" ", "")
sir_caractere = sir_caractere.replace(",", "")
sir_secundar = {}
incrementare = 0

# First step, we find how many repetitions of each char exits & store them in a dict
for x in sir_caractere:
    if x in sir_secundar:
        sir_secundar[x] += 1
    else:
        sir_secundar[x] = 1

# Second step, we check to see if only one of those chars show up with uneven numbers
nr_uneven_chars = 0
for x in sir_secundar.values():
    if x % 2  != 0:
        nr_uneven_chars += 1

# Third step, checking if the chars have the right value to be formed into a palindrom
if nr_uneven_chars > 1:
    print(f" Can't form a palindrom with the given text!")
else:
    # Fourth step, we change order of chars and store them in a new list, in a palindrom order
    palindrom_list = []
    key_list = list(sir_secundar.keys()) # We create a list containing only the keys
    val_list = list(sir_secundar.values()) # We create a list containing only the values
    for x in val_list: # we find the char that is uneven and we add it to a new list
        if x % 2  != 0:
            a = val_list.index(x) # we store the index of the key with uneven numbers
            comparison = x
            while comparison > 0:
                palindrom_list.append(key_list[a])
                comparison -= 1
    for x in val_list: # we find the chars that are even and attach to the head and end of the list
        if x % 2 == 0:
            a = val_list.index(x)  # we store the index of the key with even numbers
            comparison = x
            existsFront = False
            while comparison > 0:
                if not existsFront:
                    palindrom_list.insert(0, key_list[a]) # we store the key to the front of the list
                    comparison -= 1
                    existsFront = True
                else:
                    palindrom_list.append(key_list[a]) # we store the key to the back of the list
                    comparison -= 1
                    existsFront = False
        key_list = key_list[1::] # we remove the elem from key list in case there's another one with the same uneven number
        val_list = val_list[1::] # we remove the elem from value list in case there's another one with the same value

print(f'''The palindrom is:
        {palindrom_list}
    ''')