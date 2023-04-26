from django.shortcuts import render
from .forms import machineFleet
from django.contrib.auth.decorators import login_required
from .models import machines
from django.contrib import messages


@login_required


def addMachine(response):
    
    if response.user.is_authenticated:
        current_username = response.user.username
        print("----------",current_username)
                
        if response.method == 'POST':
            addmachine = machineFleet(response.POST)
            if addmachine.is_valid():
                
                
                
                registration_number = response.POST.get('registration_number')
                machine_type = response.POST.get('machine_type')
                mark = response.POST.get('mark')
                model = response.POST.get('model')
                date_of_purches = response.POST.get('date_of_purches')
                year_of_manufacture = response.POST.get('year_of_manufacture')
                country_of_origine = response.POST.get('country_of_origine')
                cost = response.POST.get('cost')
                owner = response.POST.get('owner')
                owner_contact = response.POST.get('owner_contact')
                 
                tag=response.user.username
                
                mid=registration_number+tag+model
                
                addmachine_save = machines(mid=mid,
                                            tag=tag,
                                            registration_number = registration_number,
                                            machine_type = machine_type,
                                            mark = mark,
                                            model = model,
                                            date_of_purches = date_of_purches,
                                            year_of_manufacture = year_of_manufacture,
                                            country_of_origine = country_of_origine,
                                            cost = cost,
                                            owner = owner,
                                            owner_contact=owner_contact,
                )
                
                addmachine_save.save()
                cleaned_data = addmachine.cleaned_data
                messages.success(response, 'Machine Registerd Sucussfully ')
                addmachine = machineFleet()
        else:
            addmachine = machineFleet()
    
        return render(response, "addmachine.html", { 'addmachine':addmachine })


def machine(response):
    
    try:
        current_username = response.user.username
        mchns = machines.objects
        allmachines = mchns.all()
        mymachines = allmachines.filter(tag__startswith=current_username)
        return render(response, "machine.html", {'mymachines':mymachines})
    except:
        
        return render(response, "machine.html", {})
    
    


    
    