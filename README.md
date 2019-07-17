# BulkPasswordStrength.py
Jay Chen 07.16.2019

Requirements:
* Download all of the files listed in the repo.
* 10000DictWord.txt, 10000Passwords.txt, output.txt, passwordlist.txt

Test a bulk set of password against 15 different password checks.

1. Password Length (e.g. Less than 8/More than 64)
2. Capital Letters (e.g. A-Z)
3. Special Characters (e.g. !@#$%^&*() )
4. Numbers (e.g. 0-9)
5. Birth Year (e.g. 1900 - 2100)
6. Lower letters e.g. a-z)
7. Repeating Numbers (e.g. 111 ,222, 333, 123 , etc.)
8. Repeating Letters (e.g. aaa, bbb, ccc)
9. Sequential Letters/Keyboard pattern (e.g. abc, cbd, qwerty, qaz, etc.)
10. Seasons (e.g. Spring, Summer, Fall, Winter)
11. Repeating Uppercase Letters (e.g. AAA, BBB, CCC)
12. Sequential Uppercase Letters (e.g. ABC, BCD, QAZ, etc.)
13. Dictionary Words (10,000 Most Common Dictionary Words)
14. Password List (10,000 Most Common Passwords)
15. Leet Mode (e.g. p@ssw0rd)

- Passwords are standardized to check for common dictionary words and common passwords by removing trailing numbers and special chars.



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

**A23456789**

Password Remaining: 6
* Check 1: Passed
* Check 2: Passed
* Check 3: Failed
-Password does not contain a special letter
* Check 4: Passed
* Check 5: Passed
* Check 6: Failed
-Password does not contain a lowercase
* Check 7: Failed
-Password contains repeating/sequential numbers
* Check 8: Passed
* Check 9: Passed
* Check 10: Passed
* Check 11: Passed
* Check 12: Passed
* Check 13: Passed
* Check 14: Failed
-Password contains a commonly used password
['6789']
* Check 15: Passed
____________________
* Check Pass: 11/15
* Strength: 94.25/140
* Time(Seconds):  0.7517054360000001

-----------------------------------------------------------------------------------


**P@ssw0rD**

Password Remaining: 4
* Check 1: Passed
* Check 2: Passed
* Check 3: Passed
* Check 4: Passed
* Check 5: Passed
* Check 6: Passed
* Check 7: Passed
* Check 8: Passed
* Check 9: Passed
* Check 10: Passed
* Check 11: Passed
* Check 12: Passed
* Check 13: Passed
* Check 14: Passed
* Check 15: Failed
-LEET Spelling Conversion
-Leet String: password
____________________
* Check Pass: 14/15
* Strength: 137.5/140
* Time(Seconds):  0.9247584329999999

------------------------------------------------------------------

**Password Strength is still being tuned** 

2. Add additional words to the 10000DictWord or 10000Passwords file to customize the comparison. 

3. Place the list of the password you want to check inside of passwordlist.txt

4. After the script has been completed, the password and strength values will be listed in output.txt

Output.txt results:

"[('123456789', 76.75), ('azazazazazazazazazaz', 87.5), ('Password', 93.0), ('security1', 93.0), ('A23456789', 94.25), ('YeloFire!', 113.0), ('P@ssw0rD', 137.5)]"


