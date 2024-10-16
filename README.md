
# Personal Task Manager

A simple yet effective web application to help users manage their tasks efficiently. Users can create, read, update, and delete tasks while keeping track of their completion status and due dates. The application also includes user authentication, allowing users to have personalized task lists.


## Features

- User authentication (registration, login, logout)
- Create, update, and delete tasks
- Mark tasks as completed
- Assign due dates to tasks
- Upload images for tasks

## Technologies Used

- **Django**: A high-level Python web framework.
- **Python**: Programming language used for backend development.
- **SQLite**: Database used to store user and task data.
- **HTML/CSS**: For frontend structure and styling.


## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/personal-task-manager.git
   cd personal-task-manager
   ```

2. **Set up a virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the requirements**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

6. **Create a superuser** (optional):
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

- Visit `http://localhost:8000` to access the application.
- Register a new user account or log in with an existing account.
- Start creating tasks, updating their statuses, and managing your task list.

## Contributing

Contributions are welcome! If you have suggestions for improvements or want to add features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


