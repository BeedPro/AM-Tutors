from django import forms

class ContactForm(forms.Form):
	name_css = forms.TextInput(attrs={'class': 'text-on-dark form-control bg-dark rounded-0', 'placeholder': 'Enter name...'})
	email_css = forms.TextInput(attrs={'class': 'text-on-dark form-control bg-dark rounded-0', 'placeholder': 'Enter email...'})
	message_css = forms.Textarea(attrs={'class': 'text-on-dark form-control bg-dark rounded-0', 'placeholder': 'Enter message...', "rows":"6"})

	name = forms.CharField(label='', max_length=100, widget=name_css)
	email = forms.EmailField(label='', widget=email_css)
	message = forms.CharField(label='', max_length=100, widget=message_css)


