# BulkPasswordStrength

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

Bulk Password Strength Checker is inspired by NIST Special Publication 800-63B

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


Instructions:

Verbose Mode provides individual check information for each password. Turning verbose mode off will allow script to run faster.

Add additional words to the 10000DictWord or 10000Passwords file to customize the comparison. 

Place the password list inside of passwordlist.txt

After the script has been completed, the password and strength values will be listed in output.txt


