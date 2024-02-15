MyFirstVector<-c(3,45,56,732)
MyFirstVector
is.numeric(MyFirstVector)
is.integer(MyFirstVector)
is.double(MyFirstVector)

v2<-c(3L,12L,243L,0L)
v2
is.numeric(v2)
is.integer(v2)
is.double(v2)

v3<-c("a","b23","Hello")
v3
is.character(v3)
is.numeric(v3)

#R converts int to char datatype
v3<-c("a","b23","Hello",7)
v3
is.character(v3)
is.numeric(v3)

#sequence
seq(1,15)
1:15
seq(1:15)
seq(1,15,2)
z<-seq(1,15,2)
z<-seq(1,15,4)

#replicate
rep(3,50)
d<-rep(3,50)
rep("a",5)
x<-c(80,20)
y<-rep(x,10)
y

#3 ways of creating vectors
x<-c(1,123,534,12,3) #combine
y<-seq(201,250,11)#sequence
z<-rep("Hi!",3)#replicate

#using the [] brackets:
w<-c("a","b","c","d","e")
w[1] #gives 1st element
w[3] #gives 3rd element
w[-1] #gives all but 1st element, omits 1st one
v<-w[-2] #gives all but 2nd element, omits 2nd one
v
w[1:3] #gives 1st to 3rd element
w[3:5] #gives 3rd to 5th element
w[c(1,3,5)] #gives 1st,3rd &5th element
w[c(-2,-4)] #omits 2nd nand 4th element alone
w[-3:-5] #omits 3rd to 5th element

#vectorized operations:
x<-rnorm(5)
x
for(i in x){
  print(i)
}

N<-100
a<-rnorm(N)
b<-rnorm(N)
c<-a*b


