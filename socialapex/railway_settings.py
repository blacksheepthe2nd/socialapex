from socialapex.settings import *

# Railway-specific settings
import os

# Get Railway environment
if os.environ.get('RAILWAY_ENVIRONMENT'):
    # Railway production settings
    DEBUG = False
    ALLOWED_HOSTS = ['.railway.app', '.up.railway.app']
    CSRF_TRUSTED_ORIGINS = ['https://*.railway.app', 'https://*.up.railway.app']
    
    # Static files with Whitenoise
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
