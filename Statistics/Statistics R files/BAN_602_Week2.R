## BAN 602 - Week 2 ##
## Introduction to R ##

ls()
rm(list=ls(all=TRUE)) 

setwd("/Users/sindhujaarivukkarasu/Desktop/R files")

# R as calculator
7+10
67.1*11
5/7

# Vectors
c(5, 8, 100) + c(3, 1, 7)
c(5, 7, 10)*c(2, 4, 3)

c(5, 8, 100) + c(3, 1)
c(5, 7, 10)*c(2, 4)

# Built-in Functions
1/sqrt(2*pi) * exp(-2)
dnorm(0)

# Built-in Help
help(dnorm)
help.search('normal distribution')
?dnorm
??'normal distribution'

# Functions
log(10)
10 + 5

#Variable Names and Assignments
name<- "Vince"
height <- 66
height
name
height %/% 12 # integer division
height %% 12 # modulus

# Data Types
5.4
10/3
1/3
10 < 15
10 > 15
'v'
"Statistics is cool"

# Data Structures
x <- 5
x
typeof(x)
is.vector(x)

x <- c('apples', 'oranges', 'bananas')
x
print(x)
length(x)
typeof(x)

# Sequence
i <- 1:10
print(i)
j <- seq(1,10,2)
j
j <- seq(100,10,-2)
j

# Indexing
x <- c('lions', 'tigers', 'bears', 'oh my!')
x
x[1]
x[length(x)]
x[-2]
x[1:2]
x[c(2,4)]
x[-(1:2)]
x <- c(57, 'columbus', 1.56)
is.vector(x)
typeof(x)
x<- c(5, 10, NA, 13)
print(x)
is.na(x)

# Boolean Indexing
x<-c(1,5,7)
x[c(TRUE, FALSE, TRUE)]
student <- c("bob", "alice", "john", "mary")
gender <- c('M', 'F', 'M', 'F')
student[gender=='M']

fruits <- c('apple', 'oranges', 'banana', 'cherry')
vegetables <- c('broccoli', 'carrot', 'asparagus', 'onion')
refrigerator <- c('apple', 'carrot', 'cheese')
refrigerator %in% fruits
refrigerator[refrigerator %in% fruits]

rnorm(n=10, sd=10)

# Matrix
x <- matrix(1:9, nrow=3, ncol=3)
x
x[2,3]
x[3,]
x[,3]

#Array
x <- array(1:12, dim=c(2,3,2))#sequence of integers from 1to 12,3 rows,2 col
x
x[2, 3, 1]

#List
my_distribution <- list('normal', 0, FALSE)
print(my_distribution)

my_distribution[1:2]

typeof(my_distribution[2])
typeof(my_distribution[[2]])
my_distribution[[2]]+10

names(my_distribution) <- c('family', 'mean', 'is.symmetric')
names(my_distribution)
print(my_distribution)

my_distribution[[2]]
my_distribution['is.symmetric']
my_distribution$family

another_distribution <- list(family = 'gaussian', mean=7, sd=1, is.symmetric=TRUE)
another_distribution
another_distribution$family

# Data frames
df <- data.frame(student = c('bob', 'alice', 'john', 'mary'), score=c(70, 90, 85, 100))
print(df)
nrow(df)
ncol(df)
dim(df)
df[1,]
levels(df[,1])
df$score

# Indexing by names
colnames(df)
attributes(another_distribution)
x <- c(john=10, bob=3, alice=7)
x
x[c('john', 'alice')]

x <- matrix(1:12, nrow=4, ncol=3)
rownames(x) <- c('john', 'alice', 'bob', 'mike')
colnames(x) <- c('homework', 'exam', 'final')
x['john',]

x['alice', 'final']

# Reading Dataset
setwd("/Users/sindhujaarivukkarasu/Desktop/R files")
babies <- read.csv(file="Babies.csv", header = TRUE)
str(babies)
head(babies)
tail(babies)

# Summary Statistics
summary(babies)
mean(babies$bwt)
sd(babies$age)
var(babies$height)
median(babies$weight)
quantile(babies$bwt)
range(babies$bwt)
max(babies$age)
min(babies$age)

cov(babies$height, babies$weight)
cor(babies$height, babies$weight)

# Transforming Dataframe
babies <- transform(babies, bmi=weight/height^2 * 708, preterm = gestation < 37*7)
babies$smoke[babies$smoke == 9] <- NA
babies$smoke <- as.logical(babies$smoke)

# Cross tabulation
x <- table(babies$smoke, babies$preterm)
x
babies <- transform(babies, smoke = factor(smoke, levels = c(FALSE, TRUE), labels=c('non-smoking', 'smoking')), 
                    preterm = factor(preterm, levels = c(FALSE, TRUE), labels=c('normal', 'preterm')))
babies

x <- table(babies$smoke, babies$preterm)
x
margin.table(x, 1)
margin.table(x, 2)

prop.table(x, 1)
prop.table(x, 2)

# Histogram
hist(babies$bwt, breaks = c(40, 70, 100, 130, 160, 190), xlab="Birth Weight", main = "Histogram of Birth Weight")

#Boxplot
boxplot(babies$height, horizontal = T, main="Boxplot", xlab="Height")

# Bar Chart
barplot(x, beside=T, legend.text = c('non-smoking', 'smoking '))

# Pie Chart
pie(x, labels = c("Normal-Non-smoking", "Normal-Smoking", "Preterm-Non-Smoking", "Preterm-Smoking"), col=c("red","green", "blue", "yellow"), main="Pie Chart")

#Scatter Plot
plot(babies$bwt, babies$gestation, xlab = "Baby Weight", ylab="Gestation Period", main="Scatter Plot")
abline(lm(gestation ~ bwt, data = babies), col = "red")

