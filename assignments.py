#code 1
a =int(input('enter a number : '))
b=int(input('enter a number : '))
print(f"The sum is : {a+b} \nThe product is {a*b}")

#code 2
num=int(input("enter a  number : "))
print(f'The sum of {num} and {num+1} is {2*num+1}')


#code 3
string_1=(input('enter the string that you wanted to : '))
char_1=(input('enter the character '))
for i in string_1:
    if i==char_1:
        print(string_1)
else:
    print(f'the char is not found  ...unable to print the string :( ')

#code 4
list =[int(i) for i in input('enter the list elements').split()]
if list[1]==list[-1]:
    print('the first and last elements are same ... ')

#code 5
def even(a):
    if a%2==0:
        return True
    else:
        return False
list =[int(i) for i in input('enter the list elements').split()]
for i in list:
    if even(i):
        print(i)

#code 6
def adding(string,oringall):
    temp = oringall[:len(oringall)//2]
    remaing =oringall[len(oringall)//2:]
    print(str(temp)+str(string)+str(remaing))
a = input('enter the string : ')
b = input('enter the string to be add in the mid : ')
adding(b,a)

#code 7

a =int(input('enter a number : '))
b=int(input('enter a number : '))
min = a if a < b else b
for i in range (min,0,-1):
    if(a%i==0 and b%i==0):
        print(f'the LCM id {i}')
        break
#code 8
year =int(input('enter the year :'))
if (year % 400 == 0) and (year % 100 == 0):
    print(f"{year} is a leap year")

elif (year % 4 ==0) and (year % 100 != 0):
    print(f"{year} is a leap year")
else:
    print('it is not a leap year')       



#code 9
word = input('Enter the string')
vow =["a","e","i","o","u"]
for i in word:
    if(i in vow):
        pass
    else:
        print(i,end="")     


#code 10
value=input("enter the string : ")
set_1=set(value)
print(set_1)  

#code 11
def sharon(a,b):
    sets_1 =set(a)
    sets_2 =set(b)
    if sets_1 == sets_2:
        print("the values are same in both the list")
list_1 =[int(i) for i in input('enter the list elements').split()]
list_2 =[int(i) for i in input('enter the list elements').split()]


#code 12
my_list =[int(i) for i in input('enter the list elements').split()]
a=int(input("enter the elements that yopu want to add : "))
inddex=int(input("enter the indices"))
my_list.insert(a,inddex)


#code 13
Rotate_list =[int(i) for i in input('enter the list elements').split()]
shift =int(input("enetr the rotete value : "))
print(f"{Rotate_list[shift:]+Rotate_list[:shift]}")