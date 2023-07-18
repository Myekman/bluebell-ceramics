<h1 align="center">Bluebell Ceramics</h1>
<div align="center"><img src=""></div>

## Project goal:
This website is a fictional ceramic studio called Bluebell Ceramics. It is designed to be responsive and accessible on a variety of devices. The main purpose of the site is to attract creativ people to join as members to be able to book sessions. 

[View the live project here.](https://)

- [User Experience (UX)](#user-experience-ux)
  - [User stories](#user-stories)
- [Agile methodology](#agile-methodology)
- [Design](#design)
  - [Wireframes](#wireframes)
- [Features](#fretures)
- [Technologies used](#technologies-used)
- [Programs & Tools](programs-&-tools)
- [Testing](#testing)
  - [Bugs](#bugs)
  - [Manual Testing](#manual-testing)
- [Validation](#validation)
- [Deployment](#deployment)
  -[Forking Repository](#forking)
  -[Making a Clone - 2 ways](#clone)
- [Credits](#credits)


## User Experience (UX):

### User stories

-   ### First Time Visitor Goals

    - As a first time visitor i want to:
    - easily understand the main purpose of the site.
    - easily navigate between pages.
    - be able to register to book a session of pain or turn.
    - be able to log out after creating an account.
      
        
-   ### Returning Visitor Goals
    - As a returning visitor i want to:
    - be able to log in with my created account.
    - be able to make a booking.
    - be able to se my booking in "my bookings".
    - be able to delete or edit my booking.
    - be able to sign out from my account. 


-   ### Frequent User Goals
    -  As a frequent visitor I can login and find my current bookings.
    -  As a frequent visitor I can change or cancel my bookings.

-   ### Agile methodology
To plan this project the github agile tool has been used. By creating user stories to break down the build-up in different stages with tasks for each user story and labels for priority.

and used the github projects page kanbanboard to keep track of what has been accrued and completed.

### Design
The design I was aiming for for this site was a luxurious and clean one, but with a warmth of earthy colors.

- Font  
the fonts i..

- Images  
The images is warm for and invited, it inspires the visitor to come and create in that cosy enviroment.  

- ### Wireframes  
  add wireframes here

## Features  
add features here 

## Technologies Used

### Languages
- Python
- JavaScript
- HTML5
- CSS3
### Frameworks, Libraries, Programs

Django: python framework used to create all the backend
Database:
PostgreSQL: the database used to store all the data.

### Programs & Tools

- [Bootstrap]([Title](https://getbootstrap.com/)), Was used to create the front-end design.
- [Gitpod](), Gitpod was used as IDE to commit and push the project to GitHub.
[Github](), Was used as a version control system to manage the code.
- [Heroku](), the hosting service used to host the website.
- [Chroome developer tools](),was used to debug the website.
- VALIDATOR ADD HERE

## Testing 

### Bugs 
Bug 1: I can change time but not date when i try to edit my bookings.
<hr>
Bug 1 solution: Change model field to "to date = models.datefield.
<hr>
Bug 2: Error message not displaying when dubblebooking.
<hr>
Bug 2 solution: Import validation error. (from django.core.exceptions import ValidationError) and code to model that raises the validation error. 
<hr>

Bug 3: The footer was floating upp.
<hr>
Bug 3 solution: Add height of 100vh to every section in every page. 

- ### Manual Testing

## Validation

## Deployment

The project was developed using Gitpod, the project code is stored on GitHub, and then deployed to Heroku. To deploy, follow these steps:

Log in to Heroku or create an account if you dont have one. When you are loged in you click the button labeled 'New'.

From the drop-down menu select 'Create new app'. Enter your app name. Select your region and Click 'Create App'.

Go to 'Settings' and scroll down to the 'Config Vars' section. Click 'Reveal Config Vars' and enter 'PORT' for the key and '8000' for the value. Then click 'Add'. Add CLOUDINARY_URL, DATABASE_URL and SECRET_KEY. The URL value must be copied from your CLOUDINARY account and the url for your databade_url from your ElephantSQL account. 

Click on the 'Deploy' tab. Next to 'Deployment method' select 'GitHub'. Connect the your GitHub repository. Under 'Manual deploy' click 'Deploy Branch'. Or you can select 'Automatic Deploys' so that the site updates when updates are pushed to GitHub.

After successful deployment message in the page top right corner click the button labeled 'Open app' and you can access live app.

#### Forking Repository
To use this code yourself it is possible to 'fork' the code on the GitHub repository through the following steps:

Create or log into your GitHub account.
Go to the repository you want to fork. 
Click the 'Fork' button in the upper right-hand corner of the page. A copy of the repository will be available in your own repository.

#### Making a Clone - 2 ways
1. Log in to GitHub go to the GitHub Repository you want to clone.
Under the repository name, click button "Code", click "Clone or download".

2. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
Open your development editorand open a terminal window.
Type git clone, and then paste the URL you copied in Step 3.
like this: git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY

Press Enter.

Your local clone will be created.

## Credits


