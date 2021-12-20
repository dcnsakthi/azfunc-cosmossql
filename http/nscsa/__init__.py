import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, doc:func.DocumentList) -> func.HttpResponse:
    
    logging.info('Python HTTP trigger function processed a request.')
 
    usersdoc = []

    for user in doc:
        userdoc = {
            "id": user['id'],
            "date": user['date'],
            "name": user['name']
        }
        usersdoc.append(userdoc)

    return func.HttpResponse(
            json.dumps(usersdoc),
            status_code=200,
            mimetype="application/json"            
    )