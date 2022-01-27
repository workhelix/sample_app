import streamlit as st
from pathlib import Path
from pandas import read_csv, DataFrame, to_datetime
import seaborn as sns
from matplotlib import pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)


def read_data(path: str) -> DataFrame:
    """
    Read csv and return pandas dataframe.

    :param path: path of file
    :return pd.DataFrame
    """
    return read_csv(Path(path))


def run():
    df = read_data("./docs/data/alixpartners_1_26_2022.csv")  # filtered data for size
    df['dt'] = to_datetime(df['month'], format='%Y-%m')
    # relplot
    fig = plt.figure(figsize=(8, 5))
    sns.relplot(x='ai_in', y='agg_sml', hue='ticker', alpha=.3, data=df)
    st.pyplot()

    # plot plasma lineplot

    sns.lineplot(x='dt', y='ai_in', hue='ticker', data=df)
    plt.ylabel('AI Hiring')
    plt.xlabel('Date')
    st.pyplot()

    # plot plasma lineplot noramalized
    df['normed_ai_in'] = df.groupby('ticker')['ai_in'].transform(lambda x: (x - x.mean()) / x.std())
    sns.set_palette('plasma_r')
    sns.lineplot(x='dt', y='normed_ai_in', hue='ticker', data=df, legend=True)
    plt.ylabel('AI Hiring')
    plt.xlabel('Date')
    st.pyplot()

    # plot plasma lineplot noramalized
    sns.lineplot(x='dt', y='agg_sml', hue='ticker', data=df, legend=True)
    plt.ylabel('Machine Learning Exposure Score (Raw)')
    plt.xlabel('Date')
    st.pyplot()

    # remote work
    plt.ylabel('Remote Work Potential Score (Raw)')
    plt.xlabel('Date')
    sns.lineplot(x='dt', y='agg_tele', hue='ticker', data=df, legend=True)
    st.pyplot()

    # ML Exposure
    g = sns.relplot(x='agg_sml', y='agg_tele', hue='ticker', data=df, legend=True)
    plt.xlabel('ML Exposure Score')
    plt.ylabel('Remote Work Exposure Score')
    #g._legend.remove()
    st.pyplot()

    # KDE Plot
    # color palette as dictionary
    palette = {"DHR": "tab:cyan",
               "SWK": "tab:orange",
               "IR": "tab:aquamarine",
               "EMR": "tab:red",
               "SPXC": "tab:yellow",
               "HON": "tab:lightpink",
               "ITW": "tab:blue",
               "GE": "tab:indigo",
               "MMM": "olive"}

    sns.kdeplot(x='agg_sml', y='agg_tele', hue='sector', data=df, legend=True)
    plt.scatter(df[df.ticker == 'DHR'].agg_sml, df[df.ticker == 'DHR'].agg_tele, alpha=.3, color="cyan")
    plt.scatter(df[df.ticker == 'SWK'].agg_sml, df[df.ticker == 'SWK'].agg_tele, alpha=.3, color="orange")
    plt.scatter(df[df.ticker == 'IR'].agg_sml, df[df.ticker == 'IR'].agg_tele, alpha=.3, color="aquamarine")
    plt.scatter(df[df.ticker == 'EMR'].agg_sml, df[df.ticker == 'EMR'].agg_tele, alpha=.3, color="red")
    plt.scatter(df[df.ticker == 'SPXC'].agg_sml, df[df.ticker == 'SPXC'].agg_tele, alpha=.3, color="yellow")
    plt.scatter(df[df.ticker == 'HON'].agg_sml, df[df.ticker == 'HON'].agg_tele, alpha=.3, color="lightpink")
    plt.scatter(df[df.ticker == 'ITW'].agg_sml, df[df.ticker == 'ITW'].agg_tele, alpha=.3, color="blue")
    plt.scatter(df[df.ticker == 'GE'].agg_sml, df[df.ticker == 'GE'].agg_tele, alpha=.3, color="indigo")
    plt.scatter(df[df.ticker == 'MMM'].agg_sml, df[df.ticker == 'MMM'].agg_tele, alpha=.3, color="olive")

    plt.xlabel('ML Exposure Score')
    plt.ylabel('Remote Work Exposure Score')
    plt.title('Relative Technological Exposure')
    plt.legend(['DHR', 'SWK', 'IR', 'EMR',
                'SPXC', 'HON', 'ITW', 'GE', 'MMM'])
    st.pyplot()
