from django.shortcuts import render
from django.http import HttpResponse
from app1.models import *
from django.db.models import Q
#Using Q for AND (Default behavior with filter()): 
#Q IS A CLASS
'''
The most common useful  cases for Q are:
1))Combining multiple conditions using logical AND, OR, or NOT.
2))Dynamically constructing queries based on varying conditions.
'''

# Create your views here.
def display(request):
    #WO=Emp.objects.all()
    #WO=Emp.objects.filter(mgr='202')
    #WO=Emp.objects.exclude(mgr='202')
    #WO=Emp.objects.all()[1:4:]#we get three records
    #WO=Emp.objects.all()[::-1]
    #WO=Emp.objects.all().order_by('mgr')
    #WO=Emp.objects.all().order_by('-mgr')
    WO=Emp.objects.all().order_by('sal')
    SS={'WO':WO}
    return render(request,'h1.html',SS)



#SHOW ME THE HARSHAD MANAGER NAME
def displaY(request):
    WP=Emp.objects.get(ename='HARSHAD')
    P=WP.mgr
    WO=Emp.objects.filter(ecode=P)
    SS={'WO':WO}
    return render(request,'h1.html',SS)


#SHOW ME THE SALARY DETAILS MAX,MIN,2ND MIN,2ND MAX
def sal(request):
    #2nd min sal
    '''
    WO=Emp.objects.all().order_by('sal')[1:2:]

    '''
    #2nd max sal
    '''
    WO=Emp.objects.all().order_by('-sal')[1:2:]
    '''
    #max sal
    '''
    WO = Emp.objects.all().order_by('-sal')[:1]
    '''
    #mix sal
    
    WO = Emp.objects.all().order_by('sal')[:1]
    
    

    SS={'WO':WO}
    return render(request,'h1.html',SS)



#PERFORM JOINS
def selectRelatedJoins(request):
    #WO=Emp.objects.all().select_related('deptno')

    #2ND MIN SALARY
    '''
    WO=Emp.objects.all().select_related('deptno').order_by('sal')[1:2:]
    '''
    #2ND MAX SAL
    '''
    WO=Emp.objects.all().select_related('deptno').order_by('-sal')[1:2:]
    '''

    #WO=Emp.objects.all().select_related('deptno').order_by('mgr')

    #WO=Emp.objects.all().select_related('deptno').order_by('sal')

    #WO=Emp.objects.all().select_related('deptno').filter(mgr=100)
    
    #WO=Emp.objects.select_related('deptno').exclude(mgr='202')

    #WO=Emp.objects.all().select_related('deptno')[1:4:]

    #WO=Emp.objects.all().select_related('deptno')[::-1]

    #WO=Emp.objects.all().select_related('deptno').filter(comm=0)



    #VAMSIKRISHNA'S MANAGER DETAILS USING ORM(join the emp table & dept table)
    '''
    WP=Emp.objects.get(ename='VAMSIKRISHNA')
    P=WP.mgr
    WO=Emp.objects.all().select_related('deptno').filter(ecode=P)
    
    '''

    #VAMSIKRISHNA'S MANAGER'S MANAGER DETAILS USING ORM (join the emp table & dept table)
    '''
    WA=Emp.objects.get(ename='HARSHAD')#TAKE THE HARSHAD RECORDS INTO AN OBJECT
    PP=WA.mgr#EXTRACT HARSHAD'S MGR   
    WP=Emp.objects.get(ecode=PP)#TAKE VAMSIKRISHNA RECORD BASED ON HARSHAD'S MGR (HARSHAD'S MGR==VAMSIKRISHNA'S ECODE)
    P=WP.mgr #EXTRACT VAMSIKRISHNA'S MGR
    WO=Emp.objects.all().select_related('deptno').filter(ecode=P)#TAKE GREESHMA RECORD BASED ON VAMSIKRISHNA'S MGR (VAMSIKRISHNA'S MGR==GREESHMA'S ECODE)
    
    '''

    #SHOW ME THE DETAILS OF EMPLOYEES WHO ARE WORKED UNDER VAMSIKRISHNA'S BY USING ORM(join the emp table & dept table)
    '''
    WP=Emp.objects.get(ename='VAMSIKRISHNA')
    P=WP.ecode
    WO=Emp.objects.all().select_related('deptno').filter(mgr=P)
    
    '''



    ''' 
    HINT:- colNAME__gte  means greater than or equal to
           colNAME__lte  means less than or equal to
            colNAME__lt  means less than 
            colNAME__gt  means greater than 
    '''
    #SALARY greater than or Equal to 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gte=80000)
    '''

    #SALARY LESS THAN or EQUAL to  80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__lte=80000)
    '''

    #SALARY greater than 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gt=80000)'
    '''

    #SALARY less than 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__lt=80000)
    '''






    #ORDER THE SALARIES BY USING ORDER METHOD

    #SALARY greater than or Equal to 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gte=80000).order_by('sal')
    '''

    #SALARY LESS THAN or EQUAL to  80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__lte=80000).order_by('sal')
    '''

    #SALARY greater than 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gt=80000).order_by('sal')
    '''

    #SALARY less than 80000
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__lt=80000).order_by('sal')
    '''
    
    #max sal
    '''
    WO = Emp.objects.all().select_related('deptno').order_by('-sal')[:1]
    '''
    #mix sal
    '''
    WO = Emp.objects.all().select_related('deptno').order_by('sal')[:1]
    '''
    #SAL GREATER THAN OR EQUAL TO 80000 AND SAL LESS THAN OR EQUAL TO 90000 
    #HINT:-  WITHOUT USING Q OBJECT BY DEFAULT IT TAKES 'AND' COMBINATION BOSS
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gte=80000,sal__lte=90000).order_by('sal')
    '''

    #SAL GREATER THAN 75000 AND SAL LESS THAN  100000 
    '''
    WO = Emp.objects.all().select_related('deptno').filter(sal__gt=75000,sal__lt=100000).order_by('sal')
    '''


    #SHOW ME THE DETAILS OF HARSHAD AND PRANAY WHO'S SAL GREATER THAN 65000 AND SAL LESS THAN  100000 
    #IN THE BELOW WE ARE USING THE COMBINATION OF 'AND' AND 'OR'  OPERATORS IN THE FILTER METHOED
    #AND Q WORKS AS PARAMETERAISED OBJECT'Q()'
    '''
    When you pass multiple conditions to the filter() method without Q, Django automatically combines them using AND logic.
    But if you want to use AND explicitly or combine it with OR,then Q objects are useful.
    '''
    '''
    WO = Emp.objects.all().select_related('deptno').filter(Q(ename='HARSHAD')|Q(ename='PRANAY')& Q(sal__gt=65000)& Q(sal__lt=100000)).order_by('sal')
    '''
    #SHOW ME THE DETAILS OF HARSHAD,PRANAY AND VAMSIKRISHNA 
    WO = Emp.objects.all().select_related('deptno').filter(Q(ename='HARSHAD') | Q(ename='PRANAY') | Q(ename='GREESHMA')).order_by('sal') 






    DD={'WO':WO}
    #return render(request,'h2.html',DD)
    return render(request,'h3.html',DD)






