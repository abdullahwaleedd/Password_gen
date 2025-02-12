import string 
import random
import string
from csv import writer





def Password():
    s1= string.ascii_lowercase #adding all the characters (LOWER CASE)
    # print(s1)
    s2 = string.ascii_uppercase #adding all the characters (APPER CASE)
    # print(s2)
    s3 = string.digits #adding all the characters (that DIGIT)
    # print(s3)
    s4 = string.punctuation #adding all the  puncuation characters
    # print(s4)
    Platform = input("Enter the name of platform : \n")
    pass_len = int(input("Enter password length: \n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    random.shuffle(s)
    passworrd = ("".join(s[0:pass_len]))
    passdata = [Platform,passworrd]

    with open('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(passdata)

    print(passworrd)



Password()