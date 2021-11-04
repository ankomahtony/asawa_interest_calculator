import streamlit as st
from functions import *
import pandas as pd
import numpy as np
import math
from bs4 import BeautifulSoup
import requests

url = "https://www.bog.gov.gh/treasury-and-the-markets/treasury-bill-rates/"

# @st.cache
def get_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup
# rows = soup.findAll('tr')



# st.write(tb2)
# st.write(date1)


if st.checkbox("See Current Ghana Treasury Bill Interest Rate"):
    soup = get_data(url)
    data = soup.findAll('tr')
    data1 = soup.findAll("tr", {"id": "table_2_row_0"})
    data2 = soup.findAll("tr", {"id": "table_2_row_1"})
    data3 = soup.findAll("tr", {"id": "table_2_row_2"})
    data4 = soup.findAll("tr", {"id": "table_2_row_3"})
    data5 = soup.findAll("tr", {"id": "table_2_row_4"})
    data6 = soup.findAll("tr", {"id": "table_2_row_5"})

    tb1 = []
    tb2 = []
    tb3 = []
    tb4 = []
    tb5 = []
    tb6 = []

    for dd in data1[0]:
        tb1.append(dd.text)

    for dd in data2[0]:
        tb2.append(dd.text)

    for dd in data3[0]:
        tb3.append(dd.text)


    for dd in data4[0]:
        tb4.append(dd.text)


    for dd in data5[0]:
        tb5.append(dd.text)


    for dd in data6[0]:
        tb6.append(dd.text)


    date1 = tb1[1]
    name1 = tb1[5]
    value1 = float(tb1[9])

    name2 = tb2[5]
    value2 = float(tb2[9])

    name3 = tb3[5]
    value3 = float(tb3[9])
    value4 = float(tb4[9])
    value5 = float(tb5[9])
    value6 = float(tb6[9])
    col1, col2, col3, col4 = st.columns([2,3,3,3])
    col1.write(f'<span style="color:#82E0AA;"> {date1}</span>', unsafe_allow_html=True)
    col1.write('<h3 style="color:#F8C471;">Ghana<h3>', unsafe_allow_html=True)
    col2.metric(name1, f'{round(value1,2)} %',round(value1-value4,2))
    col3.metric(name2, f'{round(value2,2)} %',round(value2-value5,2))
    col4.metric(name3, f'{round(value3,2)} %',round(value3-value6,2))

    st.caption(f'Source: {url}')

c1,c2,c3 = st.columns([2,12,2])
c2.write("<h1 style='color:#F9B0D0;'>INTEREST CALCULATOR</h1>",unsafe_allow_html=True)
# st.markdown('www.bog.gov.org')

what_to_cal = st.selectbox("What do you want to calculate", [ 'Future Value', 'Present Value', 'Interest Rate', 'Terms(Periods)'])



left_column1, right_column1,  = st.columns([4,1])
# st.markdown("""<hr style="height:2px;color:#333;background-color:#999;" /> """, unsafe_allow_html=True)

if what_to_cal != 'Present Value':
    pv = left_column1.number_input('Present Value:', key='principal')
    # right_column1.write("<br>", unsafe_allow_html=True)

if what_to_cal != 'Future Value':
    fv = left_column1.number_input('Future Value:', key='future_value')

# st.markdown("""<hr style="height:1px;color:#333;background-color:#999;" /> """, unsafe_allow_html=True)

type = left_column1.selectbox('Interest Method:', ['Compound', 'Simple'])

left_column, right_column,  = st.columns([4,1])
if what_to_cal != 'Years':
    year = left_column.slider('Years:')
    month = left_column.slider('Month:', min_value=0, max_value=12)
    
    right_column.metric('Year: ', year)
    right_column.metric('Month: ', month)


# st.markdown("""<hr style="height:2px;color:#333;background-color:#999;" /> """, unsafe_allow_html=True)
if what_to_cal != 'Interest Rate':
    interest = left_column.slider('Interest Rate:', 0.00, 100.00, step=0.1)
    with right_column:
        st.metric('Interest Rate:',f'{interest} %')



if what_to_cal == 'Present Value':
    st.write(f'<span style="font-size:20pt; color:#82E0AA;">Present Value: {round(APV(st.session_state.future_value, type, interest, year+month/12),2)}</span>', unsafe_allow_html=True)

    chart_data = pd.DataFrame(
        [APV(st.session_state.future_value, type, interest, i) for i in range(year,-1,-1)],
        columns=['Values'])
    
    if st.checkbox('Show Graph'):
        st.area_chart(chart_data)

elif what_to_cal == 'Future Value':
    st.write(f'<span style="font-size:20pt; color:#F8C471;">Future Value: {round(AFV(st.session_state.principal, type, interest, year+month/12),2)}</span>', unsafe_allow_html=True)

    year_index = [y for y in range(year+1)]
    chart_data = pd.DataFrame({
        'Year':[AFV(st.session_state.principal, type, interest, i) for i in year_index]}, index=year_index)

    if st.checkbox('Show Graph'):
        st.area_chart(chart_data)

elif what_to_cal == 'Interest Rate' and pv > 0:
    st.metric('Interest Rate:', f'{round(interestRate(pv, fv, type, year+month/12) * 100, 2)} %')

elif what_to_cal == 'Years' and pv > 0 and interest != 0:
    year = yearsExpected(pv, fv, type, interest / 100)
    month = math.ceil((year - math.floor(year)) * 12)
    if month == 12:
        month = 0
        year += 1
    st.write('Terms:', math.floor(year),'years ',month, 'months')
