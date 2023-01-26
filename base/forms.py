from django import forms
from base.models import Employee, Role


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {'name': forms.TextInput(),
                   'dob': DateInput(),
                   'doj': DateInput(),
                   'department': forms.Select(),
                   'role': forms.Select(),
                   'address': forms.Textarea(),
                   'city': forms.TextInput(),
                   'state': forms.TextInput(),
                   'country': forms.TextInput(),
                   'zipcode': forms.TextInput(),
                   #    'active': forms.BooleanField(),
                   #    'on_leave': forms.BooleanField(),
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['role'].queryset = Role.objects.none()

        if 'department' in self.data:
            try:
                department_id = int(self.data.get('department'))
                self.fields['role'].queryset = Role.objects.filter(
                    department_id=department_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Role queryset
        elif self.instance.pk:
            self.fields['role'].queryset = self.instance.department.role_set.order_by(
                'name')
