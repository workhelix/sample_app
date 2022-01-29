import streamlit as st
from pathlib import Path
from pandas import read_csv, DataFrame, to_datetime
import seaborn as sns
from matplotlib import pyplot as plt

from ..utils.ploting_utils import Plotly

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

    st.header("Sample Analytics Capabilities")
    st.markdown("The charts below are all interactive. To focus on a specific competitor, "
                "simply toggle names on the legend to right of each chart.")

    # Ai Exposure by Group
    fig = Plotly()
    fig.scatter(x='ai_in', y='agg_sml',
                data=df, group='ticker',
                title="Industry AI Exposure by Index")

    # Normalized Hiring
    df['normed_ai_in'] = df.groupby('ticker')['ai_in'].transform(lambda x: (x - x.mean()) / x.std())
    hiring_option = st.selectbox("Would you like to Normalize the data?", ('Standard', 'Normalized'))
    if hiring_option == 'Standard':
        fig = Plotly(mode='lines+markers')
        fig.scatter(x='dt', y='ai_in',
                    data=df, group='ticker',
                    title=f"AI Hiring by Index, {hiring_option}",
                    date=True)
    else:
        fig = Plotly(mode='lines+markers')
        fig.scatter(x='dt', y='normed_ai_in',
                    data=df, group='ticker',
                    title=f"AI Hiring by Index, {hiring_option}",
                    date=True)

    # SML Line Plot
    fig = Plotly('lines+markers')
    fig.scatter(x='dt', y='agg_sml',
                data=df, group='ticker',
                title='Machine Learning Exposure Score Over Time by Index',
                date=True)

    # remote work
    fig = Plotly("lines+markers")
    fig.scatter(x='dt', y='agg_tele',
                data=df, group='ticker',
                title='Remote Work Trends Over Time by Index',
                date=True)

    # ML Exposure x Remote Work
    fig = Plotly()
    fig.scatter(x='agg_sml', y='agg_tele',
                data=df, group='ticker',
                title='ML Exposure Score as Compared to Remote Work Score by Index',
                date=True)

    # Density Contour Plot
    fig = Plotly()
    fig.contour_plot(x='agg_sml', y='agg_tele',
                     data=df, group='ticker',
                     title='Remote Work Score As Compared to ML Exposure Score Contour Plot by Index',
                     scatter=True)
    # sns.kdeplot(x='agg_sml', y='agg_tele', hue='sector', data=df, legend=True)
    # plt.scatter(df[df.ticker == 'DHR'].agg_sml, df[df.ticker == 'DHR'].agg_tele, alpha=.3, color="cyan")
    # plt.scatter(df[df.ticker == 'SWK'].agg_sml, df[df.ticker == 'SWK'].agg_tele, alpha=.3, color="orange")
    # plt.scatter(df[df.ticker == 'IR'].agg_sml, df[df.ticker == 'IR'].agg_tele, alpha=.3, color="aquamarine")
    # plt.scatter(df[df.ticker == 'EMR'].agg_sml, df[df.ticker == 'EMR'].agg_tele, alpha=.3, color="red")
    # plt.scatter(df[df.ticker == 'SPXC'].agg_sml, df[df.ticker == 'SPXC'].agg_tele, alpha=.3, color="yellow")
    # plt.scatter(df[df.ticker == 'HON'].agg_sml, df[df.ticker == 'HON'].agg_tele, alpha=.3, color="lightpink")
    # plt.scatter(df[df.ticker == 'ITW'].agg_sml, df[df.ticker == 'ITW'].agg_tele, alpha=.3, color="blue")
    # plt.scatter(df[df.ticker == 'GE'].agg_sml, df[df.ticker == 'GE'].agg_tele, alpha=.3, color="indigo")
    # plt.scatter(df[df.ticker == 'MMM'].agg_sml, df[df.ticker == 'MMM'].agg_tele, alpha=.3, color="olive")
    #
    # plt.xlabel('ML Exposure Score')
    # plt.ylabel('Remote Work Exposure Score')
    # plt.title('Relative Technological Exposure')
    # plt.legend(['DHR', 'SWK', 'IR', 'EMR',
    #             'SPXC', 'HON', 'ITW', 'GE', 'MMM'])
    # st.pyplot()
