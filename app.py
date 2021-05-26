import streamlit as st
import logging 
import os
from datetime import datetime

def load_logs_file():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    logs_file = open(dir_root + '/logs_file.log', 'r')
    return logs_file


logging.info(str(datetime.now()))

logs_data = load_logs_file()

st.write('Refresh to see logs.')
list_of_logs = ""
for line in logs_data:
    list_of_logs += "> "+ line            
st.code(list_of_logs)