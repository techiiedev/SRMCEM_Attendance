from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    # ── Landing & Auth ──────────────────────────────────────────────────────
    path('',                views.index,           name='index'),
    path('dashboard/',      views.dashboard,       name='dashboard'),
    path('waiting-approval/', views.waiting_approval, name='waiting_approval'),
    path('renotify-admin/', views.renotify_admin,  name='renotify_admin'),

    # ── Attendance ───────────────────────────────────────────────────────────
    path('mark/<str:s_class>/<int:sub_id>/', views.mark_attendance, name='mark_attendance'),

    # ── Reports ──────────────────────────────────────────────────────────────
    path('reports/',                    views.view_reports, name='reports'),
    path('export-pdf/<int:record_id>/', views.export_pdf,   name='export_pdf'),
    path('export-docx/<int:record_id>/',views.export_docx,  name='export_docx'),

    # ── Student Management ───────────────────────────────────────────────────
    path('manage-students/',                    views.manage_students, name='manage_students'),
    path('delete-student/<int:student_id>/',    views.delete_student,  name='delete_student'),

    # ── Teacher / Admin Management ───────────────────────────────────────────
    path('manage-teachers/',                    views.manage_teachers,  name='manage_teachers'),
    path('approve-teacher/<int:teacher_id>/',   views.approve_teacher,  name='approve_teacher'),
    path('reject-teacher/<int:teacher_id>/',    views.reject_teacher,   name='reject_teacher'),

    # ── Auth ─────────────────────────────────────────────────────────────────
    path('register/', views.register, name='register'),
    path('login/',    auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/',   views.logout_view, name='logout'),
]