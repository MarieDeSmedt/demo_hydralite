
import hydralit as hy
from page.firstPage import display1
from page.secondPage import display2

#app = hy.HydraApp(title='demo hydralite')
app = hy.HydraApp(title='demo hydralite',favicon="🐙",hide_streamlit_markers=True,use_navbar=True, navbar_sticky=True)

@app.addapp()
def firstpage():
    display1()

@app.addapp()
def secondpage():
    display2()


app.run()