console.log("AI INTERVIEW SYSTEM INITIALIZED");

/* ================= PAGE FADE ================= */

document.body.style.opacity = "0";
document.body.style.transition = "0.6s";

/* ================= CARD HOVER EFFECT ================= */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        const cards =
        document.querySelectorAll(

            ".card"

        );

        cards.forEach((card) => {

            card.addEventListener(

                "mousemove",

                (e) => {

                    const rect =
                    card.getBoundingClientRect();

                    const x =
                    e.clientX - rect.left;

                    const y =
                    e.clientY - rect.top;

                    const centerX =
                    rect.width / 2;

                    const centerY =
                    rect.height / 2;

                    const rotateX =
                    ((y - centerY) / 25);

                    const rotateY =
                    ((centerX - x) / 25);

                    card.style.transform =

                    `
                    perspective(1000px)
                    rotateX(${rotateX}deg)
                    rotateY(${rotateY}deg)
                    translateY(-8px)
                    scale(1.02)
                    `;

                }

            );

            card.addEventListener(

                "mouseleave",

                () => {

                    card.style.transform =

                    `
                    perspective(1000px)
                    rotateX(0deg)
                    rotateY(0deg)
                    translateY(0px)
                    scale(1)
                    `;

                }

            );

        });

    }

);

/* ================= BUTTON GLOW EFFECT ================= */

const buttons =
document.querySelectorAll("button");

buttons.forEach((btn) => {

    btn.addEventListener(

        "mouseenter",

        () => {

            btn.style.boxShadow =

            "0 0 25px rgba(37,99,235,0.5)";

            btn.style.transform =

            "scale(1.05)";

        }

    );

    btn.addEventListener(

        "mouseleave",

        () => {

            btn.style.boxShadow =

            "none";

            btn.style.transform =

            "scale(1)";

        }

    );

});

/* ================= PAGE LOAD ================= */

window.addEventListener(

    "load",

    () => {

        document.body.style.opacity = "1";

    }

);

/* ================= TYPING EFFECT ================= */

const headings =
document.querySelectorAll(

    "h1"
);

headings.forEach((heading) => {

    heading.style.animation =

    "fadeIn 1.2s ease";

});

/* ================= VIDEO INTERVIEW ================= */

const questions = [

    "Tell me about yourself",

    "What are your strengths?",

    "Why should we hire you?",

    "Explain your project",

    "What is Machine Learning?",

    "What are your career goals?",

    "What are your weaknesses?",

    "Why do you want this job?"

];

let questionIndex = 0;

let questionTimer;

async function startCamera(){

    try{

        const stream =

        await navigator.mediaDevices.getUserMedia({

            video:true,
            audio:false

        });

        const video =
        document.getElementById(

            "video"
        );

        if(video){

            video.srcObject = stream;

        }

        askQuestion();

        questionTimer =

        setInterval(

            askQuestion,

            60000

        );

    }

    catch(error){

        alert(

            "Please Allow Camera Permission"

        );

        console.log(error);

    }

}

function askQuestion(){

    const questionText =
    document.getElementById(

        "question"
    );

    if(questionText){

        questionText.innerHTML =

        questions[questionIndex];

        questionIndex++;

        if(

            questionIndex >=
            questions.length

        ){

            questionIndex = 0;

        }

    }

}

function skipQuestion(){

    askQuestion();

}

function showFeedback(){

    clearInterval(questionTimer);

    const feedback =
    document.getElementById(

        "feedback"
    );

    if(feedback){

        feedback.style.display =

        "block";

    }

}