import os

class FileUploadException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)



def upload_resume(self, resume_file):
    try:

        if not os.path.exists(resume_file):
            raise FileUploadException("File not found.")

        
        max_file_size = 10 * 1024 * 1024  
        if os.path.getsize(resume_file) > max_file_size:
            raise FileUploadException("File size exceeded. Maximum allowed size is 10 MB.")

        
        supported_formats = [".pdf", ".docx"]
        if not any(resume_file.endswith(format) for format in supported_formats):
            raise FileUploadException("Unsupported file format. Please upload a PDF or DOCX file.")

        
        print("File uploaded successfully.")

    except FileUploadException as e:
        print("File upload error:", e)



