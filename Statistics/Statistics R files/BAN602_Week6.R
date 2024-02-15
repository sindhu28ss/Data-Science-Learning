# BAN 602 Week 6 #

rm(list=ls(all=TRUE)) 
setwd("/Users/Somak/Desktop")
install.packages("agricolae")
library(agricolae)

#### Completely Randomized Design ####
## Auto Shine Example
asData <- read.csv("AutoShine.csv", stringsAsFactors = FALSE, skipNul = TRUE)

anova_as <- aov(Number_of_Washes~Wax_Type, data=asData)

summary(anova_as)

## Reed Manufacturing Example
rmData <- read.csv("ReedManufacturing.csv", stringsAsFactors = FALSE, skipNul = TRUE)

anova_rm <- aov(Hours_Worked~Manufacturing_Plant, data=rmData)

summary(anova_rm)

print(LSD.test(anova_rm, trt= "Manufacturing_Plant", p.adj="bonferroni"))


#### Randomized Block Design ####
## Crescent Oil Example
coData <- read.csv("CrescentOil.csv", stringsAsFactors = FALSE, skipNul = TRUE)

anova_co <- aov(MPG~Gasoline_Blend + as.factor(Automobile), data=coData)

summary(anova_co)


#### Factorial Experiment ####
## State of Ohio Hourly Wage Study

hwData <- read.csv("OhioWageSurvey.csv", stringsAsFactors = FALSE, skipNul = TRUE)

anova_hw <- aov(Hourly_Wage~Industry*Location, data=hwData)

summary(anova_hw)

