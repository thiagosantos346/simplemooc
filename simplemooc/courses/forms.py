from django import forms
from django.core.mail import send_mail
from django.conf import settings


class ContactCourse(forms.Form):
	"""docstring for ContactCourse"""
	name = forms.CharField(label='Nome', max_length=100)
	email = forms.EmailField(label='E-mail' )

	message = forms.CharField(
					label='Mensagem/Dúvida',
					widget=forms.Textarea
					)
	
	def send_mail(self, curse):
		subject = ' [%s] contato.' %curse
		message = 'Nome: % (name)s;-E-mail: %(email)s;%(message)s'
		message = {

			'name': self.clenead_data['name'],
			'email': self.cleade_data['email'],
			'message': self.cleaned_data['message'],

		}

		message = message % context
		send_mail(
					subject,
					message,
					setttings.DEFAULT_FROM_MAIL,
					[setttings.CONTACT_MAIL] 
				)