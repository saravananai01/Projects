'''#Hello World:

print("Welcome To You",sep=" ",end="\t")
print("Hello World")
print('Helo world welcome to you')

a=10;
b=50;
d=a+b;
print(d);

#Operators:

a=int(input("Enter Value A :"));
b=int(input("Enter Value B :"));
c=int(input("Enter Value C :"));
print("Your Value A Is     :",a);
print("Your Value B Is     :",b);
print("Your Value C Is     :",c);
print("Your Answer Is      :",a+b-c);

#If In Condition Using:

if a>b :
    print("A greter Than B");
else :
    print("B greter Than A");

#If Shoutcut Usings:

print("A greter Than B") if a>b else print("B greter Than A");

print("A greter Than B") if a>b else print("A And B Is Equal") if a==b else print("B greter Than A");

#If AND OR Condition Using:

if a>b and c>d :
    print("Both Condition Same");
if a>b or c>d :
    print("Any Condtion is True")


#Concatinate:
First_name=input("Enter Your First_name :");
Last_name=input("Enter Your Last_name   :");
print("Your First_name :",First_name);
print("Your Last_name  :",Last_name);
print(First_name + " " + Last_name);

#Tesing Usege String:
print(First_name.strip());
print(First_name.upper());
print(Last_name.lower());
print(First_name.title());
print(First_name.replace("S","s"));

#While Condition:

i=int (input("Enter Your Value I :"));

while i < 10:
    print (i)
    i += 1
    
#While Break Statement:

while i<20:
    print(i)
    if(i==20):
        break
    i +=1

#While Continue Statement:
    
while i<30:
    i += 1
    if (i==30):
        continue
    print(i)

#while else statement:
while i<20:
    print(i)
    i += 1
else:
    print("I Is longer Less Than 20")


#For Loop:
  #List[]:
fruits=(input("Enter Your Value I :")).split(",")
#fruits=["Apple","Banana","Cherry","Orange","lemon","Mango"]
for y in fruits:
    print(y)

for z in "Apple":
    print(z)

#fruits=(input("Enter Your Value I :")).split(",")
fruits=["Apple","Banana","Cherry","Orange","lemon","Mango"]
for x in fruits:
    if x == "lemon":
        break
    z=x.split(",")
    print(z)


fruits=(input("Enter Your Value I :")).split(",")
for x in fruits:
    if x == "banana":
        continue
    z=x.split(",")
    print(z)


#range:1
for x in range(10):
    print(x)

#range:2
for y in range(2,20):
    print(y)

#range:3
for x in range(3,40,4):
    print(x)

#range:4
a=int(input("Enter Your Number :"))
for x in range(a):
    print(x)
else:
    print("Finaly Finished")

color=["Red","Big","Tasty"]
fruits=["Apple","Banana","Cherry","Orange","lemon","Mango"]

for x in color:
    for y in fruits:
        print(x,y)

#fuction:
def my_fuction(f_name):
    print(f_name + "Std")

my_fuction("Zara ")
my_fuction("Darko ")
my_fuction("Ealini ")

def my_fuction(f_name,l_name):
    print(f_name + " " + l_name)

my_fuction("Zara","zyana")

#Particulare Name def_function:

def my_function(*kids):
    print("The yougest kids is " + kids[3])

my_function("Zara","Elanila","Vainavi","Eyalini")

def my_function1(kids1,kids2,kids3):
    print("The elder kids is " + kids2)
my_function1(kids1="zayana",kids2="Vainavi",kids3="Eyalini")

def my_function(x):
    return 5 + x
print(my_function(6))
print(my_function(8))
print(my_function(9))

    #Array:

bike=["Duke","Mt-15","R15"] 
x1=len(bike)
print(x1)

bike1=["BMw","Duke","Mt-15","R15"]
for x in bike1:
    print(x)
number=[1,0,9,7,5,2,4,8,6,3]
bike2=["BMw","Duke","Mt-15","R15","Hero","Honda"]
bike_name=["Hero","Honda"]
bike2.append("Pulsur")
bike2.pop(1)
bike2.insert(4,"Pulsur")
bike2.remove("Duke")
bike2.clear()
bike_copy=bike2.copy()
x=bike2.count("Duke")
bike2.extend(bike_name)
index = bike2.index("BMw")
bike2.reverse()
number.sort()
number.sort(reverse=True)
print(number)

Number1=input("Enter Your Number : ").split(",")
Number2=input("Enter Your Number : ").split(",")
Number1.append(0)
Number2.clear()
x=Number1.copy()
print(Number1)'''

    #Class:
 #without ___str___ function:
class std_name:
    def __init__(self,name,age,address):
        self.stname=name
        self.stage=age
        self.staddress=address
s1=std_name("Saravanan",20,"Peravurani")
print(s1.stname)
print(s1.staddress)
print(s1.stage)


class cstname:
    def __init__(self,name,age):
        self.csname=name
        self.csage=age

    def __str__(self):
        return f"{self.name}({self.csage})"
    s1.