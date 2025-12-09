This project is a fully functional Customer Support Ticketing System built with the Django framework. It features a structured workflow where authenticated users can create support tickets with attachments, categorized by department and priority. Each ticket contains a threaded discussion section where both users and staff can post replies, enabling real-time communication and issue resolution.

The project uses Django’s ModelForm architecture to capture ticket and reply data and integrates FileField support for document/image attachments. The routing is modular, with clean separation using tickets/urls.py and project-level URL inclusion. Views use login_required decorators to ensure secure access, and message alerts are integrated for user feedback.

A powerful Django Admin dashboard is included, enabling administrators to manage tickets, track activity logs, monitor internal notes, and oversee all user interactions. The admin panel is enhanced using custom filters, search fields, and list displays for improved data visibility.

The project architecture is deployment-ready, supporting static and media file handling, REST API serialization for future mobile or frontend integration, and compatibility with Render, Railway, and PythonAnywhere for cloud deployment.

This system demonstrates real-world backend concepts including:

Model-view-template design

Authentication and access control

Form handling and validation

File uploads and media management

Admin customization

URL routing and namespace management

REST serialization

Scalability for future API or frontend expansion


# 🎫 Django Ticket Support System

A full-stack **Django-based Ticketing & Customer Support System** that enables users to create support tickets, upload attachments, and communicate through threaded replies. The system includes an admin dashboard for managing tickets, replies, departments, and internal notes. Designed with clean architecture using Django models, views, forms, URL routing, and media handling.

---

## 🚀 Features

### 🧑‍💻 User Features
- User authentication and login protection
- Create support tickets with title, description, priority, department, and attachments
- View ticket details and conversation history
- Add replies with optional file uploads
- View all previous replies in chronological order
- Automatic success messages using Django messages

### 🛠️ Admin Features
- Fully functional Django Admin dashboard
- Manage Tickets, Ticket Replies, Departments, Activity Logs, and Internal Notes
- Search, filter, and sort data efficiently
- Add notes or update ticket status through admin panel

### 💾 Backend Architecture
- Django Models (Ticket, TicketReply, Department, ActivityLog, InternalNote)
- Django Forms for ticket creation and reply submission
- Login Protected Views using `login_required`
- Dedicated URL routing with namespacing
- File uploads and media management (`MEDIA_URL` / `MEDIA_ROOT`)
- Django REST Framework serializers for future API expansion

---

## 🗂️ Project Structure

tickets/
│── admin.py
│── models.py
│── views.py
│── forms.py
│── urls.py
│── templates/tickets/
support_project/
│── settings.py
│── urls.py
static/
media/
manage.py


---

## 🧰 Tech Stack

- **Python 3**
- **Django 6**
- **Bootstrap (optional for UI)**
- **SQLite / PostgreSQL (any DB compatible)**
- **Django REST Framework** (serializers prepared)
- **HTML, CSS, JavaScript**

---

## 📦 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/Ticket_Support.git
cd Ticket_Support

---

# 🎉 DONE!  
Your README is now professional, ATS-friendly, and suitable for recruiters and GitHub users.

If you want, I can also create:

✅ Project banner  
✅ Badges (Python, Django, License, etc.)  
✅ Screenshots section  
✅ Installation GIF  

Just tell me!

GitHub: https://github.com/GautamSingh0310
(share your views with me!)
Email: singhgautam0304@gmail.com
