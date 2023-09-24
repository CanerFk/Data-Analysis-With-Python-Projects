import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    df = pd.read_csv("adult.data.csv")

    race_count = df["race"].value_counts()

    average_age_men = round(df.loc[df["sex"] == "Male", "age"].mean(), 1)

    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    higher_education = df[df["education"].isin(["Bachelors", "Masters", "Doctorate"])]
    lower_education = df[~df["education"].isin(["Bachelors", "Masters", "Doctorate"])]

    higher_education_rich = round((np.sum((higher_education["salary"] == ">50K").values) / len(higher_education)) * 100, 1)
    lower_education_rich = round((np.sum((lower_education["salary"] == ">50K").values) / len(lower_education)) * 100, 1)

    min_work_hours = df["hours-per-week"].min()

    num_min_workers = df[df["hours-per-week"] == min_work_hours]
    rich_percentage = round((np.sum((num_min_workers["salary"] == ">50K").values) / len(num_min_workers)) * 100, 1)

    
    temp = df.groupby('native-country')['salary'].apply(lambda x: (x == '>50K').mean() * 100)
    highest_earning_country = temp.idxmax()
    highest_earning_country_percentage = round(temp.max(),1)

    top_IN_occupation = df.loc[(df['native-country'] == 'India') & (df['salary'] == '>50K'), 'occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with the highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in a country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
