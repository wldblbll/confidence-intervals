#import pandas as p
import sys
import datetime
#import plotly.express as px
import streamlit
import os
#from math import ceil as arrondi_sup
import math

import pandas as p

__version__ = 1.0

try:
    streamlit.set_option('deprecation.showfileUploaderEncoding', False)
except:
    pass

def get_proportion_bounds(n, r, z):
    ##### Calculation
    p = r/n
    q = 1-p
    A = 2*r + z*z
    B = z*math.sqrt(z*z+4*r*q)
    C = 2.*(n+z*z)
    # Confidence Interval Lower Bound
    cilb = (A-B)/C
    # Confidence Interval Upper Bound
    ciup = (A+B)/C
    return cilb, ciub


streamlit.title("Confidence Intervals calculator")
status = streamlit.empty()

CI_type = streamlit.sidebar.selectbox("CI Type", ["Proportions", "Others: TBD"])

if CI_type=="Proportions":
    n = streamlit.sidebar.number_input("N (size)", min_value=0, max_value=10000000, value=10)
    r = streamlit.sidebar.number_input("r (observed occurences)", min_value=0, max_value=n, value=0)
    z_dic = {"90%":1.645, "95%":1.960, "99%":2.576}
    confidence_level = streamlit.sidebar.selectbox("Confidence level", list(z_dic.keys()))    
    z = z_dic[confidence_level]
    cilb, ciub = get_proportion_bounds(n, r, z)

    streamlit.write(f"for n={n} and r={r}")
    streamlit.write("measured proportion is %.1f%%" % (float(r/n)*100))
    streamlit.write("CI is [%.1f%%  , %.1f%%]" % (cilb*100, ciup*100))


