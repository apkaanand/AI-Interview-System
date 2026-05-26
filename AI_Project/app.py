from flask import *
import json
import os

app = Flask(__name__)

app.secret_key = "ai_project"

# ================= DATABASE =================

DB_FILE = "users.json"

if os.path.exists(DB_FILE):

    try:

        with open(DB_FILE, "r") as file:

            users = json.load(file)

    except:

        users = {}

else:

    users = {}

# ================= MCQ QUESTIONS =================

questions = [

    {
        "question":"Which is used in AI?",
        "options":[
            "Machine Learning",
            "MS Paint",
            "Notepad",
            "Photoshop"
        ],
        "answer":"Machine Learning"
    },

    {
        "question":"Python is a?",
        "options":[
            "Programming Language",
            "Browser",
            "Game",
            "Operating System"
        ],
        "answer":"Programming Language"
    },

    {
        "question":"HTML is used for?",
        "options":[
            "Web Design",
            "Cooking",
            "Gaming",
            "Hacking"
        ],
        "answer":"Web Design"
    },

    {
        "question":"CSS is used for?",
        "options":[
            "Styling",
            "Database",
            "Video Editing",
            "Networking"
        ],
        "answer":"Styling"
    },

    {
        "question":"Which database is popular?",
        "options":[
            "MySQL",
            "Instagram",
            "YouTube",
            "Spotify"
        ],
        "answer":"MySQL"
    },

    {
        "question":"Flask is a?",
        "options":[
            "Python Framework",
            "Game",
            "Phone",
            "Software"
        ],
        "answer":"Python Framework"
    },

    {
        "question":"Which is frontend language?",
        "options":[
            "JavaScript",
            "Python",
            "C",
            "Java"
        ],
        "answer":"JavaScript"
    },

    {
        "question":"AI means?",
        "options":[
            "Artificial Intelligence",
            "Automatic Internet",
            "Auto Input",
            "Advanced Integration"
        ],
        "answer":"Artificial Intelligence"
    },

    {
        "question":"Which is backend language?",
        "options":[
            "Python",
            "HTML",
            "CSS",
            "Photoshop"
        ],
        "answer":"Python"
    },

    {
        "question":"Which company made ChatGPT?",
        "options":[
            "OpenAI",
            "Google Maps",
            "Meta Mask",
            "Netflix"
        ],
        "answer":"OpenAI"
    },

    {
        "question":"JavaScript runs in?",
        "options":[
            "Browser",
            "Fridge",
            "Camera",
            "TV"
        ],
        "answer":"Browser"
    },

    {
        "question":"Which is AI field?",
        "options":[
            "Deep Learning",
            "Painting",
            "Cooking",
            "Driving"
        ],
        "answer":"Deep Learning"
    },

    {
        "question":"Which company owns Instagram?",
        "options":[
            "Meta",
            "Google",
            "Netflix",
            "Tesla"
        ],
        "answer":"Meta"
    },

    {
        "question":"Which is operating system?",
        "options":[
            "Windows",
            "HTML",
            "CSS",
            "AI"
        ],
        "answer":"Windows"
    },

    {
        "question":"Which language is best for AI?",
        "options":[
            "Python",
            "HTML",
            "CSS",
            "PHP"
        ],
        "answer":"Python"
    }

]

# ================= AI QUESTIONS =================

ai_questions = [

    "Tell me about yourself",

    "Why should we hire you?",

    "What are your strengths?",

    "What are your weaknesses?",

    "Where do you see yourself in 5 years?"

]

# ================= HOME =================

@app.route('/')

def home():

    return render_template(

        'index.html'

    )

# ================= REGISTER =================

@app.route(

    '/register',

    methods=['GET','POST']

)

def register():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        users[username] = password

        with open(

            DB_FILE,
            "w"

        ) as file:

            json.dump(users, file)

        return redirect(

            '/login'

        )

    return render_template(

        'register.html'

    )

# ================= LOGIN =================

@app.route(

    '/login',

    methods=['GET','POST']

)

def login():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        if (

            username in users

            and

            users[username] == password

        ):

            session['user'] = username

            return redirect(

                '/dashboard'

            )

    return render_template(

        'login.html'

    )

# ================= DASHBOARD =================

@app.route('/dashboard')

def dashboard():

    if 'user' not in session:

        return redirect(

            '/login'

        )

    return render_template(

        'dashboard.html',

        user=session['user']

    )

# ================= MCQ =================

@app.route(

    '/interview',

    methods=['GET','POST']

)

def interview():

    if 'index' not in session:

        session['index'] = 0
        session['score'] = 0

    index = session['index']

    if request.method == 'POST':

        selected = request.form['answer']

        correct = questions[index]['answer']

        if selected == correct:

            session['score'] += 1

        session['index'] += 1

        return redirect(

            '/interview'

        )

    if index >= len(questions):

        score = session['score']

        total = len(questions)

        session.pop('index')

        return render_template(

            'result.html',

            score=score,
            total=total

        )

    return render_template(

        'interview.html',

        question=questions[index]

    )

# ================= AI HR =================

@app.route(

    '/ai',

    methods=['GET','POST']

)

def ai():

    if 'ai_index' not in session:

        session['ai_index'] = 0

    index = session['ai_index']

    if request.method == 'POST':

        session['ai_index'] += 1

        return redirect('/ai')

    if index >= len(ai_questions):

        session.pop('ai_index')

        result = """

        Excellent communication skills
        with strong confidence level.

        """

        return render_template(

            'feedback.html',

            result=result

        )

    return render_template(

        'ai.html',

        question=ai_questions[index]

    )

# ================= VIDEO =================

@app.route('/video')

def video():

    return render_template(

        'video.html'

    )

# ================= RESUME =================

@app.route(

    '/resume',

    methods=['GET','POST']

)

def resume():

    if request.method == 'POST':

        score = 8

        skills = [

            "Python",
            "Flask",
            "HTML",
            "CSS"

        ]

        feedback = """

        Strong technical foundation
        with good development skills.

        """

        return render_template(

            'resume_result.html',

            score=score,
            skills=skills,
            feedback=feedback

        )

    return render_template(

        'resume.html'

    )

# ================= PROGRESS =================

@app.route('/progress')

def progress():

    score = session.get(

        'score',
        0

    )

    return render_template(

        'progress.html',

        score=score

    )

# ================= CERTIFICATE =================

@app.route('/certificate')

def certificate():

    return render_template(

        'certificate.html',

        user=session.get(

            'user',
            'Student'

        )

    )

# ================= ADMIN =================

@app.route(

    '/admin',

    methods=['GET','POST']

)

def admin():

    if request.method == 'POST':

        username = request.form['username']

        password = request.form['password']

        if (

            username == "Anand"

            and

            password == "Alexa"

        ):

            session['admin'] = True

            return redirect(

                '/adminpanel'

            )

    return render_template(

        'login.html'

    )

# ================= ADMIN PANEL =================

@app.route('/adminpanel')

def adminpanel():

    if 'admin' not in session:

        return redirect(

            '/admin'

        )

    return render_template(

        'admin.html',

        total_users=len(users),

        users=users

    )

# ================= ADMIN LOGOUT =================

@app.route('/admin_logout')

def admin_logout():

    session.pop(

        'admin',
        None

    )

    return redirect('/')

# ================= LOGOUT =================

@app.route('/logout')

def logout():

    session.clear()

    return redirect('/')

# ================= MAIN =================

if __name__ == '__main__':

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=True

    )