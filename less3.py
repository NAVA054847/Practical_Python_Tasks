import re
import os
from re import search

# pattern = r'\d+'
# text = "יש לי 3 תפוזים ו-2 תפוחים"
# result = re.findall(pattern, text)
# print(result)
#
# #פלט
# #['3', '2']
# print("---------------")
# # ביטוי רגולרי שיתאים למספר טלפון ישראלי בפורמט הבא: 05X-XXXXXXX( כשה-X הם ספרות).
#
# contain=re.compile(r'05\d\-\d\d\d\d\d\d\d')
# p=contain.search("059ם7172267")
# print(p)
#
# print("---------------")
# #השתמשי בפונקציה re.sub(), לכתוב קוד שמחליף את כל התווים מיוחדים בטקסט (בפרט: !, @, #) ברווחים.
#
# s="nv!@jhh;#"
# n=re.sub(r'[!@#]'," ",s)
# print(n)
#
# print("---------------")
# s = "aba Agjg Vkhk is Nice"
# a = re.compile(r'\b[A-Z]')  # מוצא אות גדולה בתחילת כל מילה
# v = a.findall(s)
# print(v)
#
# print("---------------")
# # את השאלה הזאת עשיתי עם הGpt כי לא ידעתי את הביטוי הרגולרי הנכון, בדקתי איתו אחרי שנסתי ולא הצלחתי
# text="nava le leder"
# pattern = r'\b[A-Za-z]{3,}\b(?:\s+\b[A-Za-z]{3,}\b)*'
# print (re.findall(pattern, text))


print("------------------------------------------")


3
os.chdir(r'C:\Users\USER\PycharmProjects\honework\שולחן העבודה\newpacket\p1\p2')
with open("myfile.txt", "w") as f:
    f.write("Hello, world!")
with open("myfile1.txt", "w") as f1:
    f1.write("Hello, world 1!")


4

temp=str(os.stat(r'C:\Users\USER\PycharmProjects\honework\שולחן העבודה\newpacket\p1\p2\myfile.txt').st_size)
t=temp+".txt"
t1="myfile.txt"


print(t1)
print(t)

try:
 os.rename(t1, t)
except:
    print("problem")


#5
list1=os.listdir(r'C:\Users\USER\PycharmProjects\honework')
[print(os.stat(m).st_size) for m in list1 if  (os.stat(m).st_size)>300 ]



