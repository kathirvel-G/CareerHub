
import sys
sys.path.append('C:/Users/kathir/OneDrive/Desktop/CareerHub/util')
sys.path.append('C:/Users/kathir/OneDrive/Desktop/CareerHub/dao')
from datetime import datetime 
from db_conn_util import DBConnUtil
from DataAccessObjectImpl import DataAccessObjectImpl

import uuid

def display_menu():
    print("Job Board Simulation")
    print("1. Retrieve Job Listings")
    print("2. Post a Job Listing")
    print("3. Search Job Listings by Salary Range")
    print("4. Create account")
    print("5. Submit a Job Application")
    print("6. Exit")

def retrieve_job_listings(dao):
    print("Retrieving job listings:")
    dao.retrieve_job_listings()
    print()

def post_job_listing(dao):
    print("Posting a job listing:")
    dao.post_job_listing()
    print()

def search_job_listings_by_salary_range(dao):
    print("Search job listings by salary range:")
    min_salary = float(input("Enter minimum salary: "))
    max_salary = float(input("Enter maximum salary: "))
    job_listings = dao.search_job_listings_within_salary_range(min_salary, max_salary)
    if job_listings:
        print("Job listings within salary range:")
        for listing in job_listings:
            print(listing)
    else:
        print("No job listings found within the specified salary range.")
    print()

def insert_applicant(dao):
    print("Inserting an applicant:")
    dao.insert_applicant_into_db()
    print()

def submit_job_application(dao):
    print("Submitting a job application:")
    job_id = int(input("Enter Job ID: "))
    applicant_id = int(input("Enter Applicant ID: "))
    cover_letter = input("Enter Cover Letter: ")
    application_id = str(datetime.now().strftime("%Y%m%d%H%M%S"))
    applicant_id_str = str(applicant_id)  
    application_id = applicant_id_str[:5]  
    dao.submit_application(job_id, applicant_id, cover_letter, application_id)
    print()

def main():
    dao = DataAccessObjectImpl()
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        try:
            if choice == "1":
                retrieve_job_listings(dao)
            elif choice == "2":
                post_job_listing(dao)
            elif choice == "3":
                search_job_listings_by_salary_range(dao)
            elif choice == "4":
                insert_applicant(dao)
            elif choice == "5":
                submit_job_application(dao)
            elif choice == "6":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except Exception as e:
            print("An error occurred:", e)

if __name__ == "__main__":
    main()
