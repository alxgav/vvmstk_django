from pyexpat import model
from uuid import uuid4
from django.db import models
from django.utils.translation import gettext_lazy as _

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


# Groups model

class Groups_students(TimeStampedModel):
    KATEGORY_CHOOSER = [
        ('B1', 'B1'),
        ('B', 'B'),
        ('C1', 'C1'),
        ('C', 'C')
    ]
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    group_name = models.CharField(_('group_number'), max_length=4)
    group_date_begin = models.DateField(_('start date'), blank=False)
    group_date_end = models.DateField(_('end date'), blank=False)
    kategory = models.CharField(_('drive kategory'), max_length=52, choices=KATEGORY_CHOOSER)
    price = models.IntegerField(_('price'), blank=False)
    time_study = models.DecimalField(_('learning time'), max_digits=5, decimal_places=1, blank=False)

    def __str__(self):
        return f'{_("Group number ")}{self.group_name} kategory {self.kategory}' 

    class Meta:
        verbose_name = _('groups of students')
        verbose_name_plural = _('groups of students')
        db_table = "content\".\"groups_students"

# passport model



# Student model

class Students(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    id_groups = models.ForeignKey('Groups_students', on_delete=models.CASCADE)
    surname = models.CharField(_('surname'), max_length=255, blank=False)
    firstname = models.CharField(_('firstname'), max_length=255, blank=False)
    middlename = models.CharField(_('middlename'), max_length=255, blank=False)
    birth_date = models.DateField(_('birthday'), blank=False)
    inn_code = models.CharField(_('inn'), max_length=10, blank=False)
    birthplace = models.CharField(_('birthplace'), max_length=255, blank=False)
    address = models.TextField(_('address'), blank=False)
    pass_num = models.CharField(_('passport number'), max_length=10, blank=False)
    pass_date = models.DateField(_('passport date'), blank=False)
    pass_plase = models.TextField(_('passport place'), blank=False)
    hospital_num = models.CharField(_('hospital number'), max_length=10, blank=False)
    hospital_date = models.DateField(_('hospital date'), blank=False)
    hospital_plase = models.TextField(_('hospital place'), blank=False)

    def __str__(self):
        return f'{_("Student ")}{self.surname} {self.firstname} {self.id_groups}' 

    class Meta:
        verbose_name = _('students')
        verbose_name_plural = _('students')
        db_table = "content\".\"students"