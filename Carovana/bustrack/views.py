# views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from .forms import FeedbackForm
from .forms import ChildForm
from .forms import BusStopForm
from .models import Child
from .models import PopRegister
from .forms import PopRegisterForm
from .models import Parent, Operator, Bus, BusTrack, Feedback, BusMileage
from .forms import ParentForm, OperatorForm, BusForm, BusMileageForm
from .models import PopRegister, Exclusion, Login
from .forms import ExclusionForm, LoginForm

@login_required
def register_management(request):
    pop_register_data = PopRegister.objects.all()
    return render(request, 'admin/register_management.html', {'pop_register_data': pop_register_data})

@login_required
def add_operator(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin/admin_dashboard.html')
    else:
        form = OperatorForm()

    return render(request, 'admin/add_operator.html', {'form': form})

@login_required
def exclusion_management(request):
    if request.method == 'POST':
        form = ExclusionForm(request.POST)
        children = Child.objects.all()  # Retrieve children from the database

        if form.is_valid():
            form.save()
            return redirect('admin/register_management.html')  # Redirect to register management or another appropriate page
    else:
        form = ExclusionForm()

    exclusions = Exclusion.objects.all()

    return render(request, 'admin/exclusion_management.html', {'form': form, 'exclusions': exclusions})


@login_required
def bus_mileage(request):
    # Assuming there is a form to submit the bus mileage
    if request.method == 'POST':
        form = BusMileageForm(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = BusMileageForm()

    bus_mileage_entries = BusMileage.objects.all()
    return render(request, 'admin/bus_mileage.html', {'form': form, 'bus_mileage_entries': bus_mileage_entries})

@login_required
def feedback_inbox(request):
    feedback_entries = Feedback.objects.all()
    return render(request, 'admin/feedback_inbox.html', {'feedback_entries': feedback_entries})

@login_required
def add_operator(request):
    if request.method == 'POST':
        form = OperatorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin/operator_dashboard.html')
    else:
        form = OperatorForm()

    return render(request, 'admin/add_operator.html', {'form': form})

@login_required
def add_remove_parent(request):
    if request.method == 'POST':
        form = ParentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('admin/admin_dashboard.html')  # redirect for further additions or actions
    else:
        form = ParentForm()

    return render(request, 'admin/add_remove_parent.html', {'form': form})  #Return to add parent to try again


@login_required
def admin_landing(request):
    return render(request, 'admin/admin_dashboard.html')

# @login_required
#def register_management(request):
    #if request.method == 'POST':
        # Assuming you have a form to submit the pop register
       # form = PopRegisterForm(request.POST)

     #   if form.is_valid():
      #      form.save()
       #     return redirect('bustrack/templates/operators/operator_dashboard.html')  # Redirect to operator dashboard or another appropriate page
   # else:
    #    form = PopRegisterForm()

    #pop_register_data = PopRegister.objects.all()

    #return render(request, 'bustrack/templates/admin/register_management.html', {'form': form, 'pop_register_data': pop_register_data}) #

@login_required
def pop_register(request):
    children = Child.objects.all()  # Retrieve children from the database
    return render(request, 'operators/pop_register.html', {'children': children})


@login_required
def add_bus_stop(request):
    if request.method == 'POST':
        form = BusStopForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('operators/operator_dashboard.html')
    else:
        form = BusStopForm()

    return render(request, 'operators/add_bustop.html', {'form': form})


@login_required
def add_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('operators/operator_dashboard.html')
    else:
        form = ChildForm()

    return render(request, 'operators/add_child.html', {'form': form})


@login_required
def bus_tracking(request):
    # a variable `bus_location` containing the bus coordinates
    bus_location = {'latitude': 37.7749, 'longitude': -122.4194}

    return render(request, 'parents/bustracking.html', {'bus_location': bus_location})


@login_required
def send_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            message = form.cleaned_data['message']
            user = request.user

            # Creates a new Feedback instance and saves it to the database
            Feedback.objects.create(user=user, message=message)

            # Provides feedback to the user that the message was sent
            return render(request, 'parents/parentfeedbacksent.html')
    else:
        form = FeedbackForm()

    return render(request, 'parents/parentfeedback.html', {'form': form})


@csrf_protect
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('admin/admin_dashboard.html')
            elif user.is_staff:
                return redirect('operators/operator_dashboard.html')
            else:
                return redirect('parents/parent_dashboard.html')
        else:
            # Handle invalid login credentials
            return render(request, 'login/login.html', {'error': 'Invalid username or password'})

    return render(request, 'login/login.html')

@login_required
def custom_logout(request):
    logout(request)
    return redirect('login/login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin/admin_dashboard.html')

@login_required
def operator_dashboard(request):
    return render(request, 'operators/operator_dashboard.html')

@login_required
def parent_dashboard(request):
    return render(request, 'parents/parents_dashboard.html')
