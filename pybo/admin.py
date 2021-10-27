from django.contrib import admin

# Register your models here.

from .models import Question

# 검색기능 
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)