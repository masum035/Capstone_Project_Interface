from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from Capstone_App.models import *

# @login_required(login_url='/signin/')
def error(request, anything=None):  # template missing
    # baseEverywhere(request=request)
    context = {
    }
    return render(request, 'error_404.html', context=context)


def signUp(request):
    context = {}
    if request.POST.get('signup'):
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('pass')
        user_exists = sign_up.objects.filter(email__exact=b,
                                             password__exact=c,
                                             name__exact=a)
        if user_exists:
            messages.error(request, message="User already exists . Please Log In")
        else:
            signup = sign_up()
            signup.email = b
            signup.password = c
            signup.name = a
            signup.save()
            messages.success(request=request, message='Successfully Signed Up!! Now Log in please.')
            return render(request=request, template_name='sign_in.html', context=context)
    else:
        messages.warning(request=request, message="Something went wrong")
    return render(request=request, template_name='sign_up.html', context=context)


def loggin(request):
    if request.POST.get('signin'):
        namee = request.POST.get('your_name')
        passlog = request.POST.get('your_pass')
        if sign_up.objects.filter(name__exact=namee).exists():
            x = sign_up.objects.filter(password__exact=passlog).exists();
            if x:
                messages.success(request=request, message=f'WelCome Back {namee} !!')
                # return render(request, 'contact.html', context=context)
                # Ekhane redirect korte hobe
                # Home2(request=request)
            else:
                messages.error(request=request, message='Invalid LogIn attempt!!!')
        else:
            messages.error(request=request, message=f'Username: {namee} not found, try again.')
    return render(request=request, template_name='sign_in.html')

def index_section(request):
    context = {
    }
    return render(request, 'index.html', context=context)

def start_working(request):
    if request.method == 'POST':
        file = request.FILES['file'].read()
        fileName = request.POST['filename']
        existingPath = request.POST['existingPath']
        end = request.POST['end']
        nextSlice = request.POST['nextSlice']

        if file == "" or fileName == "" or existingPath == "" or end == "" or nextSlice == "":
            res = JsonResponse({'data': 'Invalid Request'})
            return res
        else:
            if existingPath == 'null':
                path = 'media/' + fileName
                with open(path, 'wb+') as destination:
                    destination.write(file)
                FileFolder = File()
                FileFolder.existingPath = fileName
                FileFolder.eof = end
                FileFolder.name = fileName
                FileFolder.save()
                if int(end):
                    res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': fileName})
                else:
                    res = JsonResponse({'existingPath': fileName})
                return res

            else:
                path = 'media/' + existingPath
                model_id = File.objects.get(existingPath=existingPath)
                if model_id.name == fileName:
                    if not model_id.eof:
                        with open(path, 'ab+') as destination:
                            destination.write(file)
                        if int(end):
                            model_id.eof = int(end)
                            model_id.save()
                            res = JsonResponse({'data': 'Uploaded Successfully', 'existingPath': model_id.existingPath})
                        else:
                            res = JsonResponse({'existingPath': model_id.existingPath})
                        return res
                    else:
                        res = JsonResponse({'data': 'EOF found. Invalid request'})
                        return res
                else:
                    res = JsonResponse({'data': 'No such file exists in the existingPath'})
                    return res

    return render(request, 'start_working.html')

def result_section(request):
    context = {
    }
    return render(request, 'result_section.html', context=context)

def about_us(request):
    context = {
    }
    return render(request, 'about_us.html', context=context)

def faq_section(request):
    context = {
    }
    return render(request, 'faq_section.html', context=context)

def workplan_section(request):
    context = {
    }
    return render(request, 'workPlan.html', context=context)