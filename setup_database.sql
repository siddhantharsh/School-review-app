-- Create the database
CREATE DATABASE IF NOT EXISTS school_reviews;

-- Use the database
USE school_reviews;

-- Create the reviews table
CREATE TABLE IF NOT EXISTS reviews (
    id INT AUTO_INCREMENT PRIMARY KEY,
    school_name VARCHAR(100) NOT NULL,
    reviewer_name VARCHAR(100) NOT NULL,
    rating INT NOT NULL CHECK (rating >= 1 AND rating <= 5),
    comment TEXT NOT NULL
);

-- Show the table structure
DESCRIBE reviews; 