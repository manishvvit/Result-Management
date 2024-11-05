from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Example student data with detailed marks
students = [
    {
        "roll_number": "123",
        "dob": "2000-01-01",
        "name": "John Doe",
        "marks": {
            "Math": {"obtained": 80, "max": 100},
            "Science": {"obtained": 85, "max": 100},
            "English": {"obtained": 75, "max": 100}
        },
        "total_obtained": 240,
        "total_max": 300,
        "result": "Pass"
    },
    {
        "roll_number": "456",
        "dob": "2001-02-02",
        "name": "Jane Smith",
        "marks": {
            "Math": {"obtained": 45, "max": 100},
            "Science": {"obtained": 50, "max": 100},
            "English": {"obtained": 40, "max": 100}
        },
        "total_obtained": 135,
        "total_max": 300,
        "result": "Fail"
    }
]

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        roll_number = request.form['roll_number']
        dob = request.form['dob']

        student = next((s for s in students if s["roll_number"] == roll_number and s["dob"] == dob), None)

        if student:
            return render_template('result.html', student=student)
        else:
            flash("Invalid Roll Number or Date of Birth. Please try again.")
            return redirect(url_for('login'))

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
