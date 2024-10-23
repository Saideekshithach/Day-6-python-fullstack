Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#string methods
#len()
a="code"
len(a)
4
b="python course"
len(b)
13
c=" "
len(c)
1
c=""
len(C)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    len(C)
NameError: name 'C' is not defined. Did you mean: 'c'?
len(c)
0
#count
a="twinkle twinkle little star"
a.count("twinkle")
2
a.count("t")
5
a.count(" ")
3
#find a string
a="python"
a[1]
'y'
a.find("n")
5
a.find("y")
1
b="codegnan"
b.find("n")
5
b.find("code")
0
a="i am in class"
a.find("in")
5
a.find("e")
-1
#replace
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
a="wait wait until you succeed"
a.replace("wait","work")
'work work until you succeed'
a.replace("wait","work",1)
'work wait until you succeed'
#escape sequences
#\n->new line
#\t->tab space
a="name\nmobileno\tmailid\naddress"
print(a)
name
mobileno	mailid
address
b="name:Saideekshitha\nmobileno:7995002237\tmailid:saideekshithach@gmail.com"
b="name:Saideekshitha\nmobileno:7995002237\tmailid:saideekshithach@gmail.com"
print(b)
name:Saideekshitha
mobileno:7995002237	mailid:saideekshithach@gmail.com
#upper()
a="hello"
a.upper()
'HELLO'
a="HI"
a.lower()
'hi'
#lower
b="HI"
b.lower()
'hi'
a="python"
a[0].upper()
'P'
#capitalize()
a.capitalize()
'Python'
d="data science"
#title
d.title()
'Data Science'
b="i love python"
b.title()
'I Love Python'
fname="saideekshitha"
lname="ch"
print(fname+lname)
saideekshithach
print(fname+" "+lname)
saideekshitha ch
print(fname.title()+" "+lname.title())
Saideekshitha Ch
print((fname+" "+lname).title)
<built-in method title of str object at 0x000001B30B3D5D40>
print((fname+" "+lname).title())
Saideekshitha Ch
a="hello world"
a.isupper()
False
a.islower()
True
a.isdigit()
False
a.isalpha()
False
b="helloworld"
a.isaplha()
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean: 'isalpha'?
a.isalpha()
False
b.isalpha()
True
a="codegnan"
a.startswith("c")
True
a.endswith("n")
True
a.isalnum()
True
a="sai123"
a.isalnum()
True
a="sai@!23"
a.isalnum()
False
b=7890
b.isdigit()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    b.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
c="7890"
c.isdigit()
True
#split()
a="python java c c++"
a.split()
['python', 'java', 'c', 'c++']
b="i am in vja"
b.split()
['i', 'am', 'in', 'vja']
c="year 2024 month 10"
c.split()
['year', '2024', 'month', '10']
a="java c c++"
>>> b=a.split()
>>> b
['java', 'c', 'c++']
>>> b[0].upper()
'JAVA'
>>> b[0].capitalize()
'Java'
>>> b[1].capitalize()
'C'
>>> b[2].capitalize()
'C++'
>>> d=b[0]+b[1]+b[2]
>>> d
'javacc++'
>>> #join()
>>> a="python","java","ml","js"
>>> "".join(a)
'pythonjavamljs'
>>> " ".join(a)
'python java ml js'
>>> "css".join(a)
'pythoncssjavacssmlcssjs'
>>> d="codegnan@"
>>> "k".join(d)
'ckokdkekgknkaknk@'
>>> e="hello"
>>> "j".join()
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    "j".join()
TypeError: str.join() takes exactly one argument (0 given)
>>> f="hello "
>>> "j".join(f)
'hjejljljoj '
>>> e="hello"
>>> "j".join(e)
'hjejljljo'
