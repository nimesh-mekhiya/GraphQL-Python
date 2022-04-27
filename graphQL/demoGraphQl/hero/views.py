from django.shortcuts import render
import base64
from hero.task import go_to_sleep
from python_graphql_client import GraphqlClient

client = GraphqlClient(endpoint="http://127.0.0.1:8000/graphql")


def index(request):
  task = go_to_sleep.delay(1)
  if request.method == 'POST':
    
    my_uploaded_file = request.FILES['document'].read() 
    encoded_string = base64.b64encode(my_uploaded_file).decode("utf-8")
    query = """
        mutation UploadFile($fileObject: String) {
          myUpload(fileData: { id: "", document: $fileObject }) {
            ok {
              document
              id
            }
          }
        }
    """
    variables = { "fileObject": encoded_string }
    client.execute(query=query, variables=variables)
  return render(request, 'fileupload.html', {'task_id': task.task_id})

def index1(request):
  task = go_to_sleep.delay(1)
  return render(request, 'fileupload.html', {'task_id': task.task_id})