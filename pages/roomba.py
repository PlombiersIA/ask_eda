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
commande = "rien"
message = "Appuyez sur un boutton !"

def get_the_right_room(commande: str) -> list:
    response = requests.get(URL_TO_ICS)
    calendar = Calendar(response.text)
    date = datetime.date.today()
    if commande == "matin":
        matin_aprem = 0
    elif commande == "aprem":
        matin_aprem = 1
    elif commande == "demain":
        date = datetime.date.today() + datetime.timedelta(days=1)
        matin_aprem = 0 
    else:
        matin_aprem = 0
    events = [event for event in calendar.events if event.begin.date() == date]
    if events:
        events.sort(key=lambda x: x.begin.time())
        event = events[matin_aprem]
        description = event.description.encode('latin-1').decode('utf-8')
        location = event.location.encode('latin-1').decode('utf-8')
        horaire = event.begin.time().strftime("%H:%M")
        intervenant = ""
        descript = ""
        for line in description.splitlines():
            if line.startswith("- Intervenant(s) :"):
                intervenant += line
            if line.startswith("- Description :"):
                descript += line
        return [location, horaire, intervenant[2:], descript[2:], date.strftime("%A %d %B")]
    else:
        message = "Fichtre !"
        return message


st.title("Room Ba is now a web app !")
# Add CSS to style the button
st.markdown(
"""
<style>
div.stButton > button:first-child {
    background-color: #eb804c;
    height: 80px;
    width: 100px;
    font-size: 26px;
}
</style>
""",
unsafe_allow_html=True,
)
commande = ""

col1, col2, col3 = st.columns(3)
with col1:
    if st.button("Matin", key="button1"):
        commande = "matin"
with col2:
    if st.button("Aprem", key="button2"):
        commande = "aprem"
with col3:
    if st.button("Demain", key="button3"):
        commande = "demain"
        
st.write("\n")
st.write("\n")

col4, col5, col6 = st.columns(3)
with col4:
    st.write(":calendar:")
with col5:
    if commande != "rien":
        message = get_the_right_room(commande)
    if message != "Fichtre !" and message !="Appuyez sur un boutton !":
        st.write(f"Date: {message[4]}")
        st.write(f"Salle(s): {message[0]}")
        st.write(f"Commence à: {message[1]}")
        st.write(message[2])
        st.write(message[3])
    elif message == "Fichtre !":
        st.write(message)
        st.write("Aucun événement trouvé pour cette date.")
    else:
        st.write(message)
