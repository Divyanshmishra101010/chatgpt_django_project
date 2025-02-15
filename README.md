# Django ChatGPT Integration

## 📌 Project Overview
This is a Django-based web application that integrates OpenAI's ChatGPT to enable chatbot functionality. Users can interact with an AI-powered chatbot through a simple frontend interface.

---

## 🚀 Features
- User-friendly chat interface
- OpenAI ChatGPT API integration
- Handles errors and API failures gracefully
- Secure API key management using `.env`

---

## 🛠️ Setup and Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/django-chatgpt.git
cd django-chatgpt
```

### 2️⃣ Create and Activate Virtual Environment
```bash
python -m venv myenv  # Create virtual environment
source myenv/bin/activate  # Activate (Linux/macOS)
myenv\Scripts\activate  # Activate (Windows)
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
Create a `.env` file in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key
```

### 5️⃣ Apply Migrations
```bash
python manage.py migrate
```

### 6️⃣ Run the Server
```bash
python manage.py runserver
```
Access the app at: [http://127.0.0.1:8000/chat/](http://127.0.0.1:8000/chat/)

---

## 🔧 Project Structure
```
chatgpt_project/   # Main project folder
│── chatgpt_app/   # Django app for ChatGPT integration
│   │── migrations/
│   │── static/    # Static files (CSS, JS)
│   │── templates/ # HTML templates
│   │── views.py   # Handles chat logic
│   │── urls.py    # URL routing
│
│── chatgpt_project/
│   │── settings.py  # Project settings
│   │── urls.py      # Main URL configuration
│
│── myenv/  # Virtual environment (excluded from Git)
│── .gitignore
│── .env  # API keys (excluded from Git)
│── requirements.txt
│── manage.py  # Django management script
```

---

## 🛠️ API Usage
The chat API is available at:
```
POST /api/chat/
```
### Request Body (JSON):
```json
{
    "message": "Hello, ChatGPT!"
}
```
### Response:
```json
{
    "response": "Hello! How can I assist you today?"
}
```

---

## 🔥 Troubleshooting
### **1️⃣ OpenAI API Quota Exceeded (Error 429)**
- Check your OpenAI quota: [OpenAI Billing & Usage](https://platform.openai.com/account/usage)
- Upgrade your plan or use a new API key.

### **2️⃣ TemplateDoesNotExist Error**
- Ensure `chat.html` exists in `chatgpt_app/templates/chat.html`.
- Run `python manage.py collectstatic` if using static files.

### **3️⃣ Server Not Running**
- Ensure `myenv` is activated before running `python manage.py runserver`.
- Check for missing dependencies with `pip install -r requirements.txt`.

---

## 📜 License
This project is open-source and available under the MIT License.

---

## 🤝 Contributing
Feel free to fork this project and submit pull requests!

---

## 📬 Contact
For any questions, reach out at: `your-email@example.com`

