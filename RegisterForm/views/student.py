from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from RegisterForm.models import Students

def student_list(request):
    query = request.GET.get('q', '')
    is_paid = request.GET.get('is_paid', '')
    
    students = Students.objects.all().order_by('-enrolled_on')

    if query:
        students = students.filter(
            Q(name__icontains=query) | 
            Q(email__icontains=query) | 
            Q(phone_number__icontains=query)
        )
    
    if is_paid:
        students = students.filter(is_paid=is_paid == 'True')

    paginator = Paginator(students, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    count = students.count()

    return render(request, 'admin/student_list.html', {
        'page_obj': page_obj,
        'count': count,
        'query': query,
        'is_paid': is_paid,
    })


def mark_as_paid(request, id):
    student = get_object_or_404(Students, id=id)
    student.is_paid = True
    student.save()
    return redirect('student_list')