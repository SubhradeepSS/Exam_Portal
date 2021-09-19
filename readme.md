
<p align='center'><img src='https://res.cloudinary.com/dqlh4eyt8/image/upload/v1630815038/playground-logo_1_jrjppd.png' width="150" ></p>
<h1 align='center'> Playground</h1>
<p align='center'>
In India, more than 95% of schools don't allow smartphones in class. Being a Computer Science teacher becomes very difficult as it is nearly impossible to check the handwritten code of each student line by line. Also talking in India, in most schools, the students don't have the privilege to have one computer each for them so that they can run their code on their own. So it becomes a nightmare for the teacher as they might have to manually type each code of each student and run it or take the risk of missing out on bugs. So we came up with Playground to make this job easier. Another reason for creating Playground was that once we entered college we understood the importance of coding. Coding not only helps you in a Software job but also helps increase logical reasoning and problem-solving ability. But many students don't have the chance of coding till they reach college. Why? Because there are so many students in India who can not afford a laptop or computer. So we decided to build a progressive web app because in today's world almost everyone uses a phone. Now they can start coding early and learn from online teachers. <br/> <br/>
In addition to that, we conducted a survey among our teachers where we found that teachers give more than 40% of their time to creating questions for various class tests, assignments and exams. So this teacher's day, we wanted to help them out. For this, we came up with crowdsourcing question bank idea. Anyone across the world can now help teachers make questions. <br/> <strong>By everyone, for teachers!❤</strong>
</p>
<img width="1327" alt="playground user interface" src="https://user-images.githubusercontent.com/67703407/132119834-68cd31ee-179a-4cff-80b1-d2979fb87146.png">

## What is it? ⛹️‍♂️
There are two subsystems of the Playground:
1. Evaluation of answer sheets of the exams conducted traditionally is a tedious and critical task. A lot of time and energy is invested by the teachers to check every single line of code, look for bugs and find the corresponding output. So, with Playground, you can simply upload a picture of a student's handwritten code and we will handle the rest. Using Google's Vision API, we scan the image and retrieve the text and give it back to you in a code editor. But unlike teachers, machines are not always right, so if some minor flaws are there you can edit them in the code editor, which will then run the code and give you the output. So instead of going through the entire code, use Playground to do it in less than 2 mins.
2. Teachers have to work hard everyday. Starting from explaining the concepts in a pace all students understand, to giving proper assignments, to clearing all the doubts. So we thought let us make another important job for our teachers super easy. With Playground, you can also easily create question papers and assignments for your students. This is done by crowdsourcing. Students and teachers across the world can add their favourite questions through a form and then you'll get a variety of coding questions which are pre-approved by us. So just select some of the random questions from our page and you're done with the assignment! It's that simple!


[![Starware](https://img.shields.io/badge/⭐-Starware-f5a91a?labelColor=black)](https://github.com/zepfietje/starware)

Playground is Starware.  
This means you're free to use the project, as long as you star its GitHub repository.  
Your appreciation makes us grow and glow up. ⭐


## Cloning the Application in local ⬇️
1. Following software needs to be setup in the system for using the application in local
* [git](https://git-scm.com/downloads)
* [python](https://www.python.org/downloads/)
* [pip](https://pip.pypa.io/en/stable/installing/)

2. Clone the repo by running the following command in any terminal
   ```sh
   git clone https://github.com/SubhradeepSS/College-Portal.git
   ```
   
3. Open the project in any source code editor.
4. Open terminal and run
   ```sh
   pip install -r requirements.txt
   ```
   This installs all the packages required for running the application locally

## Running the Application 🚚
### Local 💻
For running the project, navigate to the project directory and follow the following instructions:

* Type the following in the command line:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    python manage.py createsuperuser
    # this will ask for username, email(optional) and password. 
    # Enter some credentials to be used later for django admin functionality.
    python manage.py runserver
  ```

* Log on to [django admin site](http://127.0.0.1:8000/admin) using the superuser credentials
    * Click on **Groups** section and create 2 groups - ***Professor*** and ***Student***
    * Click on **Users** section and create some users, and also make each user belong to one of the groups- Professor/Student as per role
    * Logout of the admin site and go to http://127.0.0.1:8000/ where the home page of the project will be rendered.

* Now any student/professor can login using their own credentials.


### Deployment 🚀
View deployed site [here](https://college-portal-v01.herokuapp.com/).
##### Credentials:
| User Type      | Username | Password |
| ----------- | ----------- | -----------|
| admin      | admin       | admin |
| student   | student_1        | password_student_1 |
| prof   | prof_1        | password_prof_1 |

The admin can create more users(professors/students) from the django admin panel and can add them to corresponding groups, after which they can login through the site.

## How we built it 🧑‍💻
We used Next.js in the frontend and Node.js in the backend with MongoDB as our database. Next, we used the Google Vision API for scanning the image and retrieving the handwritten text. The handwritten text was displayed in a code editor with full syntax highlighting and available for currently two languages, c++ and python. When you click submit, we generated a new code file for the corresponding language and displayed it's output on the screen. For the second section of Playground, we created a form which adds data to the database. Then we retrieve the data through axios and display the questions that are approved. We created a special route with a passcode for admins, where they can manually approve the questions in the database.

## Challenges we ran into 🥺
We faced numerours challenges throughout the journey. Firstly, we had to look for a good OCR model. We checked so many github repositories and packages but we couldn't find a one that had very high efficiency. So we finally decided to go with the Google Vision API in Google Cloud. But in Google Cloud, for getteing the API key, we needed credit card details and since none of had one, we had to borrow it from a friend which led us to our next challenge. We saw that while development, we had already used up so many requests and if we made the site live, the number of requests will increase because of which our friend might have to pay to Google Cloud. Since we wanted to remain in the free tier, we decided not to host the web application. Other than that we tried creating our very own compiler for the first time, which were initailly full of bugs and it took us a lot of time to fix them.

## Accomplishments that we're proud of 😎
The biggest accomplishment for us was that we learned so many new things in just 2 days. We implemented OCR, TypeScript, Axios and API calls. We were able to overcome all the challenges and were able to create a completely functional prototype the way we had envisioned. Even though one of our teammates fell sick and wasn't able to contribute, we didn't lose hope and stayed up all night. It was tiring, but fun as well. I am most proud of the fact that this product will be able to help many teachers across the globe.

## What we learned 🤓
Being a group of javascript developers, we tried our hands on typescript this time. We learnt how to use Next.js and implement it with TypeScript and SCSS. Moreover, we created a progressive web app with offline support as well. As we wanted to read the handwritten text, we found out about OCR for text extraction. We researched on it and finally decided to try out the Google Vision API which was something very new for us.

## Built With 💕
- [ ] [Django](https://www.djangoproject.com/)
- [ ] [Django REST Framework](https://www.django-rest-framework.org/)
- [ ] Python
- [ ] HTML
- [ ] CSS
- [ ] JavaScript
- [ ] [Bootstrap](https://getbootstrap.com/)
- [ ] [Postman](https://www.postman.com/)
- [ ] [Visual Studio Code](https://code.visualstudio.com/)
- [ ] [Heroku](https://www.heroku.com/)


## Next steps 🔥
Next, we want to increase the support by providing more options for languages like javascript, java, c and so on. We also want to increase the variety of questions varying through a variety of topics and difficulty levels. In addition to that, we plan to create a neural search framework that will allow us to filter the questions on the basis of topic and difficulty and help you find similar questions. Lastly, we wish to build our very own OCR model for text extraction. This will solve our problems of billing while using external models.

<img src='https://challengepost-s3-challengepost.netdna-ssl.com/photos/production/challenge_photos/001/637/595/datas/full_width.png' />


## Contributing 👩‍💻
Any contributions made to the project are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
