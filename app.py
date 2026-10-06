from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template("dashboard.html")

@app.route('/special-session')
def special_session():
    return render_template("special_session.html")

@app.route('/call-for-papers')
def call_for_papers():
    return render_template("call_for_papers.html")

@app.route('/advisory-committee')
def advisory_committee():
    return render_template("advisory_committee.html")

@app.route('/organizing-committee')
def organizing_committee():
    return render_template("organizing_committee.html")
    
@app.route('/technical-committee')
def technical_committee():
    return render_template("technical_committee.html")
    
@app.route('/steering-committee')
def steering_committee():
    return render_template("steering_committee.html")

@app.route('/IEEE-committee')
def IEEE_committee():
    return render_template("IEEE_committee.html")

@app.route('/approved-session')
def approved_session():
    return render_template("approved_session.html")

@app.route('/tracks')
def become_a_sponser():
    return render_template("tracks.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/important-dates')
def important_dates():
    return render_template("important_dates.html")

@app.route('/registration-details')
def registration_details():
    return render_template("registration_details.html")

# @app.route('/pay-registration-fees')
# def pay_registration_fees():
#     return render_template("pay_registration_fees.html")

@app.route('/paper-submission')
def paper_submission():
    return render_template("paper_submission.html")

@app.route('/keynotes')
def keynotes():
    return render_template("keynotes.html")

@app.route('/schedule')
def schedule():
    return render_template("schedule.html")



if __name__ == "__main__":
    app.run(debug=True)
