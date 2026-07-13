import os
import json
import pymysql
import pymysql.cursors
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load secret key parameters and tokens safely out of your root .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET", "build_cv_secret_fallback_key_123")

def get_db_connection():
    """Establishes an on-demand database connection using pure PyMySQL drivers."""
    return pymysql.connect(
        host=os.getenv("MYSQL_HOST", "127.0.0.1"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD"),
        database=os.getenv("MYSQL_DB", "ai_resume_db"),
        cursorclass=pymysql.cursors.DictCursor  # Automatically structures rows as dictionary maps
    )

# ==========================================
#         FRONTEND VIEW CONTROLLERS
# ==========================================

@app.route('/')
def home_page():
    """Serves the main aesthetic menu landing page dashboard view hub."""
    return render_template('index.html')

@app.route('/builder')
def builder_page():
    """Serves the feature-packed live canvas resume customizer workspace environment."""
    return render_template('builder.html')

@app.route('/portfolio')
def portfolio_page():
    """Serves your new data explorer history tracker log archive view table."""
    return render_template('portfolio.html')

# ==========================================
#             API ENDPOINT ROUTING
# ==========================================

@app.route('/api/save-cv', methods=['POST'])
def save_custom_cv_record():
    """
    Saves your current resume fields, design customizations, 
    and block summaries straight to your MySQL database instance.
    """
    try:
        data = request.get_json()
        if not data or not data.get('name'):
            return jsonify({"error": "Bad Request. Critical field 'name' parameter is missing."}), 400
            
        connection = get_db_connection()
        with connection.cursor() as cursor:
            query = """
                INSERT INTO parsed_resumes (
                    candidate_name, email, chosen_layout, chosen_font, 
                    chosen_color, raw_text, chronological_body
                ) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (
                data.get('name'),
                data.get('email', ''),
                data.get('layout', 'layout-classic'),
                data.get('font', 'font-sans'),
                data.get('color', '#4F46E5'),
                data.get('summary_box', ''),     # maps to raw_text
                data.get('experience_box', '')  # maps to chronological_body
            ))
            
        connection.commit()
        connection.close()
        
        return jsonify({
            "status": "success", 
            "message": "Resume blueprint successfully archived inside BuildCV.ai portfolio!"
        }), 201
        
    except Exception as e:
        return jsonify({"error": f"Database transactional pipeline execution crash: {str(e)}"}), 500


@app.route('/api/list-cvs', methods=['GET'])
def list_saved_cv_blueprints():
    """Fetches all past layout histories from MySQL to display on the Portfolio tracker table."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            # Queries the exact columns altered in MySQL Workbench
            cursor.execute("""
                SELECT id, candidate_name, email, chosen_layout, created_at 
                FROM parsed_resumes 
                ORDER BY created_at DESC
            """)
            rows = cursor.fetchall()
            
        connection.close()
        return jsonify({"status": "success", "data": rows}), 200
        
    except Exception as e:
        return jsonify({"error": f"Failed fetching database logs matrix index: {str(e)}"}), 500


@app.route('/api/saved-resumes', methods=['GET'])
def get_saved_resumes_list():
    """Helper dropdown endpoint to pull high-level index profiles inside the builder view template loader."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, candidate_name, created_at FROM parsed_resumes ORDER BY created_at DESC LIMIT 10")
            rows = cursor.fetchall()
        connection.close()
        return jsonify({"status": "success", "data": rows}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/api/resume/<int:resume_id>', methods=['GET'])
def get_single_resume(resume_id):
    """Fetches a specific database blueprint configuration record to inject back into your form fields."""
    try:
        connection = get_db_connection()
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT candidate_name, email, chosen_layout, chosen_font, chosen_color, raw_text, chronological_body 
                FROM parsed_resumes 
                WHERE id = %s
            """, (resume_id,))
            row = cursor.fetchone()
        connection.close()
        
        if row:
            return jsonify({"status": "success", "data": row}), 200
        return jsonify({"error": "Target user profile layout blueprint index not found"}), 404
        
    except Exception as e:
        return jsonify({"error": f"Extraction query failure logged: {str(e)}"}), 500

# ==========================================
#          ENGINE INITIALIZATION LOOP
# ==========================================

if __name__ == '__main__':
    # Stand up your local development runtime background listening stack wrapper service
    app.run(debug=True, port=5000)
