import logging
import uuid
import datetime
import azure.functions as func

def main(req: func.HttpRequest, doc: func.Out[func.Document]) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.route_params.get('name')

    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        usersdoc = func.DocumentList() 
        users_dict = {
            "id": str(uuid.uuid4()),
            "date": str(datetime.date.today()),
            "name": name
        }
        usersdoc.append(func.Document.from_dict(users_dict))
        doc.set(usersdoc)
        
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )