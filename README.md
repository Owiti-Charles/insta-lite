# insta-lite

>[Owiti-Charles](https://github.com/Owiti-Charles)  
  
# Description  
This is a clone of  Instagram where people share their  images and videos for other users to view. 
Users can sign up, login, view and post photos, search and follow other users.
##  Live Link  
 Click [View Site](https://instalite.herokuapp.com/)  to visit the site
  
## Screenshots 
###### Home page
 
<img src="https://raw.githubusercontent.com/Owiti-Charles/insta-lite/master/static/images/instagram.png">
 
 ###### user profile
 <img src="https://raw.githubusercontent.com/Owiti-Charles/insta-lite/master/static/images/profile.png"> 


 
## User Story  
  
* Sign in to the application to start using.  
* Upload a pictures to the application. 
* Search for different users using their usernames.  
* See your profile with all your pictures.  
* Follow other users and see their pictures on my timeline.  
  

  
## Setup and Installation  
To get the project .......  
  
##### Cloning the repository:  
 ```bash 
 https://github.com/Owiti-Charles/insta-lite.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd insta-lite pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations instagram
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Running the application  
 ```bash 
 python manage.py server 
```
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.6](https://www.python.org/)  
* [Django 1.11](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Known Bugs  
* There are no known bugs currently but pull requests are allowed incase you spot a bug  
  
## Contact Information   
If you have any question or contributions, please email me at [mikeycharlesm7@gmail.com]  
  
## License 

* [![License](https://img.shields.io/packagist/l/loopline-systems/closeio-api-wrapper.svg)](https://github.com/Owiti-Charles/Picture-Globe/blob/master/LICENSE)  
* Copyright (c) 2019 **Owiti Charles**