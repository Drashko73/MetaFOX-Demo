# Broker settings
broker_url = 'pyamqp://guest@localhost:5672//'

# List of modules to import when the Celery worker starts.
imports = [
    'metafox.tasks'
]

# Backend settings
result_backend = 'redis://localhost:6379/0'

# Worker settings
worker_pool = 'solo'

# Task settings
task_serializer = 'json'

# Task result settings
result_serializer = 'json'

# Logging settings
log_level = 'INFO'