from django.shortcuts import render,redirect
from django.contrib import messages
from pprint import  pprint
from django.contrib.auth import login, authenticate
from GamificationForEmployees.forms import SignUpForm, ChangePasswordForm
from GamificationForEmployees.models import Monthly
from GamificationForEmployees.models import Yearly, predResults
from django.contrib.auth.models import User
from datetime import datetime
import pandas as pd

import os,sys
sys.path.append(os.path.dirname(os.getcwd()))
import json



from django.http import JsonResponse
import random


def home(request):
    if request.user.is_authenticated:
        
        if request.user.is_superuser:

            table1 = Monthly.objects.all()
            table2 = Yearly.objects.all()
        else:
            print(1)
            table1 = Monthly.objects.filter(e_no=request.user.username[4:])
            table2 = Yearly.objects.filter(e_no=request.user.username[4:])

        return render(request, 'home.html',{'table1':table1,'table2':table2, 'datatable3':table2})
    else:
        return redirect('user_login')


def predict_chances(request):

    if request.method == 'POST':

        month = request.POST.get('month')
        emp_no = request.POST.get('emp_no')
        grade = request.POST.get('grade')
        score = float(request.POST.get('score'))
        bonus_score = float(request.POST.get('bonus_score'))

        path = os.path.abspath(os.path.dirname(__name__))
        model = pd.read_pickle(path+"/new_model.pickle")

        # Make prediction
        result = model.predict([[month, grade, score, bonus_score]])
        mappedWords = {1:'Free Trip',2:'Free Meal',3:'Breakfast/Lunch With Leadership',4:'Social Media Appreciation',5:'Discount Voucher',6:'Appreciation Certificate',7:'Work Hard. Try Again!'}
        classification = mappedWords[result[0]]

        predResults.objects.create(month = month, grade = grade, score = score,
                                   bonus_score = bonus_score, result=classification,e_no=emp_no)
        users = User.objects.all()
        emp_details = []
        for i in range(0,len(users)):
            if users[i].username != 'admin':
                emp_details.append({'emp_no':users[i].username[4:],'emp_name':users[i].first_name+' '+users[i].last_name})

        return render(request,'ML.html',{'result': classification, 'month': month,
                             'grade': grade, 'score': score,'users':emp_details, 'bonus_score': bonus_score,'e_no':emp_no })
    users = User.objects.all()
    emp_details = []
    for i in range(0,len(users)):
        if users[i].username != 'admin':
            emp_details.append({'emp_no':users[i].username[4:],'emp_name':users[i].first_name+' '+users[i].last_name})

    return render(request, 'ML.html', {'result':'', 'score':0,'e_no':0,'bonus_score':0,'users':emp_details,'grade':'','month':0})

def getDataByEno(request):
    e_no = request.GET.get('e_no')
    data = Monthly.objects.filter(e_no=e_no).first()
    # print(data.grade)
    return JsonResponse({'grade':data.grade,'month':data.month,'score':data.bonus,'bonus_score':data.bonus_score})

def getDataByMonth(request):
    e_no = request.GET.get('e_no')
    month = request.GET.get('month')
    data = Monthly.objects.filter(e_no=e_no,month=month).first()
    # print(data.grade)
    return JsonResponse({'grade':data.grade,'score':data.bonus,'bonus_score':data.bonus_score})



def createUsers(request):
    monthly = Monthly.objects.all()
    e_no_check = []
    for i in range(0,len(monthly)):
        print(monthly[i].e_name)
        check = e_no_check.count(monthly[i].e_no)
        if check == 0:
            e_no_check.append(monthly[i].e_no)
            name = monthly[i].e_name.split(' ')
            first_name = name[0]
            last_name = name[1]
            username = 'user'+ monthly[i].e_no
            password = 'pass'+monthly[i].e_no
            User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password)

def changePassword(request):
    if request.method == 'POST':
        current_password = request.POST.get('current_password')
        new_password = request.POST.get('new_password')
        new_password_check = request.POST.get('new_password_again')
        userID = request.user.id

        user = User.objects.get(id=userID)
        
        if user.check_password(current_password):
            if new_password == new_password_check:
                user.set_password(new_password)
                messages.success(request,'Password changed !')
            else:
                messages.warning(request,'Password do not match')
                
        else:
            messages.warning(request,'Current password is not corrent. Please try again')
        return redirect('changePassword')
    else:
        form = ChangePasswordForm()
        return render(request, 'changePassword.html', {'form': form})
        # Error Code

def index(request):
    monthly = Monthly.objects.all()
    return render(request,'index.html',{'table':monthly})
def usersDataMonthly(request):
    table = Monthly.objects.all()
    return render(request,'users_monthly.html',{'table':table})

def usersDataYearly(request):
    table = Yearly.objects.all()
    return render(request,'users_yearly.html',{'table':table})

def top20ByScore(list1, N=20):
    final_list = []
  
    for i in range(0, N): 
        max1 = 0
          
        for j in range(len(list1)):     
            if list1[j] > max1:
                max1 = list1[j]
                  
        list1.remove(max1)
        final_list.append(max1)
    l = sorted(final_list,reverse=True)
    return l

def usersMonthlyPerformance(request):
    table = Monthly.objects.all()
    data = []
    top_20 = []
    for i in range(0,len(table)):
        for j in range(1,13): 
            if table[i].month == str(j):
                bonus = (int(table[i].present)*5) - (int(table[i].absent)*5) + (int(table[i].no_roaster_deviation)*5) - (int(table[i].roaster_deviation)*5) + (float(table[i].overtime_hours)*5) + (int(table[i].training_session)*15) - (int(table[i].safety_risk_rating))
                # bonus_score= (float(table[i].total_working_hours))+ float(bonus)
                data.append({"emp_no": table[i].e_no, "bonus" : bonus, "month" : j})
    
    current_month = datetime.now().month
    bonus_list = []
    emp_no_list = []
    for j in data:
        if j["month"] == current_month:
            bonus_list.append(j["bonus"])
            emp_no_list.append(j["emp_no"])
    top20 = top20ByScore(bonus_list)
    score = []
    emp_no = []
    for j in top20:
        for i in data:
            if i["bonus"] == j and j not in score:
                score.append(j)
                emp_no.append(i["emp_no"])

                # top_20.append({"emp_no": j["emp_no"], "bonus" : j["bonus"], "month" : j["month"]})

            # labels.append(j["emp_no"])
            # score.append(j["bonus"])
    
    # print(type(current_month))
    months = [{"number":1,"value":"January"},{"number":2,"value":"Febuary"},{"number":3,"value":"March"},{"number":4,"value":"April"},{"number":5,"value":"May"},{"number":6,"value":"June"},{"number":7,"value":"July"},{"number":8,"value":"August"},{"number":9,"value":"September"},{"number":10,"value":"October"},{"number":11,"value":"November"},{"number":12,"value":"December"}]
    
    return render(request,'users_monthly_performance.html',{'score':score,'emp_no':emp_no, "month":current_month, "months":months})

def changeMonth(request):
    month = request.GET.get('month')
    # print(month)
    table = Monthly.objects.all()
    data = []
    top_20 = []
    for i in range(0,len(table)):
        for j in range(1,13): 
            if table[i].month == str(j):
                bonus = (int(table[i].present)*5) - (int(table[i].absent)*5) + (int(table[i].no_roaster_deviation)*5) - (int(table[i].roaster_deviation)*5) + (float(table[i].overtime_hours)*5) + (int(table[i].training_session)*15) - (int(table[i].safety_risk_rating))
                data.append({"emp_no": table[i].e_no, "bonus" : bonus, "month" : j})
    
    current_month = month
    bonus_list = []
    emp_no_list = []
    for j in data:
        if j["month"] == int(current_month):
            bonus_list.append(j["bonus"])
            emp_no_list.append(j["emp_no"])
    # print(bonus_list)
    top20 = top20ByScore(bonus_list)
    score = []
    emp_no = []
    for j in top20:
        for i in data:
            if i["bonus"] == j and j not in score:
                score.append(j)
                emp_no.append(i["emp_no"])

    return JsonResponse({'score':score,'emp_no':emp_no})

def usersYearlyPerformance(request):
    table = Yearly.objects.all()
    data = []
    top_20 = []
    for i in range(0,len(table)):
       
        bonus = (int(table[i].present)*5) - (int(table[i].absent)*5) + (int(table[i].no_roaster_deviation)*5) - (int(table[i].roaster_deviation)*5) + (float(table[i].overtime_hours)*5) + (int(table[i].training_session)*15) - (int(table[i].safety_risk_rating))
        data.append({"emp_no": table[i].e_no, "bonus" : bonus})

    bonus_list = []
    emp_no_list = []
    for j in data:
        bonus_list.append(j["bonus"])
        emp_no_list.append(j["emp_no"])
    top20 = top20ByScore(bonus_list)
    score = []
    emp_no = []
    for j in top20:
        for i in data:
            if i["bonus"] == j:
                score.append(j)
                emp_no.append(i["emp_no"])

    
    return render(request,'users_yearly_performance.html',{'score':score,'emp_no':emp_no})

def userYearlyPerformanceByID(request, value):
    table = Yearly.objects.filter(e_no=value[4:])
    
    for i in table:       
        bonus = (int(i.present)*5) - (int(i.absent)*5) + (int(i.no_roaster_deviation)*5) - (int(i.roaster_deviation)*5) + (float(i.overtime_hours)*5) + (int(i.training_session)*15) - (int(i.safety_risk_rating))

    return render(request,'user_yearly_performance.html',{"score":bonus,'emp_no':value[4:]})

def userMonthlyPerformanceByID(request, value):
    table = Monthly.objects.filter(e_no=value[4:])
    data = []
    
    for i in table:
        for j in range(1,13): 
            if i.month == str(j):
                bonus = (int(i.present)*5) - (int(i.absent)*5) + (int(i.no_roaster_deviation)*5) - (int(i.roaster_deviation)*5) + (float(i.overtime_hours)*5) + (int(i.training_session)*15) - (int(i.safety_risk_rating))
                data.append(bonus)
    
    
    
    
    return render(request,'user_monthly_performance.html',{"score":data})

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'User Created')
            
            return redirect('usersignup')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

