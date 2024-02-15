# 1. random number generation

# generate float random numbers from 0 and 1
import random
print(random.random()) #1 is exclusive

# generate float uniform distributed number from a to b.
import random
print(random.uniform(5, 100)) #interval both are inclusive

# genrate random normal distributed number
import random
print(random.normalvariate(0, 2)) #mean and std

#-----------------------------------------------------------------------------------------

# using numpy to generate multiple random normal distributed numbers (standard normal)
import numpy as np
import matplotlib.pyplot as plt
print(np.random.randn(5))
print(np.random.randn(5,2)) # an array or random numbers
plt.hist(np.random.randn(1000))

# generate random normal with mean 4, and variance 25
import matplotlib.pyplot as plt
import numpy as np
x=np.random.randn(1000)*5+4
plt.hist(x)

# use numpy to generate an array of uniformly distributed random numbers
print(np.random.rand(5,2)) # 5 x 2 array
plt.hist(np.random.rand(1000))

# random binomial distribution
print(np.random.binomial(4,0.5,2))  # number of trials, probability of each trial, # generated samples
plt.hist(np.random.binomial(1000,.5,100))

# bernoulli
print(np.random.binomial(1,0.5,10))
plt.hist(np.random.binomial(1,0.5,10))

# exponential
print(np.random.exponential(10,1000)) # parameter is 1/lambda -> time iterval between two arrivals,  (scale, n)
                                    # lambda is the intensity of arrival: num arrival in one unit of time. 
                                    # If 0.1 arrival per hours, then one arrival takes 10 hours on average
print(np.random.exponential(10,(2,3)))
plt.hist(np.random.exponential(10,1000)) 


# central limit theorem
# The central limit theorem states that if you have a population with mean μ and standard deviation σ 
# and take sufficiently large random samples from the population with replacement , 
# then the distribution of the sample means will be approximately normally distributed.

import numpy as np
import matplotlib.pyplot as plt
import statistics
avg_uniform=[]
avg_binomial=[]
avg_exp=[]
for _ in range(1000):
    avg_uniform.append(statistics.mean(np.random.rand(1000)))
    avg_exp.append(statistics.mean(np.random.exponential(5,1000)))
    avg_binomial.append(statistics.mean(np.random.binomial(10,0.5,1000)))
plt.hist(avg_uniform)
plt.hist(avg_binomial)
plt.hist(avg_exp)

# get a random choice from a list
import random
x=[1,2,3,4]
print(random.choice(x))

# get multiple random choices from a list
# note that the choice method allows replacement, meaning that you could get result [3,3]
import random
x=[1,2,3,4]
print(random.choices(x,k=2))

# # get multiple random choices from a weighted choice list
from random import choices
print(choices(['red', 'black', 'green'],[0.8,0.1,0.1], k = 6)) # the red color has higher probability to appear

# extract random sample from a list
# note that the random sample does not allow replacement. Once a number is selected, it cannot be selected again
import random 
x=[1,2,3,4]
sample=random.sample(x,2)
print(sample)

# randomize the sequence of a list
import random 
x=[1,2,3,4]
random.shuffle(x)
print(x)

# row a dice 20 times, and count the number of 6 (how many 6 value are in the list)
import random 
print(random.choices([1,2,3,4,5,6],k=20).count(6))
# --------------------------------------------------------------------------------------
# 2.  simulation example 1

''' ######## Exercise 1 ########'''
# Replace 20 cards from a deck of 52 playing cards
# and determine the average proportion of cards with a ten, jack, queen, or king. 
# It means that there are 16 ten cards and 36 other cards. 
# Set the weights for random.choices model with these values)
# Do 10000 iterations to calculate the average
import random
import statistics
proportion=[] # define an empty list to append proportions
iterations = 10000 # let's do 10000 iterations to calculate the average
cards = ["10"] * 16 + ["other"] * 36 # Define the cards in the deck

for _ in range(iterations):
    # Sample 20 cards from the deck
    sampled_cards = random.choices(cards, k=20)
    # Count the number of "10" cards in the sampled set
    count_10s = sampled_cards.count("10")
    proportion.append(count_10s/20)
    
average_proportion = statistics.mean(proportion)
print(f"Average proportion of '10' cards in 10000 iterations: {average_proportion:.4f}")

'''for loop alternative:
for _ in range(iterations):    
    sampled_cards = random.choices(cards, k=20).count("10")
    proportion.append(sampled_cards/20)    
'''

#--------------------------------------------------------------------------------------
# 3. simulation example 2

# testing the difference between drug and placebo
# the result from drug or placebo is listed below
drug = [54, 73, 53, 70, 73, 68, 52, 65, 65]
placebo = [54, 51, 58, 44, 55, 52, 42, 47, 58, 46]
# the question is, are there real(significant) differnce?

import statistics
import random

observed_diff = statistics.mean(drug) - statistics.mean(placebo)

# now let's do 10000 times resampling permutation test to determine the difference between the drug and the placebo
n = 10000
count = 0
combined = drug + placebo # combine the two lists together
for i in range(1,n):
    random.shuffle(combined)
    new_diff=statistics.mean(combined[:len(drug)])-statistics.mean(combined[len(drug):])
    # it is crucial to know that the for index [a:b], a is inclusive but b is exclusive 
    # so we don't need (combined[len(drug)+1:]) in the second half
    count+=new_diff>observed_diff

print(count)
# out of 10000 resampling permutation test, count variable is always very small.
# so we can say drug is effective. 
# we do need to do hypothesis testing for this claim. 
# But that is out of the scope of this class.
# --------------------------------------------------------------------------------------
# 4. simulation example 3_queuing system

# suppose customers come to a store at a rate of 20 per hour, 
# so the parameter for the exponential is 1/20
# suppose customers get serviced at a rate of 30 per hour, 
# so the parameter for the exponential is 1/30

# the rate of either event is 50
# and the prob of customer arrival occurs next is 20/50
# the prob of customer get serviced occurs next is 30/50

import numpy as np
import matplotlib.pyplot as plt
lamda = 20 # the customer arrival rate
mu = 30 # the service rate, it has to be larger than lamda, otherwise the queue will explode
time = 8 # we only observe the first 8 time units (mins, hours, or whatever)
t = 0 # the current time
Q = 0 # the current queue length

Q_length=[]
eventime=[]

while t<time:
    if Q==0:
        T_next=np.random.exponential(1/lamda,1)[0] # we add [0] as the output is an array
        Q=1
        Q_length.append(Q)
    else:
        T_next=np.random.exponential(1/50,1)[0]
        r=np.random.rand(1).squeeze() # Squeeze() is used when we want to remove single-dimensional entries from the shape of an array. 
        Q=Q+(1 if r<=lamda/(lamda+mu) else -1) # If the prob is smaller than the prob customer arrival occurs,
        #then 1, otherwise -1)
        Q_length.append(Q)
    t+=T_next
    eventime.append(t)

print(Q_length)
print(eventime)

plt.step(eventime,Q_length)


# --------------------------------------------------------------------------------------
# 4.5 trade off between number of service station and its cost
# Now we have a more realistic situation
# 1. if the queue is too long, customer will leave the queue -> max queue length is 5. Any incoming customers will leave
# 2. service for each customer will make $5 profits
# 3. we need to pay $20 for each service station per day
# the question is: if the customer comes at a rate lamda = 100/hour, and service rate is 3/hour, 
# what is the best number of service stations to deploy?

import numpy as np
import matplotlib.pyplot as plt

profitPerService = 5
salaryPerServiceStation = 20

lamda = 20 # the customer arrival rate
mu = 30 # the service rate, it has to be larger than lamda, otherwise the queue will explode
time = 8 # we only observe the first 8 time units (mins, hours, or whatever)

def simQ(numServiceStation, lamda, mu, time,maxQ):
    t = 0
    Q = 0
    eventime=[]
    totalProfit = 0
    actualmu = mu*numServiceStation # the actual service rate is the service rate of a single station * the number of stations
    
    while t<time:
        if Q==0:
            T_next=np.random.exponential(1/lamda,1)[0]
            Q=1
        else:
            T_next=np.random.exponential(1/(lamda+actualmu),1)[0]
            r=np.random.rand(1).squeeze()
            if r<=lamda/(lamda+actualmu):
                Q = min(maxQ,Q+1) # any customer out of the queue is lost
            else:
                Q-=1
                totalProfit+=profitPerService # profit is only registered when we complete one service
        t+=T_next
        eventime.append(t)
    
    return totalProfit-salaryPerServiceStation*numServiceStation # the trade off


profit = {}
for numStation in range(0,200,10): # check service stations = 1,2,3
    avgProfit = 0
    print(numStation)
    for _ in range(10):
        simProfit = simQ(numServiceStation=numStation,lamda=20,mu=30,time=8,maxQ=5)
        avgProfit += simProfit
    avgProfit = avgProfit/20 # denominator = lamda
    profit[numStation]=avgProfit
    
print(profit)
# --------------------------------------------------------------------------------------
# 5. rain and commute

''' ######## Exercise 2 ########'''

# suppose a professor walks from home to the office. 
# He has 3 umbrella in the office and 3 umbrella at home.
# if it is raining when the professor walks to office from home, 
# or walks to home from office, 
# he has to bring 1 umbrella to office or to home.
# suppose the probability to rain is 20% anytime. 
# How many days will these umbrella last before either the home 
# or the office has 0 umbrella.
# do 10 simulations 
from random import choices
import matplotlib.pyplot as plt
import statistics

def simulate_rainy_days():
    home_umbrellas = 3
    office_umbrellas = 3
    days = 0
    
    while home_umbrellas > 0 and office_umbrellas > 0:
        # Simulate the morning commute
        if choices([True, False], [0.2, 0.8])[0] and home_umbrellas > 0:
            home_umbrellas -= 1
            office_umbrellas += 1
        
        # Simulate the evening commute
        if choices([True, False], [0.2, 0.8])[0] and office_umbrellas > 0:
            office_umbrellas -= 1
            home_umbrellas += 1
        
        days += 1

    return days

# Run the simulation 10 times
simulation_results = []

for _ in range(10):
    result = simulate_rainy_days()
    simulation_results.append(result)

# Compute the mean and standard deviation
mean_days = statistics.mean(simulation_results)
std_dev_days = statistics.stdev(simulation_results)

# Print the average number of days and standard deviation
print(f"Average days before running out of umbrellas: {mean_days}")
print(f"Standard deviation of days: {std_dev_days}")

# Plot the simulation results
plt.hist(simulation_results)

''' ______________________________________________'''

# --------------------------------------------------------------------------------------
# 6. gambling strategies.

# strategy 1
# We start with $5000, we bet $1 every round, 
# and the winning probability is 50%.
# if we win, we get back the $1 bet plus another $1. 
# if we lose, we lose the $1 bet.
# play 10 rounds

# strategy 2
# We start with $5000, the winning probability is 50%.
# Each time we win, we bet $1 next time. 
# Each time we lose, we bet 3 times the previous bet next time
# play 10 rounds

# which strategy gives higher winning rate?

# program strategy 1
import numpy as np
import statistics
def strategy1():
    money=5000
    result=np.random.binomial(1,0.5,10)
    for i in result:
        if i==1:
            money+=1
        else:
            money-=1
    return money
print(strategy1())

# checking wining rate
ifwining=[]
for i in range(10000):
    ifwining.append(strategy1()>5000)
print(statistics.mean(ifwining))
# checking expected reward
avgReward = 0
for i in range(10000):
    avgReward += strategy1()
print(avgReward/10000)


# program strategy 2
''' ######## Exercise 3 ########'''

''' _______________________________________________'''

import numpy as np
import statistics
def strategy2():
    money=5000
    result=np.random.binomial(1,0.5,10)
    bet=1
    for i in result:
        if i==1:
            money+=bet
            bet=1
        else:
            money-=bet
            bet=bet*3
    return money
print(strategy2())

# checking wining rate
ifwining=[]
for i in range(10000):
    ifwining.append(strategy2()>5000)
print(statistics.mean(ifwining))
# checking expected reward
avgReward = 0
for i in range(10000):
    avgReward += strategy2()
print(avgReward/10000)


# --------------------------------------------------------------------------------------
# 7. sucessful people are 2% hard working and 98% lucky?

import numpy as np

max_luck=1 # suppose luck accounts for 10%
max_ability=9 # suppose ability accounts for 90%
n_iteration=100
n_people=1000000
# according to the following report, 295450 people in the world are super rich (net worth over $30 million)
# https://robbreport.com/lifestyle/news/world-population-increase-ultra-high-net-worth-individuals-1234622357/
pct_superrich=295450/7000000000 
pctBestAbilityAlsoSuperRichLst = []

for i in range(n_iteration):
    np.random.seed(i+1)
    if i%100==0:
        print(i)
    luck=np.random.uniform(0, max_luck, n_people)
    ability=np.random.uniform(0, max_ability, n_people)
    total=luck+ability
    bestTotal=np.argsort(total)[::-1][:int(n_people*pct_superrich)] # np.argsort(x)[::-1] list from max to min value.
                                                                    # if only the total score matters, these people should be rich
    bestAbility=np.argsort(ability)[::-1][:int(n_people*pct_superrich)] # if only the ability score matters, these people should be rich
    pctBestAbilityAlsoSuperRich = len(set(bestTotal) & set(bestAbility))/len(bestTotal)
    # print(pctBestAbilityAlsoSuperRich)
    pctBestAbilityAlsoSuperRichLst.append(pctBestAbilityAlsoSuperRich)

probBestAbilityAlsoSuperRich=np.mean(pctBestAbilityAlsoSuperRichLst)
print(probBestAbilityAlsoSuperRich)

# if luck accounts for 10% of your total score, then only 2% of the best ability people can get super rich 

# you can use seed to set the randomState so that you can replicate the random number generator
import numpy as np
np.random.seed(2)
print(np.random.rand(3))




