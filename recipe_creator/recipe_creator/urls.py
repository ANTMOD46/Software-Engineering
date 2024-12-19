from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static
from django.conf import settings
from recipes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # หน้าแรก
    path('user-home/', views.home_user, name='home_user'),  # หน้า Home สำหรับผู้ใช้
    path('login/', views.login_view, name='login'),  # หน้า Login
    path('signup/', views.signup_view, name='signup'),  # หน้า Signup
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),  # กลับไปหน้า home หลังจากออกจากระบบ
    path('recipes/', include('recipes.urls')),  # รวม URL ของแอป recipes
    path('stats/', views.my_stats, name='my_stats'),  # สถิติของฉัน
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
