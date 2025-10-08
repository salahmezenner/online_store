# 🛍️   SalahStore – Full-Stack E-Commerce Web App

> A modern online shopping experience built with **Django** and **Bootstrap** — featuring products, categories, a dynamic cart, and a secure checkout flow.

---

## 🎯 Project Overview

**SalahStore** is a fully functional e-commerce platform developed as part of my Django learning and portfolio journey.  
It focuses on providing a clean, intuitive shopping experience with real-world features like a product catalog, cart management, checkout, and live stock updates.

🧩 Built completely from scratch using:
- **Django 5 (Python)** for backend logic  
- **Bootstrap 5** for modern responsive UI  
- **AJAX (Fetch API)** for smooth, real-time cart updates  

---

## 🌟 Features

✅ **Homepage**
- Hero banner and featured product grid  
- Category cards with hover animations  

✅ **Catalog**
- Browse all products or filter by category  
- Each product has image, price, and description  

✅ **Cart System**
- Add/remove items, choose quantity  
- Real-time quantity updates with AJAX  
- Cart total recalculates instantly  

✅ **Checkout**
- Secure order creation form  
- Auto stock reduction after purchase  

✅ **Admin Dashboard**
- Manage products, orders, and stock directly via Django Admin  

---

## 🧰 Tech Stack

| Area | Technologies |
|------|---------------|
| **Frontend** | HTML5, CSS3, Bootstrap 5, AJAX |
| **Backend** | Python 3, Django 5 |
| **Database** | SQLite (local) / PostgreSQL (prod) |

---

## 💻 Setup Instructions

### 1️⃣ Clone the repository  
git clone https://github.com/yourusername/mystore.git 

cd mystore

### 2️⃣ Create a virtual environment

python -m venv venv

source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3️⃣ Install dependencies

pip install -r requirements.txt

### 4️⃣ Run migrations

python manage.py migrate

### 5️⃣ Run the app

python manage.py runserver

Then open your browser at 👉 http://127.0.0.1:8000/

---

## 🏁 Future Enhancements

🔹 Add user authentication (login/register)

🔹 Integrate Stripe payments

🔹 Add order history for users

🔹 Deploy to Render with a live domain

## 👨‍💻 Author
Mezenner Salah
📧 mezennersalah@yahoo.com

