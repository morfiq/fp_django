from rest_framework.views import APIView

# from .serializers import userDataSerializers
from .serializers import FileUploadSerializer
from .serializers import SaveFileSerializer
from .models import fpuserdata
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework import status, generics
import io, csv, pandas as pd
import json
import psycopg2
# Create your views here.
# class AllData(APIView):
#     def get(self, request):
#         data = UserData.objects.all()
#         serialize = userDataSerializers(data, many=True)
#         return Response(serialize.data)
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import RegisteredUser
from .forms import RegisterForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

class UploadFileView(generics.CreateAPIView):
    serializer_class = FileUploadSerializer
    serializer_class2 = SaveFileSerializer
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        file = serializer.validated_data['file']
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # serializer.save()
        file_data = json.load(file)


        # Establishing the connection
        conn = psycopg2.connect(
            database="fp_db", user='postgres', password='inman', host='127.0.0.1', port='5432'
        )
        # Setting auto commit false
        conn.autocommit = True
        print("==================")
        print('connected')
        # Creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # Preparing SQL queries to INSERT a record into the database.
        # cursor.execute("""SELECT table_name FROM information_schema.tables
        #        WHERE table_schema = 'public'""")
        # for table in cursor.fetchall():
        #     print(table)
        # cursor.execute("""SELECT * FROM information_schema.columns WHERE table_schema = 'public' AND table_name = 'fp_app_fpuserdata'""")
        # for table in cursor.fetchall():
        #     print(table)
        for i in file_data:
            print('data:' + str(i))
            # serializer2 = self.serializer_class2(data=i)
            # serializer2.is_valid(raise_exception=True)
            # serializer2.save()
            cursor.execute('''INSERT INTO fp_app_fpuserdata(userid, id1, title, body) VALUES (%s,%s,'%s','%s');'''%(i['userId'],i['id'],i['title'],i['body']))
        #     print(str(i))
            # UserData.objects.create(name='Rufus', data=i)
        # for i in file_data:
        #     print(str(i['id']))
        # serializer2
        conn.commit()
        conn.close()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)
def app_homepage(request):
    # try:
    #     if usrnme:
    #         userdetails = {'username': usrnme}
    #         return render(request, "loggedin.html", userdetails)
    # except NameError:
    #     return render(request, "homepage.html")
    return render(request, "homepage.html")

def contact_us(request):
    try:
        if usrnme:
            return render(request, "contactUs.html")
    except NameError:
        return render(request, "contactUs.html")

#
# class UserListView(ListView):
#     model = RegisteredUser
#     template_name = "user_data.html"
#     context_object_name = 'alldata'
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully")
            return redirect("signin")
    else:
        form = RegisterForm()
        user_info = {'form': form}
        return render(request, "register.html", user_info)


def signin(request):
    global usrnme
    if request.method == 'POST':
        usrnme = request.POST.get('username')
        psswrd = request.POST.get('pswd')
        print("==============")
        print(usrnme)
        print(psswrd)
        try:
            user = RegisteredUser.objects.get(name=usrnme)
            if usrnme == user.name and psswrd == user.password:
                return redirect("loggedin")
            else:
                messages.info(request, "Incorrect password")
                return redirect("signin")
        except ObjectDoesNotExist:
            messages.info(request, "The user does not exist")
            return redirect("signin")

    else:
        return render(request, "signin.html")


def loggedin(request):

    # image_file = RegisteredUser.objects.get(name=usrnme)

    # pic_path = str(image_file.profilePic)
    # full_pic_path = 'media/' + pic_path
    userdetails = {'username': usrnme}
    return render(request, "loggedin.html", userdetails)

def all_data(request):
        # global usrnme
        usrnme = request.POST.get('username')
        psswrd = request.POST.get('pswd')
    # if request.method == 'POST':
    #     prod_list = request.POST.getlist('products')
    #     prod_str = ",".join(prod_list)
        all_data = fpuserdata.objects.values_list('userid', 'id1', 'title', 'body')
        nom_columnes = ['userId', 'id', 'title', 'body']
        userdetails = {'username': usrnme, 'table_data': all_data, 'nom_columnes' : nom_columnes}
        return render(request, "fpdata.html", userdetails)
        # messages.success(request, "Order created successfully: " + prod_str)


def logout(request):
    global usrnme
    del usrnme
    return render(request, "logout.html")


class UserListView(ListView):
    model = RegisteredUser
    template_name = "user_data.html"
    context_object_name = 'alldata'


class UserDetailView(DetailView):
    model = RegisteredUser


class UserCreateView(CreateView):
    model = RegisteredUser
    form_class = RegisterForm


class UserUpdateView(UserPassesTestMixin, UpdateView):
    model = RegisteredUser
    form_class = RegisterForm

    def test_func(self):
        if self.request.user.is_active:
            return True
        else:
            return False


class UserDeleteView(UserPassesTestMixin, DeleteView):
    model = RegisteredUser
    success_url = '/userlist'

    def test_func(self):
        if self.request.user.is_active:
            print(self.request.user)
            return True
        else:
            return False

        all_entries = Entry.objects.all()