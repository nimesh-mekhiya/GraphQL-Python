from django.test import TestCase
from python_graphql_client import GraphqlClient

client1 = GraphqlClient(endpoint="http://127.0.0.1:8000/graphql")

file = "longbase64encodedstring"
variables = { "fileObject": file }
    
class FileUploadTest(TestCase):
    def test_file_graphql_query(self):
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
        variables = { "fileObject": file }
        response = client1.execute(query=query, variables=variables)
        data = response['data']['myUpload']
        self.assertTrue(data.get('ok') != "")
