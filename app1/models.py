from django.db import models

# Create your models here.
class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    mgr=models.CharField(max_length=100) 
    mname=models.CharField(max_length=100)
    
    def __str__(self):
       return str(self.deptno)
   
class Emp(models.Model):
    eno=models.CharField(max_length=100,primary_key=True)
    ecode=models.CharField(max_length=100)
    ename=models.CharField(max_length=100)
    hiredate=models.DateField()
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    sal=models.FloatField(max_length=100)
    comm=models.FloatField(max_length=100)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)

    def __str__(self):
       return self.eno