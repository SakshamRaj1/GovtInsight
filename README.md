🏛️ GovtInsight
Government Scheme Monitoring and Citizen Complaint Management System

GovtInsight is a Flask-based web application that enables citizens to explore government schemes, monitor implementation progress, share feedback through voting, and submit complaints related to government initiatives. The platform aims to promote transparency, accountability, and citizen participation.

✨ Features
🏛️ Government Schemes: Browse central and state government schemes.
📊 Progress Monitoring: View scheme implementation status and program summaries.
👍 Scheme Voting: Upvote or downvote schemes to express public opinion.
🔐 User Authentication: Register and log in to a personal account.
📝 Complaint Management: Submit complaints related to government initiatives.
📎 Document Uploads: Attach supporting documents to complaints.
👤 User Profile: View personal activity and complaint history.
🛠️ Admin Dashboard: Review complaints and update their statuses.
📈 Progress Analytics: Display implementation progress through visual summaries.
🛠️ Tech Stack
Technology	Description
Python	Backend programming
Flask	Web framework
Flask-SQLAlchemy	Database ORM
Flask-Login	Authentication and session management
WTForms	Form handling and validation
SQLite	Database
HTML	Frontend structure
CSS	Styling
JavaScript	Frontend interactivity
📁 Project Structure
GovtInsight/
├── app.py
├── config.py
├── model.py
├── requirements.txt
├── instance/
├── static/
├── templates/
├── govtinsight.db
└── README.md


Note: The contents of static/ and templates/ depend on the actual repository structure. The SQLite database may be created at runtime.

⚙️ Installation and Setup
Prerequisites
Python 3.9 or later
pip
Git
1. Clone the Repository
git clone https://github.com/SakshamRaj1/GovtInsight.git

2. Navigate to the Project Directory
cd GovtInsight

3. Create a Virtual Environment
python -m venv .venv

4. Activate the Virtual Environment

Windows:

.venv\Scripts\activate


Linux / macOS:

source .venv/bin/activate

5. Install Dependencies
pip install -r requirements.txt

6. Run the Application
python app.py


Open your browser and visit:

http://127.0.0.1:5000/

🗄️ Database Configuration

GovtInsight uses SQLite by default. The database configuration is defined in config.py.

SQLALCHEMY_DATABASE_URI = 'sqlite:///govtinsight.db'


You can change the configuration to use another supported database backend if needed.

🎯 Use Cases
Public policy transparency platforms
Government scheme tracking dashboards
Civic complaint management systems
Citizen engagement portals
Government program monitoring applications
🚀 Future Enhancements
Integration with official government APIs
Advanced analytics and interactive dashboards
Email and SMS notifications for complaint updates
Scheme search and filtering
Role-based access control
Improved security and audit logging
Production deployment
🤝 Contributing

Contributions are welcome!

Fork the repository.
Create a new branch.
Make your changes.
Commit your changes.
Push your branch.
Open a pull request.
📄 License

Add a license file if you intend to distribute this project under an open-source license.

🔗 Repository

GovtInsight on GitHub

⭐ If you find this project useful, consider giving the repository a star!
