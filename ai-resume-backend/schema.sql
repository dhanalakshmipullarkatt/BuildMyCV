-- 1. Create a dedicated database instance for your application context
CREATE DATABASE IF NOT EXISTS ai_resume_db;

-- 2. Target this instance for all subsequent modifications
USE ai_resume_db;

-- 3. Construct a structural storage table for candidates
CREATE TABLE IF NOT EXISTS parsed_resumes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    candidate_name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    skills TEXT,
    experience_years INT DEFAULT 0,
    raw_text LONGTEXT,
    ai_score INT,
    ai_feedback TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
