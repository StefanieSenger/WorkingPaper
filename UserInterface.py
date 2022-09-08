
import streamlit as st
import requests
import io
#from pdfminer.high_level import extract_text

st.markdown('# PAPER FELLOW')
#file=st.file_uploader('Upload a file', type='pdf')
st.markdown('### Insert the path to your file to continue')
#url_upload='http://127.0.0.1:8000/uploadfile'
#st.markdown(file.getvalue())
#response = requests.post(url, {'file':file})
#st.markdown(response.content)

url_path='http://127.0.0.1:8000/path'
path = st.text_input('Insert path:')
params={'path':path}
if path:

    try:
        st.markdown('### Oh so you are interesting in:')
        response=requests.get(url_path, params).json()
        st.markdown(f"{response['topic']} and I'm {response['accuracy']*100}% sure")
    except:
        'File not found'
