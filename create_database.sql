-- Database setup for Advertisement Personalization System
-- Run this script to create all necessary tables

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS project_data;
USE project_data;

-- Table 1: userdata2 - Stores current detected user information
DROP TABLE IF EXISTS userdata2;
CREATE TABLE userdata2 (
    id INT PRIMARY KEY,
    gender VARCHAR(50),
    age VARCHAR(50),
    fashion_type VARCHAR(100)
);

-- Insert default row with id=1 (used by the application)
INSERT INTO userdata2 (id, gender, age, fashion_type) 
VALUES (1, 'Male', '(18-28)', 'None');

-- Table 2: image_data - Stores advertisement images and links
DROP TABLE IF EXISTS image_data;
CREATE TABLE image_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    gender VARCHAR(50) NOT NULL,
    age VARCHAR(50) NOT NULL,
    fashion_type VARCHAR(100),
    img LONGBLOB NOT NULL,
    link VARCHAR(500),
    INDEX idx_gender_age (gender, age),
    INDEX idx_gender_age_fashion (gender, age, fashion_type)
);

-- Display table structures
DESCRIBE userdata2;
DESCRIBE image_data;

SELECT 'Database and tables created successfully!' AS Status;
