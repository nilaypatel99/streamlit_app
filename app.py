import streamlit as st

st.title("Whitefang")

col1,col2=st.columns(2)

with col1:
    st.image('images.jfif')
with col2:
    st.write("""White Fang, novel by Jack London, published in 1906. The novel was intended as a companion piece to The Call of the Wild (1903), in which a domesticated dog reverts to a wild state. White Fang is the story of a wolf dog that is rescued from its brutal owner and gradually becomes domesticated through the patience and kindness of its new owner, Weedon Scott. White Fang eventually defends Scott’s father from attack by an escaped convict.""")
