# Store Price List - Django Web Application

A Django-based web application that allows store owners to manage their store profiles and product inventories. Guest users can browse all stores and products, while registered store owners can create accounts, manage their store details, and maintain their product inventory.

## 📋 Table of Contents

- [Overview](#overview)
- [Setup Guide](#setup-guide)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Installation & Setup](#installation--setup)
- [Usage](#usage)
- [Changes Made](#changes-made)
- [Before & After Comparison](#before--after-comparison)
- [Models](#models)
- [Views & URLs](#views--urls)
- [Security Features](#security-features)

## 🎯 Overview

This Django web application is a port of the iOS Store Price List app concept. It provides a platform where:
- **Guest Users**: Can browse and view all stores and their products (read-only)
- **Store Owners**: Can register accounts, create store profiles, and manage their product inventory

The application ensures proper data isolation - each store owner can only manage their own store and products.

## 🛠 Setup Guide

### Setup Django Environment (Windows Only)

#### Requirements:
1. Windows Operating System
2. Python installed (Python 3.8 or higher recommended)
3. IDE or text editor (VS Code, PyCharm, etc.)

#### Default Admin Credentials:
- **Username**: `admin`
- **Password**: `admin`

#### Step-by-Step Setup Guide in CMD:

**Important**: Open Command Prompt as a regular user (NOT as Administrator)

1. **Install Virtual Environment Wrapper for Windows**
   ```cmd
   pip install virtualenvwrapper-win
   ```

2. **Check if virtualenvwrapper is working**
   ```cmd
   workon
   ```

3. **Create a new virtual environment**
   ```cmd
   mkvirtualenv final_django_environment
   ```

4. **Activate the virtual environment**
   ```cmd
   activate
   ```
   *Note: After creating the virtual environment, it should activate automatically. If not, use the command above.*

5. **Install Django**
   ```cmd
   pip install django
   ```

6. **Navigate to C drive root**
   ```cmd
   cd C://
   ```

7. **Create project directory**
   ```cmd
   mkdir FinalDjangoProject
   ```

8. **Navigate into the project directory**
   ```cmd
   cd FinalDjangoProject
   ```

9. **Start a new Django project**
   ```cmd
   django-admin startproject StorePriceList
   ```

10. **Navigate into the project directory**
    ```cmd
    cd StorePriceList
    ```

11. **Start the Django development server (to test)**
    ```cmd
    python manage.py runserver
    ```
    *Press Ctrl+C to stop the server*

12. **Create a new Django app**
    ```cmd
    python manage.py startapp myapp
    ```

13. **Run database migrations**
    ```cmd
    python manage.py migrate
    ```

14. **Create a superuser (admin account)**
    ```cmd
    python manage.py createsuperuser
    ```
    *Follow the prompts to create your admin account. You can use:*
    - Username: `admin`
    - Email: (optional)
    - Password: `admin` (or your preferred password)

#### Additional Notes:
- To activate the virtual environment in future sessions, use: `workon final_django_environment`
- To deactivate the virtual environment, use: `deactivate`
- Make sure you're in the virtual environment before running Django commands
- The virtual environment name will appear in parentheses in your command prompt when activated

#### Verifying Installation:
After completing the setup, you can verify everything is working by:
1. Starting the server: `python manage.py runserver`
2. Opening your browser to: `http://127.0.0.1:8000/`
3. You should see the Django welcome page
4. Access admin panel at: `http://127.0.0.1:8000/admin/`

## ✨ Features

### For Guest Users
- Browse all registered stores
- View store details (name, address, contact info, description)
- View all products from all stores with prices
- No registration required

### For Store Owners
- **Account Management**
  - Register with email and full name
  - Login with email and password
  - Secure logout functionality
  
- **Store Profile Management**
  - Create and edit store profile
  - Store name, address, zip code, phone, email, description
  - One store profile per user (OneToOne relationship)
  
- **Product Inventory Management**
  - Add new products to their store
  - Edit existing products
  - Delete products
  - View all products in their inventory
  - Duplicate product name validation within store
  - Price validation (positive numbers only)

## 🛠 Technology Stack

- **Backend**: Django 5.0.4
- **Database**: SQLite3
- **Frontend**: HTML, CSS, JavaScript
- **Authentication**: Django's built-in authentication system
- **Styling**: Bootstrap 4, Custom CSS

## 📁 Project Structure

```
StorePriceList_Web/
├── manage.py
├── db.sqlite3
├── README.md
├── myapp/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py          # User registration and inventory forms
│   ├── models.py         # StoreProfile and Inventory models
│   ├── views.py          # View functions
│   ├── urls.py           # URL routing
│   ├── tests.py
│   ├── static/
│   │   ├── css/          # Stylesheets
│   │   └── js/           # JavaScript files
│   └── templates/
│       ├── base.html
│       ├── home.html     # Guest view (all stores)
│       ├── login.html
│       ├── register.html
│       └── dashboard.html # Store owner dashboard
└── StorePriceList/
    ├── __init__.py
    ├── settings.py       # Django settings
    ├── urls.py           # Main URL configuration
    ├── wsgi.py
    └── asgi.py
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Navigate to the project directory**
   ```bash
   cd StorePriceList_Web
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install Django (if not already installed)**
   ```bash
   pip install django
   ```

4. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Open your browser and go to: `http://127.0.0.1:8000/`
   - Admin panel: `http://127.0.0.1:8000/admin/`

## 📖 Usage

### For Guest Users
1. Visit the home page
2. Browse all available stores
3. View store details and products
4. Click "Account" button to register or login if you want to manage a store

### For Store Owners

#### Registration
1. Click "Account" button on the home page
2. Click "Sign Up" or go to `/registerpage/`
3. Fill in:
   - Full Name
   - Email (used as username)
   - Password
   - Confirm Password
4. Click "Register Account"
5. You'll be automatically logged in and redirected to the dashboard

#### Login
1. Go to `/loginPage/`
2. Enter your email and password
3. Click "Login"
4. You'll be redirected to your dashboard

#### Managing Store Profile
1. After login, you'll see the Dashboard
2. Click on "Store-Profile" tab
3. Fill in your store details:
   - Store Name *
   - Address *
   - Zip Code *
   - Phone *
   - Email Address *
   - Description *
4. Click "Save" to save your store profile

#### Managing Products
1. Click on "Inventory" tab in the dashboard
2. **Add Product**: Click "Create" button, fill in product details, click "Add Product"
3. **Edit Product**: Click "Edit" button next to a product, modify details, click "Save Changes"
4. **Delete Product**: Click "Delete" button next to a product and confirm

#### Logout
1. Click the "Logout" button in the dashboard header
2. You'll be logged out and redirected to the home page

## 🔄 Changes Made - Part 1

### Major Changes

#### 1. **Account Creation System**
   - **Before**: Used Django's default UserCreationForm with username field
   - **After**: Custom form using email as username, matching iOS app concept
   - Added `first_name` field for user's full name
   - Email validation to prevent duplicate registrations
   - Email is normalized (lowercase, trimmed) before saving

#### 2. **Login System**
   - **Before**: Login required username
   - **After**: Login uses email address (matching iOS app)
   - Email is normalized before authentication
   - Better error messages

#### 3. **User-Store Relationship**
   - **Before**: StoreProfile could exist without proper user linking
   - **After**: Each user automatically gets a StoreProfile on registration/login
   - One-to-one relationship enforced (one store per user)
   - StoreProfile email defaults to user's email

#### 4. **Product Ownership & Security**
   - **Before**: Products could potentially be created without proper store linking
   - **After**: 
     - Products are always linked to the user's store profile
     - Users can only see/manage their own products
     - Security checks prevent editing/deleting other users' products
     - Products include both `user` and `store_profile` foreign keys

#### 5. **Data Isolation**
   - **Before**: Potential for users to see/manage other users' data
   - **After**: 
     - Dashboard only shows products from the logged-in user's store
     - All product operations verify ownership
     - Proper filtering in all views

#### 6. **Validation & Error Handling**
   - **Before**: Basic validation
   - **After**:
     - Duplicate product name validation within each store
     - Price validation (must be positive number)
     - Email format validation
     - Better error messages displayed to users
     - Form error display in registration

#### 7. **Logout Functionality**
   - **Before**: Logout button redirected to home but didn't log out
   - **After**: Proper logout view that logs out user and redirects to home

#### 8. **Guest User Experience**
   - **Before**: Home page logged out users automatically
   - **After**: Guest users can browse all stores and products without logging in

## 📊 Before & After Comparison

### Registration Form

**Before:**
- Fields: Username, Email, Password, Confirm Password
- Username was separate from email
- No name field

**After:**
- Fields: Full Name, Email, Password, Confirm Password
- Email is used as username (matching iOS app)
- Name field added for user identification
- Better form validation and error display

### Login Form

**Before:**
- Input: Username field
- Users had to remember their username

**After:**
- Input: Email field
- Users login with their email address
- More intuitive and matches iOS app

### Dashboard

**Before:**
- Displayed: `Hello, {{request.user}}` (username)
- Products might not be properly filtered
- No ownership verification

**After:**
- Displayed: `Hello, {{request.user.first_name|default:request.user.email}}` (name or email)
- Only shows products from user's own store
- All operations verify ownership

### Product Management

**Before:**
- Products could be created without proper store linking
- No duplicate name checking
- Limited validation

**After:**
- Products always linked to user's store profile
- Duplicate product name validation within store
- Price validation (positive numbers)
- Ownership verification for edit/delete operations

### Home Page

**Before:**
- Automatically logged out users
- Limited guest access

**After:**
- Guest users can browse all stores and products
- No automatic logout
- Better separation between guest and authenticated views

## 🗄 Models

### StoreProfile
- **Relationship**: OneToOne with User (one store per user)
- **Fields**:
  - `user`: Foreign key to User (OneToOne)
  - `store_name`: Store name
  - `address`: Store address
  - `zip_code`: Zip/postal code
  - `phone`: Contact phone number
  - `email_address`: Store email
  - `description`: Store description

### Inventory
- **Relationships**: 
  - ForeignKey to User
  - ForeignKey to StoreProfile
- **Fields**:
  - `product_id`: Primary key (AutoField)
  - `user`: Foreign key to User
  - `store_profile`: Foreign key to StoreProfile
  - `product_name`: Product name
  - `product_description`: Product description
  - `price`: Product price (DecimalField)

## 🔗 Views & URLs

### URL Patterns
- `/` - Home page (guest view)
- `/registerpage/` - User registration
- `/loginPage/` - User login
- `/logout/` - User logout
- `/dashboard/` - Store owner dashboard (requires login)
- `/add_product/` - Add product form (requires login)
- `/delete-product/<id>/` - Delete product (requires login)
- `/edit-product/` - Edit product (requires login)

### Key Views
- `home()`: Displays all stores and products (guest and authenticated)
- `registerPage()`: Handles user registration
- `loginPage()`: Handles user authentication
- `logoutPage()`: Handles user logout
- `dashboard()`: Main dashboard for store owners (login required)
- `add_product()`: Add new product (login required)
- `edit_product()`: Edit existing product (login required)
- `delete_product()`: Delete product (login required)

## 🔒 Security Features

1. **Authentication Required**: Dashboard and product management require login
2. **Ownership Verification**: Users can only edit/delete their own products
3. **Data Isolation**: Each user only sees their own store and products
4. **CSRF Protection**: All forms include CSRF tokens
5. **Email Validation**: Email format validation and duplicate checking
6. **Password Security**: Django's built-in password hashing and validation
7. **Input Sanitization**: All inputs are trimmed and validated

## 📝 Notes

- The application uses SQLite3 as the default database (suitable for development)
- For production, consider switching to PostgreSQL or MySQL
- Email functionality (password reset, etc.) is not implemented but can be added
- The application follows Django best practices and security guidelines

## 🐛 Troubleshooting

### Common Issues

1. **Migration Errors**
   - Run: `python manage.py makemigrations myapp`
   - Then: `python manage.py migrate`

2. **Template Not Found**
   - Ensure templates are in `myapp/templates/` directory
   - Check `settings.py` for correct `TEMPLATES` configuration

3. **Static Files Not Loading**
   - Run: `python manage.py collectstatic` (if using production)
   - Ensure `STATIC_URL` is set in `settings.py`

4. **Login Not Working**
   - Ensure you're using email (not username)
   - Check that user exists in database
   - Verify password is correct

## 🔄 Changes Made - Part 2

### Form Validation & UI Redesign

#### 1. **Enhanced Form Validation (Matching iOS App)**
   - **Registration Form Validations**:
     - Name validation: "Enter your full name" if name is empty
     - Email format validation: "Enter a valid email address" for invalid email format
     - Password length validation: "Password must be at least 6 characters"
     - Password match validation: "Passwords do not match" if passwords don't match
     - Duplicate email check: "Email already registered" if email exists
     - Success message: "Account Created Successfully! Let's set up your store details."
   
   - **Login Form Validations**:
     - Empty field check: "Please enter email and password" if fields are empty
     - Email format validation: "Enter a valid email address" for invalid format
     - Account existence check: "Account not found" if email doesn't exist
     - Password validation: "Incorrect password" if password is wrong
   
   - **Implementation**:
     - Server-side validation in `forms.py` with custom `clean_*` methods
     - Client-side JavaScript validation for real-time feedback
     - Specific error messages matching iOS app exactly

#### 2. **Redesigned Login Page**
   - **Before**: Basic Bootstrap form with minimal styling
   - **After**: 
     - Modern gradient background (purple/blue gradient)
     - Centered card design with rounded corners and shadow
     - Shopping cart icon at the top
     - "Welcome to Store Price List" title with subtitle
     - Password visibility toggle (eye icon)
     - Remember Me checkbox functionality
     - Improved input fields with icons and focus states
     - Better error message display with styled alerts
     - "Continue as Guest" button with hover effects
     - Responsive design for all screen sizes

#### 3. **Redesigned Registration Page**
   - **Before**: Basic Bootstrap form with minimal styling
   - **After**:
     - Modern gradient background matching login page
     - Centered card design with rounded corners and shadow
     - User-plus icon at the top
     - "Create Your Account" title with subtitle
     - Password visibility toggle for both password fields
     - Real-time form validation with JavaScript
     - Improved input fields with icons and focus states
     - Better error message display with styled alerts
     - Success message display
     - "Continue as Guest" button with hover effects
     - Responsive design for all screen sizes

#### 4. **Password Visibility Toggle**
   - Added eye/eye-slash icon toggle for password fields
   - Works on both login and registration pages
   - Toggle between showing and hiding password text
   - Smooth icon transition animation

#### 5. **Client-Side Validation**
   - Real-time validation before form submission
   - Prevents form submission if validation fails
   - Shows alert messages matching server-side errors
   - Email format validation using regex
   - Password length and match validation
   - Name field validation

#### 6. **Improved Error Handling**
   - Specific error messages matching iOS app exactly:
     - "Enter your full name"
     - "Enter a valid email address"
     - "Password must be at least 6 characters"
     - "Passwords do not match"
     - "Email already registered"
     - "Please enter email and password"
     - "Account not found"
     - "Incorrect password"
   - Styled error messages with red background
   - Success messages with green background
   - Better visual feedback for users

#### 7. **Enhanced User Experience**
   - Smooth transitions and hover effects
   - Better visual hierarchy
   - Consistent color scheme (blue for login, green for register)
   - Improved spacing and typography
   - Professional gradient backgrounds
   - Modern card-based design
   - Better accessibility with proper labels and autocomplete

#### 8. **Remember Me Functionality**
   - Added Remember Me checkbox to login form
   - Stores preference in localStorage
   - Maintains state across page reloads

### Technical Improvements

#### Form Validation Updates
- Added `clean_first_name()` method for name validation
- Enhanced `clean_email()` with regex pattern matching
- Added `clean_password1()` for password length validation
- Enhanced `clean()` method for password match validation
- All validation messages match iOS app exactly

#### View Updates
- Updated `loginPage()` view with step-by-step validation matching iOS
- Updated `registerPage()` with success message matching iOS
- Better error message handling with specific messages

#### Template Updates
- Complete redesign of `login.html` with modern UI
- Complete redesign of `register.html` with modern UI
- Added inline CSS for better styling control
- Added JavaScript for client-side validation and password toggle
- Improved form structure and accessibility

## 🔄 Changes Made - Part 3

### Changes from Part 2

#### 1. **Store Profile Completion Requirement (Matching iOS App)**
   - **Before (Part 2)**: Users could access Inventory tab even with incomplete store profile
   - **After (Part 3)**: 
     - Users must complete all store profile fields before accessing Inventory
     - Save button is disabled until all required fields are filled
     - Real-time validation updates button state as user types
     - Inventory tab is blocked with alert message if store profile is incomplete
     - Matches iOS app behavior exactly
   
   - **Validation Requirements**:
     - Store Name (required)
     - Address (required)
     - Zip Code (required)
     - Phone (required)
     - Email Address (required, must be valid format)
     - Description (required)
     - All fields must be filled and email must be valid format

#### 2. **Account Button Navigation Change**
   - **Before (Part 2)**: "Account" button on home page linked to registration page
   - **After (Part 3)**: "Account" button now links to login page first
   - More intuitive user flow - existing users login, new users can navigate to register
   - Matches common web application patterns

#### 3. **Top-Right Popup Notifications (Enhanced from Part 2)**
   - **Before (Part 2)**: Error and success messages displayed inline within the form on login/registration pages
   - **After (Part 3)**: 
     - All error and success messages appear as popup notifications in top-right corner
     - Applied to login, registration, AND dashboard pages
     - Smooth slide-in animation from the right
     - Auto-dismiss after 5 seconds
     - Manual close button (×) for immediate dismissal
     - Different styles for error (red), success (green), and info (blue) messages
     - Icons for each notification type (exclamation, check, info)
     - Multiple notifications stack vertically
     - Better user experience than inline messages

#### 4. **Store Profile Section UI/UX Redesign**
   - **Before (Part 2)**: Basic form with minimal styling, simple error messages, no completion requirement
   - **After (Part 3)**: 
     - **Prominent Incomplete Form Alert**:
       - Eye-catching yellow/orange gradient alert box at top of form
       - Animated warning icon with pulse effect
       - Clear heading: "Complete Your Store Profile"
       - Dynamic list showing exactly which fields are missing
       - Auto-updates as user fills fields
       - Auto-hides with smooth animation when form is complete
       - Dismissible close button
     
     - **Enhanced Form Fields**:
       - Compact form design with reduced spacing (margin-bottom: 12px instead of 20px)
       - Modern, clean input styling with rounded corners
       - Required field indicators (red asterisks)
       - Real-time field validation with visual feedback
       - Invalid fields: Red border, light red background, shake animation
       - Valid fields: Green border, light green background
       - Individual error messages below each field with warning icons
       - Smooth focus states with blue border and shadow
       - Better spacing and typography
       - Form centered with max-width: 800px
     
     - **Improved Save Button**:
       - Icon added (save icon)
       - Enhanced styling with hover effects
       - Clear disabled state when form incomplete
       - Visual feedback on state changes
       - Smooth transitions and animations
       - Shows "Saving..." spinner during submission
     
     - **Real-Time Validation**:
       - Validates fields as user types (on input, keyup, paste)
       - Validates on field blur (when user leaves field)
       - Updates missing fields list dynamically
       - Updates save button state in real-time
       - Provides immediate feedback

#### 5. **Inventory Tab Access Control**
   - **Before (Part 2)**: No restrictions on accessing Inventory tab
   - **After (Part 3)**:
     - JavaScript prevents clicking Inventory tab if store profile incomplete
     - Alert message: "Please complete your store profile before accessing the inventory."
     - Automatically switches back to Store Profile tab
     - Inventory tab appears visually disabled (reduced opacity) when incomplete
     - Works with localStorage tab persistence

#### 6. **Dashboard Responsive Design & Positioning Fixes**
   - **Before (Part 2)**: 
     - Header had fixed/absolute positioning causing overlap issues
     - Footer overlapping form fields
     - Navigation bar using float causing layout issues
     - Non-responsive modals and tables
     - Components overlapping each other
   
   - **After (Part 3)**:
     - **Header Section**:
       - Flexbox layout replacing absolute positioning
       - Removed container/border around "DASHBOARD" text
       - Gradient background with proper spacing
       - Owner name (top-left) uses responsive font sizing with `clamp()`
       - Text truncation for long names
       - Logout button adapts to screen size
       - Stacks vertically on mobile devices
       - All elements properly aligned and spaced
     
     - **Footer Section**:
       - Removed footer completely (was overlapping content)
       - All footer-related code removed from dashboard
     
     - **Navigation Bar**:
       - Horizontal tabs on desktop using flexbox
       - Vertical stacking on mobile
       - Removed float and fixed margins
       - Responsive button sizing
       - Smooth transitions between layouts
     
     - **Form Fields**:
       - Compact design with reduced padding
       - Full-width inputs on all devices
       - Proper font sizing (prevents iOS zoom)
       - Touch-friendly input sizes
       - Responsive alert boxes
     
     - **Tables**:
       - Horizontal scroll on small screens
       - Responsive column sizing
       - Touch-friendly action buttons
       - Proper spacing on mobile
       - Fixed display properties for proper table rendering
     
     - **Modals & Slide Navigation**:
       - Fully responsive with proper z-index management
       - Responsive max-width constraints
       - Proper positioning without conflicts
     
     - **Positioning Conflicts Fixed**:
       - Overrode conflicting `position: absolute` and `position: fixed` from external CSS
       - Changed header elements from absolute to relative positioning
       - Removed float conflicts
       - Proper z-index hierarchy (header: 100, modals: 10000, slide-nav: 9999)
       - Clear float conflicts with `clear: both` and `overflow: hidden`
       - All components properly contained within their parents
     
     - **Media Queries**:
       - Breakpoints at 768px (tablets) and 480px (mobile)
       - Optimized layouts for each breakpoint
       - Flexible typography using `clamp()`
       - Proper viewport handling

### Technical Improvements from Part 2

#### View Updates
- Added `is_store_complete()` function to check store profile completion
- Passes `is_store_complete` status to template
- Redirects after save to refresh completion status
- Success notification: "Store details saved successfully"

#### Template Updates
- Added JavaScript validation functions matching iOS app logic
- Real-time Save button state management
- Inventory tab access prevention
- Override of `openTab` function to check completion status
- Notification container and styling added to dashboard page
- Form submission validation with loading state
- Global `isStoreComplete` variable for cross-script access

#### JavaScript Enhancements
- Real-time field validation functions
- Dynamic missing fields list generation
- Form completion checking
- Field-level error display
- Auto-hide alert when form complete
- Tab access control logic
- Safe CSRF token retrieval with null checks
- Multiple event listeners (input, blur, change, keyup, paste) for real-time updates

#### CSS Enhancements
- Custom animations (slideDown, slideUp, pulse, shake, fadeIn, slideInRight)
- Gradient backgrounds for alerts and header
- Modern form field styling with transitions
- Enhanced button states and hover effects
- Professional color scheme (yellow/orange for warnings, green for success, red for errors)
- Compact form design with optimized spacing
- Responsive design with flexbox layouts
- CSS `clamp()` for fluid typography
- Media queries for mobile (480px) and tablet (768px) breakpoints
- Override styles with `!important` to fix external CSS conflicts

## 📄 License

This project is part of a group project for educational purposes.

## 👥 Contributors

Developed as part of a group project, porting the iOS Store Price List app concept to Django web application.

---

**Last Updated**: Based on changes made to align with iOS app concept, fix account creation and product ownership issues (Part 1), implement form validation with UI redesign (Part 2), and add store profile completion requirement with top-right popup notifications and comprehensive dashboard UI/UX improvements (Part 3).

