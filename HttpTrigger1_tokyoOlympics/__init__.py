import logging
import sys
import azure.functions as func
import datetime
from datetime import datetime

sys.path.append('..')

#from HttpTrigger1_tokyoOlympics.operations import io
#from .operations import io
from app import main
import pandas as pd
from functools import reduce
from .app import main


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    main_execution = main()
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             main_execution,
             status_code=200
        )