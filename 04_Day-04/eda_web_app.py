from re import A
import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

from pandas_profiling import ProfileReport, profile_report

st.markdown('''
        # Exploratory Data Analysis Web App
        This app is developed by DigiPro Developers called **EDA App**        
        ''')


# How to uplaod a file from PC

with st.sidebar.header('Upload your dataset in CSV format'):
    uploaded_file = st.sidebar.file_uploader('Upload your file', type=['CSV'])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown('[Example CSV File](https://raw.githubusercontent.com/AammarTufail/pythonkachilla_version2/main/02_pandas_tips%26tricks/tips.csv)')


# Profiling report for Pandas

if uploaded_file is not None:
    @st.cache
    
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv

    df = load_csv()

    pr = ProfileReport(df, explorative=True)
    st.header('**Input Dataframe**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV File. Please, uplaod your required dataset.')
    if st.button('Press to use example data'):
        # Example dataset
        @st.cache

        def load_data():
            a = pd.DataFrame(np.random.rand(100,5),
                                columns=['A','B','C','D','E'])
            return a
        df = load_data()
        pr = ProfileReport(df, explorative=True)
        st.header('**Input Dataframe**')
        st.write(df)
        st.write('---')
        st.header('**Profiling Report with Pandas')
        st_profile_report(pr)

st.markdown('''       
        *All rights reserved with Developer & Data Analysit Syed Zafar Abbas*
        ''')