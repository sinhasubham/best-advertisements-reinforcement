import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import csv


csv_filename = 'mydb'
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
sums_of_rewards = [0] * d
N = len(df) + 1

# Reinforcement algorithm
def reinforce(db):
        global df, d, ads_selected, numbers_of_selections, sums_of_rewards, N
        total_reward = 0
        n= 0
        while n < len(df) + 1:
            ad = 0
            max_upper_bound = 0
            for i in range(0, d):
                if (numbers_of_selections[i] > 0):
                    average_reward = sums_of_rewards[i] / numbers_of_selections[i]
                    delta_i = math.sqrt(3/2 * math.log(n + 1) / numbers_of_selections[i])
                    upper_bound = average_reward + delta_i
                    print(upper_bound, i + 1)
                else:
                    upper_bound = 1e400
                if upper_bound > max_upper_bound:
                    max_upper_bound = upper_bound
                    ad = i
            ads_selected.append(ad)
            numbers_of_selections[ad] = numbers_of_selections[ad] + 1
            try:
                print("Advertisement " + str((ad + 1)) + " is on the display.Press 1 to watch or 2 to skip.")
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
            sums_of_rewards[ad] = sums_of_rewards[ad] + reward
            total_reward = total_reward + reward
            n = n +1
            print(numbers_of_selections)
            print(ads_selected)
reinforce(df)
