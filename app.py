from flask import Flask, render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///databas2.db"
db = SQLAlchemy(app)

class appoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    patientName = db.Column(db.String(200), nullable=False)
    dob = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    mobileNumber = db.Column(db.Integer, nullable=False)
    specialization = db.Column(db.String(200), nullable=False)
    doctorName = db.Column(db.String(200), nullable=False)
    appointmentDate = db.Column(db.Integer, nullable=False)
    appointmentSlot = db.Column(db.String(200), nullable=False)
    TimeOfBooking = db.Column(db.DateTime, default=datetime.utcnow)

    

    def __repr__(self) -> str:
        return f"{self.patientName}"

with app.app_context():
    db.create_all()



@app.route('/appointment.html', methods=['GET','POST'])
def appointment():
    if request.method=='POST':
        patientName = request.form['patientName']
        dob = request.form['dob']
        city = request.form['city']
        email = request.form['email']
        mobileNumber = request.form['mobileNumber']
        specialization = request.form['specialization']
        doctorName = request.form['doctorName']
        appointmentDate = request.form['appointmentDate']
        appointmentSlot = request.form['appointmentSlot']
        databas2 = appoint(patientName=patientName, dob=dob, city=city, email=email, mobileNumber=mobileNumber, specialization=specialization, doctorName=doctorName, appointmentDate=appointmentDate, appointmentSlot=appointmentSlot)
        db.session.add(databas2)
        db.session.commit()
    return render_template('appointment.html')


@app.route('/admindata.html')
def admindata():
    allappoint = appoint.query.all()
    return render_template('admindata.html',allappoint=allappoint)

@app.route('/adminlogin.html')
def adminlogin():
    return render_template('adminlogin.html')

@app.route('/doctor.html')
def doctor():
    return render_template('doctor.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/home.html')
def home():
    return render_template('home.html')

@app.route('/services.html')
def services():
    return render_template('services.html')



@app.route('/delete/<int:id>')
def delete(id):
    databas2 = appoint.query.filter_by(id=id).first()
    db.session.delete(databas2)
    db.session.commit()
    return redirect("/admindata.html")

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    if request.method=='POST':
        patientName = request.form['patientName']
        dob = request.form['dob']
        city = request.form['city']
        email = request.form['email']
        mobileNumber = request.form['mobileNumber']
        specialization = request.form['specialization']
        doctorName = request.form['doctorName']
        appointmentDate = request.form['appointmentDate']
        appointmentSlot = request.form['appointmentSlot']
        databas2 = appoint.query.filter_by(id=id).first()
        databas2.patientName=patientName
        databas2.dob=dob
        databas2.city=city
        databas2.email=email
        databas2.mobileNumber=mobileNumber
        databas2.specialization=specialization
        databas2.doctorName=doctorName
        databas2.appointmentDate=appointmentDate
        databas2.appointmentSlot=appointmentSlot
        db.session.add(databas2)
        db.session.commit()
        return redirect("/admindata.html")
    databas2 = appoint.query.filter_by(id=id).first()
    return render_template('update.html', databas2=databas2)




@app.route('/search_by_phone', methods=['POST'])
def search_by_phone():
    if request.method == 'POST':
        search_phone = request.form['search_phone']
        print(f"Searching for phone number: {search_phone}")
        search_results = appoint.query.filter_by(mobileNumber=search_phone).all()
        print(f"Search Results: {search_results}")
        return render_template('admindata.html', allappoint=search_results)


@app.route('/show_all_records_clear', methods=['POST'])
def show_all_records_clear():
    allappoint = appoint.query.all()
    return render_template('admindata.html', allappoint=allappoint)



@app.route('/search_by_phone_appointment', methods=['POST'])
def search_by_phone_appointment():
    if request.method == 'POST':
        search_phone = request.form['search_phone']
        print(f"Searching for phone number: {search_phone}")
        search_results = appoint.query.filter_by(mobileNumber=search_phone).all()
        print(f"Search Results: {search_results}")
        return render_template('appointment.html', appointments=search_results)



@app.route('/show_all_records_appointment', methods=['POST'])
def show_all_records_appointment():
    allappoint = appoint.query.all()
    return render_template('appointment.html', allappoint=allappoint)


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    # Check if the username and password match the predefined values
    if username == 'adminhp@gmail.com' and password == 'admin123':
        # Redirect to the admin data page
        return redirect('/admindata.html')
    else:
        # If the username or password is incorrect, render the login page with an error message
        return render_template('adminlogin.html', message='Invalid ID or password. Please try again.')



if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
