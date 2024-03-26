
class InvalidEmailFormatException(Exception):
    def __init__(self, message):
        self.message = message 
        super().__init__(self.message)




def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailFormatException("Error, Invalid email format")
    
   
    domain = email.split("@")[1]
    # print(domain)
  
    top_level_domain = domain.split(".")[0].lower()
    # print(top_level_domain)

    
    allowed_domains = ['gmail', 'yahoo', 'hotmail']  # Add more if needed

    if top_level_domain not in allowed_domains:
        raise InvalidEmailFormatException("Error, Invalid email domain")

    print("Email validation successful")




