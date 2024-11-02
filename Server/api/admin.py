from django.contrib import admin
from .models import User, Lecturer, Student, Course, Assignment, Submission, GradingResult

admin.site.register(Lecturer)
admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Assignment)
admin.site.register(Submission)
admin.site.register(GradingResult)


# Compare this snippet from Server/api/urls.py: