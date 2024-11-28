from django.db import models
import datetime

# 投票模型
# class Vote(models.Model):
#     choice = models.CharField(max_length=5)  # "cats" 或 "dogs"
#     timestamp = models.DateTimeField(default=datetime.datetime.now)
#
#     def __str__(self):
#         return f"{self.choice} vote at {self.timestamp}"
#
# # 日志模型（可选，保存按钮点击日志）
# class VoteLog(models.Model):
#     choice = models.CharField(max_length=5)  # "cats" 或 "dogs"
#     timestamp = models.DateTimeField(default=datetime.datetime.now)
#
#     def __str__(self):
#         return f"Clicked {self.choice} at {self.timestamp}"
#
#
# from django.db import models
#
#
# # Create your models here.
# class Demo(models.Model):
#     car_num = models.CharField(max_length=32)
#     park_name = models.CharField(max_length=32)
#     jinru_Date = models.CharField(max_length=32)
#     chuqu_Date = models.CharField(max_length=32)
#     time = models.CharField(max_length=32)

from django.db import models

# class Vote(models.Model):
#     option = models.CharField(max_length=100)  # 投票选项
#     count = models.IntegerField(default=0)  # 该选项的投票数，初始为 0
#
#     def __str__(self):
#         return self.option


from django.db import models


class Vote(models.Model):
    choice = models.CharField(max_length=5)  # "cats" 或 "dogs"
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"{self.choice} vote at {self.timestamp}"
    class Meta:
        db_table='vote'