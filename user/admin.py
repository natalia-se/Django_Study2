from django.contrib import admin
from user.models import User, FormSubmission

admin.site.register(User)

@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'text')
