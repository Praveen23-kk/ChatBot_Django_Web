# Django ChatterBot Web App

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-3.2+-green.svg)](https://www.djangoproject.com/)
[![ChatterBot](https://img.shields.io/badge/ChatterBot-1.0.5-orange.svg)](https://github.com/gunthercox/ChatterBot)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A simple yet powerful web-based chatbot application built with the Django framework and the ChatterBot library. This project provides a clean user interface for real-time conversations with a trainable AI bot.



![ChatBot Demo](https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXY0aWp5Nmx0ZXI0NjEweHY1ZGs0ZGF4M25sbmRuNWdncHE0ZDQ3YyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/U0IbLd9eLAPNMEGfGy/giphy.gif)

## ✨ Features

- **Interactive Chat Interface**: A clean and simple UI for seamless conversation.
- **Real-time Responses**: Get instant replies from the chatbot powered by AJAX, so the page doesn't need to reload.
- **Trainable AI**: The bot uses ChatterBot's logic adapters and can be trained on custom conversation corpuses.
- **Scalable Backend**: Built on the robust and scalable Django web framework.
- **Easy to Set Up**: Get the project running locally with just a few commands.

## 🛠️ Tech Stack

- **Backend**: Django
- **Chatbot Engine**: ChatterBot
- **Frontend**: HTML, CSS, JavaScript (with AJAX for asynchronous requests)
- **Database**: SQLite (default, easily configurable)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Make sure you have the following installed on your system:
- Python (3.8 or higher)
- pip (Python package installer)
- Git

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Praveen23-kk/ChatBot_Django_Web.git
    cd ChatBot_Django_Web
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install the required dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Train the ChatterBot corpus:**
    This is a crucial step to make your bot knowledgeable. This command trains the bot on an English corpus.
    ```sh
    python manage.py train
    ```

5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

7.  **Open your browser** and navigate to `http://127.0.0.1:8000/`. You should now be able to chat with your bot!

## 📂 Project Structure

Here is an overview of the key files in the project:
ChatBot_Django_Web/
├── Chatbot_Project/ # Main Django project settings
│ ├── settings.py
│ └── urls.py
├── chatbot/ # The core chatbot Django app
│ ├── admin.py
│ ├── apps.py
│ ├── views.py # Contains the logic for handling chat requests
│ └── urls.py
├── static/ # CSS, JS, and image files
├── templates/ # HTML templates
│ └── index.html
├── manage.py # Django's command-line utility
└── requirements.txt # List of Python dependencies


## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is distributed under the MIT License. See the `LICENSE` file for more information.

## 📧 Contact

Praveen Kumar - [praveennaaz23@gmail.com](mailto:praveennaaz23@gmail.com)

Project Link: [https://github.com/Praveen23-kk/ChatBot_Django_Web](https://github.com/Praveen23-kk/ChatBot_Django_Web)
