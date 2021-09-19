
<p align='center'><img src='https://res.cloudinary.com/animega/image/upload/v1632041851/online-exam-software-500x500_a9a8li.jpg' width="150" ></p>
<h1 align='center'> College Portal</h1>
<p align='center'>
Due to pertaining covid situation, it has been quite a hassle for colleges to conduct examinations for students and there are limited Indian platforms available for school students for this purpose. Also many unprivileged students who can't pay high fee to schools charging extra money from them for conducting assessements and grading, this platform will be a viable solution for this problem and will provide a cost effective, seamless and transparent experience for teachers as well as studetns and will be widely availbale for all schools.<br></br>
Furthermore, we performed a survey of our teachers and discovered that they spend more than 60% of their time developing questions for various class assessments, assignments, and exams. So, we decided to lend a hand. For this, we devised the concept of a platform where teachers can just input the questions to conduct any kind of tests.<br></br> 
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

## Team ✨

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://aniket.live"><img src="https://avatars.githubusercontent.com/u/67703407?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Aniket Pal</b></sub></a><br /><a href="#infra-Aniket762" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/Aniket762/playground/commits?author=Aniket762" title="Tests">⚠️</a> <a href="https://github.com/Aniket762/playground/commits?author=Aniket762" title="Code">💻</a> <a href="#ideas-Aniket762" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/Aniket762/playground/commits?author=Aniket762" title="Documentation">📖</a> <a href="#projectManagement-Aniket762" title="Project Management">📆</a></td>
    <td align="center"><a href="http://aabhassao.me"><img src="https://avatars.githubusercontent.com/u/58210877?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Aabhas Sao </b></sub></a><br /><a href="#design-kirito-236" title="Design">🎨</a> <a href="#infra-kirito-236" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="https://github.com/Aniket762/playground/commits?author=kirito-236" title="Code">💻</a></td>
    <td align="center"><a href="https://sumana.live/"><img src="https://avatars.githubusercontent.com/u/63084088?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Sumana Basu</b></sub></a><br /><a href="#design-sumana2001" title="Design">🎨</a> <a href="https://github.com/Aniket762/playground/commits?author=sumana2001" title="Documentation">📖</a> <a href="https://github.com/Aniket762/playground/commits?author=sumana2001" title="Code">💻</a></td>
  </tr>
</table>

## Prerequisites 👨‍💻

### Install Node JS
Refer to https://nodejs.org/en/ to install nodejs

### Install create-react-app
Install create-react-app npm package globally. This will help to easily run the project and also build the source files easily. Use the following command to install create-react-app

```bash
npm install -g create-react-app
```

## Cloning and Running the Application in local 💻

Clone the project in localhost
```bash
git clone https://github.com/Aniket762/playground.git
```
Install all the npm packages. Go into the web folder and type the following command to install all npm packages

```bash
npm install
```

In order to run the application in development mode type the following command

```bash
yarn dev
```

The Application Runs on **localhost:3000**

### To spin up the backend server

Navigate to the main project folder in a seperate terminal. Then install all npm packages
```bash
npm install 
```

If you don't have nodemon globally installed on your system, install it so the server can autorefresh 
```bash
npm install -g nodemon
```

Now it's time to spin up the backend server. Run the lines
```bash
npm run dev
```
If you get an error immediately, don't worry. The final step is to connect to the MongoDB database.

Note: The Server Runs on **localhost:8080**

## Connecting to the Database
Spin up your cluster in MongoDB and replace your connection with URI in `.env`
If you face any problems, refer to the [MongoDB](https://www.mongodb.com/blog/postquick-start-nodejs-mongodb--how-to-get-connected-to-your-database) website.


## Connecting to the Database if you haven't used MongoDB Atlas before
Install the MongoDB Node.js Driver with the following command:
```bash
npm install mongodb
```

Set up a [MongoDB Atlas Database](https://www.youtube.com/watch?v=rPqRyYJmx2g) by following this short MongoDB setup video till the *3:20* mark. Stop after that mark!

On your Cluster home page, select CONNECT > Connect your application. 
1. Select Node.js in the drop down for your driver, and select the latest version. 
1. Then, copy the connecting string (URI).
1. Paste this string as the value of mongoURI inside `.env` of this project.

Replace the `<password>` section of the string with your Database Access password. Viola, your server should now successfuly connect to MongoDB!
## How we built it 🧑‍💻
We used Next.js in the frontend and Node.js in the backend with MongoDB as our database. Next, we used the Google Vision API for scanning the image and retrieving the handwritten text. The handwritten text was displayed in a code editor with full syntax highlighting and available for currently two languages, c++ and python. When you click submit, we generated a new code file for the corresponding language and displayed it's output on the screen. For the second section of Playground, we created a form which adds data to the database. Then we retrieve the data through axios and display the questions that are approved. We created a special route with a passcode for admins, where they can manually approve the questions in the database.

## Challenges we ran into 🥺
We faced numerours challenges throughout the journey. Firstly, we had to look for a good OCR model. We checked so many github repositories and packages but we couldn't find a one that had very high efficiency. So we finally decided to go with the Google Vision API in Google Cloud. But in Google Cloud, for getteing the API key, we needed credit card details and since none of had one, we had to borrow it from a friend which led us to our next challenge. We saw that while development, we had already used up so many requests and if we made the site live, the number of requests will increase because of which our friend might have to pay to Google Cloud. Since we wanted to remain in the free tier, we decided not to host the web application. Other than that we tried creating our very own compiler for the first time, which were initailly full of bugs and it took us a lot of time to fix them.

## Accomplishments that we're proud of 😎
The biggest accomplishment for us was that we learned so many new things in just 2 days. We implemented OCR, TypeScript, Axios and API calls. We were able to overcome all the challenges and were able to create a completely functional prototype the way we had envisioned. Even though one of our teammates fell sick and wasn't able to contribute, we didn't lose hope and stayed up all night. It was tiring, but fun as well. I am most proud of the fact that this product will be able to help many teachers across the globe.

## What we learned 🤓
Being a group of javascript developers, we tried our hands on typescript this time. We learnt how to use Next.js and implement it with TypeScript and SCSS. Moreover, we created a progressive web app with offline support as well. As we wanted to read the handwritten text, we found out about OCR for text extraction. We researched on it and finally decided to try out the Google Vision API which was something very new for us.

## Built With 💕
- [ ] React
- [ ] Nextjs 
- [ ] Nodejs
- [ ] Javascript
- [ ] Express
- [ ] Typescript
- [ ] MongoDB
- [ ] Mongoose
- [ ] Google Cloud Platform
- [ ] Google Vision API
- [ ] Cloudinary
- [ ] Scss
- [ ] Vercel
- [ ] Heroku


## Future Scope 🔥
We want to bring in features like proctoting and AI based plagiarism checker. We want to incorporate a discussion forum for students sorted in differnet class groups as well as subjects, where one particular student can consult the concerned faculty or other fellow students. In addition to that, we plan to create a practice support for mock tests that will allow students to practice the questions on the basis of topic and difficulty with random allocation of questions. Finally, we wish to build and expand the project so organisations like CBSE and NTA Could make use of the servie.




