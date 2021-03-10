from django.forms import ModelForm
from .models import *
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = [
            'r_number',
            'seating_capacity'
        ]


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = [
            'uid',
            'name'
        ]


class MeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'pid',
            'time',
            'day'
        ]
        widgets = {
            'pid': forms.TextInput(),
            'time': forms.Select(),
            'day': forms.Select(),
        }


class updateMeetingTimeForm(ModelForm):
    class Meta:
        model = MeetingTime
        fields = [
            'time',
            'day',
        ]
        widgets = {
            'time': forms.Select(),
            'day': forms.Select(),
        }


class updateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_name',
            'max_numb_students',
            'instructors',
        ]


class updateSectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['department', 'num_class_in_week']



class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('course_number', 'course_name', 'max_numb_students', 'instructors')


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['dept_name', 'courses']


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['section_id', 'department', 'num_class_in_week']


