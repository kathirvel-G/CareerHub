from datetime import datetime

class JobApplication:
    def __init__(self, ApplicationID, JobID, ApplicantID, ApplicationDate, CoverLetter):
        self.ApplicationID = ApplicationID
        self.JobID = JobID
        self.ApplicantID = ApplicantID
        self.ApplicationDate = ApplicationDate
        self.CoverLetter = CoverLetter


    def get_ApplicationID(self):
        return self.ApplicationID

    def get_JobID(self):
        return self.JobID

    def get_ApplicantID(self):
        return self.ApplicantID

    def get_ApplicationDate(self):
        return self.ApplicationDate

    def get_CoverLetter(self):
        return self.CoverLetter

    def set_ApplicationID(self, ApplicationID):
        self.ApplicationID = ApplicationID
    def set_JobID(self, JobID):
        self.JobID = JobID

    def set_ApplicantID(self, ApplicantID):
        self.ApplicantID = ApplicantID

    def set_ApplicationDate(self, ApplicationDate):
        self.ApplicationDate = ApplicationDate

    def set_CoverLetter(self, CoverLetter):
        self.CoverLetter = CoverLetter

