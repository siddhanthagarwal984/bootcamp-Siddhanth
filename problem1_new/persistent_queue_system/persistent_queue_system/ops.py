import streamlit as st
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class OpsConsole:
    def __init__(self):
        self.queue = PersistentQSQLite()

    def display_active_jobs(self):
        """
        Display only pending and processing jobs.
        """
        active_statuses = ['pending', 'processing']
        jobs = self.queue.get_jobs_by_status(active_statuses)
        
        st.header("Active Jobs")
        
        if not jobs:
            st.write("No active jobs found.")
        else:
            # Enhanced job display with more details
            for job in jobs:
                with st.expander(f"Job ID: {job['job_id']}"):
                    st.write(f"Status: {job['status']}")
                    st.write(f"Created At: {job['created_at']}")
                    st.write(f"Attempts: {job['attempts']}")
                    if job.get('error_message'):
                        st.warning(f"Error: {job['error_message']}")

    def display_job_summary(self):
        """
        Provide a summary of current job system state.
        """
        job_health = self.queue.monitor_job_health()
        
        st.sidebar.header("Job System Overview")
        for status, details in job_health.items():
            st.sidebar.metric(
                label=f"{status.capitalize()} Jobs", 
                value=details['count']
            )

    def run(self):
        st.title("Operations Console - Job Queue")
        
        self.display_job_summary()
        self.display_active_jobs()

def main():
    console = OpsConsole()
    console.run()

if __name__ == "__main__":
    main()