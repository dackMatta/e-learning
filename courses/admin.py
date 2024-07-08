from django.contrib import admin
from .models import Subject,Course,Modules

# Register your models here.

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display=['title','slug']
    prepopulated_fields= {'slug': ('title',)}

class ModuleInLine(admin.StackedInline):
    model=Modules


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=['title','subjects','created']
    list_filter=['created','subjects']
    search_fields=['title','overview']
    prepopulated_fields= {'slug': ('title',)}
    inlines=[ModuleInLine]
                         