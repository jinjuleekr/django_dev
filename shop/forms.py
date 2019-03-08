from django import forms

# db의 model과는 다름
class ContactForm(forms.Form):
    name = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        print("이메일을 보냅니다.")