import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("medical_examination.csv")

df['overweight'] = ((df['weight'] / ((df['height'] / 100) ** 2)) > 25).astype(int)

df['cholesterol'] = df['cholesterol'].apply(lambda x: 0 if x == 1 else 1)
df['gluc'] = df['gluc'].apply(lambda x: 0 if x == 1 else 1)

def draw_cat_plot():
    cardio_df = df[['cardio','active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']]
    
    df_cat = pd.melt(cardio_df, id_vars=['cardio'], var_name='variable', value_name='value')

    fig = sns.catplot(x="variable", hue="value", col="cardio", data=df_cat, kind='count')
    fig.set_axis_labels("variable", "total")

    fig = fig.fig  

    fig.savefig('catplot.png')
    return fig



def draw_heat_map():
    # Clean the data
    df_heat = df[(df["ap_lo"]<=df["ap_hi"])&
                (df["height"]>=df["height"].quantile(0.025))&
                (df["height"]<=df["height"].quantile(0.975))&
                (df["weight"]>=df["weight"].quantile(0.025))&
                (df["weight"]<=df["weight"].quantile(0.975))]

    corr = df_heat.corr()
    mask = np.triu(corr)

    fig, ax = plt.subplots(figsize = (10,8))

    sns.heatmap(corr, annot = True, fmt=".1f", linewidths= .5, mask = mask, square=True,ax = ax)


    fig.savefig('heatmap.png')
    return fig
