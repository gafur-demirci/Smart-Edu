from django.shortcuts import render, redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_login(request):
    # gelen method POST ise yani giriş yapılmak isteniyorsa
    if request.method == 'POST':
        # login formumuza işlemi yönlendireceğimiz form variable ı tanımlıyoruz
        form = LoginForm(request.POST)
        # eğer form doğru doldurulmuş ise
        if form.is_valid():
            # kullanıcıdan ilgili alanları cleaned_data dict ile alıyoruz ve bu bilgiler 
            # ile user variable ını authenticate ile oluşturuyoruz
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request ,username= username, password= password)
            # eğer ilgli user varsa yani None değil ise
            if user is not None:
                # ve eğer aktif statusünde ise
                if user.is_active:
                    # login ile user giriş yapıyor ve anasayfaya geri yönlendiriliyor.
                    login(request, user)
                    return redirect('index')
                # user active değil ise bir mesaj göstereceğiz
                else:
                    messages.info(request, 'Disabled Account')
            # user yoksa yani username veya password yanlış girilmiş ise
            else:
                messages.info(request, 'Check Your Username or Password')
    # eğer post methodu gelmemişse                
    else:
        # boş login formu göndermek için oluşturulan variable
        form = LoginForm()
    return render(request, 'login.html', {'form' : form})


def user_register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account has been created, You can LOGIN')
            return redirect('login')
    
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form' : form})

def user_logout(request):
    logout(request)
    return redirect('index')

@login_required(login_url='login')
def user_dashboard(request):
    current_user = request.user
    return render(request, 'dashboard.html')
