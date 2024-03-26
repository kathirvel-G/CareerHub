class JobListing:
    def __init__(self, JobId, CompanyId, JobTitle, JobDescription, JobLocation, Salary, JobType, PostedDate):
        self.JobId = JobId
        self.CompanyId = CompanyId
        self.JobTitle = JobTitle
        self.JobDescription = JobDescription
        self.JobLocation = JobLocation 
        self.Salary = Salary
        self.JobType = JobType 
        self.PostedDate = PostedDate 
        self.applicants = [] 

    def set_JobId(self, JobId):
        self.JobId = JobId
        
    def set_CompanyId(self, CompanyId):
        self.CompanyId = CompanyId

    def set_JobTitle(self,JobTitle):
        self.JobTitle = JobTitle

    def set_JobDescription(self,JobDescription):
        self.JobDescription = JobDescription

    def set_JobLocation(self, JobLocation):
        self.JobLocation = JobLocation

    def set_Salary(self,Salary):
        self.Salary = Salary

    def set_JobType(self, JobType):
        self.JobType = JobType

    def set_PostedDate(self, PostedDate):
        self.PostedDate = PostedDate


    def get_JobId(self):
        return self.JobId

    def get_CompanyId(self):
        return self.CompanyId

    def get_JobTitle(self):
        return self.JobTitle

    def get_JobDescription(self):
        return self.JobDescription

    def get_JobLocation(self):
        return self.JobLocation

    def get_Salary(self):
        return self.Salary

    def get_JobType(self):
        return self.JobType

    def get_PostedDate(self):
        return self.PostedDate
            


    def Apply(self, applicant_id, cover_letter):
            self.applicants.append({"applicant_id": applicant_id, "cover_letter": cover_letter})

    def GetApplicants(self):
            return self.applicants






