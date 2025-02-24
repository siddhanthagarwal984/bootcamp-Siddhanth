import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "supervisor/queue.db"

def get_active_jobs():
    """Fetch only pending & processing jobs"""
    conn = sqlite3.connect(DB_PATH)
    query = "SELECT id, job_id, status, created_at FROM jobs WHERE status IN ('pending', 'processing') ORDER BY created_at DESC"
    jobs_df = pd.read_sql_query(query, conn)
    conn.close()
    return jobs_df

st.title("Ops Console - Persistent Queue System")

# Show active jobs
st.header("Active Jobs")
jobs = get_active_jobs()
if jobs.empty:
    st.write("No active jobs found.")
else:
    st.dataframe(jobs)
