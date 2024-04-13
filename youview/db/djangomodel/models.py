from django.db import models

class Log(models.Model):
    ACTION_CHOICES=(
        ('CREATE', 'Create'),
        ('UPDATE', 'Update'),
        ('DELETE', 'Delete')
    )
    action          = models.CharField(max_length=10,choices=ACTION_CHOICES)
    model_name      = models.CharField(max_length=100)
    remarks         = models.CharField(max_length=225,unique=True)
    description     = models.CharField(max_length=225,blank=True,null=True)
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.CharField(max_length=225,unique=True)
    updated_by      = models.CharField(max_length=225,unique=True)

    def __str__(self):
        return f"{self.action} | {self.remarks}" 
    
    class Meta:
        ordering = ['-created_date','-update_date']
        db_table = "uv_log"


    