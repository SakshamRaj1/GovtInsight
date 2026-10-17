from flask import Flask, render_template, request, redirect, url_for,session,flash,send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_,or_,func
from flask_login import LoginManager, login_user, UserMixin, logout_user, login_required, current_user
from model import db,User,Manifesto, Votes,Complaint,Reports,Upload
from config import Config
import os
from datetime import datetime
import random
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField



app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

with app.app_context():
    db.create_all()
class UploadFileForm(FlaskForm):
    file=FileField("File")
    submit=SubmitField("Upload file")


    
@app.route('/')
def home():
    return render_template('home.html',user=current_user)
@app.route('/admin/complaints')
def admin_complaints():
    complaints = Complaint.query.all() 
    return render_template('admin_complaints.html', complaints=complaints)

@app.route('/admin/update_status/<int:complaint_id>', methods=['POST'])
def update_status(complaint_id):
    new_status = request.form['status']
    complaints=Complaint.query.filter_by(complaint_id=complaint_id).first()
    complaints.status=new_status
    db.session.commit()
    return redirect(url_for('admin_complaints'))
@app.route('/upvote/<int:scheme_id>')
@login_required
def upvote(scheme_id):
    # Check if user already voted on this scheme
    existing_vote = Votes.query.filter_by(user_id=current_user.id, scheme_id=scheme_id).first()
    #scheme_name=Manifesto.query.filter_by(scheme_id=scheme_id).first()
    if existing_vote:
        return ('You have already voted on this scheme.')
    else:
        vote = Votes(user_id=current_user.id, scheme_id=scheme_id, upvote=1, downvote=0)
        db.session.add(vote)
    
    db.session.commit()
    flash("Your upvote has been recorded!", "success")
    return redirect(request.referrer or url_for('cengov'))

@app.route('/downvote/<int:scheme_id>')
@login_required
def downvote(scheme_id):
    #scheme_name=Manifesto.query.filter_by(scheme_id=scheme_id).first()
    existing_vote = Votes.query.filter_by(user_id=current_user.id, scheme_id=scheme_id,).first()
    if existing_vote:
        return ('You have already voted on this scheme.')
    else:
        vote = Votes(user_id=current_user.id, scheme_id=scheme_id, upvote=0, downvote=1)
        db.session.add(vote)

    db.session.commit()
    flash("Your downvote has been recorded.", "success")
    return redirect(request.referrer or url_for('cengov'))





@app.route('/View')
def view():
    # Get all promises with their statuses
    manifesto_data = Manifesto.query.all()
    
    # Calculate counts for each status
    status_counts = {
        'Completed': Manifesto.query.filter_by(status='Completed').count(),
        'Not Completed': Manifesto.query.filter_by(status='Not Completed').count(),
        'In Progress': Manifesto.query.filter_by(status='In Progress').count()
    }
    
    # Calculate percentages
    total = sum(status_counts.values())
    completed_percentage = round((status_counts['Completed'] / total) * 100, 1) if total > 0 else 0
    not_completed_percentage = round((status_counts['Not Completed'] / total) * 100, 1) if total > 0 else 0
    in_progress_percentage = round((status_counts['In Progress'] / total) * 100, 1) if total > 0 else 0

    # Complaint data for bar chart
    promises_data_query = db.session.query(
        Manifesto.scheme_name,
        func.count(Complaint.complaint_id).label('complaints')
    ).outerjoin(Complaint, Manifesto.scheme_id == Complaint.scheme_id) \
     .group_by(Manifesto.scheme_id) \
     .order_by(func.count(Complaint.complaint_id).desc()) \
     .all()

    promises_data = [
        {"promise": scheme, "complaints": complaints}
        for scheme, complaints in promises_data_query
    ]

    # Top 5 most complained promises
    top5 = promises_data[:5]
    top5_total = sum(item["complaints"] for item in top5) or 1
    for item in top5:
        item["percent"] = round((item["complaints"] / top5_total) * 100, 1)

    # Bar chart data
    filtered_data = [p for p in promises_data if p["complaints"] > 0]
    bar_labels = [p["promise"] for p in filtered_data]
    bar_data = [p["complaints"] for p in filtered_data]

    return render_template(
        'view.html',
        manifestc=Manifesto.query.filter_by(status='Completed').all(),
        manifestn=Manifesto.query.filter_by(status='Not Completed').all(),
        manifesto=Manifesto.query.filter_by(status='In Progress').all(),
        completed_percentage=completed_percentage,
        not_completed_percentage=not_completed_percentage,
        in_progress_percentage=in_progress_percentage,
        top5=top5,
        bar_labels=bar_labels,
        bar_data=bar_data,
        user=current_user
    )

@app.route('/complaint')
@login_required
def complaint():
    total_complaints =Complaint.query.count()
    total_resolved = Complaint.query.filter_by(status='Resolved').count()
    manifestos = Manifesto.query.all()
    states_and_uts = ['Delhi', 'Maharashtra', 'UP', 'Gujarat', 'Karnataka']  # or fetch dynamically
    tenure_options = ['2014-2019', '2019-2024', '2024-2029']
    complaints=Complaint.query.filter_by(user_id=current_user.id).all()
    
    return render_template(
        'complaint.html',
        total_complaints=total_complaints,
        total_resolved=total_resolved,
        states_and_uts=states_and_uts,
        tenure_options=tenure_options,
        manifestos=manifestos,
        complaints=complaints
    )


@app.route('/search-manifesto', methods=['GET'])
def search_manifesto():
    query = request.args.get('query', '')
    results = Manifesto.query.filter(Manifesto.scheme_name.ilike(f"%{query}%")).all()
    return render_template('complaint.html', manifestos=results, total_complaints=0, total_resolved=0, states_and_uts=[], tenure_options=[])

@app.route('/file-complaint', methods=['POST'])
@login_required
def file_complaint():
    form=UploadFileForm()
    scheme_id=request.form.get('scheme_id')
    manifesto=Manifesto.query.get(scheme_id)
    scheme_name=manifesto.scheme_name
    gov_type = request.form['gov_type']
    state = request.form['state']
    tenure = request.form['tenure']
    codescription= request.form['codescription']
    gov_id_file = request.files['gov_id']
    #support_files = request.files.getlist('support_docs')

    # Save government ID file
    #gov_id_filename = secure_filename(gov_id_file.filename)
    #gov_id_file.save(os.path.join(app.config['UPLOAD_FOLDER'], gov_id_filename))

    # Save supporting documents
    #support_filenames = []
    #for file in support_files:
        #filename = secure_filename(file.filename)
        #file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        #support_filenames.append(filename)

    new_complaint = Complaint(
        user_id=current_user.id,
        scheme_id=scheme_id,
        scheme_name=scheme_name,
        description=codescription,
        status='pending',
        gov_type=gov_type,
        state=state,
        tenure=tenure,

       # gov_id=gov_id_filename,
        #support_docs=','.join(support_filenames)
    )
    uploaded=Upload(
        filename=gov_id_file.filename,
        data=gov_id_file.read()

    )

    db.session.add(new_complaint)
    db.session.add(uploaded)
    db.session.commit()
    complaint_number = random.randint(100000, 999999)
    # Here you can save form data / files to DB or filesystem
    states_and_uts = ["Delhi", "Maharashtra", "Punjab", "Goa"]
    tenure_options = ["2024-Current", "2019-2024", "2014-2019"]
    total_complaints = 1216  # just increment for demo
    total_resolved = int(0.1 * total_complaints)
    complaint_number = f"CMP-{random.randint(10000,99999)}"

    flash(f'Complaint filed successfully. Your complaint number is {complaint_number}', 'success')
    return redirect(url_for('complaint'))

@app.route('/download/<upload_id>')
def download(upload_id):
    upload=Upload.query.filter_by(id=upload_id).first()
    #return send_file(BytesIO(upload.data),attachment_filename=upload.filename, as_attachment=True)

@app.route('/Login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email=request.form['email']
        password=request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.password == password:
            login_user(user)
            return redirect(url_for("profile"))
        elif email=='admin@gmail.com' and password== 'admin':
            return redirect(url_for('admin_complaints'))
        else:
            return "Invalid credentials" 
    return render_template('login.html')


@app.route('/Signup',methods=['GET','POST'])
def signup():
    if request.method=='POST':
        fullname=request.form['name']
        emailid=request.form['email']
        passw=request.form['password']
        phone_no=request.form['phone']
        aadhar_no=request.form['aadhaar']

        new_user=User(name=fullname,email=emailid,phone=phone_no,password=passw,aadhar=aadhar_no)
        db.session.add(new_user)
        db.session.commit()
        return redirect ('/Login') 

    return render_template('signup.html')

@app.route('/Central-Govt')
def cengov():
    manifestos=Manifesto.query.filter_by(start_year=20).all()
    manifestos2=Manifesto.query.filter_by(start_year=2019).all()
    
    #Vote=Votes.query.filter_by(scheme_id=Manifesto.scheme_id ).group_by(Manifesto.scheme_id).all()
    #total_upvotes=func.sum(Votes.upvote)
    #total_downvotes=func.sum(Votes.downvote)
    
    results = db.session.query(
    Manifesto.scheme_id,
    Manifesto.scheme_name,
    Manifesto.tenure,
    Manifesto.status,
    Manifesto.description,
    func.sum(Votes.upvote).label('total_upvotes'),
    func.sum(Votes.downvote).label('total_downvotes')
    ).outerjoin(Votes, Votes.scheme_id==Manifesto.scheme_id).group_by(Manifesto.scheme_id).all()
    
    return render_template('cengov.html',manifesto=manifestos,results=results)

@app.route('/State-Govt')
def stategov():
    manifestos = Manifesto.query.filter_by(scheme_type='state').all()
    
    results = db.session.query(
        Manifesto.scheme_id,
        Manifesto.scheme_name,
        Manifesto.tenure,
        Manifesto.status,
        Manifesto.description,
        func.sum(Votes.upvote).label('total_upvotes'),
        func.sum(Votes.downvote).label('total_downvotes')
    ).outerjoin(Votes, Votes.scheme_id == Manifesto.scheme_id)\
     .filter(Manifesto.scheme_type == 'state')\
     .group_by(Manifesto.scheme_id).all()
    return render_template('stategov.html',results=results)

@app.route('/profile',methods=['POST','GET'])
@login_required
def profile():
    voted_promises = Votes.query.filter_by(user_id=current_user.id).all()
    filed_complaints = Complaint.query.filter_by(user_id=current_user.id).all()
    
    return render_template(
        'profile.html',
        voted_promises=voted_promises,
        filed_complaints=filed_complaints,user=current_user
    )

if __name__ == '__main__':
    app.run(debug=True)
