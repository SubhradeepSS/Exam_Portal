<p align='center'><img src='https://user-images.githubusercontent.com/46227193/133924458-d6f66df8-f0f8-4d56-951e-213200a2ad83.jpeg' width="300" ></p>
<p align='center'>
Due to pertaining covid situation, it has been quite a hassle for colleges and schools to conduct examinations for students and there are limited Indian platforms available for students for this purpose. Also many unprivileged students who can't pay high fee to schools charging extra money from them for conducting assessements and grading, this platform will be a viable solution for this problem and will provide a cost effective, seamless and transparent experience for teachers as well as studetns and will be widely availbale for all schools.<br></br>
Furthermore, we performed a survey of our teachers and discovered that they spend more than 60% of their time developing questions for various class assessments, assignments, and exams. So, we decided to lend a hand. For this, we devised the concept of a platform where teachers can just input the questions to conduct any kind of tests.<br></br> 
</p>
<p align='center'><img src='https://user-images.githubusercontent.com/46227193/133924440-7ddb553c-d8bb-47dc-a46f-01e45a96328c.png' width="800" ></p>

## What is it? ⛹️‍♂️
The project is a complete Exam Portal system built for educational institutions like schools and colleges. The portal serves as a single platform that can be used by all the professors and students, having their own set of work to be done. Following are the three levels of users along with the supported features that can be done by them in the portal:
* ***admin*** 🛠
   * maintains the entire portal system through the django-admin site.
   * has access to the entire database consisting of all the data stored.

* ***professor*** 👔

   * MCQ questions can be created/edited by professors which then further can be added to one or more question paper created by them.
   * The professor can create different groups of students as per their wish.
   * Exams can be created which can have a Question paper alloted to it by them.

* ***student*** 🧑‍
   * Can attempt exams allotted to them within the time constraints set by the professor
   * Can view their marks and solutions after completing the exam.
   * Have a list of all the exams completed and yet to be attempted in a single page 



## Cloning the Application in local ⬇️
1. Following software needs to be setup in the system for using the application in local
   * [git](https://git-scm.com/downloads)
   * [python](https://www.python.org/downloads/)
   * [pip](https://pip.pypa.io/en/stable/installing/)

2. Clone the repo by running the following command in any terminal
   ```sh
   git clone https://github.com/SubhradeepSS/Exam_Portal.git
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
View deployed site [here](https://exam_portal-v01.herokuapp.com/).
##### Credentials:
| User Type      | Username | Password |
| ----------- | ----------- | -----------|
| admin      | admin       | admin |
| student   | student_1        | password_student_1 |
| prof   | prof_1        | password_prof_1 |

The admin can create more users(professors/students) from the django admin panel and can add them to corresponding groups, after which they can login through the site.

## Built With 💕
* [Django](https://www.djangoproject.com/)
* [Django REST Framework](https://www.django-rest-framework.org/)
* Python
* HTML
* CSS
* JavaScript
* [Bootstrap](https://getbootstrap.com/)
* [Postman](https://www.postman.com/)
* [Visual Studio Code](https://code.visualstudio.com/)
* [Heroku](https://www.heroku.com/)


## API info 👷
The APIs were built using **`Django`** and **`Django RESTFramework`**, which were further tested out using **`Postman`**. Some of the APIs tested can be found out [here](https://documenter.getpostman.com/view/11308411/UUxtEAco).

## Next steps 🔥
- [ ] Support for separate subjects and courses alloted to professors and students.
- [ ] Improved exam proctoring using AI based plagiarism checker, video and audio recording.
- [ ] Discussion forum for students sorted in different class groups as well as subjects, where one particular student can consult the concerned faculty or other fellow students. 
- [ ] Proper result and analysis reports of exams(subjectwise) in dashboard for the students.
- [ ] Professor's view of complete date of students enrolled in their subjects.


## Contributing 👩‍💻
Any contributions made to the project are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
