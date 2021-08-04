import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Assessing & Preparing Dataset
data = 'https://raw.githubusercontent.com/gohil-jay/Widhya-ML-Internship/main/Week-3/clean_data.csv'
dataset = pd.read_csv(data)
dataset

clean_dataset = dataset[['Followers', 'time', 'Likes']]
clean_dataset

# Visualizing Dataset

temp_1 = clean_dataset['Likes']
temp_1.plot()

temp_2 = clean_dataset['Followers']
temp_2.plot(colormap = 'Reds_r')

temp_3 = clean_dataset['time']
temp_3.plot(colormap='Accent')

temp_4 = clean_dataset
temp_4.plot(x='Likes', y='Followers')

temp_5 = clean_dataset
temp_5.plot()

plt.hist(clean_dataset["time"], color=['green'])
plt.show()

plt.hist(clean_dataset["Likes"], color=['orange'])
plt.show()

plt.hist(clean_dataset["Followers"], color=['purple'], orientation='horizontal')
plt.show()

plt.hist(clean_dataset, stacked = True)
plt.show()

plt.scatter(clean_dataset['time'], clean_dataset['Likes'])

plt.xlabel("VALUES")
plt.ylabel("SEQUENCE")
plt.title("VALUES vs SEQUENCE", color="blue")

plt.show()

plt.scatter(clean_dataset['Likes'], clean_dataset['Followers'], c = "Red")

plt.scatter(clean_dataset['time'], clean_dataset['Followers'], c = "purple")
plt.scatter(clean_dataset['time'], clean_dataset['Likes'], c = "Green")

# Visualization of ML performance

original_values = [28, 33, 30, 43, 20, 46, 93, 31, 40, 29, 12, 136, 17, 17, 157, 14, 19, 16, 12, 31]
predicted_values = [29, 40, 31, 32, 29, 50, 32, 32, 32, 36, 29, 153, 30, 49, 57, 32, 28, 29, 29, 78]
list_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

plt.scatter(list_values, predicted_values, marker="*", color = '#FFA500')
plt.scatter(list_values, original_values, color = '#1f77b4')

temp_99 = clean_dataset['Likes']
temp_99.plot.area()

clean_dataset[['Likes', 'time']].plot.area(stacked = False)
clean_dataset.plot.area()

# Understanding correlation among columns

print("Visualizing correlation between features using heatmap -->", "\n"*2)
plot_1 = sns.heatmap(clean_dataset.corr(method='pearson'), cmap='Reds')
print(plot_1)

print("Visualization of Dataframe --> \n")
plot_var_1 = sns.pairplot(clean_dataset, kind = 'scatter', diag_kind='kde', palette=["C0", "C1", "C2"])
plot_var_2 = plot_var_1.map_lower(sns.kdeplot, levels=3)
plot_1 = plot_var_2.map_upper(sns.kdeplot, levels=3)
print(plot_1)
