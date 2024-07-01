from django.shortcuts import render
from RegisterForm.models.students import Students
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def registration_form(request):
    return render(request, 'website/registration_form.html')

@csrf_exempt
def student_register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        whatsapp_number = request.POST.get('whatsapp')
        phone_number = request.POST.get('phone')
        college_name = request.POST.get('college')
        dob = request.POST.get('birthday')
        gender = request.POST.get('gender')
        department = request.POST.get('department')
        year = request.POST.get('year')

        student = Students.objects.create(
            name=name,
            email=email,
            whatsapp_number=whatsapp_number,
            phone_number=phone_number,
            college_name=college_name,
            dob=dob,
            gender=gender,
            department=department,
            year=year
        )
        student.save()

        return JsonResponse({'success': True, 'name': name, 'email': email, 'whatsapp_number': whatsapp_number})

    return JsonResponse({'success': False}, status=405)
