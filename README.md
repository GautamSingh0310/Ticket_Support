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
