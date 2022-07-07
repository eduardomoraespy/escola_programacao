from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit, HTML
from django import forms

from escolar.models import Professor


class CadastroProfessorForm(forms.ModelForm):

    telefone = forms.CharField(
        label='Telefone',
        required=True,
        help_text='Digite apenas números',
        widget=forms.TextInput(
            attrs={'data-mask': '(99)99999-9999'}
        )

    )


    def __init__(self, *args, **kwargs):
        super(CadastroProfessorForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('sobrenome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('telefone', css_class="form-control form-control-sm"), css_class='col-md-2'),
                Div(HTML(
                    '''

                        <button class="btn btn-success has-ripple mt-2" onclick="adicionar()">
                            Adicionar Tel
                            <i class="feather icon-phone-call"></i>
                        </button>

                    '''
                ), css_class='col-md-2'),
                Div(HTML(
                    '''
                        <label for="telefone_lista" class=" requiredField">
                            Lista de telefone
                            <span class="asteriskField">*</span> 
                        </label>
                        <select name="telefone_lista" id="telefone_lista" class="form-control form-control-sm"></select>
                    '''
                ), css_class='col-md-2'),
                Div(css_class='col-md-8'),
                Div(css_class='col-md-8', css_id='add_telefone'),
                Div(Field('endereco', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('cidade', css_class="form-control form-control-sm"), css_class='col-md-4'),
                Div(Field('estado', css_class="form-control form-control-sm"), css_class='col-md-2'),
                
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
        model = Professor
        fields = ('__all__')
        error_messages = {
            'nome':{
                'required':'O campo nome é obrigatório!'
            },
            'sobrenome':{
                'required':'O campo sobrenome é obrigatório!'
            },
            'email':{
                'required':'O E-mail é obrigatório!'
            },
            'estado':{
                'required':'O campo estado é obrigatório!'
            },
            'cidade':{
                'required':'O campo cidade é obrigatório!'
            },
            'endereco':{
                'required':'O campo endereço é obrigatório!'
            },
        }


class DetailProfessorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DetailProfessorForm, self).__init__(*args, **kwargs)


        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('sobrenome', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('email', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('estado', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('cidade', css_class="form-control form-control-sm"), css_class='col-md-12'),
                Div(Field('endereco', css_class="form-control form-control-sm"), css_class='col-md-12'),
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
        model = Professor
        fields = ('__all__')


class EditaProfessorForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditaProfessorForm, self).__init__(*args, **kwargs)


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
        model = Professor
        fields = ('__all__')




