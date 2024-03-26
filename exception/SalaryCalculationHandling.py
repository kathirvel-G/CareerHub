
from JobListing import JobListing


class InvalidSalaryException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



def calculate_average_salary(job_listings):
    total_salary = 0
    valid_job_listings = []
    invalid_job_listings = []

    for job in job_listings:
        try:
            if job.Salary < 0:
                raise InvalidSalaryException(f"Negative salary found for JobID: {job.JobID}")
            total_salary += job.Salary
            valid_job_listings.append(job)
        except InvalidSalaryException as e:
            invalid_job_listings.append(job)
            print("Error:", e)

    if valid_job_listings:
        average_salary = total_salary / len(valid_job_listings)
        print("Average salary offered:", average_salary)
    else:
        print("No valid job listings found")

    if invalid_job_listings:
        print("Invalid job listings:", invalid_job_listings)


