from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('sugar', 'السكري'),
        ('insulin', 'مقاومة الإنسولين'),
        ('pressure', 'ضغط الدم'),
    ]
    
    title = models.CharField(max_length=200, verbose_name="عنوان المقال")
    content = models.TextField(verbose_name="المحتوى")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, verbose_name="القسم")
    image = models.ImageField(upload_to='articles/', blank=True, null=True, verbose_name="صورة المقال")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title