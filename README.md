Clone the Repository: Clone the project repository to your local machine.

Install Dependencies: Navigate to the project directory and install the required dependencies listed in requirements.txt.

Run the Server: Start the server. The URL for uploading a CSV file is:
http://127.0.0.1:8000/api/upload-csv/

Test API in Postman:

Use the POST method in Postman.
In the Body tab, choose the form-data option.
Add a key named file, set its type to File, and upload the CSV file.
Send the request to receive the response.
Check Admin Panel:
To verify if the data has been updated on the admin side, go to:
http://127.0.0.1:8000/admin
