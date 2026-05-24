console.log("AI INTERVIEW SYSTEM INITIALIZED");

/* ================= CARD HOVER ================= */

document.addEventListener(

    "DOMContentLoaded",

    () => {

        const cards =
        document.querySelectorAll(".card");

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

/* ================= BUTTON EFFECT ================= */

const buttons =
document.querySelectorAll("button");

buttons.forEach((btn) => {

    btn.addEventListener(

        "mouseenter",

        () => {

            btn.style.boxShadow =

            "0 0 25px rgba(37,99,235,0.5)";

        }

    );

    btn.addEventListener(

        "mouseleave",

        () => {

            btn.style.boxShadow =

            "none";

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