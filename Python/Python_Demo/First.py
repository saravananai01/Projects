#Hello World:

print("Hello World");
print("Welcome To Saravanan");
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
fruits=["Apple","Banana","Cherry","Orange","lemon","Mango"]
for y in fruits:
    print(y)

for z in "Apple":
    print(z)

fruits=["Apple","Banana","Cherry","Orange","lemon","Mango"]
for x in fruits:
    if x == "lemon":
        break
    print(x)

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
 