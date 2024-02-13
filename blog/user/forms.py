from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class RegisterForm(forms.Form):
    # Kullanıcı adı alanı olusturulru
    username = forms.CharField(max_length=50, label="Kullanıcı Adı", widget=forms.TextInput(
        attrs={"class": "form-control", "placeholder": "Kullanıcı Adı"}))
    # widget ile parola alanı olduu belirtilir
    password = forms.CharField(
        max_length=50, label="Parola", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm = forms.CharField(
        max_length=50, label="Paroloyu Doğrula", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):  # overide edilen metod yazılır
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")  # bilgiler alınır
        if confirm and password and password != confirm:  # bosmu eşleşiyormu diye karşılaştıtılt
            raise forms.ValidationError(
                "Parolalar eşleşmiyor")  # hata fırlatılır
        values = {
            "username": username,
            "password": password
        }  # degerler sozluk yapısına yazılır
        return values  # değer dondurulur


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, label="Kullanıcı Adı", widget=forms.TextInput(attrs={
                               'class': 'form-control'}))
    password = forms.CharField(max_length=50, label="Parola", widget=forms.PasswordInput(attrs={
                               'class': 'form-control'}))
    # cleana gerek yok karşılastırma yapmıcaksak bilgiler overide edilmiş halde gelir bos olması durumu vs hata verir
# form ile bilgiler djanjo documantiond a bulunabilri
