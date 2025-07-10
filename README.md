# School Reviews

A modern, minimal web app for submitting and browsing school reviews. Built with Flask, MySQL, and Bootstrap, inspired by Typeform’s clean UI.

---

## 🚀 Features

- **Add Reviews:** Submit a review for any school, including rating and comments.
- **Browse Reviews:** See all reviews in a clean, responsive table.
- **Live Search:** Instantly filter reviews by school name as you type.
- **Form Validation:** Both client and server-side validation for all fields.
- **Flash Messages:** User-friendly error and success notifications.
- **Modern UI:** Custom CSS and Bootstrap for a Typeform-inspired, mobile-friendly look.

---

## 🛠️ Tech Stack

- **Backend:** Python 3, Flask
- **Database:** MySQL
- **Frontend:** Bootstrap 5, custom CSS, Animate.css
- **Templating:** Jinja2

---

## 📦 Project Structure

```
school_review_app/
├── app.py              # Main Flask app
├── config.py           # DB config
├── requirements.txt    # Python dependencies
├── templates/          # Jinja2 HTML templates
│   ├── base.html
│   ├── add_review.html
│   └── reviews.html
├── static/             # (Optional) Custom CSS/JS
├── setup_database.sql  # DB schema
└── README.md
```

---

## ⚡ Setup & Run

1. **Clone the repo:**
   ```bash
   git clone <repo-url>
   cd school_review_app
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Set up the database:**
   - Start MySQL and run `setup_database.sql` in your MySQL client.
   - Update `config.py` with your DB credentials.
4. **Run the app:**
   ```bash
   python app.py
   ```
5. **Open in browser:**
   - Add reviews: [http://localhost:5000/addreview](http://localhost:5000/addreview)
   - Browse reviews: [http://localhost:5000/reviews](http://localhost:5000/reviews)

---

## ✨ Usage
- Fill out the review form and submit.
- Browse all reviews, use the search bar to filter by school name.
- All data is stored in MySQL and loaded dynamically.

---

## 🙌 Credits
- UI inspired by [Typeform](https://www.typeform.com/surveys)
- Built by [Your Name]

---

## License
MIT 