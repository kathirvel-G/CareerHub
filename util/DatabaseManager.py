
from JobListing import JobListing
from Company import Company
import pyodbc
from Applicant import Applicant 
from JobApplication import JobApplication
class DatabaseManager:
    def __init__(self, connection):
        self.connection = connection

    def initialize_database(self):
        cursor = self.connection.cursor()

        
        try:
       
            cursor.execute("""
                CREATE TABLE Company (
                    CompanyID INT PRIMARY KEY,
                    CompanyName NVARCHAR(255),
                    Location NVARCHAR(255)
                )
            """)
            print("Company table created.")

   
            cursor.execute("""
                CREATE TABLE Applicant (
                    ApplicantID INT PRIMARY KEY,
                    FirstName NVARCHAR(100),
                    LastName NVARCHAR(100),
                    Email NVARCHAR(255),
                    Phone NVARCHAR(20),
                    Resume NVARCHAR(MAX)
                )
            """)
            print("Applicant table created.")

           
            cursor.execute("""
                CREATE TABLE JobListing (
                    JobID INT PRIMARY KEY,
                    CompanyID INT,
                    JobTitle NVARCHAR(255),
                    JobDescription NVARCHAR(MAX),
                    JobLocation NVARCHAR(255),
                    Salary DECIMAL(18, 2),
                    JobType NVARCHAR(50),
                    PostedDate DATETIME,
                    FOREIGN KEY (CompanyID) REFERENCES Company(CompanyID)
                )
            """)
            print("JobListing table created.")

            cursor.execute("""
                CREATE TABLE JobApplication (
                    ApplicationID INT PRIMARY KEY,
                    JobID INT,
                    ApplicantID INT,
                    ApplicationDate DATETIME,
                    CoverLetter NVARCHAR(MAX),
                    FOREIGN KEY (JobID) REFERENCES JobListing(JobID),
                    FOREIGN KEY (ApplicantID) REFERENCES Applicant(ApplicantID)
                )
            """)
            print("JobApplication table created.")

            
            self.connection.commit()
        except pyodbc.Error as e:
            print("An error occurred while creating tables:", e)
        finally:
      
            cursor.close()

    def insert_job_listing(self):
        try:
            cursor = self.connection.cursor()
            job_listings = [
                JobListing(JobId=1, CompanyId=101, JobTitle="Software Developer", JobDescription="Developing web applications", JobLocation="New York", Salary=80000, JobType="Full-time", PostedDate="2024-02-15"),
                JobListing(JobId=2, CompanyId=102, JobTitle="Data Analyst", JobDescription="Analyzing data trends", JobLocation="San Francisco", Salary=75000, JobType="Remote", PostedDate="2024-01-15"),
                JobListing(JobId=3, CompanyId=103, JobTitle="Marketing Manager", JobDescription="Creating marketing strategies", JobLocation="Chicago", Salary=70000, JobType="Full-time", PostedDate="2024-03-11"),
                JobListing(JobId=4, CompanyId=104, JobTitle="Software Engineer", JobDescription="Developing software solutions", JobLocation="Seattle", Salary=85000, JobType="Full-time", PostedDate="2024-01-10"),
                JobListing(JobId=5, CompanyId=105, JobTitle="Business Analyst", JobDescription="Analyzing business processes", JobLocation="Los Angeles", Salary=72000, JobType="Full-time", PostedDate="2024-03-01"),
                JobListing(JobId=6, CompanyId=106, JobTitle="Product Manager", JobDescription="Managing product development", JobLocation="Austin", Salary=90000, JobType="Full-time", PostedDate="2024-03-02"),
                JobListing(JobId=7, CompanyId=107, JobTitle="UI/UX Designer", JobDescription="Designing user interfaces", JobLocation="Boston", Salary=78000, JobType="Full-time", PostedDate="2023-12-15"),
                JobListing(JobId=8, CompanyId=108, JobTitle="Data Scientist", JobDescription="Analyzing complex datasets", JobLocation="Denver", Salary=82000, JobType="Full-time", PostedDate="2023-01-10"),
                JobListing(JobId=9, CompanyId=109, JobTitle="Project Manager", JobDescription="Overseeing project development", JobLocation="Miami", Salary=85000, JobType="Full-time", PostedDate="2024-01-01"),
                JobListing(JobId=10, CompanyId=110, JobTitle="Network Engineer", JobDescription="Managing network infrastructure", JobLocation="Dallas", Salary=80000, JobType="Full-time", PostedDate="2024-03-03")
            ]

            for job in job_listings:
                cursor.execute("""
                    INSERT INTO JobListing (JobId, CompanyId, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (job.JobId, job.CompanyId, job.JobTitle, job.JobDescription, job.JobLocation, job.Salary, job.JobType, job.PostedDate))

            self.connection.commit()
            print("Job listings inserted successfully.")

        except pyodbc.IntegrityError as e:
            if 'FOREIGN KEY' in str(e):
                print("An error occurred due to foreign key constraint violation:", e)
                print("Make sure the CompanyID referenced in the JobListing table exists in the Company table.")
            else:
                print("An error occurred while inserting companies:", e)
                print("Duplicate keys found. Make sure CompanyID values are unique.")
            
            self.connection.rollback()

        finally:
            
            cursor.close()


    def insert_companies(self):

        try:
                cursor = self.connection.cursor()

               
                companies = [
                    Company(CompanyId=101, CompanyName="Company A", Location="New York"),
                    Company(CompanyId=102, CompanyName="Company B", Location="San Francisco"),
                    Company(CompanyId=103, CompanyName="Company C", Location="Chicago"),
                    Company(CompanyId=104, CompanyName="Company D", Location="Seattle"),
                    Company(CompanyId=105, CompanyName="Company E", Location="Los Angeles"),
                    Company(CompanyId=106, CompanyName="Company F", Location="Austin"),
                    Company(CompanyId=107, CompanyName="Company G", Location="Boston"),
                    Company(CompanyId=108, CompanyName="Company H", Location="Denver"),
                    Company(CompanyId=109, CompanyName="Company I", Location="Miami"),
                    Company(CompanyId=110, CompanyName="Company J", Location="Dallas")
                ]

                
                for company in companies:
                    cursor.execute("""
                        INSERT INTO Company (CompanyID, CompanyName, Location)
                        VALUES (?, ?, ?)
                    """, (company.CompanyId, company.CompanyName, company.Location))

               
                self.connection.commit()
                print("Companies inserted successfully.")

        except pyodbc.IntegrityError as e:
            print("An error occurred while inserting companies:", e)
            print("Duplicate keys found. Make sure CompanyID values are unique.")

        finally:
                
            cursor.close()





    def insert_applicants(self):
        try:
            cursor = self.connection.cursor()

          
            applicants = [
                Applicant(ApplicantID=1, FirstName="John", LastName="Doe", Email="john.doe@example.com", Phone="1234567890", Resume="John_Doe_Resume.pdf"),
                Applicant(ApplicantID=2, FirstName="Jane", LastName="Smith", Email="jane.smith@example.com", Phone="9876543210", Resume="Jane_Smith_Resume.pdf"),
                Applicant(ApplicantID=3, FirstName="Michael", LastName="Johnson", Email="michael.johnson@example.com", Phone="5678901234", Resume="Michael_Johnson_Resume.pdf"),
                Applicant(ApplicantID=4, FirstName="Emily", LastName="Brown", Email="emily.brown@example.com", Phone="6789012345", Resume="Emily_Brown_Resume.pdf"),
                Applicant(ApplicantID=5, FirstName="David", LastName="Wilson", Email="david.wilson@example.com", Phone="4567890123", Resume="David_Wilson_Resume.pdf"),
                Applicant(ApplicantID=6, FirstName="Sarah", LastName="Taylor", Email="sarah.taylor@example.com", Phone="7890123456", Resume="Sarah_Taylor_Resume.pdf"),
                Applicant(ApplicantID=7, FirstName="Chris", LastName="Martinez", Email="chris.martinez@example.com", Phone="2345678901", Resume="Chris_Martinez_Resume.pdf"),
                Applicant(ApplicantID=8, FirstName="Amanda", LastName="Anderson", Email="amanda.anderson@example.com", Phone="8901234567", Resume="Amanda_Anderson_Resume.pdf"),
                Applicant(ApplicantID=9, FirstName="Ryan", LastName="Garcia", Email="ryan.garcia@example.com", Phone="3456789012", Resume="Ryan_Garcia_Resume.pdf"),
                Applicant(ApplicantID=10, FirstName="Olivia", LastName="Martinez", Email="olivia.martinez@example.com", Phone="9012345678", Resume="Olivia_Martinez_Resume.pdf")
            ]

           
            for applicant in applicants:
                cursor.execute("""
                    INSERT INTO Applicant (ApplicantID, FirstName, LastName, Email, Phone, Resume)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (applicant.ApplicantID, applicant.FirstName, applicant.LastName, applicant.Email, applicant.Phone, applicant.Resume))

            
            self.connection.commit()
            print("Applicant profile created successfully.")

        except pyodbc.IntegrityError as e:
                print("An error occurred due to duplicate key values:", e)
                print("Ensure that the ApplicantID values are unique.")
           
                self.connection.rollback()

        finally:
          
            cursor.close()






    def insert_job_applications(self):
        try:
            cursor = self.connection.cursor()

            
            job_applications = [
                JobApplication(ApplicationID=1, JobID=1, ApplicantID=1, ApplicationDate="2024-02-18", CoverLetter="John Doe's cover letter"),
                JobApplication(ApplicationID=2, JobID=2, ApplicantID=2, ApplicationDate="2024-01-20", CoverLetter="Jane Smith's cover letter"),
                JobApplication(ApplicationID=3, JobID=3, ApplicantID=3, ApplicationDate="2024-03-25", CoverLetter="Michael Johnson's cover letter"),
                JobApplication(ApplicationID=4, JobID=4, ApplicantID=4, ApplicationDate="2024-01-13", CoverLetter="Emily Brown's cover letter"),
                JobApplication(ApplicationID=5, JobID=5, ApplicantID=5, ApplicationDate="2024-03-09", CoverLetter="David Wilson's cover letter"),
                JobApplication(ApplicationID=6, JobID=6, ApplicantID=6, ApplicationDate="2024-03-15", CoverLetter="Sarah Taylor's cover letter"),
                JobApplication(ApplicationID=7, JobID=7, ApplicantID=7, ApplicationDate="2023-12-17", CoverLetter="Chris Martinez's cover letter"),
                JobApplication(ApplicationID=8, JobID=8, ApplicantID=8, ApplicationDate="2024-03-15", CoverLetter="Amanda Anderson's cover letter"),
                JobApplication(ApplicationID=9, JobID=9, ApplicantID=9, ApplicationDate="2023-01-22", CoverLetter="Ryan Garcia's cover letter"),
                JobApplication(ApplicationID=10, JobID=10, ApplicantID=10, ApplicationDate="2024-03-19", CoverLetter="Olivia Martinez's cover letter")
            ]

            
            for application in job_applications:
                cursor.execute("""
                    INSERT INTO JobApplication (ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter)
                    VALUES (?, ?, ?, ?, ?)
                """, (application.ApplicationID, application.JobID, application.ApplicantID, application.ApplicationDate, application.CoverLetter))

            
            self.connection.commit()
            print("Job applications inserted successfully.")

        except pyodbc.IntegrityError as e:
                if 'FOREIGN KEY' in str(e):
                    print("An error occurred due to foreign key constraint violation:", e)
                    print("Make sure the CompanyID referenced in the JobListing table exists in the Company table.")
                else:
                    print("An error occurred while inserting companies:", e)
                    print("Duplicate keys found. Make sure CompanyID values are unique.")
            
                self.connection.rollback()

        finally:
            
            cursor.close()


    def get_job_listings(self):
        try:
            
            cursor = self.connection.cursor()

            
            cursor.execute("SELECT * FROM JobListing")
            job_listings = cursor.fetchall()

            
            cursor.close()

            return job_listings
        except pyodbc.Error as e:
            print("Error fetching job listings:", e)
            return None

    def get_companies(self):
        try:
            
            cursor = self.connection.cursor()

            
            cursor.execute("SELECT * FROM Company")
            companies = cursor.fetchall()

            
            cursor.close()

            return companies
        except pyodbc.Error as e:
            print("Error fetching companies:", e)
            return None

    def get_applicants(self):
        try:
           
            cursor = self.connection.cursor()

            
            cursor.execute("SELECT * FROM Applicant")
            applicants = cursor.fetchall()

           
            cursor.close()

            return applicants
        except pyodbc.Error as e:
            print("Error fetching applicants:", e)
            return None

    def get_applications_for_job(self, jobID):
        try:
            
            cursor = self.connection.cursor()

            
            cursor.execute("SELECT * FROM JobApplication WHERE JobId = ?", (jobID,))
            job_applications = cursor.fetchall()

            
            cursor.close()

            return job_applications
        except pyodbc.Error as e:
            print("Error fetching job applications for job ID {}: {}".format(jobID, e))
            return None
