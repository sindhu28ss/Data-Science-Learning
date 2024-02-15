#Matrices
?matrix

my.data<-1:20
my.data

#matrix(data = NA, nrow = 1, ncol = 1, byrow = FALSE,
#dimnames = NULL)
A<-matrix(my.data,4,5)
A
A[2,3]

B<-matrix(my.data,4,5,byrow=T)
B
B[2,5]

#rbind()-binds vectors into matrix row by row
r1<-c("I","am","Happy")
r2<-c("what","a","day")
r3<-c(1,2,3)

c<-rbind(r1,r2,r3)
c

#cbind()-binds vectors into matrix column by column
c1<- 1:5
c2<- -1:-5

d<-cbind(c1,c2)
d



