import os

ENVIRONMENT = os.environ.get('project_name_env', 'local')

if ENVIRONMENT == 'local':
    SETTINGS_MODULE = 'config.settings.local'
elif ENVIRONMENT == 'development':
    SETTINGS_MODULE = 'config.settings.development'
elif ENVIRONMENT == 'production':
    SETTINGS_MODULE = 'config.settings.production'
    