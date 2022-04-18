from django import forms
from searchSystem import  models


class SearchForm(forms.Form):
    disease_choices=((2,'不知'),(1,'病害'),(0,'虫害'))
    keywords_choices=((0,'疾病名称'),(1,'症状描述'))
    disease_type=forms.IntegerField(

        label='病虫害类型',

        widget=forms.Select(choices=disease_choices,attrs={'class':'form-select vegetable-class','aria-label':'choose vegetable class'}),
        required=False,

    )
    plant_type = forms.IntegerField(
        label='蔬菜种类',
        widget=forms.Select(attrs={'class':'form-select vegetable-class','aria-label':'choose vegetable class'}),
        required=False,

    )
    organ_type=forms.MultipleChoiceField(
        label='为害部位',
        widget=forms.CheckboxSelectMultiple(attrs={'type':"checkbox"}),
        required=False,


    )
    # harm_type = forms.IntegerField(
    #
    #     label='为害类型',
    #
    #     widget=forms.Select(choices=((1,'部位同时为害'),(2,'非部位同时为害')),attrs={'class':'form-select vegetable-class','aria-label':'choose vegetable class','disabled':'True'}),
    #     required=False,
    #
    # )
    keywords = forms.CharField(
        label='疾病名关键字（可选）',
        widget=forms.TextInput(attrs={'class':"form-control" }),

        required=False,
    )

    keywordsSelect = forms.IntegerField(

        widget=forms.Select(choices=keywords_choices,attrs={'class':'form-select keywords-class','style':'flex: 1;border: 1px solid #171819'}),
        required=False,

    )

    keywordsSelectInput = forms.CharField(

        widget=forms.TextInput(attrs={'type':'text','class':'form-control','style':'flex:5'}),
        help_text='以空格分隔字符',
        required=False,
    )

    def __init__(self, *args, **kwargs):  # 执行父类的构造方法
        super().__init__(*args, **kwargs)
        self.fields['plant_type'].widget.choices = models.Plant.objects.all().values_list('id', 'plant_name')
        self.fields['organ_type'].choices = models.Plant_organs.objects.all().values_list('id', 'organs_name')

class CommentForm(forms.Form):
   messageInput = forms.CharField(
       widget=forms.Textarea(attrs={'class':'form-control','id':'message-text'})
   )



