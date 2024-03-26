import sys
sys.path.append('C:/Users/kathir/OneDrive/Desktop/CareerHub/util')
sys.path.append('C:/Users/kathir/OneDrive/Desktop/CareerHub/exception')
sys.path.append('C:/Users/kathir/OneDrive/Desktop/CareerHub/Entity')
from datetime import datetime

from db_conn_util import DBConnUtil
from JobListing import JobListing 
from Applicant import Applicant
import pyodbc
from DatabaseManager import DatabaseManager
from Company import Company
from EmailFormatHandling import InvalidEmailFormatException
from EmailFormatHandling import validate_email
from DatabaseConnectionHandling import DatabaseConnectionError
from DatabaseConnectionHandling import DatabaseQueryError
from ApplicationDeadlineHandling import ApplicationDeadlineException
from ApplicationDeadlineHandling import submit_application1
from FileUploadHandling import FileUploadException
from FileUploadHandling import upload_resume


class DataAccessObjectImpl:
    def __init__(self):
        self.db_conn_util = DBConnUtil()

    @staticmethod
    def retrieve_job_listings():
        try:
           
            connection = DBConnUtil.get_connection()

         
            cursor = connection.cursor()

           
            cursor.execute("SELECT JobID, CompanyID, JobTitle, Salary FROM JobListing")

            
            job_listings = cursor.fetchall()

            
            for job_listing in job_listings:
                print(job_listing)

           
            cursor.close()
            connection.close()

        except pyodbc.Error as e:
            
            raise DatabaseQueryError("Error retrieving joblistings: ")


    def post_job_listing(self):
        try:
            
            connection = DBConnUtil.get_connection()

            
            print("Enter job listing information:")
            JobID = input("Job ID: ")
            CompanyID = input("Company ID: ")
            JobTitle = input("Job Title: ")
            JobDescription = input("Job Description: ")
            JobLocation = input("Job Location: ")
            Salary = input("Salary: ")
            JobType = input("Job Type: ")
            PostedDate = input("Posted Date (YYYY-MM-DD): ")

           
            job_listing = JobListing(JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)

            
            cursor = connection.cursor()
            cursor.execute(""" 
                INSERT INTO JobListing (JobID, CompanyID, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (job_listing.JobId, job_listing.CompanyId, job_listing.JobTitle, job_listing.JobDescription,
                  job_listing.JobLocation, job_listing.Salary, job_listing.JobType, job_listing.PostedDate))

           
            connection.commit()
            print("Job listing posted successfully.")

        except pyodbc.Error as e:
            
            raise DatabaseQueryError("Error posting job listing:")
            # print("Error posting job listing: ")

        finally:
           
            cursor.close()
            connection.close()

    @staticmethod
    def search_job_listings_within_salary_range(min_salary, max_salary):
        try:
           
            connection = DBConnUtil.get_connection()

            
            cursor = connection.cursor()
            cursor.execute("""
                SELECT j.JobTitle, c.CompanyName, j.Salary
                FROM JobListing j
                INNER JOIN Company c ON j.CompanyId = c.CompanyId
                WHERE j.Salary BETWEEN ? AND ?
            """, (min_salary, max_salary))

           
            job_listings = []
            for row in cursor.fetchall():
                job_title, company_name, salary = row
                job_listings.append((job_title, company_name, salary))

            
            cursor.close()
            connection.close()

            return job_listings

        except pyodbc.Error as e:
            
            raise DatabaseQueryError("Error searching joblistings: ")
            return []

    def insert_applicant_into_db(applicant):

        try:
            print("Enter applicant information:")
            ApplicantID = int(input("Applicant ID: "))
            FirstName = input("First Name: ")
            LastName = input("Last Name: ")
            Email = input("Email: ")
            validate_email(Email)
            Phone = input("Phone: ")
            Resume = input("Resume: ")
            applicant = Applicant(ApplicantID, FirstName, LastName, Email, Phone, Resume)
            
            
            connection = DBConnUtil.get_connection()

            
            cursor = connection.cursor()

            
            cursor.execute("""
                INSERT INTO Applicant (ApplicantID, FirstName, LastName, Email, Phone, Resume)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (applicant.ApplicantID, applicant.FirstName, applicant.LastName, applicant.Email, applicant.Phone, applicant.Resume))

           
            connection.commit()
            print("Applicant profile created successfully.")

            
            cursor.close()
            connection.close()

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error inserting applicant: ")
        except Exception as e:
            print("An unexpected error occurred:", e)



    def submit_application(self, job_id, applicant_id, cover_letter, application_id):
        try:
            connection = DBConnUtil.get_connection()
            cursor = connection.cursor()

            
            current_time = datetime.now()

            deadline = datetime(2024, 4, 13, 23, 59, 59)

            
            if current_time > deadline:
                raise ApplicationDeadlineException()

            else:
                cursor.execute("""
                    INSERT INTO JobApplication(ApplicationID, JobId, ApplicantID, ApplicationDate, CoverLetter)
                    VALUES (?, ?, ?, ?, ?)
                """, (application_id, job_id, applicant_id, current_time, cover_letter))

                connection.commit()
                print("Job application submitted successfully.")

        except pyodbc.Error as e:
            raise DatabaseQueryError("Error: {}".format(str(e)))

        except ApplicationDeadlineException as e:
            print("Application submission error:", e)

        finally:
            cursor.close()
            connection.close()



