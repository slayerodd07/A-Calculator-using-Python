'''
This is a basic calculator that I created which only deals with non negative integers.
This calculator can perform addition(+),subtraction(-),multiplication(*),division(/),
square root(sqrt), find the remainder(%),find the power(^),find the factorial(!) and 
find the log(log).To perform the required operation, the user must input a and b as 
non-negative integers and input the operators(given inside the parentheses for respective 
operations in the previous sentence) according to the choice.If a and b are not integers
the program will return 'None' and nothing will happen.

It is to be mentioned that,in case of finding the power, this calculator will always 
return a**b. And for operations that requires only one value to work with(factorial,
square root), the user must input b as zero.Otherwise the program will not work.Besides,
the log operation returns the value of log of a with the base of b.

It is noted that the result is stored in a text file called 'cps109_a1_output.txt' 
and then displayed.To keep the history of previous calculations, the user must input 
'Yes' for history. If the user inputs 'No', only the final result will remain in the 
output file. If anything other than 'Yes' or 'No' is selected no calculations will be 
conducted and nothing will be added to the output file.In this case, 'None' will be 
displayed as a result regardless of what the inputs are.This is also true for when the 
inputs are wrong.

Some examples of input and output are given below:
eg 1. Input :
        a:2
        b:4
        operator:'+'
        history : 'Yes'
     Output:
        6
eg 2. Input:
        a:-2
        b:5
        operator:'-'
        history: 'No'
      Output:
          Your inputs must be non-negative
eg 3. Input:
        a:400
        b:2
        operator:'^'
        history: 'No'
      Output:
          160000
eg 4. Input:
        a:4
        b:0
        operator:!
        history: 'Yes'
      Output:
          24
eg 5. Input:
        a:5
        b:4
        operator:'*'
        history: 'dahsjdhj'
      Output:
          None
eg 6. Input:
        a: abc
        b: 5.4
        operator:'+'
        history: No
      Output:
          None
N.B: Please note that the output of the last test according to the screenshot should be 
in the output text file when the checker will attempt their first test.

'''
#I created a user defined function to find power
def power(x,y):
    p = 1
    if y==0:
        return p
    else:
        for i in range(y): 
#for loop is used to find the answer
            p = p*x
        return p
     
def factorial(z):
    i = 1
    f = 1
#while loop is used to find factorial
#z+1 is taken as i=1 and I want the number itself to multiply with f
    while i<z+1:
        f = f*i
        i = i+1
    return f

#this user defined function (writing) is used to write to an output file
def writing(x):
    with open('cps109_a1_output.txt','w') as f:
        f.write(x)
#the output file is read after writing to display the result
    with open('cps109_a1_output.txt','r') as r:
        return r.read()
#the user defined function (appending) adds to output file keeping the history
def appending(x):
    with open('cps109_a1_output.txt','a') as a:
        x = '\n'+ x
        a.write(x)
#the last line of the output file is read and returned to display the latest result
    with open('cps109_a1_output.txt','r') as r:
        last_line = r.readlines()[-1]
        return last_line
    

def calculator(a,b,operator,history):
#math is imported to be used later
    import math
#creating a list with valid operators
    operators = ['+','-','*','/','%','^','sqrt','!','log']
#a,b must be integer and history must be a string
    if type(history)!=str:
        return None 
    try:
        float(a)-int(a)==0 
        float(b)-int(a)==0 
    except:
        return None
    a=int(a)
    b=int(b)
    
#the calculator only deals with non-negative integers
    if a<0 or b<0:
        x = 'Your inputs must be non-negative'

    else:
#checking if the operator is valid
        if operator in operators:
            if operator == '+':
                x=str(a+b)
            if operator == '-':
                x=str(a-b)
            if operator == '*':
                x=str(a*b)
            if operator == '/':
#try and except method prevents the program to face error if denominator is zero
                try:
                    x=str(a/b)
                except:
                    x='Please review your inputs'
            if operator == '%':
#if try and except was not used,the program would crash when denominator is zero
                try:
                    x=str(a%b)
                except:
                    x='Please review your inputs'
            if operator == '^':
#the calculator has a limit to calculate power and factorials
                if a<=10000 and b<=10000:
#the result is called from the power function previously stated
                    x=str(power(a,b))
                else:
                    x='Sorry, your inputs are too big for us'
            if operator == 'sqrt':
#one of  the conditions of the calulator to find square root or factorial is b=0
                if b!=0:
                    x='Please review your inputs'
                else:
                    x=str(math.sqrt(a))
            if operator == '!':
                if b!=0:
                    x='Please review your inputs'
                else:
                    if a<=10000:
                        x=str(factorial(a))
                    else:
                        x='Sorry,the input is too big for us'
            if operator == 'log':
                try:
                    x=str(math.log(a,b))
                except:
                    x='Your input is not valid'
        else:
            x='We cannot complete your operation'
#the output file is updated according to the choice of user
#the result is returned
    if history.lower()=='yes':
        return appending(x)
    if history.lower()=='no':
        return writing(x)
    
        
#taking the inputs from the user
a = input('Enter your first non-zero integer,a: ')
b = input('Enter your second non-zero integer,b: ')
operator = input('Enter a valid operator: ')
history = input('Do you want to keep your history?: ')
print(calculator(a, b, operator,history))
    
