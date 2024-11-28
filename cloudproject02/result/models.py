from django.db import models
from django.db import models
# Create your models here.
class Vote(models.Model):
    id = models.BigAutoField(primary_key=True)  # 主键字段
    choice = models.CharField(max_length=255)  # 假设 choice 是一个字符类型字段
    # 其他字段可能会被自动检测出来

    class Meta:
        managed = False  # 避免 Django 尝试迁移或修改该表
        db_table = 'vote'  # 明确指定表名