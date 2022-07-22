import streamlit as st
import pandas as pd
import numpy as np

st.title('Multiply 2 Numbers')



num1 = st.number_input('Enter 1st Number')
num2 = st.number_input('Enter 2nd Number')

prod=num1*num2

st.title(f'{num1} x {num2} = {prod}')