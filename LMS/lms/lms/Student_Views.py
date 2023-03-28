from django.shortcuts import render,redirect
from lm_system.models import Student_Notification,Student,Student_leave
from django.contrib import messages

def HOME(request):
    return render(request,'Student/home.html')

def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)
        
        context = {
            'notification':notification,
        }
    return render(request,'Student/notification.html',context)

def STUDENT_NOTIFICATION_MARK_AS_DONE(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')

def STUDENT_LEAVE(request):
    student = Student.objects.get(admin = request.user.id)
    Student_leave_history = Student_leave.objects.filter(student_id = student)
    
    context = {
            'student_leave_history':Student_leave_history,
    }
    
    return render(request,'Student/apply_leave.html',context)


def STUDENT_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')
        
        student_id = Student.objects.get(admin = request.user.id)
        
        student_leave = Student_leave(
            student_id = student_id,
            date = leave_date,
            message = leave_message
        )
        student_leave.save()
        messages.success(request,'Leave was successfully sent !')
        return redirect('student_leave')