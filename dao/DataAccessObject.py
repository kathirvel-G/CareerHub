from abc import ABC, abstractmethod

class DataAccessObject(ABC):
    @abstractmethod
    def retrieve_job_listings(self):
        pass

    @abstractmethod
    def create_applicant_profile(self, applicant_data):
        pass

    @abstractmethod
    def submit_job_application(self, job_id, applicant_id, application_data):
        pass

    @abstractmethod
    def post_job_listing(self, job_data):
        pass

    @abstractmethod
    def search_job_listings_by_salary_range(self, min_salary, max_salary):
        pass
