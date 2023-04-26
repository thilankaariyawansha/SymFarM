from django import forms


class lands(forms.Form):
    
    IrRf_CHOICES = [ ('rf', 'RF'),
        ('ir', 'IR'),
        
    ]
    
    first_name = forms.CharField(label= 'First Name (මුල් නම):')
    last_name = forms.CharField(label= 'Last Name (මුල් නම):')
    nic = forms.CharField(label= 'NIC (මුල් නම):')
    address = forms.CharField(label= 'Address (මුල් නම):')
    contact_number = forms.CharField(label= 'Phone (මුල් නම):')
    
    lat = forms.CharField(label='Latitude (අක්ෂාංශ):')
    log = forms.CharField(label='Longitude (දේශාංශ):')
    area = forms.CharField(label='Area (ha) (ඉඩමේ ප්‍රමාණය හෙක්ටයාර):')
    ownership = forms.CharField(label='Ownership (ඉඩමේ අයිතිය) :')
    rf_ir = forms.ChoiceField(label='RF/IR (වර්ශාපොශිත/ජලවහන):', choices=IrRf_CHOICES)
    soil = forms.CharField(label='Soil Type (පාංශු කාණ්ඩය ) :')
    
    
    class Meta:
        fields = '__all__'
    
   