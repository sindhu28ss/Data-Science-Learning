#integer
x<-2L
typeof(x)

#double
y<-2.5
typeof(y)

#complex
z<-3+2i
typeof(z)

#character
a<-"h"
typeof(a)

#logical
q1<-T
typeof(q1)

q2<-F
typeof(q2)

#Arithmetic operations:
a<-10
b<-5
c<-a+b
c

#variables
var1<-2.5
var2<-4
result<-var1/var2
result

answer<-sqrt(4)
answer

greeting<-"Hello"
name<-"Bob"
message<-paste(greeting,name)
message

#Logical operators
#True T
#False F

4<5
10>100
4==5

result<-4<5
result
typeof(result)

result2<-!T
result2

result | result2
result & result2

isTRUE(result)

#While loop

while(FALSE){
  print("Hello World")
}

while(TRUE){
  print("Hello World")
}

counter<-1
while(counter<12){
  print(counter)
  counter=counter+1
}

#for loop
for(i in 1:5){
  print("Hello World")
}

for(i in 5:10){
  print("Hello World")
}

#if statements-if else block
# remove objects from a specified environment
rm(answer) 
x<-rnorm(1)
if(x>1){
  answer<-"Greater than 1"
}else{
  answer<-"Less than or equal to 1"
}

#Nested
rm(answer) 
x<-rnorm(1)
if(x>1){
  answer<-"Greater than 1"
}else{
  if(x>=-1){
    answer<-"Between -1 and 1"
  }
  else{
    answer<-"Less than -1"
  }
}

#chaining statements

rm(answer) 
x<-rnorm(1)
if(x>1){
  answer<-"Greater than 1"
}else if(x>=-1){
  answer<-"Between -1 and 1"
}else{
  answer<-"Less than -1"
}
  

















