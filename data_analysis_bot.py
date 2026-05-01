import pandas as pd
from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def setup_database(file):
    df = pd.read_csv(file)
    df.columns = df.columns.str.replace(" ", "_")

    engine = create_engine("sqlite:///data.db")
    df.to_sql("data_table", engine, if_exists="replace", index=False)
    
    return df


def create_agent():
    db = SQLDatabase.from_uri("sqlite:///data.db")

    llm = ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.3-70b-versatile"
    )

    agent = create_sql_agent(
        llm=llm,
        db=db,
        verbose=True
    )

    return agent
