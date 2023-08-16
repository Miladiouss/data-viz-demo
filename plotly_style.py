"""Project: Plotly Scientific Plot Styling
Version: 1.0
Author: miladiouss
Date: Aug 07, 2023
Description: Enhance appearance of plotly figures to meet publication-quality standards.
Usage:
  with open("plotly-style.yaml", "r") as stream:
      style_dict = yaml.safe_load(stream)
  fig.update(style_dict)
"""
import plotly.graph_objects as go


def update_layout(fig: go.Figure):
    """Enhance appearance of plotly figures by updating its layout.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        A plotly figure object
    """
    fig.layout.font.family = "Times New Roman"
    fig.layout.width = 850
    fig.layout.legend.bgcolor = "rgba(0, 0, 0, 0)"
    fig.layout.legend.font.family = "monospace"
    fig.layout.legend.itemsizing = "constant"
    fig.layout.font.size = 20
    fig.layout.margin.t = 75
    fig.layout.margin.b = 75
    fig.layout.margin.l = 75
    fig.layout.margin.r = 75
    fig.layout.margin.pad = 0
    fig.layout.plot_bgcolor = "rgba(0, 0, 0, 0)"
    fig.layout.showlegend = True
    fig.layout.xaxis.linecolor = "black"
    fig.layout.xaxis.mirror = True
    fig.layout.xaxis.showline = True
    fig.layout.xaxis.ticks = "inside"
    fig.layout.yaxis.linecolor = "black"
    fig.layout.yaxis.mirror = True
    fig.layout.yaxis.showline = True
    fig.layout.yaxis.ticks = "inside"
    fig.layout.xaxis.gridcolor = "rgba(0, 0, 0, .15)"
    fig.layout.yaxis.gridcolor = "rgba(0, 0, 0, .15)"
    fig.layout.xaxis.zerolinecolor = "rgba(0, 0, 0, .15)"
    fig.layout.yaxis.zerolinecolor = "rgba(0, 0, 0, .15)"
    fig.layout.xaxis.zeroline = False
    fig.layout.yaxis.zeroline = False
    fig.layout.xaxis.minor.ticks = "inside"
    fig.layout.xaxis.minor.ticklen = 2
    fig.layout.xaxis.minor.showgrid = True
    fig.layout.xaxis.minor.gridcolor = "rgba(1, 1, 1, .05)"
    fig.layout.yaxis.minor.ticks = "inside"
    fig.layout.yaxis.minor.ticklen = 2
    fig.layout.yaxis.minor.showgrid = True
    fig.layout.yaxis.minor.gridcolor = "rgba(1, 1, 1, .05)"
    fig.layout.title.font.size = 22
