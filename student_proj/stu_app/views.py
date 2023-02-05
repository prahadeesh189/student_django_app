from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 

from django.views.decorators.csrf import csrf_exempt

from stu_app.models import Student
from stu_app.serializers import StudentSerializer

from rest_framework.decorators import api_view



@api_view(['GET'])
@csrf_exempt
def studentALL(request):

    if (request.method=='GET'):
        students = Student.objects.all()
        return JsonResponse(StudentSerializer(students,  many=True).data, safe=False)

    return JsonResponse({"message":"Unsuccessfull request"}, safe=False)



@api_view(['GET'])
@csrf_exempt
def studentSearch(request, Idnum):

    if (request.method=='GET'):

        try:
            students_data = Student.objects.get(Id=Idnum)
            return JsonResponse(StudentSerializer([students_data],  many=True).data, safe=False)
        except:
            return JsonResponse({"message":"Student Not Found"}, safe=False)


    return JsonResponse({"message":"Unsuccessfull request"}, safe=False)



@api_view(['POST'])
@csrf_exempt
def studentAdd(request):

    if (request.method=='POST'):
        students_data = Student(name=request.data.get('name'), branch=request.data.get('branch'), college_name=request.data.get('college-name'))
        students_data.save()
        return JsonResponse({"message":"Successfull Student Data Added"}, safe=False)   
        # return JsonResponse({"message":"Student Data Not Added"}, safe=False)

    return JsonResponse({"message":"Unsuccessfull request"}, safe=False)



@api_view(['PUT'])
@csrf_exempt
def studentUpdate(request):

    if (request.method=='PUT'):

        students_data = Student.objects.get(Id=request.data.get('Id'))
        

        if request.data.get("name")!=None and len(request.data.get("name")) > 0:
            students_data.name = request.data.get("name") 
        if request.data.get("branch")!=None  and len(request.data.get("branch")) > 0:
            students_data.branch = request.data.get("branch")            
        if request.data.get("college-name")!=None and len(request.data.get("college-name")) > 0:
            students_data.college_name = request.data.get("college-name")

        students_data.save()
        return JsonResponse({"message":"Successfull Student Data Updated"}, safe=False)   

        # return JsonResponse({"message":"Student Data Not Added"}, safe=False)

    return JsonResponse({"message":"Unsuccessfull request"}, safe=False)



def front(request):
    context = { }
    return render(request, "index.html", context)