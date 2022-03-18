<h1 align="center">Fortune Teller</h1>

[Click here to view the live project](https://the-best-fortune-teller.herokuapp.com/)

![respons image](https://user-images.githubusercontent.com/83631970/158982938-31d7a8e8-ce44-4206-826c-b82d7466fc5e.png)

Welcome to the Best Fortune Teller! Do you want to know your future? Just ask our program which relies on the answers from the famous Magic 8-Ball game. This project was created for educational purposes only and was created as a project for the Code Institute course.
Welcome to the best fortune teller. Want to know your future? Just ask our program which relies on the answers from the famous Magic 8-Ball game. This project was created for educational purposes only and was created as a project for the Code Institute course.

In this project that runs on a terminal created by Code Institute, we have a welcome message, then the user has to enter the name, asks a question and the program runs a random answer based on the game Magic 8-Ball.

---

# Table of contents

- [User Experience](#user-experience)
    - [User Experience](#user-stories)
        - [User stories](#user-stories)
- [Design](#design)
    - [Diagrams](#diagrams)
    - [FlowChart](#flowchart)
- [Features](#features)
- [Technologies Used](#technology)
- [Testing](#testing)
    - [Code Validation](#code-validation)
    - [Performance testing](#performance-testing)
- [Resolved Issues](#resolved_issues)
- [Deployment](#deployment)
- [Credits](#credits)

# User Experience
## User stories

        1. As a Visitor, I want to easily understand the main purpose of the app.
        2. As a Visitor, I want to be able to easily play the game.
        3. As a Visitor, I want to have a good time.
[Back to Table of contents](#table-of-contents)
___

# Design
## Diagrams
![Untitled Diagram drawio (3)](https://user-images.githubusercontent.com/83631970/158985056-3863ab94-95ef-4c51-bb21-76a673c045b1.png)

## FlowChart
![Untitled Diagram drawio (2)](https://user-images.githubusercontent.com/83631970/158984895-530972f0-eeea-4029-b98b-bf75c48277c1.png)

[Back to Table of contents](#table-of-contents)
___

# Features
![Screenshot (246)](https://user-images.githubusercontent.com/83631970/158986990-fdd89480-9800-44fa-9ff3-eec28f35a5ed.png)
* Welcome message
![1](https://user-images.githubusercontent.com/83631970/158987384-9301f495-a504-4744-b1c9-f87b4eb1371e.png)
* Asks for name and question
![2](https://user-images.githubusercontent.com/83631970/158987386-d945396c-2cd8-4741-a482-29e3c49a2e50.png)
* Gives an answer
![3](https://user-images.githubusercontent.com/83631970/158987504-d5dc98d2-0653-4149-8c4f-f6cf2a7578d9.png)
[Back to Table of contents](#table-of-contents)
___

# Tecnologies Used
* Python;
* Heroku;
* Node.js;
* Google Sheets API.

[Back to Table of contents](#table-of-contents)
___

# Testing
## Code Validation
* PEP-8 - all errors fixed 

[Back to Table of contents](#table-of-contents)
___

## Performance testing
![light](https://user-images.githubusercontent.com/83631970/158993597-d9f6c47b-5dd2-4a2c-bd28-923d32930c91.png)

[Back to Table of contents](#table-of-contents)
___

# Resolved Issues
![erro 1](https://user-images.githubusercontent.com/83631970/158995898-d78032a1-f4f2-4ce7-850a-a58667310995.png)
- [x] I fixed this error by changing the name of the google sheets sheet.
![erro 2](https://user-images.githubusercontent.com/83631970/158995908-a5e4f157-eaa8-4eac-b500-fba9ab382176.png)
- [x] I fixed this error of a string answer with brackets changing the get_all_values funtion for all_magic_ball_answers.col_values(1) function.

[Back to Table of contents](#table-of-contents)
___

# Deployment
This project was deployed using Code Institue's mock terminal for Heroku.
The steps for deployment are:

- Sign in to Heroku;
- Create a new Heroku app;
- In settings, add two config vars: Key Port and value 8000 and other with the Key CREDS of my creds.json; 
- Set the buildbacks to Python and NodeJS;
- Connect the Heroku app to the GitHub repository
- Deploy the project

[Back to Table of contents](#table-of-contents)
___

### Credits

* I used the code teach in the Code Institute Python lessons;
* I used the teachings about google sheets learned in the Love Sandwiches lesson;
* I used the information in [wikipedia](https://en.wikipedia.org/wiki/Magic_8-ball) about the game Magic 8-Ball.

[Back to Table of contents](#table-of-contents)
___

