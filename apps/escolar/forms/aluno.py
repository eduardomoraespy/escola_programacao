from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (HTML, Button, Div, Field, Layout,
                                 Submit)
from django import forms

from ..models import Aluno


class CadastroAlunoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CadastroAlunoForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('sobrenome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('estado', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('cidade', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('endereco', css_class="form-control form-control-sm"), css_class='col-md-6'),
                #Div(Field('telefoneID', css_class="form-control"), css_class='col-md-6'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/ "'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Aluno
        fields = ('__all__')




