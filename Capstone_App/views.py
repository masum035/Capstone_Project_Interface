from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from Capstone_App.forms import Video_form
from Capstone_App.models import *

import torch
import numpy as np
import cv2
from time import time

class ObjectDetection:

    def __init__(self, videofile, out_file):
        self.videofile = videofile
        self.model = self.load_model()
        self.classes = self.model.names
        self.out_file = out_file
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("\n\nDevice Used:", self.device)

    def get_video_from_url(self):
        return cv2.VideoCapture(cv2.samples.findFile("."+self.videofile))

    def load_model(self):
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)

        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.2:
                x1, y1, x2, y2 = int(row[0] * x_shape), int(row[1] * y_shape), int(row[2] * x_shape), int(
                    row[3] * y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def __call__(self):
        player = self.get_video_from_url()
        # assert player.isOpened()
        x_shape = int(player.get(cv2.CAP_PROP_FRAME_WIDTH))
        y_shape = int(player.get(cv2.CAP_PROP_FRAME_HEIGHT))
        four_cc = cv2.VideoWriter_fourcc(*"MJPG")
        out = cv2.VideoWriter(self.out_file, four_cc, 20, (x_shape, y_shape))
        while True:
            start_time = time()
            ret, frame = player.read()
            if not ret:
                break
            results = self.score_frame(frame)
            frame = self.plot_boxes(results, frame)
            end_time = time()
            fps = 1 / np.round(end_time - start_time, 3)
            print(f"Frames Per Second : {fps}")
            out.write(frame)



global_context = {}


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
    lastvideo = Video.objects.last()

    if request.method == "POST":
        form = Video_form(data=request.POST or None, files=request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request=request, message="file Uploaded successfully.")
    else:
        form = Video_form()

    context = {
        'uploaded_file': lastvideo,
        'form': form,
    }

    return render(request, 'start_working.html', context=context)


def result_section(request):
    context = {
    }
    lastvideo = Video.objects.last()
    detection = ObjectDetection(lastvideo.video.url, "media/output.avi")
    detection()
    global_context = {'video_file_found': lastvideo, }
    return render(request, 'result_section.html', context=global_context)


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


def contact_section(request):
    context = {
    }
    return render(request, 'contact.html', context=context)


