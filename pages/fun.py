import os
import streamlit as st
import os
import datetime
import requests
from ics import Calendar, Event
from dotenv import load_dotenv

# load the Environment Variables. 
load_dotenv()
URL_TO_ICS = os.getenv('URL_TO_ICS')
response = requests.get(URL_TO_ICS)
calendar = Calendar(response.text)

def planning(date):
    events = [event for event in calendar.events if event.begin.date() == date]
    events.sort(key=lambda x: x.begin.time())
    for i in events:
        date = i.begin.date().strftime("%d/%m/%Y")
        description = i.description.encode('latin-1').decode('utf-8')   
        location = i.location.encode('latin-1').decode('utf-8')
        horaire = i.begin.time().strftime("%H:%M")
        horaire_fin = i.end.time().strftime("%H:%M")
        st.write(f"Date: {date}")
        st.write(f"Salle: {location[:-1]}")
        st.write(f"Commence à {horaire} et fini à {horaire_fin}")
        st.write(description)
        st.write("\n")
        st.write("\n")



col1, col2, col3 = st.columns(3,gap="large")

with col1:
    date = datetime.date.today()
    planning(date)

with col2:
    date = datetime.date.today() + datetime.timedelta(days=1)
    planning(date)

with col3:
    date = datetime.date.today() + datetime.timedelta(days=2)
    planning(date)
