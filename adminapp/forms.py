from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
# from .models import *
from store.models import *

class ProductForm(forms.ModelForm):
	class Meta:
		model = Products
		fields = ['name','price','category','description','image']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-8 mb-0'),
				Column('price', css_class='form-group col-md-4 mb-0'),
				Column('category', css_class='form-group col-md-12 mb-0'),
				Column('description', css_class='form-group col-md-12 mb-0'),

			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				),
			
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)

class categoriform(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name']
		
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-8 mb-0'),
			),
	
			HTML(""" <div class="text-left mt-4"> <button class="btn btn-sm btn-labeled btn-info" type="submit" title="Save"><span class="btn-label"><i class='fa fa-save'></i></span> Save</button>"""),
			HTML("""  <button class="btn btn-sm btn-labeled btn-secondary" onclick=self.history.back()><span class="btn-label"><i class="fa fa-window-close"></i></span> Cancel</button></div>""")
		)