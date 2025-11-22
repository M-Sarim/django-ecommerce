# Django E-commerce

A robust Django-based e-commerce web application designed to facilitate seamless online shopping experiences. This platform offers a user-friendly interface for customers to browse products, manage their cart, and securely complete purchases with integrated payment processing.

## Features

- 🛍️ **Product Catalog** - Browse products with detailed descriptions and images
- 🔐 **User Authentication** - Secure account management with django-allauth
- 🛒 **Shopping Cart** - Add, modify, and remove items with real-time updates
- 💳 **Secure Checkout** - Stripe payment integration for safe transactions
- 🎟️ **Coupon System** - Apply discount coupons to orders
- 📦 **Order Management** - Track order history and generate PDF receipts
- 👨‍💼 **Admin Interface** - Comprehensive dashboard for managing products, orders, and users
- 📱 **Responsive Design** - Seamless browsing across all devices
- 🔍 **Product Search** - Find products quickly with search functionality

## Tech Stack

- **Backend**: Django 4.x, Python 3.x
- **Frontend**: Bootstrap 5, Material Design Bootstrap (MDB)
- **Database**: SQLite (development), PostgreSQL-ready
- **Payment**: Stripe API
- **Authentication**: django-allauth
- **Forms**: django-crispy-forms
- **PDF Generation**: ReportLab

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/realsanjeev/django-ecommerce.git
   cd django-ecommerce
   ```

2. **Create and Activate Virtual Environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**

   Create a `.env` file in the `src/` directory with the following:
   ```env
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   STRIPE_PUBLISHABLE_KEY=your-stripe-publishable-key
   STRIPE_SECRET_KEY=your-stripe-secret-key
   ```

5. **Run Migrations**
   ```bash
   cd src
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

7. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://localhost:8000`

**Default Admin Credentials**: `admin@admin.com` / `admin`

### Docker Installation (Alternative)

If you have Docker installed:

1. **Build the Docker Image**
   ```bash
   docker build -t django-ecommerce .
   ```

2. **Run the Container**
   ```bash
   docker run -p 8000:8000 --name django-ecommerce-container django-ecommerce
   ```

Access the application at `http://localhost:8000`

## Development

### Code Formatting with Pre-commit

This project uses `pre-commit` hooks to maintain code quality.

**Run pre-commit on all files:**
```bash
pre-commit run --all-files
```

**Update hooks to latest versions:**
```bash
pre-commit autoupdate
```

### Running Tests

```bash
cd src
python manage.py test
```

## Screenshots

### Authentication
![Authentication Feature](images/authentication_image.png)

### Product Ordering Process
![Product Order Process](images/product_order_process.png)

### Additional Features
![Other Features](images/other_features.png)

## Project Structure

```
django-ecommerce/
├── src/
│   ├── accounts/          # User authentication
│   ├── address/           # Address management
│   ├── orders/            # Order processing
│   ├── payments/          # Payment & coupons
│   ├── products/          # Product catalog
│   ├── refunds/           # Refund handling
│   ├── search/            # Search functionality
│   ├── templates/         # HTML templates
│   └── ecommerce/         # Project settings
├── requirements.txt
├── Dockerfile
└── README.md
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is open source and available for educational purposes.

## Contact

For questions or feedback, reach out via:

- **GitHub**: [@realsanjeev](https://github.com/realsanjeev)
- **LinkedIn**: [Connect on LinkedIn](https://linkedin.com/in/realsanjeev)

---

Built with ❤️ using Django
