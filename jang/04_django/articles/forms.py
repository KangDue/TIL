from django import forms
from .models import Article


# class ArticleForm(forms.Form):
#     NATION_A = 'kr'
#     NATION_B = 'ch'
#     NATION_C = 'jp'
#     NATIONS_CHOICES = [
#         (NATION_A, '한국'),
#         (NATION_B, '중국'),
#         (NATION_C, '일본'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     nation = forms.ChoiceField(choices=NATIONS_CHOICES)
    # nation = forms.ChoiceField(choices=NATIONS_CHOICES, widget=forms.RadioSelect)

#widget의 keyward 인자로 html상 tag를 입력 ex) id, method 등등
#attrs의 dict형태로 넣는다.
#widget은 db와 아무런 연관이 없고 input의 표현만 담당
class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(
            attrs={
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the Title',
                'maxlength' : 10, #유효성검사의 역할을 하진 않음.
            }
        )
    )
    
    content= forms.CharField(
        label = "내용",
        widget = forms.Textarea(
            attrs={
                'placeholder':'Enter ther content',
                'rows':5,
                'cols':50,
                'class': 'my-content form-control',
            }
        ),
        error_messages={ #html이 띄우는 메시지 외에 오류메시지 출력 
            'required':"Please enter your content",
        }
    )


    class Meta:
        model = Article
        fields = '__all__'
        # exclude = ('title',)
