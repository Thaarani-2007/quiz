from django.contrib import admin
from django.contrib.auth.models import User
from .models import Subject, Topic, Question, studentdetails, result

class TopicFilter(admin.SimpleListFilter):
    title = 'Topic'
    parameter_name = 'topic'

    def lookups(self, request, model_admin):
        subject_id = request.GET.get('subject')
        if subject_id:
            return Topic.objects.filter(subject_id=subject_id).values_list('id', 'name')
        else:
            return []

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(topic_id=self.value())
        else:
            return queryset

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('subject', 'topic', 'class_name', 'question_text', 'correct_answer',)
    list_filter = ('subject', TopicFilter, 'class_name',)
    search_fields = ('question_text', 'option1', 'option2', 'option3', 'option4',)

    # def formfield_for_foreignkey(self, db_field, request, **kwargs):
    #     if db_field.name == "topic":
    #         # Filter topics based on the selected subject
    #         subject_id = request.GET.get('id_subject')
    #         print(subject_id)
    #         if subject_id:
    #             kwargs["queryset"] = Topic.objects.filter(subject_id=subject_id)
    #         else:
    #             kwargs["queryset"] = Topic.objects.none()
    #     return super().formfield_for_foreignkey(db_field, request, **kwargs)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('subject', 'name',)
    list_filter = ('subject',)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class studentdetailsAdmin(admin.ModelAdmin):
    list_display= ("Admission_No", "Student_name",)
    search_fields= ("Admission_No", "Student_name",)


class resultAdmin(admin.ModelAdmin):
    list_display = ('admission_no',"name","section", 'topic', 'score')
    search_fields = ("name",)




admin.site.register(Question, QuestionAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Subject, SubjectAdmin)
# admin.site.register(studentdetails, studentdetailsAdmin)
admin.site.register(result, resultAdmin)






















# from django.contrib import admin
# from .models import Subject, Topic, Question

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'topic', 'class_name', 'question_text', 'correct_answer',)
#     list_filter = ('subject', 'topic', 'class_name',)
#     search_fields = ('question_text', 'option1', 'option2', 'option3', 'option4',)

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'name',)
#     list_filter = ('subject',)

# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)



# from django.contrib import admin
# from .models import Subject, Topic, Question

# class TopicFilter(admin.SimpleListFilter):
#     title = 'Topic'
#     parameter_name = 'topic'

#     def lookups(self, request, model_admin):
#         subject_id = request.GET.get('subject_id')
#         if subject_id:
#             return Topic.objects.filter(subject_id=subject_id).values_list('id', 'name')
#         else:
#             return []

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(topic_id=self.value())
#         else:
#             return queryset

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'topic', 'class_name', 'question_text', 'correct_answer',)
#     list_filter = ('subject', TopicFilter, 'class_name',)
#     search_fields = ('question_text', 'option1', 'option2', 'option3', 'option4',)

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'name',)
#     list_filter = ('subject',)

# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)





# from django.contrib import admin
# from .models import Subject, Topic, Question

# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'topic', 'class_name', 'question_text', 'correct_answer',)
#     list_filter = ('subject', 'topic', 'class_name',)
#     search_fields = ('question_text', 'option1', 'option2', 'option3', 'option4',)

# class TopicAdmin(admin.ModelAdmin):
#     list_display = ('subject', 'name',)
#     list_filter = ('subject',)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == "subject":
#             # Filter topics based on the selected subject
#             kwargs["queryset"] = Subject.objects.all()
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# class SubjectAdmin(admin.ModelAdmin):
#     list_display = ('name',)
    # search_fields = ('name',)



