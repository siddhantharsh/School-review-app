import os
from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import config

app = Flask(__name__)
app.secret_key = os.environ.get(
    'SECRET_KEY', 'dev-secret-key-change-in-production'
)

# Database configuration
DB_CONFIG = config.DB_CONFIG


def get_db_connection():
    """Create database connection"""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except Error as e:
        print(f"Database connection failed: {e}")
        return None


def validate_review(school_name, reviewer_name, rating, comment):
    """Validate review data and return errors list"""
    errors = []

    if not school_name or not school_name.strip():
        errors.append("School name is required")
    elif len(school_name.strip()) > 100:
        errors.append("School name must be 100 characters or less")

    if not reviewer_name or not reviewer_name.strip():
        errors.append("Reviewer name is required")
    elif len(reviewer_name.strip()) > 100:
        errors.append("Reviewer name must be 100 characters or less")

    try:
        rating_int = int(rating)
        if rating_int < 1 or rating_int > 5:
            errors.append("Rating must be between 1 and 5")
    except (ValueError, TypeError):
        errors.append("Rating must be a number between 1 and 5")

    if not comment or not comment.strip():
        errors.append("Comment is required")
    elif len(comment.strip()) > 1000:
        errors.append("Comment must be 1000 characters or less")

    return errors


@app.route('/')
def index():
    """Redirect to add review page"""
    return redirect(url_for('add_review'))


@app.route('/addreview', methods=['GET', 'POST'])
def add_review():
    """Handle review submission"""
    if request.method == 'POST':
        school_name = request.form.get('school_name', '').strip()
        reviewer_name = request.form.get('reviewer_name', '').strip()
        rating = request.form.get('rating', '').strip()
        comment = request.form.get('comment', '').strip()

        errors = validate_review(school_name, reviewer_name, rating, comment)

        if errors:
            for error in errors:
                flash(error, 'error')
            return render_template(
                'add_review.html',
                school_name=school_name,
                reviewer_name=reviewer_name,
                rating=rating,
                comment=comment
            )

        conn = get_db_connection()
        if not conn:
            flash('Database connection failed. Please try again.', 'error')
            return render_template('add_review.html')

        try:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO reviews (school_name, reviewer_name, rating, comment) VALUES (%s, %s, %s, %s)',
                (
                    school_name,
                    reviewer_name,
                    int(rating),
                    comment
                )
            )
            conn.commit()
            cursor.close()
            conn.close()

            flash('Review submitted successfully!', 'success')
            return redirect(url_for('add_review'))

        except Error as e:
            flash(
                f'Failed to save review: {str(e)}', 'error'
            )
            conn.close()
            return render_template('add_review.html')

    return render_template('add_review.html')


@app.route('/reviews')
def reviews():
    """Display all reviews, optionally filtered by school name"""
    school_query = request.args.get('school', '').strip()
    conn = get_db_connection()
    if not conn:
        flash('Database connection failed. Please try again.', 'error')
        return render_template('reviews.html', reviews=[])

    try:
        cursor = conn.cursor(dictionary=True)
        if school_query:
            cursor.execute(
                'SELECT * FROM reviews WHERE school_name LIKE %s ORDER BY id DESC',
                (f'%{school_query}%',)
            )
        else:
            cursor.execute('SELECT * FROM reviews ORDER BY id DESC')
        all_reviews = cursor.fetchall()
        cursor.close()
        conn.close()
    except Error as e:
        flash(f'Failed to load reviews: {str(e)}', 'error')
        conn.close()
        all_reviews = []

    return render_template('reviews.html', reviews=all_reviews)


if __name__ == '__main__':
    app.run(debug=True) 