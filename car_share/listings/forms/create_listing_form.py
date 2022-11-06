from django import forms


class CreateListingForm(forms.Form):
    location = forms.CharField(max_length=40)
    owner = forms.CharField(max_length=40)
    car_type = forms.CharField(max_length=40)
    gas_percent = forms.IntegerField(min_value=0, max_value=100)
    mileage = forms.IntegerField(min_value=0)
    make_model = forms.CharField(max_length=40)
    renter = forms.CharField(max_length=40)

    def clean(self):
        data = super().clean()
        cleaned_data = {}
        contains_location = False
        contains_owner = False
        contains_car_type = False
        contains_gas_percent = False
        contains_mileage = False
        contains_make_model = False
        contains_renter = False

        for key, value in data.items():
            if key == 'location':
                contains_location = True
                cleaned_data['location'] = data['location']
            if key == 'owner':
                contains_owner = True
                cleaned_data['owner'] = data['owner']
            if key == 'car_type':
                contains_car_type = True
                cleaned_data['car_type'] = data['car_type']
            if key == 'gas_percent':
                contains_gas_percent = True
                cleaned_data['gas_percent'] = data['gas_percent']
            if key == 'mileage':
                contains_mileage = True
                cleaned_data['mileage'] = data['mileage']
            if key == 'make_model':
                contains_make_model = True
                cleaned_data['make_model'] = data['make_model']
            if key == 'renter':
                contains_renter = True
                cleaned_data['renter'] = data['renter']

        if cleaned_data['location'] == '':
            self.add_error('location', 'This field is required')
        if cleaned_data['owner'] == '':
            self.add_error('owner', 'This field is required')
        if cleaned_data['car_type'] == '':
            self.add_error('car_type', 'This field is required')
        if cleaned_data['gas_percent'] == '':
            self.add_error('gas_percent', 'This field is required')
        if cleaned_data['mileage'] == '':
            self.add_error('mileage', 'This field is required')
        if cleaned_data['make_model'] == '':
            self.add_error('make_model', 'This field is required')

        return cleaned_data
