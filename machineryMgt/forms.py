from django import forms


class machineFleet(forms.Form):
    
    
    registration_number = forms.CharField(max_length=200)
    machine_type = forms.CharField(max_length=200)
    mark = forms.CharField(max_length=200)
    model = forms.CharField(max_length=200)
    date_of_purches = forms.DateField()
    year_of_manufacture = forms.CharField(max_length=200)
    country_of_origine = forms.CharField(max_length=200)
    cost = forms.IntegerField()
    owner = forms.CharField(max_length=200)
    owner_contact=forms.CharField(max_length=200)
    
    img = forms.ImageField()
    
    
    class Meta:
        fields = '__all__'
    
   
    

    