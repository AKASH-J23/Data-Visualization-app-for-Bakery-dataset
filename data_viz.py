import pandas as pd
import numpy as np 
import streamlit as st
import matplotlib.pyplot as plt

figure=plt.figure()
def date_converter(date_col):
    result=list()
    values=date_col.values
    for value in values:
        result.append(str(value).split(" ")[0])
    return result

st.markdown("<h1 style='text-align: center;'> Data Visualization For Bakery Dataset </h1>",unsafe_allow_html=True)
st.markdown("---",unsafe_allow_html=True)
files_names=list()
files=st.file_uploader("Upload Files",type=["csv"])
if files:
    option= st.radio("Select Entity against Date",options=["None","TransactionNo","Items","Daypart","DayType"])
    if option!="None":
        data=pd.read_csv(files)
        dates=date_converter(data["DateTime"])
        item=list(data[option])
        index=np.arange(len(dates))
        # plt.xticks(index,dates)
        # plt.gcf().autofmt_xdate()
        plt.bar(index,item)
    st.write(figure)

