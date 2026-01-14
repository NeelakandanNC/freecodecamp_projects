#1 dataset.groupby('race').size()

#2 dataset[dataset['sex']=='Male']['age'].mean()

#3 dataset[dataset['education'] == 'Bachelors'].shape[0] / dataset.shape[0] * 100

#4 dataset[
#     (dataset['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) &
#     (dataset['salary'] > 50000)
# ].shape[0] / dataset[dataset['salary'] > 50000].shape[0] * 100

#5 dataset[
#     (~dataset['education'].isin(['Bachelors', 'Masters', 'Doctorate'])) &
#     (dataset['salary'] > 50000)
# ].shape[0] / dataset[dataset['salary'] > 50000].shape[0] * 100

#or

# ((~dataset['education'].isin(['Bachelors','Masters','Doctorate'])) 
#  [dataset['salary'] > 50000]).mean() * 100


#6 dataset['hours-per-week'].min()

#7 dataset[
#     (dataset['hours-per-week'] == dataset['hours-per-week'].min()) &
#     (dataset['salary'] > 50000)
# ].shape[0] / dataset[dataset['hours-per-week'] == dataset['hours-per-week'].min()].shape[0] * 100

#8 dataset.groupby('native-country')['salary'].apply(
#     lambda x: (x > 50000).mean() * 100
# ).idxmax()

#9 dataset.groupby('occupation').apply(
#     lambda x: (x['salary'] > 50000).mean() * 100
# ).idxmax()


#1 How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
#2 What is the average age of men?
#3 What is the percentage of people who have a Bachelor's degree?
#4 What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
#5 What percentage of people without advanced education make more than 50K?
#6 What is the minimum number of hours a person works per week?
#7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
#8 What country has the highest percentage of people that earn >50K and what is that percentage?
#9 Identify the most popular occupation for those who earn >50K in India.