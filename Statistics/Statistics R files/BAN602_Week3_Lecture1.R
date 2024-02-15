## BAN 602 - Week 3 Lecture 1 ##


## Random sampling 5 numbers from a set of 1 to 40
sample(1:40,5)

## Modeling coin toss
sample(c("H", "T"), 10, replace=T)
?sample
## With unequal probabilities
sample(c("success", "failure"), 10, replace=T, prob=c(0.2, 0.8))

## For combination: N choose n
choose(10, 2)

## Function to compute permutation/combination
perm = function(n, x) {
  factorial(n) / factorial(n-x)
}

comb = function(n, x) {
  factorial(n) / factorial(n-x) / factorial(x)
}

## Call the functions just created
perm(10, 2)
comb(10, 2)

## Creating Normal density distribution and plotting it
x <- seq(-4,4,0.1)
plot(x,dnorm(x),type="l")
curve(dnorm(x), from=-4, to=4)

#Compute the value of probability for a normal dist with mu=0, sd=1, x=0
dnorm(0, mean = 0, sd = 1)

# Probability of z-score=3
dnorm(3)

## Creating a binomial distribution and plotting it
x <- 0:50
plot(x,dbinom(x,size=50,prob=.33),type="h")

x <- 0:15
plot(x,dpois(x,lambda = 10),type="h")

x <- 0:15
plot(x, dhyper(x, 20, 50, 15),type="h")



## Using Cumulative distribution function
## Probability of getting a value of 160 or more from a normal distribution with mean 132 and sd 13
## (pnorm returns the integral from -infinity to the value specified in the pnorm function)

## lower.tail = F gets us the area under the bell curve on the right side of x=160
pnorm(160,mean=132,sd=13, lower.tail = F)
1-pnorm(160,mean=132,sd=13)

ppois(10, lambda=12)

phyper(5, 20, 50, 15)

# Plot CDF of normal dist

z_scores <- seq(-3, 3, by = .1)
pvalues <- pnorm(z_scores)
plot(pvalues, type = "l", main = "CDF of the Standard Normal Distribution", xlab= "Quantiles", ylab="Probability Density") 

# Probability of getting 16 or more successes in 20 trials of a binomial with probability of success being 0.5
1-pbinom(15,size=20,prob=.5)

1-pexp(2, rate=1/3)

# qnorm() is the inverse of pnorm(): It gets us the z-score of the pth quantile of the normal distribution
## what is the z-score corresponding to the 99.87th percentile of standard normal distribution
qnorm(.9987)
10000/qnorm(0.975)
qnorm(pnorm(3))

qbinom(0.2, 10, 1/3)
qpois(0.8, 12, lower.tail=F)
qpois(0.2, 12, lower.tail=T)
## Generate random numbers from a distribution: first set a seed to replicate the random numbers later
set.seed(1-29-2020)
# Generate five random numbers from a standard normal distribution
rnorm(5)

## Generate 100 random numbers from the normal distribution with mean 70, sd=5 and plot them in a histogram
observations <- rnorm(100, mean = 70, sd = 5)
hist(observations, breaks = 20)

#Generate 10 random numbers (number of successes) from a binomial distribution with 20 trials and 0.5 success probability
rbinom(10,size=20,prob=.5)

rpois(5, lambda = 10)

cointoss <- function() { 
  x <- sample(c('H', 'T'), size = 1)
              return(x) 	
} 

while(cointoss() != 'H') { 
	print("Darn, tails") 
} 
print("Yay, heads!") 

if(cointoss() == 'H') {
  print("Heads, you wash the dishes") 
} else { 
	print("Tails, I wash the dishes") 
} 


