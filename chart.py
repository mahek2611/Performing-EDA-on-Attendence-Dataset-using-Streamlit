import pandas as pd 
import numpy as np 
import streamlit as st 
import matplotlib.pyplot as plt
import seaborn as sns

dataset = st.container()

with dataset:
  st.write("Attendence Dataset")
  df = pd.read_csv('/content/All_Children_Excel_Program_Attendance_20240525.csv')
  st.write(df.head())
  st.write("Attendence")
  st.bar_chart(df.Library.value_counts()[0:15])
  st.write(df.describe())
  st.write("Students of Primary Age Group")
  st.line_chart(df['Primary Age Group'].value_counts())
  st.write("Primary Event Type of Student")
  st.area_chart(df['Primary Event Type'].value_counts())
  st.write("Sum of Attendance")
  attendance_by_person = df.groupby('Title')['Attendance'].sum()[0:15]
  attendance_by_person = attendance_by_person.sort_values(ascending=False)
  st.line_chart(attendance_by_person)
  st.write("Published Status")
  st.bar_chart(df['Published Status'].value_counts())
  st.write("Attendance month Wise")
  events_by_month = df.groupby('Month')['Attendance'].count()
  events_by_month = events_by_month.sort_values(ascending=False)
  st.scatter_chart(events_by_month)