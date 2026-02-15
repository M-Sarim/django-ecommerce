# Django E-commerce

> ## 🎓 Software Re-Engineering Assignment 1
> **GitHub Username:** M-Sarim
> **Student Roll Number:** [Insert Your Roll Number Here]
> 
> ### Task 2: Docker Execution Steps
> To run this project locally via Docker, the following commands were used:
> 1. **Build the image:** 
>    docker build -t sre-assignment-1 .
> 2. **Run the container:**
>    docker run -p 8000:8000 sre-assignment-1
> 
> ### Task 4: SonarQube Analysis Steps
> To perform static code analysis, SonarQube and SonarScanner were deployed via Docker:
> 1. **Start the SonarQube Server:**
>    ```bash
>    docker run -d --name sonarqube -p 9000:9000 sonarqube:community
>    ```
> 2. **Run the SonarScanner (Excluding static libraries to prevent memory bottlenecks):**
>    ```bash
>    docker run --rm \
>      -e SONAR_HOST_URL="[http://host.docker.internal:9000](http://host.docker.internal:9000)" \
>      -v "$(pwd):/usr/src" \
>      sonarsource/sonar-scanner-cli \
>      -Dsonar.projectKey=SRE-Assignment-01 \
>      -Dsonar.token=<YOUR_SONARQUBE_TOKEN> \
>      -Dsonar.exclusions="**/static/**,**/static_cdn/**,**/migrations/**"
>    ```
> ---

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
- Docker & Docker Desktop (Recommended)
- Git

### Installation (Standard)

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/M-Sarim/django-ecommerce.git](https://github.com/M-Sarim/django-ecommerce.git)
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

## License

This project is open source and available for educational purposes.

## Contact

* **Original Author**: [@realsanjeev](https://github.com/realsanjeev)
* **Fork Maintained By**: [@M-Sarim](https://www.google.com/search?q=https://github.com/M-Sarim)

---

# Built with ❤️ using Django
