from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit, HTML
from django import forms

from escolar.models import Menu


class CadastroMenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroMenuForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_menu', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('caminho', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-menu/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Menu
        fields = ('__all__')
        error_messages = {
            'nome_menu':{
                'required':'O campo nome_menu é obrigatório!'
            },
            'caminho':{
                'required':'O campo caminho é obrigatório!'
            },
        }


class DetailMenuForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(DetailMenuForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_menu', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('caminho', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Voltar', css_class="btn btn-warning has-ripple mr-2",
                            onclick='window.location.href="/lista-menu/"'),
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Menu
        fields = ('__all__')


class EditaMenuForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditaMenuForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_menu', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('caminho', css_class="form-control form-control-sm"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-menu/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Menu
        fields = ('__all__')
        error_messages = {
            'nome_menu':{
                'required':'O campo nome_menu é obrigatório!'
            },
            'caminho':{
                'required':'O campo caminho é obrigatório!'
            },
        }

