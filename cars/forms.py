from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    time_type = 'time'

class CarRentalForm(forms.Form):
    pick_up_location = forms.CharField(label='Pick-up Location', max_length=100)
    drop_off_location = forms.CharField(label='Drop-off Location', max_length=100)
    pick_up_date = forms.DateField(label='Pick-up Date')
    pick_up_time = forms.TimeField(label='Pick-up Time')
    drop_off_date = forms.DateField(label='Drop-off Date')
    drop_off_time = forms.TimeField(label='Drop-off Time')

    widgets = {
                'pick_up_date': DateInput,
            }
    

    