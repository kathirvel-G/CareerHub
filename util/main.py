from db_property_util import DBPropertyUtil
from db_conn_util import DBConnUtil
from DatabaseManager import DatabaseManager
from JobListing import JobListing
from Company import Company
from Applicant import Applicant 
from JobApplication import JobApplication
# from DatabaseConnectionHandling import DatabaseQueryError

if __name__ == "__main__":
    

    # Getting database connection using DBConnUtil
    connection = DBConnUtil.get_connection()
    print("Connection Object:", connection)

    db_manager = DatabaseManager(connection)
    db_manager.initialize_database()

    


    # for company in companies:
    # db_manager.insert_companies()

    

    db_manager.insert_job_listing()


    # db_manager.insert_applicants()
    # db_manager.insert_job_applications()


    # print(db_manager.get_job_listings())
    # print(db_manager.get_companies())
    # print(db_manager.get_applicants())
    # print(db_manager.get_applications_for_job(1))



    


    
