import numpy as np
import matplotlib.pyplot as plt

#%% problem 4a
# consider 3 points in 2D space: 1, 2, 3
# 1 and 2 are connected by a line of length A
# 1 and 3 are connected by a line of length B
# 2 and 3 are connected by a line of length C
# let there be 3 independent variables tA, tB, tC that represent the time it takes to travel from 1 to 2, 1 to 3, and 2 to 3
# tA. tB, tC are all exponentially distributed
# f(tA) = 1/4 * e^(-tA/4)
# f(tB) = 1/3 * e^(-tB/3)
# f(tC) = 2/3 * e^(-2tC/3)

arr_tbc = []
for i in range(1000):
    # generate a random number from each of the distributions of tB and tC
    tB = np.random.exponential(3)
    tC = np.random.exponential(3/2)
    # add them together
    total_time = tB + tC
    arr_tbc.append(total_time)

# plot the normalized histogram of the total time
plt.hist(arr_tbc, bins=20, density=True)
plt.title('Normalized Histogram of Total Time')
plt.xlabel('Total Time')
plt.ylabel('Frequency')
plt.show()

#%% problem 4b
# calculate the mean of the total time
arr_ta = []
for i in range(1000):
    tA = np.random.exponential(4)
    arr_ta.append(tA)
mean_ta = np.mean(arr_ta)
print(mean_ta)
mean_tbc = np.mean(arr_tbc)
print(mean_tbc)

#%% problem 4c
# count how many times the travel time is > 12
count_a = 0
for timea in arr_ta:
    if timea > 12:
        count_a += 1
count_bc = 0
for timebc in arr_tbc:
    if timebc > 12:
        count_bc += 1
print(count_a / 1000)
print(count_bc / 1000)


#%% problem 5a
# y = (F) / (50000 * (1 - X))
# F = 100
# X is a random variable that is uniformly distributed between 0.5 and 0.9
tip_deflection = []
x_values = []
for i in range(1000):
    X = np.random.uniform(0.5, 0.9)
    y = 100 / (50000 * (1 - X))
    tip_deflection.append(y)
    x_values.append(X)

# plot the histogram of the tip deflection
plt.hist(tip_deflection, bins=20)
plt.title('Histogram of Tip Deflection')
plt.xlabel('Tip Deflection')
plt.ylabel('Frequency')
plt.show()

# plot the histogram of X values
plt.hist(x_values, bins=20)
plt.title('Histogram of X Values')
plt.xlabel('X Values')
plt.ylabel('Frequency')
plt.show()

#%% problem 5b
# calculate the mean of the tip deflection
mean_tip_deflection = np.mean(tip_deflection)
print(mean_tip_deflection)
# actual answer is 0.0080472

#%% problem 5c
# now let F be normally distributed with mean 0 and standard deviation 1000
part_c = []
for i in range(1000):
    F = np.random.normal(0, 1000)
    X = np.random.uniform(0.5, 0.9)
    y = F / (50000 * (1 - X))
    part_c.append(y)

# plot the normalized histogram of the tip deflection
plt.hist(part_c, bins=20)
plt.title('Histogram of Tip Deflection with 2 Random Variables X and F')
plt.xlabel('Tip Deflection')
plt.ylabel('Frequency')
plt.show()