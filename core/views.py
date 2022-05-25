import os
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
# from core.forms import SignUpForm, LoginForm, AddState
from django.contrib import messages
from core.models import State, Pollution
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
import pandas as pd
from django.contrib.auth.models import User
from django.core import serializers
from django.db.models import Avg, Count
from django.http import JsonResponse
from django.http import HttpResponse
import json as simplejson
from sklearn import metrics
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
# from xgboost im
from sklearn.preprocessing import LabelEncoder

# this method is used for make prediction of user input using ajax call.


def makePrediction(request):
    Data = request.POST["dataset"]
    dict_data = simplejson.loads(Data)

    prepare_dataset = Pollution.objects.values('City', 'Pm2', 'Pm10', 'No', 'No2', 'Nox', 'Nh3', 'Co', 'So2',
                                               'O3', 'Benzene', 'Toluene', 'Xylene', 'Aqi', 'Air_quality')
    dataset = pd.DataFrame(prepare_dataset)
    le = LabelEncoder()
    dataset['City'] = le.fit_transform(dataset['City'].astype(str))
    dataset['Air_quality'] = le.fit_transform(
        dataset['Air_quality'].astype(str))
    y = dataset["Air_quality"]
    x = dataset[['City', 'Pm2', 'Pm10', 'No', 'No2', 'Nox', 'Nh3', 'Co', 'So2',
                 'O3', 'Benzene', 'Toluene', 'Xylene', 'Aqi']]
    X_train, X_test, y_train, y_test = train_test_split(
        x, y, test_size=0.3, random_state=0)
    # prediction started
    gbc = XGBClassifier(learning_rate=0.01, n_estimators=100, max_depth=1,
                        min_child_weight=6, subsample=0.8, seed=13)
    gbc.fit(X_train, y_train)
    pred = gbc.predict(X_test)
    final_test = pd.DataFrame({"City": dict_data["cityName"], "Pm2": [float(dict_data['Pm2'])], "Pm10": [float(dict_data['Pm10'])], "No": [float(dict_data["No"])], "No2": [float(dict_data["No2"])], "Nox": [float(dict_data["Nox"])], "Nh3": [float(dict_data["Nh3"])], "Co": [float(dict_data["Co"])], "So2": [float(dict_data["So2"])],
                               "O3": [float(dict_data["O3"])], "Benzene": [float(dict_data["Benzene"])], "Toluene": [float(dict_data["Toluene"])], "Xylene": [float(dict_data["Xylene"])], "Aqi": [float(dict_data["Aqi"])]})

    final_output = gbc.predict(final_test)
    final_output = int(final_output[0])
    result = {0: "Good", 1: "Moderate", 2: "Poor",
              3: "Satisfactor", 4: "Severe", 5: "Very Poor"}

    data = {"Output": result[final_output]}
    return JsonResponse({"data": data})
    # nameSate = dict_data["stateinput"]
    # print(nameSate)
    # prepare_dataset = Pollution.objects.filter(SUBDIVISION=dict_data['stateinput']).values("ANNUAL","Jan_Feb","Mar_May","Jun_Sep","Oct_Dec");
    # dataset = pd.DataFrame(prepare_dataset)
    # X = dataset[['Jan_Feb', 'Mar_May', 'Jun_Sep','Oct_Dec']]
    # Y = dataset['ANNUAL'].values.reshape(-1,1)
    # X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.20,random_state=1)
    # regr = LinearRegression()
    # regr.fit(X_train, Y_train)
    # y2_pred = regr.predict(X_test)
    # final_test = pd.DataFrame({"Jan_Feb":[int(dict_data['jan_feb'])], "Mar_May":[int(dict_data['mar_may'])], "Jun_Sep":[int(dict_data["jun_sep"])], "Oct_Dec":[int(dict_data["oct_dec"])]})
    # print(final_test)
    # final_output = regr.predict(final_test)
    # print(final_output[0][0])
    # data = {"final_output":final_output[0][0],"mean_square_error" : metrics.mean_squared_error(Y_test, y2_pred), "root_mean_square_error" : np.sqrt(metrics.mean_squared_error(Y_test, y2_pred))}*/


# Home
def home(request):
    if request.user.is_authenticated:
        posts = State.objects.all()
        pol = Pollution.objects.all()
        city_names = ['Ahmedabad', 'Aizawl', 'Amaravati', 'Amritsar', 'Bengaluru', 'Bhopal',
                      'Brajrajnagar', 'Chandigarh', 'Chennai', 'Coimbatore', 'Delhi', 'Ernakulam',
                      'Gurugram', 'Guwahati', 'Hyderabad', 'Jaipur', 'Jorapokhar', 'Kochi', 'Kolkata',
                      'Lucknow', 'Mumbai', 'Patna', 'Shillong', 'Talcher', 'Thiruvananthapuram',
                      'Visakhapatnam']

        context = {
            'posts': posts,
            "home": "current",
            'city_names': city_names
        }
        return render(request, 'core/home.html', context)
    else:
        return redirect('/')


# about
def about(request):
    return render(request, 'core/about.html', {"about": "current"})


# Contact
def contact(request):
    return render(request, 'core/contact.html', {"contact": "current"})


# dashboard
def dashboard(request):
    # if request.user.is_authenticated:
    posts = State.objects.all()
    user = request.user
    gps = user.groups.all()
    full_name = user.get_full_name()
    context = {
        'posts': posts,
        'fullname': full_name,
        'groups': gps,
        "dashboard": "current"

    }
    return render(request, 'core/dashboard.html', context)
    # else:
    #     return redirect("/login/")


# LOGOUT
def user_logout(request):
    logout(request)
    return redirect("/")


# Signup
# Signup
def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        print(username,email,pass1)
        # if pass1==pass2:
        if User.objects.filter(username=username).exists():
            messages.success(request, "This user is already taken")

        else:
            user = User(username=username, email=email, password=pass1)
            user.save()
            messages.success(
                request, "Congratulation Your ID has been created !!")
            return redirect('/')

        # else:
        #     messages.error(request,"Password did not matched !!")

    context = {
        "signup": "current"
    }
    return render(request, 'core/login_style.html', context)


def user_login(request):
    # if not request.user.is_authenticated :: means user is not logged in so the else part will be executed
    if request.method == "POST":
        print("er:-", request)
        print("form is executed in post request")
        username = request.POST.get('loginusername')
        print(username)
        password = request.POST.get('passwordinput')
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            messages.error(request, "You have logged in successfully")
            return JsonResponse({"data": "Yes"})
        else:
            print("wrong credentials")
            messages.error(request, "Invalid username or password")
            return JsonResponse({"data": "No"})
    else:
        print("it is executed in get request")

        return render(request, 'core/login_style.html')
# def user_signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             messages.success(request, "Congratulations Your ID is Created")
#             user = form.save()
#             group = Group.objects.get(name='Author')
#             user.groups.add(group)
#     else:
#         form = SignUpForm()

#     context = {
#         'signup': form,
#         # "signup": "current"
#     }
#     return render(request, 'core/login_style.html', context)


# # Login
# def user_login(request):
#     print("**************login executed")
#     # if not request.user.is_authenticated :: means user is not logged in so the else part will be executed
#     if request.method == "POST":
#         # form = LoginForm(request=request, data=request.POST)
#         # if form.is_valid():
#             uname = form.cleaned_data['username']
#             upass = form.cleaned_data['password']
#             user = authenticate(username=uname, password=upass)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, "Logged in Successfuly")
#                 return redirect("/home")

#     else:
#         form = LoginForm()
#     context = {
#         'form': form,
#         "login": "current"
#     }
#     return render(request, 'core/login_style.html', context)
#     # else:
#     #     # this will execute when the user is already logged in
#     #     return render(request,'core/login.html')

# # add new post
# def add_post(request):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             form = AddState(request.POST, request.FILES)
#             if form.is_valid():
#                 title = form.cleaned_data['title']
#                 desc = form.cleaned_data['desc']
#                 pic = form.cleaned_data['pic']
#                 pst = State(title=title, desc=desc, pic=pic)
#                 pst.save()
#                 messages.success(request, "Post is Added Successfully")
#                 form = AddState()

#         else:
#             form = AddState()
#         img = State.objects.all()
#         context = {
#             'form': form,
#             'img': img
#         }
#         return render(request, 'core/addpost.html', context)
#     else:
#         return redirect('/login/')


# update post

# def update_post(request, id):
#     if request.user.is_authenticated:
#         if request.method == "POST":
#             pi = State.objects.get(pk=id)
#             form = AddState(request.POST, request.FILES, instance=pi)
#             if form.is_valid():
#                 form.save()
#                 messages.success(request, "Post Updated Successfully")

#         else:
#             pi = State.objects.get(pk=id)
#             form = AddState(instance=pi)
#         context = {
#             'form': form,
#             "pi": pi
#         }
#         return render(request, 'core/updatepost.html', context)
#     else:
#         return redirect('/login/')


# delete post
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            pi = State.objects.get(pk=id)
            pi.delete()
            messages.success(request, "One Post is Deleted")
        return redirect("/dashboard/")
    else:
        return redirect('/login/')


def detailsPost(request, id):
    if request.user.is_authenticated:
        pi = State.objects.get(pk=id)
        return render(request, "core/detail_post.html", {"post": pi})

# os.chdir("C:\\Users\\AQIB\\Downloads\\ML")
# df = pd.read_csv("city_day.csv")
# df1 = df.copy()
# df1['PM2.5']=df1['PM2.5'].fillna((df1['PM2.5'].median()))
# df1['PM10']=df1['PM10'].fillna((df1['PM10'].median()))
# df1['NO']=df1['NO'].fillna((df1['NO'].median()))
# df1['NO2']=df1['NO2'].fillna((df1['NO2'].median()))
# df1['NOx']=df1['NOx'].fillna((df1['NOx'].median()))
# df1['NH3']=df1['NH3'].fillna((df1['NH3'].median()))
# df1['CO']=df1['CO'].fillna((df1['CO'].median()))
# df1['SO2']=df1['SO2'].fillna((df1['SO2'].median()))
# df1['O3']=df1['O3'].fillna((df1['O3'].median()))
# df1['Benzene']=df1['Benzene'].fillna((df1['Benzene'].median()))
# df1['Toluene']=df1['Toluene'].fillna((df1['Toluene'].median()))
# df1['Xylene']=df1['Xylene'].fillna((df1['Xylene'].median()))
# df1['AQI']=df1['AQI'].fillna((df1['AQI'].median()))
# df1['AQI_Bucket']=df1['AQI_Bucket'].fillna('Moderate')
# arr = df1.to_numpy()
# list_arr = arr.tolist()
# for row in list_arr:
#     c = Pollution(City=row[0].upper(), Date=row[1], Pm2=row[2], Pm10=row[3], No=row[4], No2=row[5], Nox=row[6],
#     Nh3=row[7], Co=row[8], So2=row[9], O3=row[10], Benzene=row[11], Toluene=row[12], Xylene=row[13], Aqi=row[14], Air_quality=row[15])
#     c.save()
