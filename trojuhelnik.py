import streamlit as st
import math
st.markdown("## Výpočty v pravoúhlém trojúhelníku ABC")
věta="Toto je ukázka využití prostřední streamlit.io v jazyku Python. Prostřední streamlit umožňuje zadávání a zobrazování dat prostřednictvím XHTML kódu, který lze zobrazit na každém webovém prohlížeči. Jazyk XHTML nemusíme vůbec znát. Zde se bude počítat odvěsna pravoúhlého trojúhelníku ABC. Zadávat se budou dvě číselné hodnoty: délka přepony c; délka odvěsny b. Počítá se odvěsna a. Zadají-li se vstupní parametry chybně, výpočet se neprovede. Bude pak možné zadání opravit. Délka přepony musí být větší než dékla odvěsky, obě čísla musí být kladná."
st.write(věta)
st.image("01_trojuhelnik.jpg",caption="Obrázek trojúhelníku ABC")
with st.form("form_zadani"):
    strana_c=st.number_input("Zadej délku přepony c:",step=0.1,value=5.0,)
    strana_b=st.number_input("Zadej délku odvěsny b:",step=0.1,value=4.0,)
    tlačítko=st.form_submit_button("Výpočet odvěsny a")
    
    if tlačítko:
        if (strana_c>0) and (strana_b>0) and (strana_c>strana_b):
            st.write(f"Zadal jsi správné hodnoty. Přepona c = {strana_c}, odvěsna b = {strana_b}.")
            strana_a=math.sqrt(strana_c**2 - strana_b**2)
            st.write(f"Délka odvěsny a = {strana_a:.2f}")
        else:
             st.write("Zadal jsi chybné hodnoty. Zadání oprav.")
       
if st.button("Znovu načíst hodnoty"):
        st.experimental_rerun()
        
        


