
from pathlib import Path
from django.utils.translation import gettext_lazy as _



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-q=2ojx9-xatz02zwk(3(tobnh*z5ac62+q3y#5_#y=sxxmn2_d'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'orders.apps.OrdersConfig',
    'payment.apps.PaymentConfig',
    'coupons.apps.CouponsConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',    # for localization
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'myshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Added manually   
LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    # ('np', _('Nepali')),
]

# The LOCALE_PATHS setting specifies the directories where Django has to look for translation files.
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'


CART_SESSION_ID = 'cart'

#  If you don’t want to set up email settings, you can tell Django to write emails to the 
# console by adding the following setting to the settings.py file:
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# For Managing Payments system
# Stripe settings

# Publishable key
STRIPE_PUBLISHABLE_KEY = 'pk_test_51NQWOMCiw8cEog3dgO5QiTHIWKPbmVAQzRD4i43TqY3n45bseg4jyxbcX9kNFEyDGyX6jWd3vWHqebnq1uzQEsbv00C1cNv4CO'     

# Secret key
STRIPE_SECRET_KEY = 'sk_test_51NQWOMCiw8cEog3dU2ljThYo6Okl260XOc9YeLyIpRLsUJFRKZ8eSwZiXgq1mEU1crIn2gSeTecDiD5hGOMOlW4900SlB4cYmQ'          
STRIPE_API_VERSION = '2022-08-01'




# Email server configuration
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'raisanj6@gmail.com'
EMAIL_HOST_PASSWORD = 'hgamxnvcptsrxmvw'
EMAIL_PORT = 587
EMAIL_USE_TLS = True




STRIPE_WEBHOOK_SECRET = 'whsec_67873a505b0c6cee06e27b692301775a5d127071e9d5517bf7310ee407510762'


# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


# Redis settings
REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 1



