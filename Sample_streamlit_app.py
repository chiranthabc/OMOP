pip install matplotlib

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
 
# Set page title
st.title('Simple Streamlit App')
 
# Generate some random data
x = np.linspace(0, 10, 100)
y = np.sin(x)
 
# Plot the data
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Sine Wave Plot')
st.pyplot(fig)
