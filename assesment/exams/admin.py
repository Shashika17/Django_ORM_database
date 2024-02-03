from django.contrib import admin
from .models import School,Summery,Assesment_Areas,Class,Student,Answers,Awards,Subject
# Register your models here.
@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Name']

@admin.register(Summery)
class  SummaryAdmin(admin.ModelAdmin):
    list_display = ['School_Id','Sydney_Participants','Sydney_Percentile','Assesment_Area_Id','Award_Id','Class_Id','Correct_answer_precentage_per_class','Correct_Answer','Student_Id','Participant','Student_score','Subject_Id','Category_Id','Year_level_name','Answer_Id','Correct_answer_id']

@admin.register(Assesment_Areas)
class  AssessmentAreaAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Name']

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
   list_display = ['ID', 'Class']

@admin.register(Student)
class  StudentAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Fullname']

@admin.register(Answers)
class AnswersAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Answers']

@admin.register(Awards)
class AwardsAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Name']

@admin.register(Subject)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ['ID', 'Subject','Subject_score']