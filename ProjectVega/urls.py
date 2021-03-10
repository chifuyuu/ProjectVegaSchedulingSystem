"""ProjectVega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import path, include
from scheduling_using_genetic import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('timetable_generation/', views.timetable, name='timetable'),
    path('add_room/', views.add_room, name='addroom'),
    path('add_professor/', views.add_professor, name='addprofessor'),
    path('professor_list/', views.professor_list_view, name='editprofessor'),
    path('add_meetingtime/', views.add_meeting_time, name='addmeetingtime'),
    path('meetingtime_list/', views.meeting_list_view, name='editmeetingtime'),
    path('add_course/', views.add_course, name='addcourse'),
    path('course_list/', views.course_list_view, name='editcourse'),
    path('add_department/', views.add_department, name='adddepartment'),
    path('delete_meetingtime/<str:pk>/', views.delete_meeting_time, name='deletemeetingtime'),
    path('delete_course/<str:pk>/', views.delete_course, name='deletecourse'),
    path('delete_professor/<int:pk>/', views.delete_professor, name='deleteprofessor'),
    path('room_list/', views.room_list, name='editrooms'),
    path('delete_room/<int:pk>/', views.delete_room, name='deleteroom'),
    path('department_list/', views.department_list, name='editdepartment'),
    path('view_department/<int:pk>/', views.view_department, name='view_department'),
    path('delete_department/<int:pk>/', views.delete_department, name='deletedepartment'),
    path('add_section/', views.add_section, name='addsection'),
    path('section_list/', views.section_list, name='editsection'),
    path('delete_section/<str:pk>/', views.delete_section, name='deletesection'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('update_room/<str:pk>/', views.updateRoom, name='update_room'),
    path('update_prof/<str:pk>/', views.updateProf, name='update_prof'),
    path('update_meetingtime/<str:pk>/', views.updateMeetingtime, name='update_meetingtime'),
    path('update_course/<str:pk>/', views.updateCourse, name='update_course'),
    path('update_department/<str:pk>/', views.updateDepartment, name='update_department'),
    path('update_section/<str:pk>/', views.updateSection, name='update_section'),
]
