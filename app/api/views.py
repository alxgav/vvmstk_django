from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from vvmstk.models import Groups_students, Students
from .serializer import Group_studentsSerializer, StudentsSerializer


@api_view(['GET'])
def getApi(request):
    api_url = {'groups':'/groups/',
               'students':'/students/',
               'group-detail':'/group-detail/<str:pk>',
               'group-create':'/group-create/',
               'student_detail':'/student/<str:pk>',}
    return Response(api_url)




@api_view(['GET'])
def getGroups(request):
    items = Groups_students.objects.all()
    serializer = Group_studentsSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getGroupDetail(request, pk):
    items = Groups_students.objects.get(id=pk)
    serializer = Group_studentsSerializer(items, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def addGroup(request):
    serializer = Group_studentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def groupUpdate(request, pk):
    items = Groups_students.objects.get(id=pk)
    serializer = Group_studentsSerializer(instance=items,  data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def groupDelete(request, pk):
    items = Groups_students.objects.get(id=pk)
    items.delete()

    return Response(f'{pk} succsesfully deleted!')

