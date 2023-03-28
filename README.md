Django Leave Management System 👨‍🎓

A student leave management system is an online software application that helps educational institutions manage and track student leaves. This system is designed to simplify the process of applying for leave, approving leave requests, and maintaining records of leaves taken by students.


1) Open project on VS code

2) Go in LMS folder,

3) If virtualenv is not installed (What is virtualenv?):

      -> $ pip install virtualenv

   Create a virtual environment

      -> $ virtualenv venv

   Activate the environment everytime you open the project

      -> $ source venv/bin/activate

4) Now you have to download some packages using below commands :
  
      -> python -m pip install Django
      -> python -m pip install Pillow
      -> pip install django-active-link

5) Now go in lms folder, 

6) Run migrations for Database

      -> $ python manage.py makemigrations
      -> $ python manage.py migrate
      
7) All Set! 🤩
   Now you can run the server to see your application up & running 🚀

      -> $ python manage.py runserver

8) To exit the environment ❎

      -> $ deactivate

9) Every time you want to open the application in browser, make sure you run:

      -> $ source venv/Scripts/activate
      -> $ python manage.py runserver
      
10) Data for login :

Admin
      Email : admin@gmail.com
      Password : admin
      
Faculty 
      Email : ckb@gmail.com
      Password : ckb123

Student 
      Email : kevan@gmail.com
      Password : kevan123
      
      
