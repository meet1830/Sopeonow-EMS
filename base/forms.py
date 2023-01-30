from django import forms
from base.models import Employee, Role
import datetime


class DateInput(forms.DateInput):
    input_type = 'date'


class AddEmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {'name': forms.TextInput(attrs={'class': 'form-control'}),
                   'dob': DateInput(attrs={'class': 'form-control'}),
                   'doj': DateInput(attrs={'class': 'form-control'}),
                   'department': forms.Select(attrs={'class': 'form-control', 'type': 'button'}),
                   'role': forms.Select(attrs={'class': 'form-control', 'type': 'button'}),
                   'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
                   'city': forms.TextInput(attrs={'class': 'form-control'}),
                   'state': forms.TextInput(attrs={'class': 'form-control'}),
                   'country': forms.TextInput(attrs={'class': 'form-control'}),
                   'zipcode': forms.NumberInput(attrs={'class': 'form-control'}),
                   'leaves': forms.NumberInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
                   'active': forms.CheckboxInput(),
                   'on_leave': forms.CheckboxInput(),
                   }

    def clean_dob(self):
        date = self.cleaned_data['dob']
        if date > datetime.date.today():  # 🖘 raise error if greater than
            raise forms.ValidationError(
                "Date of birth cannot be in the future!")
        return date

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
