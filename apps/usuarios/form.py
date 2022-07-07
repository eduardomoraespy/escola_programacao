from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit
from django import forms

from usuarios.models import Usuario


class CadastroUsuarioForm(forms.ModelForm):

    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'password'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(CadastroUsuarioForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('password', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('is_active', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_staff', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_superuser', css_class="form-control form-control-sm"), css_class='col-md-12'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-usuario/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser',)
        error_messages = {
            'email':{
                'required':'O E-mail é obrigatório para o registro'
            },
            'password':{
                'required':'A senha é obrigatória para o registro'
            },
        }


class DetailUsuarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DetailUsuarioForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('is_active', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_staff', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_superuser', css_class="form-control form-control-sm"), css_class='col-md-12'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Voltar', css_class="btn btn-warning has-ripple mr-2",
                            onclick='window.location.href="/lista-usuario"'),
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Usuario
        fields = ('email', 'is_active', 'is_staff', 'is_superuser',)


class EditaUsuarioForm(forms.ModelForm):

    password = forms.CharField(
        label='Senha',
        required=True,
        widget=forms.TextInput(
            attrs={
                'type': 'password'
            }
        )
    )

    def __init__(self, *args, **kwargs):
        super(EditaUsuarioForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('password', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('is_active', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_staff', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('is_superuser', css_class="form-control form-control-sm"), css_class='col-md-12'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-usuario"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Usuario
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser',)
        error_messages = {
            'email':{
                'required':'O E-mail é obrigatório para o registro'
            },
            'password':{
                'required':'A senha é obrigatória para o registro'
            },
        }




