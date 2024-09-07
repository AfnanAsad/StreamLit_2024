import streamlit as st

st.header("_Streamlit_ is Fun :blue[cool] :sunglasses:angry:")
st.header("This is a header with a divider", divider="gray")

code = '''def check():
        print('All Fine')'''
st.code(code,language="python")
