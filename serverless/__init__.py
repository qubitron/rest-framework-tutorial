import logging
import os
import sys
# Adjust PYTHONPATH for Django Application Folder
sys.path.append(os.getcwd())  # noqa
logging.info('sys.path: {}'.format(sys.path))  # noqa

import azure.functions as func
from wsgi_adapter import AzureWSGIHandler

# Establish the base URL. Not super pretty...
os.environ.setdefault('FUNCTIONS_MOUNT_POINT', 'api/serverless')  # noqa

from tutorial.wsgi import application
azure_application = AzureWSGIHandler(application)


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    response: func.HttpResponse = azure_application(req)
    return response
