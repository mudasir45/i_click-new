from django.db import models

# Create your models here.
class SupervisorDetails(models.Model):
    s_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    qualif = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='media/supervisors_images/')

    def __str__(self):
        return self.name



class ProjectDetails(models.Model):
    p_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20, null=True, blank=True)
    password = models.CharField(max_length=20, null=True, blank=True)
    project_title = models.CharField(max_length=200, null=True, blank=True)
    project_description = models.TextField(null=True, blank=True)
    member1 = models.CharField(max_length=200, null=True, blank=True)
    member1_rol = models.CharField(max_length=200, null=True, blank=True)
    member2 = models.CharField(max_length=200, null=True, blank=True)
    member2_rol = models.CharField(max_length=200, null=True, blank=True)
    member3 = models.CharField(max_length=200, null=True, blank=True)
    member3_rol = models.CharField(max_length=200, null=True, blank=True)
    dept = models.CharField(max_length=30, null=True, blank=True)
    member1_pic = models.ImageField(upload_to='media/project_images/')
    member2_pic = models.ImageField(upload_to='media/project_images/')
    member3_pic = models.ImageField(upload_to='media/project_images/')
    supervisor = models.ForeignKey(SupervisorDetails, null=True, blank=True, on_delete=models.CASCADE, related_name='supervisor_project')

    def __str__(self):
        return f"({self.member2}-{self.dept})"

class ReviewersDetails(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    name = models.CharField(max_length=200)
    qualif = models.CharField(max_length=200, null=True, blank=True)
    picture = models.ImageField(upload_to='media/reviewers_images/', null=True, blank=True)
    # reviews = models.ManyToManyField(Reviews, null=True, blank=True, related_name='reviewers')
    
    def __str__(self):
        return self.name


class Reviews(models.Model):
    id = models.AutoField(primary_key=True)
    review = models.TextField(null=True, blank=True)
    rating1 = models.IntegerField(null=True, blank=True)
    rating2 = models.IntegerField(null=True, blank=True)
    rating3 = models.IntegerField(null=True, blank=True)
    rating4 = models.IntegerField(null=True, blank=True)
    t_rating = models.IntegerField(null=True, blank=True)
    project = models.ForeignKey(ProjectDetails, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews_project')
    reviewer = models.ForeignKey(ReviewersDetails, null=True, blank=True, on_delete=models.CASCADE, related_name='reviewers')

    def __str__(self):
        return self.review



