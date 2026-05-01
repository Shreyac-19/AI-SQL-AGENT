import streamlit as st
from data_analysis_bot import setup_database, create_agent
from advance_data_analysis import plot_data

st.title("AI SQL Data Analyst Agent")

uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file:
    df = setup_database(uploaded_file)

    st.subheader("Data Preview")
    st.dataframe(df.head())

    agent = create_agent()

    question = st.text_input("Ask your question:")

    if question:
        with st.spinner("Processing..."):
            result = agent.run(question)

        st.subheader("Answer")
        st.write(result)

    st.subheader("Visualization")
    fig = plot_data(df)
    st.pyplot(fig)