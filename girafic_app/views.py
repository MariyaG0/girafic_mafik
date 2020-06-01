from django.shortcuts import render
from girafic_app.forms import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
# from girafic_app.forms import SomeForm
from django.contrib.auth.decorators import login_required
from .forms import UserForm, ClientDataForm, BoxOrderForm, DreamcatcherOrderForm, LetterOrderForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import Box, Dreamcatcher, Catalog, Letter, Order

# Create your views here.
def boxes(request):
    boxes = Catalog.objects.filter(name='Текущий').last().box.all()
    # some_form = SomeForm()
    # if request.method == 'POST':
    #     some_form = SomeForm(request.POST)
    #     if some_form.is_valid():
    #         print('Валидация прошла успешно!')
    #         print('name: ' + some_form.cleaned_data['name'])
    #         print('mail: ' + some_form.cleaned_data['mail'])
    #         print('text: ' + some_form.cleaned_data['text'])
    #     else:
    #         print('Ты тупой кусок говна!')
    return render(request, 'boxes.html', {'boxes': boxes})#'some_form': some_form})


def catalog(request):
    box = Catalog.objects.filter(name='Текущий').last().box.all().last()
    dream = Catalog.objects.filter(name='Текущий').last().dreamcatcher.all().last()
    letter = Catalog.objects.filter(name='Текущий').last().letter.all().last()
    box_ = Catalog.objects.filter(name='Архивный').last().box.all().last()
    dream_ = Catalog.objects.filter(name='Архивный').last().dreamcatcher.all().last()
    letter_ = Catalog.objects.filter(name='Архивный').last().letter.all().last()
    last_done = sorted(list(filter(None, [box_, dream_, letter_])), key=lambda obj: obj.data, reverse=True)[0]
    type_of_item = None
    if isinstance(last_done, Box):
        type_of_item = 'box'
    if isinstance(last_done, Dreamcatcher):
        type_of_item = 'dream'
    if isinstance(last_done, Letter):
        type_of_item = 'letter'
    return render(request, 'catalog.html', {'box': box, 'dream': dream, 'letter': letter, 'last_done': last_done, 'type_of_item': type_of_item})


@login_required(login_url='login')
def form(request):
    client_data_form = ClientDataForm()
    box_order_form = BoxOrderForm(prefix='box')
    dreamcatcher_order_form = DreamcatcherOrderForm(prefix='dream')
    letter_order_form = LetterOrderForm(prefix='letter')
    box = None
    dreamcatcher = None
    letter = None
    if request.GET.get('type_') == 'box':
        box = Box.objects.get(id=request.GET.get('id_'))
        box_order_form = BoxOrderForm(prefix='box', initial={
            'lenght': box.lenght,
            'width': box.width,
            'height': box.height,
            'name': str(box)
        })
    if request.GET.get('type_') == 'dreamcatcher':
        dreamcatcher = Dreamcatcher.objects.get(id=request.GET.get('id_'))
        dreamcatcher_order_form = DreamcatcherOrderForm(prefix='dream', initial={
            'diameter': dreamcatcher.diameter,
            'name': str(dreamcatcher)
        })
    if request.GET.get('type_') == 'letter':
        letter = Letter.objects.get(id=request.GET.get('id_'))
        letter_order_form = LetterOrderForm(prefix='box', initial={
            'lenght': letter.lenght,
            'width': letter.width,
            'color': letter.color,
            'name': str(letter)
        })
    if request.method == "POST":
        order = Order.create(request.user)
        order.save()
        client_data_form = ClientDataForm(request.POST)
        if client_data_form.is_valid():
            client_data = client_data_form.save(commit=False)
            client_data.order = order
            client_data.save()
        if 'button_box_order_form' in request.POST:
            box_order_form = BoxOrderForm(request.POST, prefix='box')
            if box_order_form.is_valid():
                box_order = box_order_form.save(commit=False)
                box_order.order = order
                box_order.save()
                return HttpResponseRedirect('{}?sent=True'.format(reverse('form', kwargs={})))
        elif 'button_dreamcatcher_order_form' in request.POST:
            dreamcatcher_order_form = DreamcatcherOrderForm(request.POST, prefix='dream')
            if dreamcatcher_order_form.is_valid():
                dreamcatcher_order = dreamcatcher_order_form.save(commit=False)
                dreamcatcher_order.order = order
                dreamcatcher_order.save()
                return HttpResponseRedirect('{}?sent=True'.format(reverse('form', kwargs={})))
        elif 'button_letter_order_form' in request.POST:
            letter_order_form = LetterOrderForm(request.POST, prefix='letter')
            if letter_order_form.is_valid():
                letter_order = letter_order_form.save(commit=False)
                letter_order.order = order
                letter_order.save()
                return HttpResponseRedirect('{}?sent=True'.format(reverse('form', kwargs={})))
            print('button_letter_order_form')
    return render(request, 'form.html', {
        'client_data_form': client_data_form,
        'box_order_form': box_order_form,
        'dreamcatcher_order_form': dreamcatcher_order_form,
        'letter_order_form': letter_order_form,
        'box': box,
        'dreamcatcher': dreamcatcher,
        'letter': letter,
        'sent': request.GET.get('sent', False)
    })


def index(request):
    box = Catalog.objects.filter(name='Текущий').last().box.all().last()
    dream = Catalog.objects.filter(name='Текущий').last().dreamcatcher.all().last()
    letter = Catalog.objects.filter(name='Текущий').last().letter.all().last()
    last_actual = sorted(list(filter(None, [box, dream, letter])), key=lambda obj: obj.data, reverse=True)[0]
    type_of_item = None
    if isinstance(last_actual, Box):
        type_of_item = 'box'
    if isinstance(last_actual, Dreamcatcher):
        type_of_item = 'dream'
    if isinstance(last_actual, Letter):
        type_of_item = 'letter'
    return render(request, 'index.html', {'last_actual': last_actual, 'type_of_item': type_of_item})


def ready(request):
    boxes_ = Catalog.objects.filter(name='Архивный').last().box.all()
    dreamcatchers = Catalog.objects.filter(name='Архивный').last().dreamcatcher.all()
    letter = Catalog.objects.filter(name='Архивный').last().letter.all()
    return render(request, 'ready.html', {'boxes_': boxes_, 'dreamcatchers': dreamcatchers, 'letter': letter})


@login_required(login_url='login')
def review(request):
    review_form = ReviewForm()
    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            curr_review = review_form.save(commit=False)
            curr_review.user = request.user
            curr_review.save()
            return HttpResponseRedirect('{}?sent=True'.format(reverse('review', kwargs={})))
    return render(request, 'review.html', {'review_form': review_form, 'sent': request.GET.get('sent', False)})


def sleep(request):
    dreamcatchers = Catalog.objects.filter(name='Текущий').last().dreamcatcher.all()
    return render(request, 'sleep.html', {'dreamcatchers': dreamcatchers})

def sign_up(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            new_user = User.objects.create_user(**user_form.cleaned_data)
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
            else:
                print('invalid login')
            return redirect('index')
    return render(request, 'registration/sign_up.html', {'user_form': user_form})

@login_required(login_url='login')
def profile(request):
    user = request.user
    orders = user.order.all()
    return render(request, 'profile.html', {'user': user, 'orders': orders})
