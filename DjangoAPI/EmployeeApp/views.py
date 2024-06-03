from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializer, EmployeeSerializer

from django.core.files.storage import default_storage

from .forms import UsersForm

# Create your views here.

def index(request):
    data = {}
    
    if request.method == 'GET':
        st = request.GET.get('DepartmentName')
        if st:
            department = Departments.objects.filter(DepartmentName__icontains=st)
            data['departmentData'] = department
    
    return render(request, "index.html", data)


def home(request):
    fn = UsersForm()
    val1= int(request.POST.get('n1',0))
    val2= int(request.POST.get('n2',0))
    # val2= int(request.POST['n2'])
    res = val1+val2
    data = {
        "result":res,
        "form" : fn,
        "title":"Home Page",
        "body":"Welcome to home page",
        "clist" : ["Java", "Python", "Javascript"],
        "student_details":[
            {"name" : "Anand", "phone" : 9898989898},
            {"name" : "Akshay", "phone" : 7979797979}
        ],
        "description": "Hello this is example for <b>Template Filter </b> in Django"
    }
    return render(request,'home.html',data)

def calculator(request):
    c=''
    try:
        if request.method =="POST":
            if request.POST.get('num1') == "":
                return render (request, "calculator.html", {'error':True})
            
            n2=eval(request.POST.get('num2'))
            n1 = int(request.POST.get('num1'))
            opr=request.POST.get('opr')
            if opr =="+":
                c = n1+n2
            elif opr =="-":
                c = n1-n2
            elif opr =="*":
                c =n1*n2
            elif opr =="/":
                c =n1/n2

    except :
        c = "Invalid opr....."
    print(c)
    return render(request, 'calculator.html',{'c':c})


@csrf_exempt
def departmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        # departments = Departments.objects.all().order_by('DepartmentName')  #order by ascending using department name
        # departments = Departments.objects.all().order_by('-DepartmentName')  #order by descending using department name with - symbol
        # departments = Departments.objects.all().order_by('-DepartmentName')[:3] #adding limit using slicing
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)
    
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        departments_serializer = DepartmentSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentId = department_data['DepartmentId'])
        departments_serializer = DepartmentSerializer(department, data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentId = id)
        department.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt
def employeeApi(request, id=0):
    if request.method == 'GET':
        employees = Employees.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)
    
    elif request.method == 'POST':
        employee_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    
    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employees.objects.get(EmployeeId = employee_data['EmployeeId'])
        employees_serializer = EmployeeSerializer(employee, data=employee_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Successfully", safe=False)
        return JsonResponse("Failed to Update")
    
    elif request.method == 'DELETE':
        employee = Employees.objects.get(EmployeeId = id)
        employee.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

@csrf_exempt #Cross-Site Request Forgery
def SaveFile(request):
    file = request.FILES['file']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)