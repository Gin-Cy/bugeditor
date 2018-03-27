#coding:utf-8

from __future__ import unicode_literals

from django.db import models

#项目类
class Project(models.Model):
    p_name = models.CharField(max_length=32)
    p_time= models.CharField(max_length=32)
    p_charge = models.CharField(max_length=32)

    def __unicode__(self):
        
        return self.p_name
        
#漏洞
        
class Bug(models.Model):
    b_name = models.CharField(max_length=32)
    b_risk = models.TextField()
    b_level = models.CharField(max_length=32)
    b_details = models.TextField(max_length=32)
    b_repair = models.TextField()
    b_url = models.CharField(max_length=200)
    b_project = models.ForeignKey("Project")
    
    def __unicode__(self):
        
        return self.b_name

class BugModel(models.Model):
    b_name = models.CharField(max_length=32)
    b_risk = models.TextField()
    b_level = models.CharField(max_length=32)
    b_details = models.TextField(max_length=32)
    b_repair = models.TextField()
    b_url = models.CharField(max_length=200)
    
    def __unicode__(self):
        
        return self.b_name
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    