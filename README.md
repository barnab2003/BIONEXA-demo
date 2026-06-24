# Bionexa

Bionexa is a full-stack online pharmacy web application built with **Django**. It provides a secure platform where customers can browse medicines, upload prescriptions for restricted drugs, manage shopping carts, place orders, and make online payments. The system also includes an administrative workflow for approving prescriptions before allowing the purchase of prescription-only medicines.

---

## Features

### User Authentication

* User registration and login
* Secure authentication using Django Authentication
* User profile management

### Home Page

* Responsive landing page
* Navigation bar
* Featured medicines

### Medicine Management

* Browse available medicines
* View medicine details
* Medicine images
* Stock management
* Prescription-required flag

### Shopping Cart

* Add medicines to cart
* Remove medicines from cart
* Quantity management
* View cart summary

### Order Management

* Place orders
* View order history
* Order items tracking
* Order total calculation

### Prescription System

* Upload prescriptions
* View uploaded prescriptions
* Prescription approval workflow
* Restrict purchase of prescription medicines

### Admin Features

* Review uploaded prescriptions
* Approve or reject prescriptions
* Manage medicines through Django Admin
* Manage users and orders

### Payment Integration

* Razorpay integration
* Secure payment processing
* Payment status tracking
* Linked payments with orders

---

# Tech Stack

### Backend

* Python
* Django

### Frontend

* HTML5
* CSS3
* Bootstrap 5

### Database

* SQLite (Development)
* PostgreSQL/MySQL (Production Ready)

### Payment Gateway

* Razorpay

---

# Project Structure

```
bionexa/
│
├── users/
├── home/
├── medicines/
├── cart/
├── orders/
├── prescriptions/
├── payments/
│
├── templates/
├── static/
├── media/
│
├── manage.py
└── requirements.txt
```

---

# Modules

## Users

* Registration
* Login
* Logout
* Profile

## Home

* Landing page
* Navigation

## Medicines

* Medicine listing
* Medicine details
* Medicine inventory

## Cart

* Add to cart
* Remove from cart
* Cart management

## Orders

* Create orders
* Order history

## Prescriptions

* Upload prescription
* Admin approval
* Prescription verification

## Payments

* Razorpay payment
* Payment verification

---

# Prescription Workflow

1. User browses medicines.
2. If the medicine requires a prescription:

   * User uploads a prescription.
3. Admin reviews the prescription.
4. Admin approves or rejects it.
5. Approved users can purchase prescription medicines.
6. Rejected users must upload a new prescription.

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/bionexa.git

cd bionexa
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment.

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py makemigrations

python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Visit:

```
http://127.0.0.1:8000
```

---

# ⚙️ Environment Variables

Create a `.env` file (or configure in `settings.py`) with:

```
SECRET_KEY=your-secret-key

DEBUG=True

RAZORPAY_KEY_ID=your_key

RAZORPAY_KEY_SECRET=your_secret
```

---
