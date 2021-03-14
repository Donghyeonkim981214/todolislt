from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import CreateView, ListView, DeleteView,  DetailView, UpdateView
from django.views.generic.edit import FormMixin

from django.urls import reverse, reverse_lazy

from . import models as todo_models
from . import forms

import datetime

from django.db.models import Q

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedOutOnlyView, CreatorOnlyView

def guest(request):
    guest_todo = todo_models.Todo.objects.filter(created_by__isnull=True)
    guest_todo.delete()
    return redirect(reverse('todo:home'))

class HomeView(FormMixin, ListView):
    model = todo_models.Todo
    context_object_name = 'todos'
    form_class = forms.TodoForm

    def get_template_names(self):
        if self.request.user.is_authenticated:
            names = ["todo/user_todo.html"]
        else:
            names = ["todo/guest_todo.html"]
        return names
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['doing'] = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = False).filter(Q(deadline__gte=datetime.date.today()) | Q(deadline__isnull=True)).order_by('-posted_day')[:5]
            context['success'] = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = True).order_by('-success_day')[:5]
            context['fail'] = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = False).filter(deadline__isnull=False).exclude(deadline__gte=datetime.date.today()).order_by('-deadline')[:5]
        else:
            context['guest_todo'] = todo_models.Todo.objects.filter(created_by__isnull=True).order_by('-posted_day')
        return super().get_context_data(**context)


class TodoListView(LoginRequiredMixin, ListView):
    model = todo_models.Todo
    template_name = "todo/list.html"
    paginate_by = 5
    context_object_name = "todo_list"

    def get_queryset(self):
        if self.kwargs['slug'] == 'Doing':
            queryset = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = False).filter(Q(deadline__gte=datetime.date.today()) | Q(deadline__isnull=True)).order_by('-posted_day')
        elif self.kwargs['slug'] == 'Success':
            queryset = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = True).order_by('-success_day')
        else:
            queryset = todo_models.Todo.objects.filter(created_by = self.request.user).filter(success = False).filter(deadline__isnull=False).exclude(deadline__gte=datetime.date.today())
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super(TodoListView, self).get_context_data(**kwargs)
        if self.kwargs['slug'] == 'Doing':
            context['sub'] = 'Doing'
        elif self.kwargs['slug'] == 'Success':
            context['sub'] = 'Success'
        else:
            context['sub'] = 'Fail'
        return context


class TodoDetailView(CreatorOnlyView, DetailView):
    model = todo_models.Todo
    template_name = "todo/detail.html"
    context_object_name = "todo"

class TodoUpdateView(CreatorOnlyView, UpdateView):
    model = todo_models.Todo
    template_name = "todo/update.html"
    form_class = forms.TodoForm
    context_object_name = "todo"

    def get_object(self): 
        todo = get_object_or_404(todo_models.Todo, pk=self.kwargs['pk'])
        return todo
    
    def form_valid(self, form):
        todo = form.save()
        todo.save()
        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('todo:detail', kwargs={'pk': self.kwargs['pk']})

def SuccessTodo(request, pk):
    todo = todo_models.Todo.objects.get(id = pk)
    todo.success = True
    todo.success_day = datetime.date.today()
    todo.save()
    try:
        next = request.POST.get('next')
        print(next)
        return redirect(resolve_url(next))
    except:
        return HttpResponseRedirect(reverse('todo:home'))


class TodoDeleteView(CreatorOnlyView, DeleteView):
    model = todo_models.Todo
    success_url = reverse_lazy('todo:home')

    def get_success_url(self):
        try:
            next = self.request.POST.get('next')
            return resolve_url(next)
        except:
            return self.success_url

class TodoCreateView(CreateView):
    template_name = "todo/create.html"
    form_class = forms.TodoForm
    success_url = reverse_lazy('todo:home')

    def form_valid(self, form):
        todo = form.save()
        if self.request.user.is_authenticated:
            todo.created_by = self.request.user
        print(todo.deadline)
        todo.save()
        return super().form_valid(form)