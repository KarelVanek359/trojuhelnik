import streamlit as st
with st.form("form_zadani"):
    aaa=st.number_input("Zadej celé číslo a:",step=0.1,value=10.0,)
    bbb=st.number_input("Zadej celé číslo b:",step=0.1,value=10.0,)
    ccc=st.text_input("Zadej řetězec:")
    tlačítko=st.form_submit_button("Odeslat")
    
    if tlačítko:
        st.write(f"Zadal jsi číslo: {aaa+bbb}")
        st.write()
       
if st.button("Znovu načíst formulář"):
        st.experimental_rerun()
        
        


