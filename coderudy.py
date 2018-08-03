Première version de l'app encodeur:

import string
import random
import datetime

print("                                                                      ")
print("- C A P T A I N  C O D E - ")
print("                                                                      ")
print ("WELCOME_BIENVENUE_歓迎_BONI | DD3 INTELLIGENCE AGENCY | SPECIAL REPORT ")
print("                                                                      ")
print("------------------------------------------------------------------------")

now = datetime.datetime.now()
print ("TIME | ", now)
print("------------------------------------------------------------------------")
#print ("YEAR | ", now.year)
#print ("MONTH | ", now.month)
#print ("DAY | ", now.day)
#print ("TIME | ", now.hour, now.minute, now.second)

from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(8, 20)))
input("ENTER AGENT ID | ")

#if input == characters:
print("AUTORISED ACCESS | ")   

#else:
    #print ("ACCESS DENIED | ")

print("------------------------------------------------------------------------")
plain_text = input("CLASSIFIED MESSAGE | ")


print("------------------------------------------------------------------------")
encrypted_text = ("ENCRYPTON | To copy: ")
for c in plain_text:
    x = ord(c)
    x = x + 12 - 6 + 3 - 4 
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)
print("------------------------------------------------------------------------")
print("                                                                      ")
print("// DD3 INTELLIGENCE DECRYPTON //")
print("                                                                      ")
encrypted_text = input("INSERT ENCRYPTON | ")
print("                                                                      ")
plain_text = ("DECRYPTED MESSAGE | ") 
for c in encrypted_text:
    x = ord(c)
    x = x - 12 + 6 - 3 + 4 
    c2 = chr(x)
    plain_text = plain_text + c2
print("------------------------------------------------------------------------")
print ("ANALYSING... | ")
print("------------------------------------------------------------------------")
print("                                                                      ")
print(plain_text) 
print("------------------------------------------------------------------------")


choix = int(input ("COPY (1) OR DESTROY (2) THIS INTEL? "))

if choix == 1:
    print("                                                                      ")
    print ("THANKS. THIS INTEL AS BEEN CLASSIFIED")
    print("                                                                      ")
    print ("YOUR GENERATED FILE CODE IS: ", password)
    print("                                                                      ")
    print("*** This message will be destroy in 20 secondes ***") 
    print("                                                                      ")
    print ("DD3 INTELLIGENCE AGENCY | TONI CAPTAIN INC. | SPECIAL REPORT ")
    print("                                                                      ")

elif choix == 2:
    f = int and str(input("DESTROY NOW? (ENTER) "))
import random
min = 1
max = 3
roll_again = "yes"
while roll_again == "yes" or roll_again == "y":
    print(random.randint(1,100000000000000000000))
    print("                                                                      ")
    print ("INTEL ERASED")
    print("------------------------------------------------------------------------")
    print ("*** /// SYSTEM RELOADING /// *** ")
    print("                                                                      ")
    print ("INTEL AS BEEN DESTROYED")
    print("                                                                      ")
    print("*** Auto-destruction in 20 secondes ***") 
    print("                                                                      ")
    print ("// DD3 INTELLIGENCE AGENCY | TONI CAPTAIN INC. | SPECIAL REPORT // ")
    print("                                                                      ")




#else:
    #int(input ("CANCEL (6) "))