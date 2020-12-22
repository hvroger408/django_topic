from django.shortcuts import render, redirect
from wikiapp import models, forms
from django.contrib.sessions.models import Session
from django.contrib import messages

# Create your views here.

def index(request, pid=None, del_pass=None):
    if 'username' in request.session:
        username = request.session['username']
        useremail = request.session['useremail']
    return render(request, 'index.html', locals())

def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            try:
                user = models.User.objects.get(name = login_name)
                if user.password == login_password:
                    request.session['username'] = user.name
                    request.session['useremail'] = user.email
                    return redirect('/')
                else:
                    messages.add_message(request, messages.WARNING, "密碼錯誤，請再檢查一次")
            except:
                messages.add_message(request, messages.WARNING, "找不到使用者")
        else:
            messages.add_message(request, messages.WARNING, "請檢查輸入的欄位內容")
    else:
        login_form = forms.LoginForm()

    return render(request, 'login.html', locals())

def logout(request):
    if 'username' in request.session:
        Session.objects.all().delete()
        return redirect('index')

def register(request):
    user = models.User.objects.all()
    try:
        user_id = request.POST['user_id']
        user_email = request.POST['user_email']
        user_pass = request.POST['user_pass']
        user_phone = request.POST['user_phone']
        user_birth = request.POST['user_birth']
        user_sex = request.POST['user_sex']
    except:
        user_id = None
        messages.add_message(request, messages.SUCCESS, '請完整填寫')
    if user_id != None:
        user = models.User.objects.create(name=user_id, email=user_email, password=user_pass, phone=user_phone, birth=user_birth, sex=user_sex)
        messages.add_message(request, messages.SUCCESS, '註冊完成')
        user.save()
    return render(request, 'register.html', locals())