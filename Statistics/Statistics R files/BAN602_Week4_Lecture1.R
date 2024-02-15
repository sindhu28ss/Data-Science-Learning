## BAN 602 - Week 4 Lecture 1 ##

## St. Andrew's College

#Probability that x-bar will be between 1687 and 1707?

pnorm(0.63)-pnorm(-0.63)
pnorm((1707-1697)/8.2)-pnorm((1687-1697)/8.2)

#Probability that the estimate of the population proportion of applicant desiring on-campus housing that is within plus or minus .05 
#of the actual population proportion
pnorm((0.77 - 0.72)/0.082)-pnorm((0.67 - 0.72)/0.082)


## Example from Survey Data in MASS package

library(MASS)
height.response <- na.omit(survey$Height)
mean(height.response, na.rm=TRUE)
n <- length(height.response)
n

## Point Estimate of Population Mean
## Suppose Sigma known to be 9.48

sigma <- 9.48                  
sem <- sigma/sqrt(n)
sem
E <- qnorm(.975)*sem
E
xbar <- mean(height.response) 
xbar

# 95% confidence Interval for Mean
xbar + c(-E, E)

## Suppose Sigma is unknown

s <- sd(height.response) 
SE <- s/sqrt(n)
SE
E <- qt(.975, df=n-1)*SE
E
xbar <- mean(height.response)
## 95% confidence Interval for Mean
xbar + c(-E, E) 


## Sample Size Calculation for Population Mean

#Sample size needed to achieve a 1.2 centimeters margin of error for population mean at 95% confidence level.
zstar <- qnorm(.975) 
sigma <- 9.48 
E <- 1.2 
zstar^2 * sigma^2/ E^2 

## Point Estimate of Population Proportion

gender.response <- na.omit(survey$Sex)
n <- length(gender.response) 
k <- sum(gender.response == "Female") 
pbar <- k/n
pbar 
SE <- sqrt(pbar*(1-pbar)/n)
SE
E <- qnorm(.975)*SE
E
pbar + c(-E, E)

## Sample Size Calculation for Population Proportion

#Sample size needed to achieve 5% margin of error for the female student proportion at 95% confidence level

zstar <- qnorm(.975) 
p <- 0.5 
E <- 0.05 
zstar^2 * p * (1-p) / E^2 

