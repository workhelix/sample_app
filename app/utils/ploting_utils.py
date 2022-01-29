import plotly.graph_objects as go
from plotly import colors
from pandas import DataFrame
from typing import List
import streamlit as st
from itertools import cycle


class Plotly:
    def __init__(self,
                 mode: str = 'markers'):
        self.mode = mode
        self.fig = go.Figure()

    @staticmethod
    def map_colors(
        data: DataFrame,
        group: str,
        color_group: List[str] = colors.qualitative.Light24
    ):
        """
        Returns a color coding for a given series (one color for every unique value).
        Will repeat colors if not enough are provided.
        """
        # get unique identifiers
        unique_series = data[group].unique()

        # create lookup table - colors will be repeated if not enough
        color_lookup_table = dict((value, color) for (value, color)
                                  in zip(unique_series, cycle(color_group)))

        # look up the colors in the table
        return color_lookup_table

    def scatter(self,
                x: str, y: str,
                data: DataFrame,
                group: str = None,
                title: str = None,
                date: bool = False,
                subplot: bool = False):

        color_map = self.map_colors(data, group)
        traces = []
        if date:
            for label in data[group].unique():
                traces.append(go.Scatter(x=data[data[group] == label][x].sort_values(),
                                         y=data[data[group] == label][y],
                                         mode=self.mode,
                                         marker=dict(size=4,
                                                     color=color_map[label]),
                                         opacity=.5,
                                         name=label
                                         )
                              )

        else:
            for label in data[group].unique():
                traces.append(go.Scatter(x=data[data[group] == label][x],
                                         y=data[data[group] == label][y],
                                         mode=self.mode,
                                         marker=dict(size=4,
                                                     color=color_map[label]),
                                         opacity=.5,
                                         name=label
                                         )
                              )

        layout = dict(template='simple_white', title=title,
                      xaxis_title=x, yaxis_title=y, showlegend=True)
        if subplot:
            return traces
        else:
            for trace in traces:
                self.fig.add_trace(trace)
            self.fig.update_layout(layout)
            st.plotly_chart(self.fig)

    def contour_plot(self,
                     x: str, y: str,
                     data: DataFrame,
                     group: str = None,
                     title: str = None,
                     scatter: bool = False):

        traces = []
        traces.append(go.Histogram2dContour(x=data[x], y=data[y],
                                            colorscale='Blues'
                                            )
                      )
        if scatter:
            traces += self.scatter(x=x, y=y,
                                   data=data,
                                   group=group,
                                   title=title,
                                   subplot=True)

        layout = dict(template='simple_white', title=title,
                      xaxis_title=x, yaxis_title=y, showlegend=False)
        for trace in traces:
            self.fig.add_trace(trace)
        self.fig.update_layout(layout)
        st.plotly_chart(self.fig)
