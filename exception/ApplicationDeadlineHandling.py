from datetime import datetime

class ApplicationDeadlineException(Exception):
    def __init__(self, message="The application deadline has passed. Applications are no longer accepted."):
        self.message = message
        super().__init__(self.message)

# def submit_application1(deadline):
#     try:
#         current_time = datetime.now()
#         if current_time > deadline:
#             raise ApplicationDeadlineException("The application deadline has passed. Applications are no longer accepted.")
                    
#         print("Application submitted successfully.")
#     except ApplicationDeadlineException as e:
#         print("Application submission error:", e)               



