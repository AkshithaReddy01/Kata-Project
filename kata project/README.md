# 🍬 Sweet Shop Management System

A full-stack web application for managing a sweet shop's inventory, built with **Python + FastAPI** (backend) and **React + TypeScript** (frontend).

## 📋 Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing](#testing)
- [Screenshots](#screenshots)
- [My AI Usage](#my-ai-usage)
- [Project Structure](#project-structure)
- [Security Features](#security-features)
- [License](#license)

## 🎯 Project Overview

The Sweet Shop Management System is a comprehensive inventory management solution that allows users to:
- Browse and search through a catalog of Indian sweets
- Purchase sweets (with automatic inventory updates)
- Manage inventory (Admin users only)
- View real-time stock levels
- Authenticate securely using JWT tokens

This project demonstrates full-stack development practices, including RESTful API design, authentication, authorization, and modern frontend development.

## ✨ Features

- ✅ **User Authentication**: Secure registration and login with JWT tokens
- ✅ **Role-Based Access Control**: Admin and regular user roles
- ✅ **Sweet Catalog**: Browse and search through available sweets
- ✅ **Inventory Management**: Purchase sweets and manage stock (Admin)
- ✅ **Search & Filter**: Search sweets by name, category, and price range
- ✅ **Shopping Cart**: Add items to cart and manage purchases
- ✅ **Responsive UI**: Modern, mobile-friendly interface
- ✅ **Comprehensive Testing**: Full test coverage for backend APIs

## 🛠️ Tech Stack

### Backend
- **Framework**: FastAPI 0.124.4
- **Language**: Python 3.12+
- **Database**: SQLite (with SQLAlchemy ORM)
- **Authentication**: JWT (JSON Web Tokens) with python-jose
- **Password Hashing**: bcrypt
- **Validation**: Pydantic
- **Testing**: pytest, pytest-asyncio, pytest-cov
- **Server**: Uvicorn

### Frontend
- **Framework**: React 18
- **Language**: TypeScript
- **Build Tool**: Vite 5
- **Routing**: React Router DOM 6
- **HTTP Client**: Axios
- **Styling**: CSS3

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8+** (Python 3.12 recommended)
- **Node.js 18+** (Node.js 24 recommended)
- **npm** or **yarn**
- **Git** (for cloning the repository)

## 🚀 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/akshithareddy01/sweet-shop-management.git
cd sweet-shop-management
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file from example
copy env.example .env  # Windows
# cp env.example .env  # Linux/Mac

# Edit .env file and set JWT_SECRET_KEY (minimum 32 characters)
# Example: JWT_SECRET_KEY=your-super-secret-jwt-key-change-in-production-min-32-chars-long-enough
```

### 3. Frontend Setup

```bash
cd ../frontend

# Install dependencies
npm install
```

## 🏃 Running the Application

### Start Backend Server

```bash
cd backend
venv\Scripts\activate  # Windows (or source venv/bin/activate on Linux/Mac)
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Backend will be available at:
- **API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Start Frontend Server

Open a new terminal:

```bash
cd frontend
npm run dev
```

Frontend will be available at: **http://localhost:5173**

### Access the Application

1. Open your browser and navigate to `http://localhost:5173`
2. Register a new account or login
3. Browse sweets, add to cart, and make purchases
4. Admin users can access the admin dashboard for inventory management

## 📡 API Endpoints

### Authentication
- `POST /api/auth/register` - Register a new user
  - Body: `{ "username": "string", "email": "string", "password": "string" }`
- `POST /api/auth/login` - Login user
  - Body: `{ "username": "string", "password": "string" }`
  - Returns: `{ "access_token": "string", "token_type": "bearer" }`

### Sweets (Protected - Requires Authentication)
- `GET /api/sweets` - Get all sweets
- `GET /api/sweets/search?name=&category=&min_price=&max_price=` - Search sweets
- `GET /api/sweets/{id}` - Get sweet by ID
- `POST /api/sweets` - Create sweet (Admin only)
- `PUT /api/sweets/{id}` - Update sweet (Admin only)
- `DELETE /api/sweets/{id}` - Delete sweet (Admin only)

### Inventory (Protected - Requires Authentication)
- `POST /api/sweets/{id}/purchase` - Purchase a sweet (decreases quantity)
  - Body: `{ "quantity": integer }`
- `POST /api/sweets/{id}/restock` - Restock sweet (Admin only)
  - Body: `{ "quantity": integer }`

## 🧪 Testing

### Backend Tests

```bash
cd backend
venv\Scripts\activate  # Activate virtual environment

# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=html

# Run specific test file
pytest tests/test_auth.py
pytest tests/test_sweets.py
pytest tests/test_inventory.py

# View coverage report
# Open htmlcov/index.html in browser
```

### Test Report

See [TEST_REPORT.md](./TEST_REPORT.md) for detailed test results and coverage information.

## 📸 Screenshots

### Login Page
The login page features a clean, modern design with email and password fields, allowing users to securely access their accounts.

![Login Page](./screenshots/login.png)

### Dashboard / Sweet Catalog
The main dashboard displays all available sweets with search and filter functionality. Users can browse by category, search by name, and add items to their cart.

![Dashboard](./screenshots/dashboard.png)

### Search & Filter Interface
The search and filter section allows users to find sweets by name or filter by category (Milk-based, Dry Sweet, Fried Sweet, Halwa, Frozen).

![Search and Filter](./screenshots/search-filter.png)

### Shopping Cart
The shopping cart interface shows all selected items with quantity controls, individual prices, and total order amount. Users can modify quantities or remove items before placing an order.

![Shopping Cart](./screenshots/cart.png)

### Product Cards
Individual sweet product cards display name, category, price, stock availability, and quick action buttons to add items to cart.

![Product Cards](./screenshots/product-cards.png)

## 🤖 My AI Usage

### AI Tools Used

Throughout the development of this project, I utilized **Cursor AI** as my primary AI coding assistant. Cursor AI is an AI-powered code editor that provides intelligent code completion, suggestions, and debugging assistance.

### How I Used AI

#### Backend Development

1. **Project Structure Setup**
   - Used Cursor AI to generate the initial FastAPI project structure
   - AI suggested the modular architecture (routers, models, schemas, middleware)
   - Generated boilerplate code for database configuration and connection setup

2. **Database Models & Schemas**
   - Asked Cursor AI to create SQLAlchemy models with proper relationships
   - AI helped design Pydantic schemas for request/response validation
   - Used AI suggestions for database field types and constraints

3. **API Route Implementation**
   - Generated initial route handlers for authentication endpoints
   - AI assisted in implementing CRUD operations for sweets management
   - Used AI to create proper error handling and status codes

4. **Authentication & Security**
   - Cursor AI helped implement JWT token generation and validation
   - AI suggested password hashing patterns using bcrypt
   - Generated middleware for protecting routes and role-based access control

5. **Testing**
   - AI generated test templates and fixtures
   - Used AI to create test cases for authentication, CRUD operations, and edge cases
   - AI helped write async test patterns for FastAPI endpoints

#### Frontend Development

1. **Component Structure**
   - Cursor AI generated React component boilerplate
   - AI suggested component organization and file structure
   - Generated TypeScript interfaces and type definitions

2. **API Integration**
   - AI helped configure Axios with interceptors for token management
   - Generated API service functions for all backend endpoints
   - AI suggested error handling patterns for API calls

3. **State Management**
   - Used Cursor AI to implement React Context for authentication
   - AI helped create CartContext for shopping cart functionality
   - Generated custom hooks for state management

4. **UI Components**
   - AI assisted in creating form components with validation
   - Generated responsive CSS layouts
   - AI suggested UI/UX improvements for better user experience

#### Code Review & Debugging

1. **Error Resolution**
   - Used Cursor AI to understand error messages and suggest fixes
   - AI helped debug CORS issues and authentication problems
   - Generated solutions for async/await patterns

2. **Code Quality**
   - AI reviewed code for potential security vulnerabilities
   - Suggested refactoring opportunities for better code organization
   - Helped identify and fix type errors in TypeScript

3. **Best Practices**
   - AI provided suggestions for following Python and React best practices
   - Helped ensure proper error handling and logging
   - Suggested improvements for code readability and maintainability

### Reflection on AI Impact

#### Positive Impacts

1. **Accelerated Development**: AI significantly sped up the development process, especially for boilerplate code and repetitive tasks. What would have taken days was completed in hours.

2. **Learning Tool**: Cursor AI served as an excellent learning resource, explaining complex concepts and suggesting modern patterns I wasn't familiar with.

3. **Error Prevention**: AI caught many potential bugs early in development, such as type mismatches, missing error handling, and security issues.

4. **Code Consistency**: AI helped maintain consistent coding style and patterns throughout the project.

5. **Documentation**: AI generated helpful comments and documentation that improved code readability.

#### Challenges Encountered

1. **Over-Reliance**: Initially, I found myself relying too heavily on AI suggestions without fully understanding the code. This required me to step back and learn the underlying concepts.

2. **Context Limitations**: Sometimes AI suggestions didn't perfectly fit the project architecture, requiring manual adjustments and refactoring.

3. **Debugging AI Code**: When AI-generated code had issues, debugging could be challenging since I hadn't written it from scratch.

4. **Best Practice Conflicts**: Occasionally, AI suggested solutions that conflicted with project requirements or team standards.

#### My Approach

1. **Pair Programming Mindset**: I treated Cursor AI as a pair programming partner rather than a code generator. I always reviewed and understood AI suggestions before implementing them.

2. **Selective Usage**: I used AI for:
   - Boilerplate and repetitive code
   - Learning new patterns and concepts
   - Debugging and error resolution
   - Code review and quality checks

3. **Manual Implementation**: For critical business logic and complex features, I wrote code manually to ensure deep understanding.

4. **Continuous Learning**: I used AI explanations as learning opportunities, researching concepts further to build my knowledge.

5. **Quality Standards**: I maintained high code quality standards regardless of whether code was AI-generated or manually written.

#### Conclusion

AI tools like Cursor AI have become invaluable in modern software development. They accelerate development, improve code quality, and serve as excellent learning resources. However, it's crucial to use them as tools to enhance your skills rather than replace understanding. The key is finding the right balance between AI assistance and manual coding to ensure you maintain deep knowledge of your codebase.

**Commit History**: All commits where AI was used include appropriate documentation. The development process followed Test-Driven Development (TDD) principles, with AI assisting in test creation and implementation.

## 📁 Project Structure

```
sweet-shop-management/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI application entry point
│   │   ├── config.py            # Configuration settings
│   │   ├── database.py          # Database setup and session management
│   │   ├── models/              # SQLAlchemy models
│   │   │   ├── user.py
│   │   │   └── sweet.py
│   │   ├── schemas/             # Pydantic schemas
│   │   │   ├── user.py
│   │   │   └── sweet.py
│   │   ├── routers/             # API route handlers
│   │   │   ├── auth.py
│   │   │   ├── sweets.py
│   │   │   └── inventory.py
│   │   ├── middleware/          # Authentication middleware
│   │   │   └── auth.py
│   │   ├── utils/               # Utility functions
│   │   │   └── auth.py
│   │   └── services/            # Business logic layer
│   ├── tests/                   # Test files
│   │   ├── conftest.py
│   │   ├── test_auth.py
│   │   ├── test_sweets.py
│   │   └── test_inventory.py
│   ├── requirements.txt         # Python dependencies
│   ├── env.example              # Environment variables example
│   ├── pytest.ini               # Pytest configuration
│   ├── create_admin.py          # Script to create admin user
│   └── seed_indian_sweets.py    # Script to seed database
├── frontend/
│   ├── src/
│   │   ├── pages/               # Page components
│   │   │   ├── Login.tsx
│   │   │   ├── Register.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   └── AdminDashboard.tsx
│   │   ├── components/         # Reusable components
│   │   │   ├── AddSweetForm.tsx
│   │   │   ├── EditSweetForm.tsx
│   │   │   ├── CartSidebar.tsx
│   │   │   ├── ProtectedRoute.tsx
│   │   │   └── AdminRoute.tsx
│   │   ├── context/            # React Context providers
│   │   │   ├── AuthContext.tsx
│   │   │   └── CartContext.tsx
│   │   ├── services/           # API service layer
│   │   │   └── api.ts
│   │   ├── App.tsx              # Main App component
│   │   └── main.tsx             # Entry point
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
├── .gitignore
├── README.md
└── TEST_REPORT.md
```

## 🔐 Security Features

- **Password Hashing**: All passwords are hashed using bcrypt before storage
- **JWT Authentication**: Secure token-based authentication
- **Protected Routes**: Middleware protects sensitive endpoints
- **Role-Based Access Control**: Admin and user role separation
- **Input Validation**: Pydantic schemas validate all inputs
- **SQL Injection Prevention**: SQLAlchemy ORM prevents SQL injection
- **CORS Configuration**: Properly configured CORS for frontend-backend communication

## 📝 Development Process

This project was developed using **Test-Driven Development (TDD)**:
1. Write a failing test (Red)
2. Write minimal code to pass (Green)
3. Refactor for quality (Refactor)
4. Repeat

The git commit history demonstrates this pattern throughout development.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Akshitha Reddy**
- GitHub: [@akshithareddy01](https://github.com/akshithareddy01)

---

**Note**: This project was developed as a TDD kata. All code follows clean coding principles and best practices.

