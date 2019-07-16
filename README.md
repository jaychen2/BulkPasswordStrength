# BulkPasswordStrength.py
Jay Chen 07.16.2019

Test a bulk set of password against 15 different password checks.

1. Password Length
2. Capital Letters
3. Special Characters
4. Numbers
5. Birth Year
6. Lower letters
7. Repeating Numbers
8. Repeating Letters
9. Sequential Letters/Keyboard pattern
10. Seasons
11. Repeating Uppercase Letters
12. Sequential Uppercase Letters
13. Dictionary Words
14. Password List
15. Leet Mode (e.g. p@ssw0rd)



_________________________________________________________________________________
Bulk Password Strength Checker is inspired by NIST Special Publication 800-63B

NIST Special Publication 800-63B

2017 NIST Password Guidelines:

-An eight character minimum and 64 character maximum length

-The ability to use all special characters but no special requirement to use them

-Restrict sequential and repetitive characters (e.g. 12345 or aaaaaa)

-Restrict context specific passwords (e.g. the name of the site, etc.)

-Restrict commonly used passwords (e.g. p@ssw0rd, etc.)

-Restrict passwords obtained from previous breach corpuses
_________________________________________________________________________________


# Instructions:

1. Verbose Mode provides individual check information for each password. Turning verbose mode off will allow script to run faster.

Verbose Output Examples:
--------------------------------------------
A23456789
--------------------------------------------
Password Remaining: 6
Check 1: Passed
Check 2: Passed
Check 3: Failed
- Password does not contain a special letter
Check 4: Passed
Check 5: Passed
Check 6: Failed
- Password does not contain a lowercase
Check 7: Failed
- Password contains repeating/sequential numbers
Check 8: Passed
Check 9: Passed
Check 10: Passed
Check 11: Passed
Check 12: Passed
Check 13: Passed
Check 14: Failed
- Password contains a commonly used password
['6789']
Check 15: Passed
____________________
Check Pass: 11/15
Strength: 94.25/140
Time(Seconds):  0.7517054360000001

-----------------------------------------------------------------------------------

--------------------------------------------
P@ssw0rD
--------------------------------------------
Password Remaining: 4
Check 1: Passed
Check 2: Passed
Check 3: Passed
Check 4: Passed
Check 5: Passed
Check 6: Passed
Check 7: Passed
Check 8: Passed
Check 9: Passed
Check 10: Passed
Check 11: Passed
Check 12: Passed
Check 13: Passed
Check 14: Passed
Check 15: Failed
-  LEET Spelling Conversion
-  Leet String: password
____________________
Check Pass: 14/15
Strength: 137.5/140
Time(Seconds):  0.9247584329999999

------------------------------------------------------------------

*Password Strength is still being tuned* 

2. Add additional words to the 10000DictWord or 10000Passwords file to customize the comparison. 

3. Place the password list inside of passwordlist.txt

4. After the script has been completed, the password and strength values will be listed in output.txt

Output.txt results:

"[('123456789', 76.75), ('azazazazazazazazazaz', 87.5), ('Password', 93.0), ('security1', 93.0), ('A23456789', 94.25), ('YeloFire!', 113.0), ('P@ssw0rD', 137.5)]"


