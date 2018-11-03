import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import csv
import random

csv_filename = 'mydb2'
# Creating empty arrays for each advertisement
Ad1 = []
Ad2 = []
Ad3 = []
Ad4 = []
Ad5 = []
alladv = [Ad1, Ad2, Ad3, Ad4, Ad5]

#Creating a dataframe to record user behaviour
df = pd.DataFrame({"Ad1": Ad1, "Ad2": Ad2, "Ad3": Ad3, "Ad4": Ad4, "Ad5": Ad5,})
df.to_csv(csv_filename + '.csv', index = False)
d = 5
ads_selected = []
numbers_of_selections = [0] * d
numbers_of_rewards_1 = [0] * d
numbers_of_rewards_0 = [0] * d
N = len(df) + 1
# Reinforcement algorithm
def reinforce(db):
        global df, d, ads_selected, numbers_of_selections, sums_of_rewards, N, \
            numbers_of_rewards_1, numbers_of_rewards_0
        total_reward = 0
        n= 0
        while n < len(df) + 1:
            ad = 0
            max_random = 0
            for i in range(0, d):
                randomness = random.betavariate(numbers_of_rewards_1[i] + 1, numbers_of_rewards_0[i] + 1)
                print(randomness, i + 1)
                if randomness > max_random:
                    max_random = randomness
                    ad = i
            ads_selected.append(ad)
            numbers_of_selections[ad] = numbers_of_selections[ad] + 1
            try:
                print("Advertisement " + str(ad + 1) + " is on the display.Press 1 to watch or 2 to skip.")
                userchoice = int(input())
                if userchoice == 1:
                    print("thank you for watching")
                    alladv[ad].append(1)
                    for i in range(len(alladv)):
                        if i != ad:
                            alladv[i].append(0)
                elif userchoice == 2:
                    for i in range(len(alladv)):
                        alladv[i].append(0)
                df = pd.DataFrame({"Ad1": Ad1, "Ad2": Ad2, "Ad3": Ad3, "Ad4": Ad4, "Ad5": Ad5})
                df.to_csv(csv_filename + '.csv', index = False)
            except ValueError:
                print("Invalid value, Please press 1 or 2")
            reward = alladv[ad][n]
            if reward == 1:
                numbers_of_rewards_1[ad] = numbers_of_rewards_1[ad] + 1
            if reward == 0:
                numbers_of_rewards_0[ad] = numbers_of_rewards_0[ad] + 1
            total_reward = total_reward + reward
            n = n +1
            print(numbers_of_selections)

reinforce(df)

