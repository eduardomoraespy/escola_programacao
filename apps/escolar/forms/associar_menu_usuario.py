from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit, HTML
from django import forms

from escolar.models import AssociarMenuUsuario


class AssociarMenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(AssociarMenuForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('tipo_usuario', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('menuID', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-menu-associar/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = AssociarMenuUsuario
        fields = ['menuID', 'tipo_usuario']
        error_messages = {
            'menuID':{
                'required':'O campo nenu é obrigatório!'
            },
            'tipo_usuario':{
                'required':'O campo tipo de usuário é obrigatório!'
            },
        }


class DetailAssociarMenuUsuarioForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(DetailAssociarMenuUsuarioForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('tipo_usuario', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('menuID', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Voltar', css_class="btn btn-warning has-ripple mr-2",
                            onclick='window.location.href="/lista-menu-associar/"'),
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = AssociarMenuUsuario
        fields = ['menuID', 'tipo_usuario']


class EditaAssociarMenuUsuarioForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditaAssociarMenuUsuarioForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('tipo_usuario', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('menuID', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-menu-associar/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = AssociarMenuUsuario
        fields = ['menuID', 'tipo_usuario']
        error_messages = {
            'menuID':{
                'required':'O campo nenu é obrigatório!'
            },
            'tipo_usuario':{
                'required':'O campo tipo de usuário é obrigatório!'
            },
        }