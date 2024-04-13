
**#Installation Clone the repository:**

bash Copy code
git clone <repository_url> cd Project

Create and activate a virtual environment (optional but recommended):

**#Install dependencies:**

pip install -r requirements.txt Usage To run the development server, execute the following command:

**#Database integration :** 

create a new database 'New_database' update the database name in the project setting.py file with username and password of your local database

Run the bellow commands for the creation of the required tables

bash
py manage.py makemigrations
py manage.py migrate

bash
python manage.py runserver 

**Endpoints**
Add a New Student URL: /newuser

Method: POST

Description: Add a new student to the database.

Update and retrive a Student details by ID URL: /user/<student_id>/

Method: PUT

Description: Retriving Update an existing student's details.

List of all student details

URL: /users/

Method: GET

Description: Retrieve details of a student by their ID.

**SQL quries that are used to insert sample data :**

INSERT INTO users.user (name, email, role) VALUES
('John Doe', 'john@example.com', 'admin');

**To retrive the all students in the table users**
SELECT * FROM users;

**Retriving the User details by there ID **
SELECT * FROM users WHERE id = <user_id>;

we have buttons on each end ponts on the home page with the statements that what they can do .


#Contributing Contributions to this project are welcome. Please follow the guidelines in CONTRIBUTING.md.
