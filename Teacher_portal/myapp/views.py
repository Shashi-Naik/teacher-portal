from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import Teacher, Student, AuditLog, SessionToken
from .helpers import hash_password, create_token, add_marks

def login_view(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        pwd = request.POST.get("password")

        try:
            teacher = Teacher.objects.get(username=uname)
            hashed, _ = hash_password(pwd, teacher.salt)
            if hashed == teacher.password_hash:
                token = create_token()
                SessionToken.objects.create(teacher=teacher, token=token)
                resp = redirect("home")
                resp.set_cookie("session_token", token, httponly=True, samesite="Strict")
                return resp
        except Teacher.DoesNotExist:
            pass
        return render(request, "login.html", {"error": "Invalid username or password"})
    return render(request, "login.html")



def logout_view(request):
    token = request.COOKIES.get("session_token")
    if token:
        SessionToken.objects.filter(token=token).delete()
    resp = redirect("login")
    resp.delete_cookie("session_token")
    return resp








def home_view(request):
    students = Student.objects.all().order_by("name")
    return render(request, "home.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        subject = request.POST.get("subject")
        try:
            marks = int(request.POST.get("marks"))
        except Exception:
            return JsonResponse({"status": "error", "msg": "Marks must be a number"})

        if not (0 <= marks <= 100):
            return JsonResponse({"status": "error", "msg": "Marks must be between 0 and 100"})

        student = Student.objects.filter(name=name, subject=subject).first()
        if student:
            old_marks = student.marks
            new_total = add_marks(student.marks, marks)
            if not new_total:
                return JsonResponse({"status": "error", "msg": "Total marks cannot exceed 100"})

            student.marks = new_total
            student.save()

            token = request.COOKIES.get("session_token")
            session = SessionToken.objects.filter(token=token).first()
            if session:
                AuditLog.objects.create(student=student, teacher=session.teacher,
                                        old_value=old_marks, new_value=new_total)
        else:
            Student.objects.create(name=name, subject=subject, marks=marks)

        return JsonResponse({"status": "ok"})




def update_marks(request, student_id):
    if request.method == "POST":
        try:
            marks = int(request.POST.get("marks"))
        except Exception:
            return JsonResponse({"status": "error", "msg": "Marks must be a number"})

        if not (0 <= marks <= 100):
            return JsonResponse({"status": "error", "msg": "Marks must be between 0 and 100"})

        student = get_object_or_404(Student, id=student_id)
        old_marks = student.marks
        student.marks = marks
        student.save()

        token = request.COOKIES.get("session_token")
        session = SessionToken.objects.filter(token=token).first()
        if session:
            AuditLog.objects.create(student=student, teacher=session.teacher,
                                    old_value=old_marks, new_value=marks)

        return JsonResponse({"status": "ok", "marks": marks})







def delete_student(request, student_id):
    if request.method == "POST":
        student = get_object_or_404(Student, id=student_id)
        student.delete()
        return JsonResponse({"status": "ok"})











