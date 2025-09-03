import streamlit as st
import time
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

st.set_page_config(layout="wide")

IMAGE_URL = "https://images.pexels.com/photos/932638/pexels-photo-932638.jpeg?auto=compress&cs=tinysrgb&w=1920"


st.markdown(f"""
<style>
.stApp {{
  background: linear-gradient(rgba(0,0,0,.35), rgba(0,0,0,.35)),
              url('{IMAGE_URL}') no-repeat center center fixed !important;
  background-size: cover !important;
}}
div[data-testid="stAppViewContainer"] > .main {{
  background: transparent !important;
}}
div.block-container {{
  background: transparent !important;
}}
section[data-testid="stSidebar"] {{
  background: rgba(255,255,255,0.08) !important;
  backdrop-filter: blur(6px);
}}
section[data-testid="stChatInput"] {{
  background: rgba(255,255,255,0.10) !important;
  backdrop-filter: blur(8px);
  border-top: 1px solid rgba(255,255,255,0.15);
  box-shadow: 0 -2px 12px rgba(0,0,0,0.15);
}}
header[data-testid="stHeader"] {{
  background: transparent !important;
}}
</style>
""", unsafe_allow_html=True)


st.write("""
# FLOATCHAT
AI-Powered Conversational Interface for ARGO Ocean Data Discovery and Visualization.
""")
st.sidebar.image("logo.png", width=200)
st.sidebar.title("OPTIONS")
page = st.sidebar.radio("Go to:", ["Home", "Explore Data", "About"])


information = """
Temperature: Measures the temperature of the ocean at various depths,
which is crucial for understanding climate change and marine ecosystems.

Salinity: Indicates the salt concentration in seawater, affecting ocean circulation and marine life.

Ocean Currents: Data on the movement of ocean water, which influences weather patterns and marine navigation.
"""

query = st.chat_input("Enter your query about ocean data:")


def steam_data():
    for sentence in information.strip().splitlines():
        if sentence.strip():
            yield sentence + "  \n"
            time.sleep(0.3)

def plot_scatter_map():
    map_path = "arabian_sea.png" 
    img = mpimg.imread(map_path)
    height, width = img.shape[:2]


    num_points = 50
    x = np.random.uniform(0, width, num_points)
    y = np.random.uniform(0, height, num_points)

    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.scatter(x, y, c='red', s=40, alpha=0.7)
    ax.axis('off')
    st.pyplot(fig)

if query:
    st.write_stream(steam_data())  
    plot_scatter_map()            
