#! /usr/bin/env python3
import os
import subprocess
import sys

from shared import verify_environment

verify_environment()

SETTINGS_KEYS = (
    'POSTGRES_SERVER_NAME',
    'POSTGRES_ADMIN_USER',
    'POSTGRES_ADMIN_PASSWORD',
    'POSTGRES_HOST',
    'APP_DB_NAME',
    'DJANGO_SETTINGS_MODULE',
    'AZ_STORAGE_ACCOUNT_NAME',
    'AZ_STORAGE_CONTAINER',
    'AZ_STORAGE_KEY',
    'FUNCTIONS_MOUNT_POINT',
)
settings_pairs = ['{}={}'.format(k, os.getenv(k)) for k in SETTINGS_KEYS]

# Only diff here with as_settings is `functionapp` for `webapp`.
settings_command = [
    'az', 'functionapp', 'config', 'appsettings', 'set',
    '--name', os.getenv('FUNCTIONS_APP_NAME'),
    '--resource-group', os.getenv('FUNCTIONS_GROUP'),
    '--settings',
] + settings_pairs

if __name__ == '__main__':
    update_settings = input('Update App Settings? [y/n]: ')
    if update_settings == 'y':
        sys.stdout.write("Updating App Settings... ")
        sys.stdout.flush()
        subprocess.check_output(settings_command)
        print("Done")
