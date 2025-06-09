Django ChatterBot Web App
![alt text](https://img.shields.io/badge/Python-3.8+-blue.svg)

![alt text](https://img.shields.io/badge/Django-3.2+-green.svg)

![alt text](https://img.shields.io/badge/ChatterBot-1.0.5-orange.svg)

![alt text](https://img.shields.io/badge/License-MIT-yellow.svg)
A simple yet powerful web-based chatbot application built with the Django framework and the ChatterBot library. This project provides a clean user interface for real-time conversations with a trainable AI bot.
Note: You can replace the GIF above with your own screenshot or a more detailed GIF of the application in action!
✨ Features
Interactive Chat Interface: A clean and simple UI for seamless conversation.
Real-time Responses: Get instant replies from the chatbot powered by AJAX, so the page doesn't need to reload.
Trainable AI: The bot uses ChatterBot's logic adapters and can be trained on custom conversation corpuses.
Scalable Backend: Built on the robust and scalable Django web framework.
Easy to Set Up: Get the project running locally with just a few commands.
🛠️ Tech Stack
Backend: Django
Chatbot Engine: ChatterBot
Frontend: HTML, CSS, JavaScript (with AJAX for asynchronous requests)
Database: SQLite (default, easily configurable)
🚀 Getting Started
Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.
Prerequisites
Make sure you have the following installed on your system:
Python (3.8 or higher)
pip (Python package installer)
Git
Installation
Clone the repository:
git clone https://github.com/Praveen23-kk/ChatBot_Django_Web.git
cd ChatBot_Django_Web
Use code with caution.
Sh
Create and activate a virtual environment:
On Windows:
python -m venv venv
.\venv\Scripts\activate
Use code with caution.
Sh
On macOS/Linux:
python3 -m venv venv
source venv/bin/activate
Use code with caution.
Sh
Install the required dependencies:
pip install -r requirements.txt
Use code with caution.
Sh
Train the ChatterBot corpus:
This is a crucial step to make your bot knowledgeable. ChatterBot comes with pre-built corpuses you can train it on.
python manage.py train
Use code with caution.
Sh
Apply database migrations:
python manage.py migrate
Use code with caution.
Sh
Run the development server:
python manage.py runserver
Use code with caution.
Sh
Open your browser and navigate to http://127.0.0.1:8000/. You should now be able to chat with your bot!
📂 Project Structure
Here is an overview of the key files in the project:
ChatBot_Django_Web/
├── Chatbot_Project/      # Main Django project settings
│   ├── settings.py
│   └── urls.py
├── chatbot/              # The core chatbot Django app
│   ├── admin.py
│   ├── apps.py
│   ├── views.py          # Contains the logic for handling chat requests
│   └── urls.py
├── static/               # CSS, JS, and image files
├── templates/            # HTML templates
│   └── index.html
├── manage.py             # Django's command-line utility
└── requirements.txt      # List of Python dependencies
Use code with caution.
🤝 Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.
Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
📄 License
This project is distributed under the MIT License. See the LICENSE file for more information.
