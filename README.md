# Coding I – Web Application Project

**Due date:** 5/14 @ Midnight  

When you finish, add your names and a demo video link here, then submit one link to your project repository.

**Group Members:** Liam Arnold, Vonde Tobin, Finn Bevill
* [Demo Video (1 per group)](http://includeyourlinkhere)

---

### Project Overview

You will begin with a **pre-built login and authentication system**. Your job is to **extend this project into a full CRUD web application** using Flask and a database.

Your application must allow users to:
- Log in (already implemented)
- Create data
- View data
- Edit data
- Delete data

Each user should only be able to access and modify **their own data**.

---

### Helpful Links for This Unit:
 - [Flask Documentation](https://flask.palletsprojects.com/en/2.3.x/)
 - [SQLite Documentation](https://www.sqlite.org/docs.html)
 - [Bcrypt Documentation](https://pypi.org/project/bcrypt/)
 - [Regex Tutorial for Python](https://docs.python.org/3/library/re.html)
 - [GitHub Cheat-Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
 - [Flask Tutorial](https://www.youtube.com/watch?t=347&v=Z1RJmh_OqeA) (we are already in a virtual environment so ignore comments about env)

---

### Project Requirements:

---

### Part I: Setup & Understanding the Base Code (10 pts)
- Fork the provided repository.
- Successfully run the starter project locally.
- Demonstrate understanding of:
  - Where login happens
  - How users are stored
  - How routes/templates are structured
- Make at least one small modification (e.g., change text on a page) to confirm setup is working.

---

### Part II: Planning Your CRUD App (10 pts)
- Decide what your app will store (journal, listings, notes, etc.).
- Clearly define:
  - What a “record”/“entry” looks like (fields in your database)
- Plan required features:
  - Create
  - Read
  - Update
  - Delete
- Sketch or describe:
  - Pages/routes you will need
  - Basic user flow (what happens after login)
- Complete `planning_and_design.txt`.

---

### Part III: Database for App Content (10 pts)
- Create a **new database table** (separate from users).
- Include appropriate fields (e.g., title, content, timestamp, user_id).
- Ensure:
  - Data persists after restarting the app
  - Each entry is linked to a specific user

---

### Part IV: READ – Display Data (10 pts)
- After login, users are taken to a **main page/dashboard**.
- This page displays a list of entries from the database.
- Requirements:
  - Data is clearly formatted
  - Only shows entries belonging to the logged-in user
  - Page updates correctly when new data is added

---

### Part V: CREATE – Add New Entries (10 pts)
- Provide a form/page to create new entries.
- On submission:
  - Data is saved to the database
  - Entry is linked to the logged-in user
- User is redirected back to the main page and sees the new entry.

---

### Part VI: UPDATE – Edit Entries (10 pts)
- Users can edit existing entries.
- Requirements:
  - Edit form pre-fills with current data
  - Changes are saved to the database
  - Only the owner can edit their entries

---

### Part VII: DELETE – Remove Entries (10 pts)
- Users can delete entries.
- Requirements:
  - Entry is removed from the database
  - Only the owner can delete their entries
  - (Optional but encouraged) confirmation before deletion

---

### Part VIII: User Data Protection & Access Control (5 pts)
- Users cannot:
  - View other users’ data
  - Edit or delete entries they do not own
- Proper checks are implemented in routes (not just hidden buttons).

---

### Part IX: Reflection + Demo Video (25 pts)
- Demo must show:
  - Creating, viewing, editing, deleting entries
  - Login working with your CRUD system
  - All team members must speak
- Reflection includes:
  - What was hardest to implement
  - One bug or issue you solved
  - One improvement you would add

---

### Optional Bonus (+10 pts each)
- Add search, filtering, or sorting
- Improve UI with CSS
- Add timestamps or ordering (newest first)
- Add categories/tags

---

### Key Focus of This Project
- You are no longer **building authentication**
- You are **building a functional database-driven application**

The most important part of this project is:
- Implementing full CRUD functionality
- Connecting data to the logged-in user
- Managing and displaying database content properly
