from django.contrib import admin

from .models import Groups_students, Students
from django.utils.translation import gettext_lazy as _


class StudentsInstanceInline(admin.TabularInline):
    model = Students
    extra = 0


@admin.register(Groups_students)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_date_begin', 'group_date_end', 'kategory',)
    fields = ('group_name', 
              'group_date_begin',
              'group_date_end', 
              'kategory', 
              'price', 
              'time_study',)
    search_fields = ('group_name', 'kategory',)
    date_hierarchy = "created_at"
    list_filter = ('group_name', 'group_date_begin',)
    inlines = [
        StudentsInstanceInline
    ]
    


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ( 'surname', 'firstname', 'middlename', 'id_groups',)
    # fields = ('surname', 'firstname', 'middlename', 'birth_date', 'inn_code', 'birthplace', 'address', 'pass_num', 'id_groups',)

    fieldsets = (
        (None, {
            'fields':('surname', 'firstname', 'middlename', 'id_groups'),
        }),
        (_('common information'), {
            'fields':('birth_date', 'inn_code', 'birthplace', 'address')
        }),
        (_('Passport'), {
            'fields':('pass_num', 'pass_date', 'pass_plase')
        }),
        (_('Hospital'), {
            'fields':('hospital_num', 'hospital_date', 'hospital_plase')
        }),
    )
