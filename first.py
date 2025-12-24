num=30
bro=num +2
print("bro=",bro)
#arithematic operator
a=5
b=2
print(a-b)
print(a+b)
print(a*b)
print(a%b)#its a modeule operator to arise remainder from values
print(a/b)
print(a**b)# this a power operator a^b
#relational/comparision operator
print("relatonal operator")
d=10
c=5
print(d==c)
print(d>c)
print(c>d)
print(d!=c)
print(c<=d)
#assimengt operator
print("assimenght operator")
f=20
f+=20
print(f)
f-=20
print(f)
f*=20
print(f)

f/=20
print(f)
f%=20
print(f)
#logical operator
a=50
b=30
print(not a<b)
print(not a>b)#not opperator is go opposite of the instructon here see example when i say to it that a>b then it return to me false print(not a>b)
value1=True
value2=True
print(value1 and value2)#and operator is true when both value is true
#type conversion 
print("type conversion")
a=2
b=4.25
sum=a+b
print("sum is =",sum)
print("type casting")
#type casting 
a="24"
b=2
c=int(a)
#c=float(a)
sum=b+c
print(sum)

#name= input("enter your a name: ") 
#print("you have enterd",name)
#c=input("enter value of c:")
#print("value of c is:",c)here take string value instead of another
print("here is another discussion of values")#this topic that how we get data from user then we use it (datatypes(input))
e=int(input("enter value of e:"))
f=int(input("enter value of f:"))
sum=e+f
print("the sum of ef =",sum)
print("subtraction below")
sub=e-f
print("the subtraction of ef =",sub)
mul=e*f
print("the multiply of ef =",mul)
print("our next topic is strings")#here how we decleare string and escape sequence
str1="basit is a good boy .\n he work daily on time"
str1="basit is a good boy ." +"he work daily on time"
print(str1)
print(len(str1))
print("what is index")#today topic is index
str2="abdul basit khan"
print(str2[10])
print("Slicing topic(which means accessing parts of a strings)")#strings ko parts ma kar na str[starting_index :ending_index]ending indx is not include
print(str2[0:9])
#negative index 
str3="basit khan"
print(str3[-8:-1])
print("String Function")#string Function
basit="basit khan is a good boy"
print(basit.endswith("boy"))# ya string batha tha hA KA USKA AKHRI string kiya agar akhri string par kho aur sa hi bi tho true otherwise not
print(basit.capitalize())#write first character is large
print(basit.replace("a","e"))#jab ham kisi chiz ko change kara kisi dusri chiz par
print(basit.find("o"))#kis jiz ko find karna ka kis jaga per para ha (means value ki ja ga maloom karna)
print(basit.count("a"))#count kar na ka kithini bar ha 
