from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import ProjectDetails
from .models import SupervisorDetails
from .models import ReviewersDetails
from .models import Reviews
from django.http import JsonResponse
import os


def index(request):
    return render(request, 'index.html') 


def stdlogin(request):
    if request.method == "POST":
        userid = request.POST.get('stdid')
        userpass = request.POST.get('pass')
        try:
            student = ProjectDetails.objects.get(username=userid)
        except ProjectDetails.DoesNotExist:
            return HttpResponse("Invalid Credentials")
        if(userpass==student.password):
            reviews = student.reviews_project.all()
            rating1_sum = 0
            rating2_sum = 0
            rating3_sum = 0
            rating4_sum = 0
            reviewer_details = []
            num_reviews = reviews.count()
            for review in reviews:
                rating1_sum += review.rating1
                rating2_sum += review.rating2
                rating3_sum += review.rating3
                rating4_sum += review.rating4
                # reviewers = review.reviewer.all()
                reviewer_details.append({
                    'reviewer_name': review.reviewer.name,
                    'reviewer_qualif': review.reviewer.qualif,
                    'review': review.review,
                    'rating1': review.rating1,
                    'rating2': review.rating2,
                    'rating3': review.rating3,
                    'rating4': review.rating4,
                    't_rating': review.t_rating,
                    'picture': review.reviewer.picture.url,
                    'avg_star': (review.rating1+review.rating2 + review.rating3 + review.rating4)/4,
                })
            if num_reviews == 0:
                rating1_avg = 0
                rating2_avg = 0
                rating3_avg = 0
                rating4_avg = 0
                total_rating = 0
                width1 = 0
                width2 = 0
                width3 = 0
                width4 = 0
                width_total = 0
                
            else:
                rating1_avg = rating1_sum/num_reviews
                rating2_avg = rating2_sum/num_reviews
                rating3_avg = rating3_sum/num_reviews
                rating4_avg = rating4_sum/num_reviews 
                total_avg = (rating1_avg + rating2_avg + rating3_avg + rating4_avg)/4
                total_rating = total_avg * 20
                width1 = rating1_avg * 20
                width2 = rating2_avg * 20
                width3 = rating3_avg * 20
                width4 = rating4_avg * 20
                width_total = total_rating
                        
            context = {
            'reviewer_details': reviewer_details,
            'student':student,
            'username':userid,
            'password':userpass,
            'rating1_avg': rating1_avg,
            'rating2_avg': rating2_avg,
            'rating3_avg': rating3_avg,
            'rating4_avg': rating4_avg,
            'total_rating':total_rating,
            'width1' : width1,
            'width2' : width2,
            'width3' : width3,
            'width4' : width4,
            'width_total' : width_total,
            
            }
            return render(request, 'student.html', context)
    return render(request, 'login.html')


def revlogin(request):
    if request.method == "POST":
        userid = request.POST.get('username')
        password = request.POST.get('pass')
        try:
            reviewer = ReviewersDetails.objects.get(username=userid)
        except ProjectDetails.DoesNotExist:
            return HttpResponse("Invalid Credentials")
        if(password==password):
            rev_id = reviewer.id 
            student = ProjectDetails.objects.all()
            # supervisor = SupervisorDetails.objects.all()
            return render(request, 'admin1.html', {'revr_id':rev_id, 'student':student })
    return render(request, 'login.html')


def admin1(request):
    return render(request, 'login.html' ) 

def adminrev(request):
    if request.method == "POST":
        project_id = request.POST.get('p_id')
        reviwer_id = request.POST.get('revr_id')

        student = ProjectDetails.objects.get(p_id=project_id)
        # reviwer = ReviewersDetails.objects.get(id=reviwer_id)
        # supervisor = SupervisorDetails.objects.get(project=student)
        return render(request, 'adminRev.html', {'student':student, 'revr_id':reviwer_id})
    return render(request, 'adminRev.html')

def submitReviwe(request):
    if request.method == "POST":
        std_id = request.POST.get('std_id')
        revr_id = request.POST.get('revr_id')
        rate1 = request.POST.get('star')
        rate2 = request.POST.get('star1')
        rate3 = request.POST.get('star2')
        rate4 = request.POST.get('star3')
        review = request.POST.get('review')
        project = ProjectDetails.objects.get(p_id=std_id)
        # supervisor = SupervisorDetails.objects.get(project=project)
        student = ProjectDetails.objects.all()
        reveiwer = ReviewersDetails.objects.get(id=revr_id)

        review = Reviews(
            review = review,
            rating1 = rate1,
            rating2 = rate2,
            rating3 = rate3,
            rating4 = rate4,
            project = project,
            reviewer=reveiwer
        )
        review.save()

        return render(request, 'admin1.html', {'message':"Review Post Successfully", 'revr_id':revr_id, 'student':student })


def student(request):
    return render(request, 'login.html') 

def stdupdate(request):
    
    if request.method == "POST":
        std_id = request.POST.get('std_id')
        username = request.POST.get('username')
        password = request.POST.get('password')
        student = ProjectDetails.objects.get(p_id=std_id)
        context = {
            'student':student,
            'username':username,
            'password':password
        }
        return render(request, 'stdupdateprofile.html', context) 
    return HttpResponse("Success")


def stdupdatedone(request):
    if request.method == "POST":
        std_id = request.POST.get('std_id')
        student = ProjectDetails.objects.get(p_id=std_id)
        # student.username = request.POST.get('username')
        # student.password = request.POST.get('password')
        student.project_title = request.POST.get('project_title')
        student.project_description = request.POST.get('project_description')
        student.member1 = request.POST.get('member1')
        student.member1_rol = request.POST.get('member1_rol')
        student.member2 = request.POST.get('member2')
        student.member2_rol = request.POST.get('member2_rol')
        student.member3 = request.POST.get('member3')
        student.member3_rol = request.POST.get('member3_rol')
        student.dept = request.POST.get('dept')
        if 'member1_pic' in request.FILES:
            if len(request.FILES) != 0:
                if len(student.member1_pic) > 0:
                    os.remove(student.member1_pic.path)
                student.member1_pic = request.FILES['member1_pic']
        # if len(request.FILES) != 0:
            if request.FILES.get('member2_pic'):
            # if len(student.member2_pic) > 0:
                # os.remove(student.member2_pic.path)
                student.member2_pic = request.FILES['member2_pic']
        if 'member3_pic' in request.FILES:
            if len(request.FILES) != 0:
                if len(student.member3_pic) > 0:
                    os.remove(student.member3_pic.path)
                student.member3_pic = request.FILES['member3_pic']
        supervisor_id = request.POST.get('supervisor')
        supervisor = SupervisorDetails.objects.get(s_id=supervisor_id)
        student.supervisor = supervisor
        student.save()

        student = ProjectDetails.objects.get(p_id=std_id)
        reviews = student.reviews_project.all()
        rating1_sum = 0
        rating2_sum = 0
        rating3_sum = 0
        rating4_sum = 0
        reviewer_details = []
        num_reviews = reviews.count()
        for review in reviews:
                rating1_sum += review.rating1
                rating2_sum += review.rating2
                rating3_sum += review.rating3
                rating4_sum += review.rating4
                # reviewers = review.reviewer.all()
                reviewer_details.append({
                    'reviewer_name': review.reviewer.name,
                    'reviewer_qualif': review.reviewer.qualif,
                    'review': review.review,
                    'rating1': review.rating1,
                    'rating2': review.rating2,
                    'rating3': review.rating3,
                    'rating4': review.rating4,
                    't_rating': review.t_rating,
                    'picture': review.reviewer.picture.url,
                    'avg_star': (review.rating1+review.rating2 + review.rating3 + review.rating4)/4,
                })
        if num_reviews == 0:
                rating1_avg = 0
                rating2_avg = 0
                rating3_avg = 0
                rating4_avg = 0
        else:
                rating1_avg = rating1_sum/num_reviews
                rating2_avg = rating2_sum/num_reviews
                rating3_avg = rating3_sum/num_reviews
                rating4_avg = rating4_sum/num_reviews         
        context = {
            'reviewer_details': reviewer_details,
            'student':student,
            'rating1_avg': rating1_avg,
            'rating2_avg': rating2_avg,
            'rating3_avg': rating3_avg,
            'rating4_avg': rating4_avg,
            }
        return render(request, 'student.html', context)

