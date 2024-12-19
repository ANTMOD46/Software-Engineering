from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.username} : {self.email}'

# Model สำหรับเก็บประเภทเครื่องดื่ม
class DrinkCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)  # ชื่อประเภทเครื่องดื่ม (เช่น ค็อกเทล, ม็อกเทล)
    description = models.TextField(blank=True)  # รายละเอียดเพิ่มเติม

    def __str__(self):
        return self.name

# Model สำหรับสูตรเครื่องดื่ม
from django.db import models
from django.contrib.auth.models import User

class DrinkRecipe(models.Model):
    name = models.CharField(max_length=200)  # ชื่อสูตร
    category = models.CharField(max_length=100)  # เก็บประเภทเป็นข้อความ
    ingredients = models.TextField()  # ส่วนผสม
    steps = models.TextField()  # ขั้นตอนการทำ
    image = models.ImageField(upload_to='recipes/images/', blank=True, null=True)  # รูปภาพ
    creator = models.ForeignKey(User, on_delete=models.CASCADE)  # ผู้สร้างสูตร
    created_at = models.DateTimeField(auto_now_add=True)  # วันที่สร้าง
    updated_at = models.DateTimeField(auto_now=True)  # วันที่อัปเดตล่าสุด

    def __str__(self):
        return self.name


# Model สำหรับการแสดงสถิติของสมาชิก
class MemberStats(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="stats")  # ลิงก์กับ User
    recipe_count = models.IntegerField(default=0)  # จำนวนสูตรที่ผู้ใช้สร้าง
    favorite_category = models.ForeignKey(DrinkCategory, on_delete=models.SET_NULL, null=True, blank=True)  # ประเภทที่ชื่นชอบ

    def __str__(self):
        return f"Stats for {self.user.username}"
