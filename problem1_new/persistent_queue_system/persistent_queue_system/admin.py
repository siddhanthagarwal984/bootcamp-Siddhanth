import streamlit as st
from persistent_queue_system.queue.sqlite_queue import PersistentQSQLite

class AdminConsole:
    def __init__(self):
        self.queue = PersistentQSQLite()

    def display_job_statistics(self):
        """Display comprehensive job statistics."""
        job_health = self.queue.monitor_job_health()
        
        st.sidebar.header("Job Statistics")
        for status, details in job_health.items():
            st.sidebar.write(f"{status.capitalize()} Jobs: {details['count']}")
            st.sidebar.write(f"  Avg Attempts: {details['avg_attempts']}")
            st.sidebar.write(f"  Max Age (days): {details['max_age_days']}")

    def display_job_queue(self):
        """Display jobs with status filtering and management."""
        statuses = st.multiselect(
            "Select Job Statuses", 
            ['pending', 'processing', 'done', 'failed', 'permanently_failed'],
            default=['pending', 'processing']
        )
        
        jobs = self.queue.get_jobs_by_status(statuses)
        
        if not jobs:
            st.write("No jobs found.")
        else:
            st.dataframe(jobs)

    def job_management_actions(self):
        """Provide job management interface."""
        job_id = st.text_input("Enter Job ID to modify:", "")
        action = st.radio("Action:", ["Resubmit", "Mark Failed", "Cancel"])

        if st.button("Update Job"):
            try:
                if action == "Resubmit":
                    self.queue.mark_failed(job_id)
                elif action == "Mark Failed":
                    self.queue.mark_failed(job_id, "Manual intervention")
                # Note: Cancellation is now a standard job status
                
                st.success(f"Job {job_id} updated successfully.")
            except ValueError as e:
                st.error(str(e))

    def run(self):
        st.title("Admin Console - Persistent Queue System")
        
        self.display_job_statistics()
        self.display_job_queue()
        self.job_management_actions()

def main():
    console = AdminConsole()
    console.run()

if __name__ == "__main__":
    main()