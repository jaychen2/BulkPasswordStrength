#Password Strength Checker - Jay Chen 07/12/2019

'''
NIST Special Publication 800-63B
_________________________________________________________________________________
2017 NIST Password Guidelines:
-An eight character minimum and 64 character maximum length
-The ability to use all special characters but no special requirement to use them
-Restrict sequential and repetitive characters (e.g. 12345 or aaaaaa)
-Restrict context specific passwords (e.g. the name of the site, etc.)
-Restrict commonly used passwords (e.g. p@ssw0rd, etc.)
-Restrict passwords obtained from previous breach corpuses
_________________________________________________________________________________


'''
import os
import sys
import json
import timeit

start = timeit.default_timer()

verboseon = 0

print('Mass Password Strength Checker by: Jay Chen')
print("Verbose mode provides more information, but takes longer to load")
verbose = input('Type \'yes\' for Verbose Mode or \'no\' to Continue: ')

if verbose == 'yes':
    verboseon = 1
elif verbose == 'Yes':
    verboseon = 1
elif verbose == 'YES':
    verboseon = 1
else:
    verboseon = 0

print(verbose)

print(verboseon)


with open(os.path.join(sys.path[0], "passwordlist.txt"), "r") as f:
    password_list = []
    password_list_leet = []
    for item in f:
        item2 = item.strip()
        password_list.append(item2)
 
            
            
#print(password_list)

#password strength weight assignment 

#less than 8/more than 64
one1 = 30
#cap letter
two2 = 17.5
#special char
three3 = 17.5
#numbers
four4 = 17.5
#birthyear
five5 = 2.5
#lower letter
six6 = 17.5
#repeatnumbers
seven7 = 6
#repeatletter
eight8 = 6
#sequential letter
nine9 = 6
#seasons
ten10 = 2.5
#repeat letter upper
eleven11 = 2.5
#seq letter upper
twelve12 = 2.5
#dictionary word
thirteen13 = 4.75
#password list
fourteen14 = 4.75
#leet mode
fifteen15 = 2.5


cap_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H' , 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
special_letters = ['!','@','#','$','%','^','&','*',' ']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
repeat_num = ['111','222','333','444','555','666','777','888','999','000','012','123','234','345','456','567','678','789','910','91011']
repeat_letters = ['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']
seq_letters = ['abc','bcd','cde','def','efg','ghi','hij','ijk','jkl','klm','lmn','mno','nop','opq','pqr','qrs','rst','stu','tuv','uvw','vwx','wxy','xyz','qwe','asd','zxc','qaz','wsx','edc','qwerty','1qa','2ws','3ed']
seasons = ['Spring', 'Summer','Fall','Winter','spring','summer','fall','winter','SPRING','SUMMER','FALL','WINTER']
#repeat_special = ['!!!','@@@','###','$$$','%%%','^^^','&&&','***','   ']
repeat_letters_upper = list(map(str.upper,['aaa', 'bbb', 'ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj', 'kkk', 'lll', 'mmm', 'nnn', 'ooo', 'ppp', 'qqq', 'rrr', 'sss', 'ttt', 'uuu', 'vvv', 'www', 'xxx', 'yyy', 'zzz']))
seq_letters_upper = list(map(str.upper,['abc','bcd','cde','def','efg','ghi','hij','ijk','jkl','klm','lmn','mno','nop','opq','pqr','qrs','rst','stu','tuv','uvw','vwx','wxy','xyz','qwe','asd','zxc','qaz','wsx','edc','qwerty','1qa','2ws','3ed']))

password_remaining = len(password_list)

 

with open(os.path.join(sys.path[0], "10000DictWord.txt"), "r") as f:
    Thousand_Dict_Word = []
    for item in f:
        if len(item)>4:
            item2 = item.strip()
            Thousand_Dict_Word.append(item2)
            item3 = item2.title()
            Thousand_Dict_Word.append(item3)
            item4 = item3.upper()
            Thousand_Dict_Word.append(item4)
    #print (Thousand_Dict_Word)
    
with open(os.path.join(sys.path[0], "10000Passwords.txt"), "r") as f:
    Thousand_Password = []
    for item in f:
        if len(item)>4:
            item2 = item.strip()
            Thousand_Password.append(item2)
            item3 = item2.title()
            Thousand_Password.append(item3)
            item4 = item3.upper()
            Thousand_Password.append(item4)
            item5 = item2.rstrip('0123456789s!@#$%^&*()')
            if len(item5)>4:
                Thousand_Password.append(item5)
                item6 = item5.lower()
                Thousand_Password.append(item6)
                item7 = item6 + "s"
                Thousand_Password.append(item7)
            
    #print (Thousand_Password)

badpassword = {}

for password in password_list:
    capletter = 0
    specialchar = 0
    numberchar = 0
    birthyear = 0
    lowerletter = 0
    repeatnum = 0
    repeatletter = 0
    seqletter = 0
    season = 0
    upperrepeatletter = 0
    upperseqletter = 0
    dictwords = 0
    thousandpass = 0
    checkcount = 0
    leetcount = 0
    
    strengthcount = 0
    
    print(' ')
    print('--------------------------------------------')
    print(password)
    print('--------------------------------------------')
    password_remaining -= 1
    print('Password Remaining: ' + str(password_remaining))
    
    if len(password) < 8:
        if verboseon == 1:
            print("Check 1: Failed")
            print("- Password is less than eight characters")
    elif len(password) > 64:
        if verboseon == 1:
            print("Check 1: Failed")
            print("- Password is more than 64 characters")
    else:
        if verboseon == 1:
            print('Check 1: Passed')
        checkcount += 1
        strengthcount += one1
    
    
    for capletters in cap_letters:
        if capletters in password:
            capletter += 1
    if capletter == 0:
        if verboseon == 1:
            print("Check 2: Failed")
            print("- Password does not contain a capital letter")
    elif capletter > 0:
        if verboseon == 1:
            print("Check 2: Passed")
        checkcount += 1
        strengthcount += two2
        
    for specialchars in special_letters:
        if specialchars in password:
            specialchar += 1
    if specialchar == 0:
        if verboseon == 1:
            print("Check 3: Failed")
            print("- Password does not contain a special letter")
    elif specialchar > 0:
        if verboseon == 1:
            print("Check 3: Passed")
        checkcount += 1
        strengthcount += three3
        
    for numbers in num:
        if numbers in password:
            numberchar += 1
    if numberchar == 0:
        if verboseon == 1:
            print("Check 4: Failed")
            print("- Password does not contain a number")
    elif numberchar > 0:
        if verboseon == 1:
            print("Check 4: Passed")
        checkcount += 1
        strengthcount += four4
        
    for x in range(1900,2100,1):
        if str(x) in password:
            birthyear += 1
    if birthyear > 0:
        if verboseon == 1:
            print("Check 5: Failed")
            print("- Password contains a possible birthyear/year")
    elif birthyear == 0:
        if verboseon == 1:
            print("Check 5: Passed")
        checkcount += 1
        strengthcount += five5
        
    for lowerletters in lower_letters:
        if lowerletters in password:
            lowerletter += 1
    if lowerletter == 0:
        if verboseon == 1:
            print("Check 6: Failed")
            print("- Password does not contain a lowercase")
    elif lowerletter > 0:
        if verboseon == 1:
            print("Check 6: Passed")
        checkcount += 1
        strengthcount += six6
        
    for repeatnums in repeat_num:
        if repeatnums in password:
            repeatnum += 1
    if repeatnum > 0:
        if verboseon == 1:
            print("Check 7: Failed")
            print("- Password contains repeating/sequential numbers")
    elif repeatnum == 0:
        if verboseon == 1:
            print("Check 7: Passed")
        checkcount += 1
        strengthcount += seven7
        
    for repeatletters in repeat_letters:
        if repeatletters in password:
            repeatletter += 1
    if repeatletter > 0:
        if verboseon == 1:
            print("Check 8: Failed")
            print("- Password contains repeating letters")
    elif repeatletter == 0:
        if verboseon == 1:
            print("Check 8: Passed")
        checkcount += 1
        strengthcount += eight8
        
    for seqletters in seq_letters:
        if seqletters in password:
            seqletter += 1
    if seqletter > 0:
        if verboseon == 1:
            print("Check 9: Failed")
            print("- Password contains sequential letters")
    elif seqletter == 0:
        if verboseon == 1:
            print("Check 9: Passed")
        checkcount += 1
        strengthcount += nine9
        
    for seas in seasons:
        if seas in password:
            season += 1
    if season > 0:
        if verboseon == 1:
            print("Check 10: Failed")
            print("- Password contains seasons")
    elif season == 0:
        if verboseon == 1:
            print("Check 10: Passed")
        checkcount += 1
        strengthcount += ten10
        
    for rlu in repeat_letters_upper:
        if rlu in password:
            upperrepeatletter += 1
    if upperrepeatletter > 0:
        if verboseon == 1:
            print("Check 11: Failed")
            print("- Password contains repeating letters in uppercase")
    elif upperrepeatletter == 0:
        if verboseon == 1:
            print("Check 11: Passed")
        checkcount += 1
        strengthcount += eleven11
        
    for slu in seq_letters_upper:
        if slu in password:
            upperseqletter += 1
    if upperseqletter > 0:
        if verboseon == 1:
            print("Check 12: Failed")
            print("- Password contains sequential letter in uppercase")
    elif upperseqletter == 0:
        if verboseon == 1:
            print("Check 12: Passed")
        checkcount += 1
        strengthcount += twelve12
        
    for dictword in Thousand_Dict_Word:    
        if dictword in password:
            off_dict = []
            dictwords += 1
            off_dict.append(dictword)
    if dictwords > 0:
        if verboseon == 1:
            print("Check 13: Failed")
            print("- Password contains a common dictionary word")
            print(off_dict)
    elif dictwords == 0:
        if verboseon == 1:
            print("Check 13: Passed")
        checkcount += 1
        strengthcount += thirteen13
        
    for passlist in Thousand_Password:
        if passlist in password:
            off_pass = []
            thousandpass += 1
            off_pass.append(passlist)
    if thousandpass > 0:
        if verboseon == 1:
            print("Check 14: Failed")
            print("- Password contains a commonly used password")
            print(off_pass)
    elif thousandpass == 0:
        if verboseon == 1:
            print("Check 14: Passed")
        checkcount += 1
        strengthcount += fourteen14
    
    
    if 1 == 1:
        a_replace = password.rstrip('0123456789!@#$%^&*()')
        a_replace = a_replace.lower()
        a_replace = a_replace.replace('@','a')
        a_replace = a_replace.replace('3','e')
        a_replace = a_replace.replace('7','t')
        a_replace = a_replace.replace('0','o')
        a_replace = a_replace.replace('$','s')
        a_replace = a_replace.replace('1','l')
        a_replace = a_replace.replace('!','i')
        a_replace = a_replace.replace('2','z')
        if a_replace in Thousand_Password or a_replace in Thousand_Dict_Word:
            
            if verboseon == 1:
                print("Check 15: Failed")
                print ("-  LEET Spelling Conversion")
                print('-  Leet String: ' + str(a_replace))
        
        else:
            if verboseon ==1:
                print("Check 15: Passed")
            checkcount += 1
            strengthcount += fifteen15
    
    print('____________________')    
    print("Check Pass: " + str(checkcount) + "/15")
    print("Strength: " + str(strengthcount) + "/140")
    
    stop = timeit.default_timer()

    print('Time(Seconds): ', stop - start)
            
    
    
    
    badpassword[password]=strengthcount
    
#print(badpassword)
print("----------------------------------------------------")
sortedbad = sorted(badpassword.items(), key=lambda x: x[1])

with open('output.txt', 'w') as file:
     file.write(json.dumps(str(sortedbad)))
     #print(file.write(json.dumps(sortedbad)))
print("# of Passwords in List: " + str(len(sortedbad)))




 
            
            
        
            
     
        
        
    
        
        