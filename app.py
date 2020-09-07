import streamlit as st

import base64
from wit import Wit

client = Wit('MVJCGTO5PI7CIB7WZZLTRWDIVEEDPA7D')

from PIL import Image


file_ = open("./1.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()



    
    

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" style="width: 100%;max-width: 400px;height: auto;display: block;margin-left: auto;margin-right: auto;" alt="robobootcamp gif">',
    unsafe_allow_html=True,
)
st.write("")
st.write("")
st.write("")
st.write("ROBO-BootCamp: AI Powered BootCamp Solution.")
st.write("Enter What You want To Learn And Get Some Resources.")

t = st.text_input("What would you like learn?")

start = st.button("Get Resources")
#med = st.button("Get User Tweets")
stop = st.button("Reset App")


if start:
    resp = client.message(t)
    try:
        if (resp['intents'][0]['confidence']) > 0.8:
            st.write(resp)
        else:
            st.write("Sorry, I don't Have Resources On This Topic Yet.")

    except:
        st.write("No intents were detected")