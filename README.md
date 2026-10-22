# 🏛️ GovtInsight

### Government Scheme Monitoring and Citizen Complaint Management System

GovtInsight is a Flask-based web application that helps citizens explore government schemes, monitor implementation progress, share feedback, and submit complaints related to government initiatives. The platform promotes transparency, accountability, and citizen participation.

## ✨ Features

- 🏛️ **Government Schemes:** Browse central and state government schemes.
- 📊 **Progress Monitoring:** View scheme implementation status and program summaries.
- 👍 **Scheme Voting:** Upvote or downvote schemes to share public opinion.
- 🔐 **User Authentication:** Register and log in to a personal account.
- 📝 **Complaint Management:** Submit complaints related to government initiatives.
- 📎 **Document Uploads:** Attach supporting documents to complaints.
- 👤 **User Profile:** View personal activity and complaint history.
- 🛠️ **Admin Dashboard:** Review complaints and update their statuses.
- 📈 **Progress Analytics:** Explore implementation progress through visual summaries.

## 🛠️ Tech Stack

| Technology | Description |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| Flask-SQLAlchemy | Database ORM |
| Flask-Login | Authentication and session management |
| WTForms | Form handling and validation |
| SQLite | Database |
| HTML | Frontend structure |
| CSS | Styling |
| JavaScript | Frontend interactivity |

## 📁 Project Structure

```text
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
```

> **Note:** The contents of `static/` and `templates/` depend on the repository structure. The SQLite database may be created at runtime.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.9 or later
- pip
- Git

### 1. Clone the repository

```bash
git clone https://github.com/SakshamRaj1/GovtInsight.git
```

### 2. Navigate to the project directory

```bash
cd GovtInsight
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 🗄️ Database Configuration

GovtInsight uses SQLite by default. The database configuration is defined in `config.py`:

```python
SQLALCHEMY_DATABASE_URI = "sqlite:///govtinsight.db"
```

You can change the configuration to use another database backend supported by SQLAlchemy.

## 🎯 Use Cases

- Public policy transparency platforms
- Government scheme tracking dashboards
- Civic complaint management systems
- Citizen engagement portals
- Government program monitoring applications

## 🚀 Future Enhancements

- Integration with official government APIs
- Advanced analytics and interactive dashboards
- Email and SMS notifications for complaint updates
- Scheme search and filtering
- Role-based access control
- Improved security and audit logging
- Production deployment

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Commit your changes.
5. Push your branch.
6. Open a pull request.

## 📄 License

Add a license file if you intend to distribute this project under an open-source license.

## 🔗 Repository

[GovtInsight on GitHub](https://github.com/SakshamRaj1/GovtInsight)

⭐ If you find this project useful, consider giving the repository a star!
