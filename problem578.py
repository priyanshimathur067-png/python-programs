
class JobTracker:

    def __init__(self):
        self.jobs = []

    def add_job(self, company, role, status):
        job = {
            "company": company,
            "role": role,
            "status": status
        }

        self.jobs.append(job)
        print("Job application added!")

    def show_jobs(self):
        for job in self.jobs:
            print(job)

    def update_status(self, company, new_status):
        for job in self.jobs:
            if job["company"].lower() == company.lower():
                job["status"] = new_status
                print("Status updated!")
                return

        print("Company not found!")

    def search_company(self, company):
        for job in self.jobs:
            if job["company"].lower() == company.lower():
                print(job)
                return

        print("No application found!")

    def count_status(self):
        status_count = {}

        for job in self.jobs:
            status = job["status"]
            status_count[status] = (
                status_count.get(status, 0) + 1
            )

        print(status_count)

    def show_interviews(self):
        for job in self.jobs:
            if job["status"].lower() == "interview":
                print(job)


tracker = JobTracker()

tracker.add_job("Google", "Python Developer", "Applied")
tracker.add_job("Infosys", "Software Engineer", "Interview")
tracker.add_job("TCS", "React Developer", "Rejected")
tracker.add_job("Wipro", "Python Developer", "Interview")

tracker.show_jobs()

tracker.update_status("Google", "Interview")

tracker.search_company("Google")

tracker.count_status()

tracker.show_interviews()
