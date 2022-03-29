from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

from upprpo import settings
from .models import Chat, Message
from django.urls import reverse
from django.views import generic, View
from django.template import loader
from django.http import Http404
from .forms import MessageForm
from django.contrib.auth.models import User


class DialogsView(generic.ListView):
    # def get(self, request):
    #     print('user id = ', request.user.id)
    #     chats = Chat.objects.filter(members=request.user.id)
    #     print('chats = ', chats.query)
    #     return render(request, 'chat/index.html', {'user_profile': request.user, 'chats': chats})
    template_name = 'chat/index.html'
    context_object_name = 'chats'

    def get_queryset(self):
        self.list_mem = Chat.objects.filter(members=self.request.user)
        return self.list_mem

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DialogsView, self).get_context_data(**kwargs)
        message = {'ans': '', 'type': 'danger', 'chats':self.list_mem}
        message['page'] = {'home': 'white', 'chat': 'secondary', 'about': 'white', 'games': 'white', 'hz': 'white'}
        if self.request.user.is_authenticated:
            res = {**message, **context}
        else:
            message['ans'], message['type'] = "please log in to access this page", 'warning'
            res = message
        return res


class MessagesView(generic.ListView):

    def post(self, request, chat_id):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        form = MessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            message = Message()
            # message.chat_id = chat_id
            chat = Chat.objects.get(id=chat_id)
            message.text = cd['text']
            message.author = request.user
            message.save()
            chat.message_set.add(message)
        return redirect(reverse('chat:chat', kwargs={'chat_id': chat_id}))

    def get_context_data_(self, *, object_list=None, **kwargs):
        #context = super(MessagesView, self).get_context_data(**kwargs)
        message = {'ans': '', 'type': 'danger', 'chat': self.messages}
        message['page'] = {'home': 'white', 'chat': 'secondary', 'about': 'white', 'games': 'white', 'hz': 'white'}
        message['form'] = MessageForm()
        # if self.request.user.is_authenticated:
        #     res = {**message, **context}
        # else:
        #     message['ans'], message['type'] = "please log in to access this page", 'warning'
        res = message
        return res

    template_name = 'chat/index.html'

    context_object_name = 'chat'

    # def get_queryset(self):
    #     self.this_chat = Message.objects.filter(members=self.request.Us)
    #     return self.list_mem

    def get(self, request, chat_id):
        self.chat = Chat.objects.get(id=chat_id)
        self.messages = self.chat.message_set
        # print(self.messages.all()[0].text)
        return render(request, 'chat/index.html', self.get_context_data_())


def createDialog(request):
    u_name = request.GET.get('u_name')
    model = Chat()
    model.save()
    model.members.add(User.objects.get(username=u_name))
    model.members.add(request.user)
    model.type = 'dialog'
    return redirect('/chat')

