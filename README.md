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
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
├── govtinsight.db
└── README.md


Note: The contents of the static/ and templates/ directories may vary depending on the actual repository structure. The SQLite database may be generated when the application runs.

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

