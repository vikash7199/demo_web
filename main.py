import streamlit as st
# import pandas as pd
# st.title("Hello world")
# st.header("python")
# st.subheader("java ")
# st.markdown("I love python language mostly")

# st.code(""" for i in range(2,4):
#         print("india)
#         """)

# dataset = pd.read_csv("set.csv")
# st.dataframe(dataset)


#create form
name = st.text_input("Enter your name")
fname = st.text_input("Enter your father name")
add = st.text_area("Enter Address")
sem = st.selectbox("select your semester:",(1,2,3,4,5,6,7,8))
button = st.button("Submit")

if button:
    st.markdown(f"""
        Name :{name}
        Father name :{fname}
        Address :{add}
        semester :{sem}""")
            
