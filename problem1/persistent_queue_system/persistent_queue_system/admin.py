from persistent_queue_system.db import get_db_connection
import streamlit as st
import sqlite3
import pandas as pd

DB_PATH = "supervisor/queue.db"

def get_jobs():
    """Fetch all jobs from the database"""
    #conn = sqlite3.connect(DB_PATH)
    conn = get_db_connection()
    query = "SELECT id, job_id, status, created_at FROM jobs ORDER BY created_at DESC"
    jobs_df = pd.read_sql_query(query, conn)
    conn.close()
    return jobs_df

def update_job_status(job_id, new_status):
    """Update a job's status in the database"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("UPDATE jobs SET status = ? WHERE id = ?", (new_status, job_id))
    conn.commit()
    conn.close()

# Streamlit UI
st.title("Admin Console - Persistent Queue System")

# Show job statistics
jobs = get_jobs()
st.sidebar.header("Job Statistics")
st.sidebar.write(f"Total Jobs: {len(jobs)}")
st.sidebar.write(f"Pending: {len(jobs[jobs['status'] == 'pending'])}")
st.sidebar.write(f"Processing: {len(jobs[jobs['status'] == 'processing'])}")
st.sidebar.write(f"Completed: {len(jobs[jobs['status'] == 'done'])}")
st.sidebar.write(f"Failed: {len(jobs[jobs['status'] == 'failed'])}")

# Show Job Table
st.header("Job Queue")
if jobs.empty:
    st.write("No jobs found.")
else:
    st.dataframe(jobs)

    # Job action section
    job_id = st.text_input("Enter Job ID to modify:", "")
    action = st.radio("Action:", ["Resubmit", "Cancel"])

    if st.button("Update Job"):
        if job_id.isdigit():
            new_status = "pending" if action == "Resubmit" else "cancelled"
            update_job_status(int(job_id), new_status)
            st.success(f"Job {job_id} updated to {new_status}. Refresh to see changes.")
        else:
            st.error("Invalid Job ID.")
