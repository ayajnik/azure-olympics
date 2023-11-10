import logging
from app import final_frame
import azure.functions as func
import datetime
from datetime import datetime
from operations import io


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

    today = datetime.today()
    today_str = today.strftime('%Y-%m-%d')
    
    final_frame.to_csv('/tmp/processedOlympicsData_'+today_str+'.csv')

    


    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             io.dumpFile('processedOlympicsData_'+today_str+'.csv'),
             status_code=200
        )
