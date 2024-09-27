from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import S_login , S_signup
from quiz.models import studentdetails, Subject, Question, Topic, result
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def home(request):
    return render(request, "homepage.html")


# def homepage(request):
#     if request.method == 'POST':
#         n1 = request.POST.get('sname')
#         n2 = request.POST.get('admno')
#         data = {
#             'fname': n1,
#             'admno': n2,
#         }
#         return render(request, "test2.html", data)



# def welcome(request):
#     return render(request, "studentpage2.html")


def Student_Login(request):
    try:
        if request.user.is_authenticated:
            return redirect("/quizpage/")
        if request.method=='POST':   
            # print("HELLO 1")         
            form_data=S_login(request.POST)
            if form_data.is_valid():
                admno = form_data.cleaned_data["admno"].upper()
                passwd = form_data.cleaned_data["password"]
                user = authenticate(request, username=admno,password=passwd)

                if user != None: 
                    auth_login(request, user)
                    if request.user.last_name=="Not Updated":
                        return redirect("/section/")
                    messages.success(request, "Login Successful!")
                    return redirect("quizpage")
                # # print(sname, admno)
                # if studentdetails.objects.filter(Admission_No__iexact = admno) and studentdetails.objects.get(Admission_No = admno).password== passwd:
                #     # return HttpResponseRedirect("/quizpage/")
                #     # return redirect("quizpage",  {"admno": admno} )
                #     print(admno)
                #     response = quizpage(request, post_data={"admno": admno})
                #     return response
                elif not User.objects.filter(username=admno).exists():
                    message="You are a new user please Sign-up to continue."
                    messages.error(request, message)
                    return HttpResponseRedirect(f"/sign-up")
                else:
                    messages.error(request, "wrong Password! please try again!!")
                    return HttpResponseRedirect(f"/Student_Login")
                    
            else:
                print(form_data.errors)

        else:
            
            form=S_login()
            data={"form":form, "message": "Student-Login"}
            return render(request, "studentpage.html",data)
    except:
        print('except box\n\n')
   
def signup(request):
    try:
        if request.user.is_authenticated:
            return redirect("/quizpage/")
        if request.user.is_authenticated and request.user.last_name=="Not Updated":
            return redirect("/quizpage/")
        if request.method=='POST':          
            form_data=S_signup(request.POST)
            if form_data.is_valid():
                sname = form_data.cleaned_data["name"].upper()
                admno = form_data.cleaned_data["admno"].upper()
                section=form_data.cleaned_data["section"].upper()
                passwd = form_data.cleaned_data["password"]
                repasswd= form_data.cleaned_data["repassword"]
                print(sname, admno)
                if  not admno[2:4]=="GA":
                    message.error(request, "please enter correct admission number")
                    return redirect("/")
                if User.objects.filter(username=admno).exists():
                    message= "Oops! You are already an user! Please Sign-in to continue!"
                    print(message)
                    messages.error(request, message)
                    return HttpResponseRedirect(f"/Student_Login")
            
                elif not User.objects.filter(username=admno).exists(): 
                    if passwd==repasswd:
                        user = User.objects.create_user(username=admno,password=passwd)
                        user.first_name= sname
                        user.last_name= section
                        user.save()
                        messages.success(request, "Sign-up successful! Please login to continue.")     
                        # newstudent=studentdetails.objects.create(Student_name=sname, Admission_No=admno, password=passwd)
                        return HttpResponseRedirect("/Student_Login/")  # Change the URL as needed
                    else:
                        return redirect("/")
        else:
            form=S_signup()
            message="Student signup"
            data={"form":form,"message": message }
            return render(request, "studentpage2.html",data)
    except:
        print('except box')

def section(request):
    try:
        if request.user.is_authenticated:
            print(request.method)
            if request.method == "POST":
                section=  request.POST.get("section")
                print(section)
                request.user.last_name=section
                request.user.save()
                return redirect("/quizpage/")
            elif request.method== "GET":
                return render(request, "section.html")
            else:
                return redirect("/")
        else:
            return redirect("Student_Login")
    except Exception as e:
        print("except box", str(e))

def quizpage(request):

    # if request.method == "POST":
    #     admno= post_data.get("admno")
    #     if admno==None:
    #         return HttpResponseRedirect("/")
    #     else:
    #         name=studentdetails.objects.filter(Admission_No=admno).values("Admission_No","Student_name")

    if request.user.is_authenticated:
        name=request.user.first_name
        subjects=Subject.objects.all().order_by('name')
        topics=Topic.objects.all().order_by("subject_id","name")
        content={"subjects": subjects, "topics": topics,"name":name}
        return render(request, "quizpage.html",content)
    else:
        return redirect("/Student_Login/")


def quiz(request, id):
    try:
        if request.user.is_authenticated:
            if request.method == "POST":
                # Get the submitted answers from the request
                submitted_answers = {key: value for key, value in request.POST.items() if key.isdigit()}
                print(submitted_answers)
                # Retrieve the correct answers for the questions in the current quiz
                correct_answers = Question.objects.filter(topic_id=id).values('id', 'correct_answer')
                print(correct_answers)
                score=0
                num=len(correct_answers)
                for answer in correct_answers:
                    question_id = str(answer['id'])
                    correct_answer = answer['correct_answer'][-1]

                    # Check if the submitted answer matches the correct answer
                    if submitted_answers.get(question_id) == correct_answer:
                        score += 1
                admission=request.user
                name=request.user.first_name
                section=request.user.last_name
                topic = get_object_or_404(Topic, id=id)
                a= result.objects.create(admission_no=admission,name=name,section=section, topic=topic, score=score)
                print(a)
                messages.info(request, f"Paper submitted! Your score is {score}/{num}")
                auth_logout(request)
                # Redirect to the submission page with the calculated score
                return HttpResponseRedirect(f"/about/")

            elif request.method == "GET":
                # Render the quiz form
                topic = Topic.objects.get(id=id)
                questions = Question.objects.filter(topic_id=id)
                context = {"questions": questions, "topic": topic}
                return render(request, "quiz.html", context)

            else:
                # Handle other request methods (e.g., PUT, DELETE)
                print(request.method)
                print("NOT GET or POST")
        else:
            return redirect("/quizpage/")
        
    except Exception as e:
        print("Exception occurred:", str(e))



    # try:
    #     if request.method == "POST":
    #         score = request.POST.get("score")
    #         if score!=0:
    #             HttpResponseRedirect(f"/submit/?score={score}")
    #     elif request.method == "GET":
    #         topic=Topic.objects.get(id=id)
    #         questions=Question.objects.filter(topic_id=id)
    #         context={"questions": questions,"topic":topic}
    #         return render(request, "quiz.html", context)
    #     else: 
    #         print(request.method)
    #         print("NOT \n\n\n\n")
            
    # except:
    #     print("except box")        
        

def about(request):
    return render(request, "about.html")

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        return redirect("/")
    else:
        return redirect("/")




# bonus



# def Student_Login(request):
#     if request.method == 'GET':
#         sname = request.GET.get('sname')
#         admno = request.GET.get('admno')
#         # Redirect to homepage with data in query parameters
#         return HttpResponseRedirect(f"/homepage/?sname={sname}&admno={admno}")

# def homepage(request):
#     sname = request.GET.get('sname')
#     admno = request.GET.get('admno')
    
#     # You can process the data here if needed.
    
#     return render(request, "test2.html", {'sname': sname, 'admno': admno})
