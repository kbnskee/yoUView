# youview

db > uv_djangomodel > model > basemodel
    created_date    = models.DateTimeField(auto_now_add = True,blank=True,null=True)
    updated_date    = models.DateTimeField(auto_now = True,blank=True,null=True)
    created_by      = models.CharField(max_length=225)
    updated_by      = models.CharField(max_length=225)