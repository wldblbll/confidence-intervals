import pandas as p
import sys
import datetime
import plotly.express as px
import streamlit
import os
from math import ceil as arrondi_sup
import pandas as p

__version__ = 1.0

try:
    streamlit.set_option('deprecation.showfileUploaderEncoding', False)
except:
    pass

streamlit.title("Confidence Intervals calculator")
status = streamlit.empty()
CommercialLaunchDate = streamlit.sidebar.date_input("CommercialLaunchDate", value=p.to_datetime('01/05/2023', format='%d/%m/%Y'))
zone = streamlit.sidebar.selectbox("Zone", ["EUR", "E2A", "ADS", "ADN", "CHN", "MSA"])
DesignType = streamlit.sidebar.selectbox("DesignType", ["CLEAN SHEET", "REFRESH", "EXTENSION"])
BaliseType = streamlit.sidebar.selectbox("BaliseType", ["B+M", "M"])
GanttCategory = streamlit.sidebar.selectbox("GanttCategory", ["WINTER", "SUMMER", "A/S"])
LaunchScope = streamlit.sidebar.selectbox("LaunchScope", ["WW", "Local"])
ProcessType = streamlit.sidebar.selectbox("ProcessType", ["MANU", "C3M"])
MoldTechno = streamlit.sidebar.selectbox("MoldTechno", ["EI", "C3M", "PA/EB/TR"])
TdGMain_Loop1 = streamlit.sidebar.number_input("TdG Loop1", min_value=0, max_value=10, value=1)
TdGMain_Loop2 = streamlit.sidebar.number_input("TdG Loop2", min_value=0, max_value=10, value=1)
Declis = streamlit.sidebar.number_input("Nbr of Indus", min_value=0, max_value=200, value=10)
CAIs_pourcents = streamlit.sidebar.number_input("% of CAIs at the LC", min_value=0, max_value=100, value=100)
is_full_regulatory_test = streamlit.sidebar.checkbox("Regulatory tests include DOT or CCC", True)
is_labelling_mandatory = streamlit.sidebar.checkbox("Include 4 month constraint for Labelling", True)
Mold_entries_per_week_in_G2LC = streamlit.sidebar.number_input("Mold_entries_per_week_in_G2LC", min_value=1.0, max_value=5.0, value=1., step=0.1)

