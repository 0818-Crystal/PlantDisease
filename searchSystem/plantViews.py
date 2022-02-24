from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.db.models import Q
from django.db import connection
import json

from searchSystem import  models
from .plantForms import SearchForm,CommentForm


def buildNode(request):
    print(request.GET)
    plant_list = list(getAllPlant())
    disease_list = list(getAllDiseaseByID(request.GET['id']))
    p_l=len(plant_list)
    d_l = len(disease_list)
    data= list()

    link = list()
    for i in range( p_l):
        data.append({'name':plant_list[i]['plant_name'],'des':plant_list[i]['plant_name'],'symbolSize':70,'category':0})
    for i in range(d_l):
         data.append(
            {'name': disease_list[i]['disease_name'], 'des': disease_list[i]['desc'], 'symbolSize': 70, 'category': 1})
         link.append(
            {'source':disease_list[i]['plant_id_id']-1,'target':p_l+i,'name':'病害名称','des': '病害名称'})

    return JsonResponse((data,link),safe=False)

def index(request):



    return render(request,'index.html')

def getAllPlant():
    plant_list = models.Plant.objects.all().values('id','plant_name')
    return plant_list

def getAllDisease():
    disease_list = models.Plant_disease.objects.all().values('id','disease_name','plant_id_id')

    return disease_list

def getAllDiseaseByID(plant_id):
    disease_list = models.Plant_disease.objects.filter(plant_id_id=plant_id).values()
    return disease_list

def searchByInput(request):
        user= request.user
        all_disease=getAllDisease()
        disease_list = list()
        for i in range(len(all_disease)):
            disease_list.append(all_disease[i]['disease_name'])
        q = {}
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                type=form.cleaned_data['disease_type']
                name=form.cleaned_data['plant_type']
                organ=form.cleaned_data['organ_type']


        else:
            if request.GET:
                form = SearchForm(request.GET)


                if form.is_valid():
                    type = form.cleaned_data['disease_type']
                    name = form.cleaned_data['plant_type']
                    organ = form.cleaned_data['organ_type']
                    keywords = form.cleaned_data['keywords']
                    harm = form.cleaned_data['harm_type']
                    print(keywords)
                    con=Q()
                    q2=Q()

                    if type!=2:
                        q2=Q(is_disease=type)

                    q3=Q(plant_id=name)
                    q4=Q()
                    if keywords:
                        q4=Q(disease_name__contains=keywords)
                    con.add(q2,'AND')
                    con.add(q3,'AND')
                    con.add(q4,'AND')

                    q = models.Plant_disease.objects.filter(con)
                    if organ:

                        if harm==1:
                            for i in organ:
                                q=q.filter(harm_organs__id=i)
                        else:
                                q=q.filter(harm_organs__in=organ)

                    q=q.distinct()


            else:
                form = SearchForm()

        return render(request, 'search.html', {'searchForm': form,'disease': q,'disease_list':disease_list,'user':user})
def searchByKeywords(request):
    user = request.user
    q = {}
    if request.method == 'POST':
        form = SearchForm(request.POST)



    else:
        if request.GET:
            form = SearchForm(request.GET)

            if form.is_valid():

                select = form.cleaned_data['keywordsSelect']
                keywords = form.cleaned_data['keywordsSelectInput']

                con = Q()


                if keywords:
                    list=keywords.split(' ')

                    if select==1:
                        for i in list:
                           con.add(('desc__contains',i),'AND')
                    else:
                        for i in list:
                           con.add(('disease_name__contains',i),'AND')

                q = models.Plant_disease.objects.filter(con)


                q = q.distinct()




        else:
            form = SearchForm()

    return render(request, 'search.html', {'searchForm': form, 'disease': q,'user':user})

def detail(request,disease_id):
    user=request.user

    if request.POST:
        form=CommentForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data['messageInput']
            obj = models.Comments(content=message, question_from=user,is_answered=False)

            obj.save()

    else:
        form = CommentForm()

    disease = get_object_or_404(models.Plant_disease,id=disease_id)

    try:
        selected_disease = models.Plant_disease.objects.get(id=disease_id)
    except (KeyError):

      return render(request, 'index.html', {

            'error_message': "You didn't select a choice.",
        })
    else:
        return render(request,'detail.html',{'disease':selected_disease,'user':user,'CommentForm':form})

def comment(request):
    comments=models.Comments.objects.filter(question_from=request.user.id)

    return render(request, 'comment.html', {'comments':comments})


def diseaseGraph(request):
    plants=getAllPlant()
    return  render(request,'graph.html',{'plants':plants})
