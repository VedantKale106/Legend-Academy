from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'legend-academy-secret-key-2025'

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'legendacademy45official@gmail.com'
app.config['MAIL_PASSWORD'] = 'mmfw nbru uidk gtim'  # Replace with Gmail App Password
app.config['MAIL_DEFAULT_SENDER'] = 'legendacademy45official@gmail.com'

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/gallery')
def gallery():
    image_folder = os.path.join(app.static_folder, 'images')
    images = []
    if os.path.exists(image_folder):
        images = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    return render_template('gallery.html', images=images)

@app.route('/donate')
def donate():
    return render_template('donate.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        try:
            msg = Message(
                subject=f'Legend Academy - New Contact Form Submission',
                recipients=['meherdishant702@gmail.com'],
                body=f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏫 LEGEND ACADEMY - CONTACT FORM SUBMISSION
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Sender Details:
📝 Name: {name}
📧 Email: {email}

Message Content:
━━━━━━━━━━━━
{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
This is an automated message from Legend Academy's contact form.
Please respond to the sender at their provided email address.
"""
            )
            mail.send(msg)
            flash('Thank you for contacting us! We will get back to you soon.', 'success')
            return redirect(url_for('contact'))
        except Exception as e:
            flash('Sorry, there was an error sending your message. Please try again or contact us directly.', 'error')
            print(f"Error: {e}")
    
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
