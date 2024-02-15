# BAN 602 Week 4 Lecture 2 #

## Example: Metro EMS

alpha <- .05 
xbar <- 13.25           # sample mean 
mu0 <- 12               # hypothesized value 
sigma <- 3.2            # population standard deviation 
n <- 40                 # sample size 
z <- (xbar-mu0)/(sigma/sqrt(n)) 
z

# Using p-value
pval <- pnorm(z, lower.tail = FALSE)  # Upper tail becasue this is an upper tail test
pval
if(pval <= alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

# Using critical value
z.alpha <- qnorm(1-alpha) 
z.alpha 
if(z >= z.alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}


## Example: Glow Toothpaste
alpha <- .03 
xbar <- 6.1             # sample mean 
mu0 <- 6                # hypothesized value 
sigma <- 0.2            # population standard deviation 
n <- 30                 # sample size 
z <- (xbar-mu0)/(sigma/sqrt(n)) 
z

# Using p-value
if(z>=0){
  pval <- 2*pnorm(z, lower.tail = FALSE)    # upper tail 
} else {
  pval <- 2*pnorm(z)    # lower tail 
}
pval
if(pval <= alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

# Using critical value
z.alpha.by.2 <- qnorm(1-alpha/2)
z.alpha.by.2
if(z >= z.alpha.by.2 | z <= -z.alpha.by.2){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

## Example: Highway Patrol
alpha <- 0.05 
xbar <- 66.2             # sample mean 
mu0 <- 65                # hypothesized value 
s <- 4.2                 # sample standard deviation 
n <- 64                  # sample size 
t <- (xbar-mu0)/(s/sqrt(n)) 
t

# Using p-value
pval <- pt(t, lower.tail = FALSE, df=n-1)  # Upper tail becasue this is an upper tail test
pval
if(pval <= alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

# Using critical value
t.alpha <- qt(1-alpha, df=n-1) 
t.alpha 
if(t >= t.alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

## Example: National Safety Council 

alpha <- 0.05
pbar <- 67/120          # sample proportion 
p0 <- .5                # hypothesized value 
n <- 120                # sample size 
z <- (pbar-p0)/sqrt(p0*(1-p0)/n) 
z  
# Using p-value
if(z>=0){
  pval <- 2*pnorm(z, lower.tail = FALSE)    # upper tail 
} else {
  pval <- 2*pnorm(z)    # lower tail 
}
pval
if(pval <= alpha){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}
# Using critical value
z.alpha.by.2 <- qnorm(1-alpha/2)
z.alpha.by.2
if(z >= z.alpha.by.2 | z <= -z.alpha.by.2){
  print("Reject Null")
} else {
  print("Fail to Reject Null")
}

## Example: Market Research Associate
res <- prop.test(x = c(120, 60), n = c(250, 150), alternative = "greater", conf.level = 0.95, correct = FALSE)
res
