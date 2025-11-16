# -------------------------
# Security
# -------------------------

# Keep the secret key secret in production!
SECRET_KEY = 'django-insecure-0q&!nuc616)94mw@ptm+74)@^m3oci&082+^kuf7_=%*2@wl7)'

# Turn off debug in production
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'yourdomain.com']

# Custom user model
AUTH_USER_MODEL = 'users.CustomUser'  # Make sure this matches your CustomUser app

# -------------------------
# HTTPS / Security Settings
# -------------------------

# Redirect all HTTP requests to HTTPS
SECURE_SSL_REDIRECT = True  # Forces HTTPS

# HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Include all subdomains
SECURE_HSTS_PRELOAD = True  # Allow browser preloading

# Secure cookies
CSRF_COOKIE_SECURE = True      # Only send CSRF cookie over HTTPS
SESSION_COOKIE_SECURE = True   # Only send session cookie over HTTPS

# Security headers
SECURE_BROWSER_XSS_FILTER = True    # Enable XSS filter in browser
SECURE_CONTENT_TYPE_NOSNIFF = True  # Prevent MIME type sniffing
X_FRAME_OPTIONS = 'DENY'            # Prevent clickjacking

# -------------------------
# Installed Apps
# -------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bookshelf',
    'relationship_app',
    'users',
]

# -------------------------
# Middleware
# -------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# -------------------------
# URL & WSGI
# -------------------------
ROOT_URLCONF = 'LibraryProject.urls'
WSGI_APPLICATION = 'LibraryProject.wsgi.application'

# -------------------------
# Templates
# -------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# -------------------------
# Database
# -------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# -------------------------
# Password Validators
# -------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# -------------------------
# Internationalization
# -------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# -------------------------
# Static files
# -------------------------
STATIC_URL = 'static/'

# -------------------------
# Default primary key field
# -------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
