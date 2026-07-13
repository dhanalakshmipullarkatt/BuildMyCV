# BuildCV.ai

BuildCV.ai is a full-stack resume builder studio built with **Python Flask** and **MySQL**. It features a live, dark-themed control workspace that instantly updates an ATS-compliant, single-column print preview canvas on the screen.

---

## ✨ Features

*   **📺 Live Split-Pane View**: Form inputs instantly update the document preview sheet in real time.
*   **🎨 Visual Theme Controls**: Switch between Classic Academic, Modern Accent, and Centered Minimalist layouts, change global font pairings, and use a visual color picker.
*   **📁 Save & Load Portfolio**: Save layouts and unformatted text data straight to a MySQL database table, then reload previous blueprints from a dropdown menu.
*   **🖨️ A4 Print Optimization**: Built-in CSS prints a white, ATS-friendly document while hiding the dark control dashboard automatically.

---

## 🚀 Quick Setup & Installation

### 1. Initialize the MySQL Database
Execute this query inside MySQL Workbench to create the schema and data tables:

```sql
CREATE DATABASE IF NOT EXISTS ai_resume_db;
USE ai_resume_db;

CREATE TABLE IF NOT EXISTS parsed_resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    chosen_layout VARCHAR(100) DEFAULT 'layout-classic',
    chosen_font VARCHAR(100) DEFAULT 'font-sans',
    chosen_color VARCHAR(50) DEFAULT '#4F46E5',
    raw_text LONGTEXT,
    chronological_body LONGTEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### 2. Configure Environment Variables
Create a file named **`.env`** in the root project folder and fill in your connection credentials:

```env
FLASK_SECRET=your_secret_session_key
MYSQL_HOST=127.0.0.1
MYSQL_USER=root
MYSQL_PASSWORD=your_mysql_root_password
MYSQL_DB=ai_resume_db
```

### 3. Install Package Dependencies
Install the pure Python MySQL driver and environment modules:
```bash
pip install Flask PyMySQL python-dotenv
```

### 4. Start the Application
Run the core web handler script:
```bash
python app.py
```
Open your web browser and navigate directly to: **`http://127.0.0.1:5000`**

---

## 📜 License
This project is licensed under the MIT License.
