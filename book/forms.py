from django import forms
from .models import Book

#book 입력, 수정, html에서 사용하기 위해

def min_length3_validator(value):
    if len(value) < 3:
        raise forms.ValidationError("3글자 이상입니다.")

# 일반 FORM
class BookForm(forms.Form):
    title = forms.CharField(label="forms 제목") #forms는 DB와 상관이 없으므로, max_length가 필요 없음
    author = forms.CharField(label="forms 저자", validators=[min_length3_validator])
    publisher = forms.CharField(label="forms 출판사", required=False)

    def save2(self, commit=True):
        book = Book(**self.cleaned_data) #{'title':'', 'author':'',....}
        if commit:
            book.save()
        return book
        
