import uuid
from datetime import datetime
from JobApplication import JobApplication
class Applicant:
    def __init__(self, ApplicantID, FirstName, LastName, Email, Phone, Resume):
        self.ApplicantID = ApplicantID  
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Phone = Phone
        self.Resume = Resume

    
    def get_ApplicantID(self):
        return self.ApplicantID

    def get_FirstName(self):
        return self.FirstName

    def get_LastName(self):
        return self.LastName

    def get_Email(self):
        return self.Email

    def get_Phone(self):
        return self.Phone

    def get_Resume(self):
        return self.Resume


    def set_ApplicantID(self, ApplicantID):
        self.ApplicantID = ApplicantID

    def set_FirstName(self, FirstName):
        self.FirstName = FirstName

    def set_LastName(self, LastName):
        self.LastName = LastName

    def set_Email(self, Email):
        self.Email = Email

    def set_Phone(self, Phone):
        self.Phone = Phone

    def set_Resume(self, Resume):
        self.Resume = Resume

    def CreateProfile(self, email, firstName, lastName, phone):
        self.Email = email
        self.FirstName = firstName
        self.LastName = lastName
        self.Phone = phone


    def ApplyForJob(self, jobID, coverLetter):
 
        application_id = application_id = str(uuid.uuid4()) 
        application_date = datetime.now()  
        new_application = JobApplication(ApplicationID=application_id, JobID=jobID,
                                         ApplicantID=self.ApplicantID, ApplicationDate=application_date,
                                         CoverLetter=coverLetter)

       
        return new_application


    
