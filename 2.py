Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=True
>>> type(x)
<class 'bool'>
>>> y=False
>>> type(y)
<class 'bool'>
>>> strl="String"
>>> print(str1)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    print(str1)
NameError: name 'str1' is not defined
>>> print(strl)
String
>>> str2="String"
>>> print(str2)
String
>>> str3="String"
>>> str2="Day's"
>>> print(str2)
Day's
>>> str2="Day"s'
SyntaxError: invalid syntax
>>> print("This is a (\\)   backslash mark")
This is a (\)   backslash mark
>>> print("This is a (\t) tab key)
      
SyntaxError: EOL while scanning string literal
>>> print("This is a (\t) tab key")
This is a (	) tab key
>>> print("These are \"single quotes\"")
These are "single quotes"
>>> string1="PYTHON TUTORIAL"
>>> print(string1[0])
P
>>> print(string1[-15])
P
>>> print(string1[14])
L
>>> print(string1[-11])
O
>>> print(string1[16])
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(string1[16])
IndexError: string index out of range
>>> string1[0]
'P'
>>> 'Z'in string1
False
>>> 'P'in string1
True
>>> tup1=(0,-1,12,212.23,100)
>>> type(tup1)
<class 'tuple'>
>>> print(tup1)
(0, -1, 12, 212.23, 100)
>>> tup2=('Red','Black',2000,"White")
>>> print(tup2)
('Red', 'Black', 2000, 'White')
>>> tup3="a1","b1","c1","d1"
>>> type(tup3)
<class 'tuple'>
>>> print(tup3)
('a1', 'b1', 'c1', 'd1')
>>> empty_tup1=()
>>> print(empty_tup1)
()
>>> single_tup1=(100,)
>>> print(single_tup1)
(100,)
>>> tup2=("Red","Black",2000,12.12)
>>> print(tup2[0])
Red
>>> tup[2]="White:
SyntaxError: EOL while scanning string literal
>>> tup[2]="White"
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    tup[2]="White"
NameError: name 'tup' is not defined
>>> print(tup2[0])
Red
>>> print(tup2[1:2])
('Black',)
>>> tup1=(1,2,3)
>>> tup2(4,5,6)
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    tup2(4,5,6)
TypeError: 'tuple' object is not callable
>>> tup2=(4,5,6)
>>> tup3=(7,8,9)
>>> tup_123=tup1+tup2+tup3
>>> print(tup_123)
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> print(tup1*4)
(1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
>>> my_list1=[5,12,13,14]
>>> print(my_list1)
[5, 12, 13, 14]
>>> my_list2=['red','blue','black','white']
>>> print(my_list2)
['red', 'blue', 'black', 'white']
>>> my_list=[]
>>> print(my_list)
[]
>>> color_list=["RED","BLUE","GREEN","BLACK"]
>>> color_list[0]
'RED'
>>> color_list[-1]
'BLACK'
>>> print(color_list[4])
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    print(color_list[4])
IndexError: list index out of range
>>> print(color_list[1:-2]

      
[DEBUG ON]
>>> 
[DEBUG OFF]
>>> print(color_list[:])
['RED', 'BLUE', 'GREEN', 'BLACK']
>>> pd={"class":"V","section":'A',"roll_no":12}
>>> print(pd["class"])
V
>>> print(pd["section")]
SyntaxError: invalid syntax
>>> print(pd)
{'class': 'V', 'section': 'A', 'roll_no': 12}
>>> 
