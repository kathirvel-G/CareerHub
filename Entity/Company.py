from  JobListing import JobListing

class Company:

    def __init__(self, CompanyId, CompanyName, Location):
        self.CompanyId = CompanyId
        self.CompanyName = CompanyName
        self.Location = Location
        self.JobListings = []

    def get_CompanyId(self):
         return self.CompanyId

    def get_CompanyName(self):
        return self.CompanyName

    def get_Location(self):
        return self.Location

    
    def set_CompanyId(self, CompanyId):
        self.CompanyId = CompanyId

    def set_CompanyName(self, CompanyName):
        self.CompanyName = CompanyName

    def set_Location(self, Location):
        self.Location = Location

    def PostJob(self, jobTitle, jobDescription, jobLocation, salary, jobType):
        new_job = JobListing(JobId=len(self.JobListings) + 1, CompanyId=self.CompanyId,
                             JobTitle=jobTitle, JobDescription=jobDescription,
                             JobLocation=jobLocation, Salary=salary, JobType=jobType,
                             PostedDate="25-02-2024")
        self.JobListings.append(new_job)
        return self.JobListings

    def GetJobs(self):
        return self.JobListings



