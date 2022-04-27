import graphene
from graphene_django import DjangoObjectType
from hero.models import FileUploadV2

class FileUploadType(DjangoObjectType): 
    class Meta:
        model = FileUploadV2
        fields = "__all__"

class Query(graphene.ObjectType):

    all_files = graphene.List(FileUploadType)
    ok = graphene.Boolean(default_value=True)
    
    def resolve_all_files(self, info, **kwargs):
        return FileUploadV2.objects.all()

# For File Upload
class FileUploadInput(graphene.InputObjectType):
    id = graphene.ID()
    document = graphene.String()
class newFileUpload(graphene.Mutation):
    class Arguments:
        file_data = FileUploadInput(required=True)    

    ok = graphene.Field(FileUploadType)

    def mutate(root, info, file_data):
        fileUpload_instance = FileUploadV2(document=file_data.document)
        fileUpload_instance.save()
        return newFileUpload(ok=fileUpload_instance)

class Mutation(graphene.ObjectType):
    my_upload = newFileUpload.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
