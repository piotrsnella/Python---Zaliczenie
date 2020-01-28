import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# set style
sns.set_style('darkgrid')

titanic_data = pd.read_csv(r".\\train.csv")

titHead = titanic_data.head()
# print(titanic_data.head())

# create histogram 

# titHist = titanic_data['Survived'].hist(bins=20)

#plot
# titHist.plot()

# line plot
# titanic_data.plot.line(x='Age', y='Fare', figsize=(8,6))

# scatter plot
# titanic_data.plot.scatter(x='Sex', y='Survived', figsize=(8,6))

# box plot
# titanic_data.plot.box(figsize=(10,8))

# hexagonal plot
# titanic_data.plot.hexbin(x='Age', y='Fare', gridsize=30, figsize=(8,6))

# kernel density plot
# titanic_data['Age'].plot.kde()


# show plot
plt.show()