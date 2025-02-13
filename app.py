from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import StringField, validators, PasswordField, SubmitField 
from wtforms.validators import DataRequired, Email
import email_validator
from flask_bootstrap import Bootstrap
from flask_mail import Mail, Message
import os

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "kashish2210"

class contactForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()]) 
    email = StringField(label='Email', validators=[DataRequired(), Email(granular_message=True)]) 
    message = StringField(label='Message')
    phone_number = StringField(label='phone number')
    submit = SubmitField(label="SEND MESSAGE")

# Flask-Mail Configuration
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = "shrivastavkashish420@gmail.com"
app.config["MAIL_PASSWORD"] = "nmfg vcvj hcvq ldbi"
app.config["MAIL_DEFAULT_SENDER"] = "shrivastavkashish420@gmail.com"

mail = Mail(app)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    cform = contactForm()
    if cform.validate_on_submit():
        name = cform.name.data
        user_email = cform.email.data  # User's entered email
        message_body = cform.message.data

        # Create email message
        msg = Message(
            subject="New Contact Form Submission",
            recipients=["shrivastavkashish420@gmail.com"],  # Your email
            body=f"Name: {name}\nEmail: {user_email}\nMessage: {message_body}",
            sender=user_email  # Set sender dynamically
        )

        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash(f"Error sending email: {str(e)}", "danger")

    return render_template("contactus.html", form=cform)

@app.route('/register', methods=['GET', 'POST'])
def userform():
    if request.method == 'POST':
        return "Hello Kashish"
    return render_template('userform.html')

@app.route('/register', methods=['GET', 'POST'])

@app.route("/")
def home():
    return render_template('index.html')
@app.route("/course")
def courses():
    return render_template('courses.html')





if __name__ == '__main__':
    app.run(debug=True)
    port = int(os.environ.get("PORT", 8000))  # Use the port provided by Render
    app.run(host="0.0.0.0", port=port)
