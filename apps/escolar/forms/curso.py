from crispy_forms.bootstrap import FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, Button, Submit, HTML
from django import forms

from escolar.models import Curso, MatriculaCurso


class CadastroCursoForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(CadastroCursoForm, self).__init__(*args, **kwargs)

        self.fields["data_inicio"] = forms.DateField(
            label='Data de Início',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.fields["data_termino"] = forms.DateField(
            label='Data de Término',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_curso', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('data_inicio', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('data_termino', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('professorID', css_class="form-control form-control-sm"), css_class='col-md-8'),
                Div(Field('ativo', css_class="form-control form-control-sm"), css_class='col-md-2'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-curso/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Curso
        fields = ('__all__')
        exclude = ['usuario_id']
        error_messages = {
            'nome_curso':{
                'required':'O campo Nome de Curso é obrigatório!'
            },
            'data_inicio':{
                'required':'O campo Data de Início é obrigatório!'
            },
            'data_termino':{
                'required':'O campo Data de Término é obrigatório!'
            },
        }


class DetailCursoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DetailCursoForm, self).__init__(*args, **kwargs)

        self.fields["data_inicio"] = forms.DateField(
            label='Data de Início',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.fields["data_termino"] = forms.DateField(
            label='Data de Término',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_curso', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('data_inicio', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('data_termino', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('professorID', css_class="form-control form-control-sm"), css_class='col-md-8'),
                Div(Field('ativo', css_class="form-control form-control-sm"), css_class='col-md-2'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-curso/"'),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Curso
        fields = ('__all__')


class EditaCursoForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditaCursoForm, self).__init__(*args, **kwargs)

        self.fields["data_inicio"] = forms.DateField(
            label='Data de Início',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.fields["data_termino"] = forms.DateField(
            label='Data de Término',
            required=True,
            widget=forms.TextInput(
                attrs={
                    'type':'date'
                }
            )
        )

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('nome_curso', css_class="form-control form-control-sm"), css_class='col-md-6'),
                Div(Field('data_inicio', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('data_termino', css_class="form-control form-control-sm"), css_class='col-md-3'),
                Div(Field('professorID', css_class="form-control form-control-sm"), css_class='col-md-8'),
                Div(Field('ativo', css_class="form-control form-control-sm"), css_class='col-md-2'),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-curso/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = Curso
        fields = ('__all__')
        error_messages = {
            'nome_curso':{
                'required':'O campo Nome de Curso é obrigatório!'
            },
            'data_inicio':{
                'required':'O campo Data de Início é obrigatório!'
            },
            'data_termino':{
                'required':'O campo Data de Término é obrigatório!'
            },
        }


class MatriculaCursoForm(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(MatriculaCursoForm, self).__init__(*args, **kwargs)

        self.fields["aluno_id"] = forms.CharField(
            label="Alunos",
            required=False,
            widget=forms.Select(
                attrs={
                    'name':'from[]',
                    'id':'multiselect',
                    'multiple':'multiple',
                }
            )
        )

        self.helper = FormHelper()
        self.helper.form_class = 'form-group'
        #self.helper.label_class = 'floating-label'
        self.helper.layout = Layout(
            Div(
                Div(Field('aluno_id', css_class="form-control form-control-sm"), css_class='col-md-5'),
                Div(HTML(
                    '''
                        <button type="button" id="multiselect_rightAll" class="btn btn-icon btn-dark has-ripple"><i class="feather icon-chevrons-right"></i></button>
                        <button type="button" id="multiselect_rightSelected" class="btn btn-block"><i class="glyphicon glyphicon-chevron-right"></i></button>
                        <button type="button" id="multiselect_leftSelected" class="btn btn-block"><i class="glyphicon glyphicon-chevron-left"></i></button>
                        <button type="button" id="multiselect_leftAll" class="btn btn-block"><i class="glyphicon glyphicon-backward"></i></button>
                    '''
                ), css_class='col-md-2'),
                # Associar alunos ao curso
                Div(HTML(
                    '''
                        <label for="aluno_lista" class=" requiredField">
                            Alunos a serem matrículados
                            <span class="asteriskField">*</span> 
                        </label>
                        <select name="to[]" id="multiselect_to" class="form-control" multiple="multiple"></select>
                    '''
                ), css_class='col-md-5'),
                Div(),
                css_class='row ml-3 mr-3'
            ),
            Div(
                FormActions(
                        Div(
                            Button('cancel', 'Cancelar', css_class="btn btn-danger has-ripple mr-2",
                            onclick='window.location.href="/lista-curso/"'),
                            Submit('save_changes', 'Salvar', css_class="btn btn-primary has-ripple"),
                            css_class='mt-3 float-right',    
                        )
                ),css_class='row float-right mr-3'
            ),
        )

    class Meta:
        model = MatriculaCurso
        fields = ('__all__')
        exclude = ['curso_id']
        error_messages = {
            'aluno_id':{
                'required':'O campo Aluno é obrigatório!'
            },
        }