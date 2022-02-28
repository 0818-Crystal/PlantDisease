from django.db import models
from django.contrib.auth.models import User
# Create your models here.


def photo_upload_path(instance, filename):
    class_name = instance.__class__.__name__.lower()

    return "{}/{}-{}/{}".format(class_name + "s", class_name, instance.pk, filename)


class Plant_organs(models.Model):
    id = models.CharField(max_length=60,primary_key=True)
    organs_name=models.CharField(max_length=50)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True,blank=True,null=True)


    def __str__(self):
        return self.organs_name

class Plant(models.Model):
    plant_name = models.CharField(max_length=255)
    alias = models.CharField(max_length=50,blank=True,null=True)
    plant_growth = models.CharField(max_length=255,blank=True,null=True)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True,blank=True,null=True)
    def __str__(self):
        return self.plant_name

class  Plant_disease(models.Model):
    plant_id = models.ForeignKey(Plant, on_delete=models.CASCADE)
    disease_name = models.CharField(max_length=255)
    alias=models.CharField(max_length=255,blank=True,null=True)
    is_disease=models.BooleanField()
    harm_part = models.CharField(max_length=2000)
    cure=models.CharField(max_length=2000,blank=True,null=True)
    desc=models.CharField(max_length=2000,blank=True,null=True)
    character=models.CharField(max_length=2000,blank=True,null=True)
    regularity=models.CharField(max_length=2000,blank=True,null=True)
    measures=models.CharField(max_length=2000)
    photos_main = models.ImageField( null=True,blank=True)
    photos_content = models.ImageField( null=True,blank=True)
    harm_organs=models.ManyToManyField(Plant_organs)
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True,blank=True,null=True)

    def __str__(self):
        return self.disease_name



class Activation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True,null=True)

class Comments(models.Model):
    content = models.CharField(max_length=500)
    answer = models.CharField(max_length=500,null=True)
    question_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='question_from+')
    answer_from = models.ForeignKey(User,on_delete=models.CASCADE,related_name='answer_from+',null=True)
    is_answered = models.BooleanField()
    create_time = models.DateField(auto_now_add=True)
    update_time = models.DateField(auto_now=True,blank=True,null=True)

    def __str__(self):
        if self.is_answered:
            return ('已回复。  发帖人：'+self.question_from.username+',内容:'+self.content)
        else:
            return ('！！待回复！！ 发帖人：'+self.question_from.username+',内容:'+self.content)

