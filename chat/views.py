from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.db.models.functions import Lower
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from upprpo import settings
from .models import Chat, Message, MessageSerializer, ChatSerializer
from django.urls import reverse
from django.views import generic, View
from django.template import loader
from django.http import Http404
from .forms import MessageForm, MultiForm
from django.contrib.auth.models import User
from os import path
from PIL import Image


def type_file(name):
    _, ext = path.splitext(name)
    print(ext)
    for type_ in ["png", "jpg", "jpeg"]:
        if ext == '.' + type_:
            return "image"
    return "file"


def user_auth_check(request):
    if not request.user.is_authenticated:
        message = {}
        message['ans'], message['type'] = "please log in to access this page", 'warning'
        message['support': 'white', 'chat'] = ''
        message['chats'] = ''
        return render(request, 'chat/index.html', message)
    return None


class DialogsView(generic.ListView):
    # def get(self, request):
    #     print('user id = ', request.user.id)
    #     chats = Chat.objects.filter(members=request.user.id)
    #     print('chats = ', chats.query)
    #     return render(request, 'chat/index.html', {'user_profile': request.user, 'chats': chats})
    template_name = 'chat/index.html'
    context_object_name = 'chats'

    def get_queryset(self):
        self.list_mem = None
        if not self.request.user.is_authenticated:
            return None
        self.list_mem = Chat.objects.filter(members=self.request.user)
        return self.list_mem

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DialogsView, self).get_context_data(**kwargs)
        message = {'ans': '', 'type': 'danger', 'chats': self.list_mem}
        message['page'] = {'home': 'white', 'support': 'white', 'chat': 'secondary', 'about': 'white', 'games': 'white',
                           'hz': 'white'}
        if self.request.user.is_authenticated:
            res = {**message, **context}
        else:
            message['ans'], message['type'] = "please log in to access this page", 'warning'
            res = message
        return res


class MessagesView(generic.ListView):

    def post(self, request, chat_id):
        print("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaatpravilos`")
        form = MessageForm(request.POST, request.FILES)
        if form.is_valid() or request.FILES:
            cd = form.cleaned_data
            message = Message()
            # message.chat_id = chat_id
            chat = Chat.objects.get(id=chat_id)
            message.text = cd['text']
            message.author = request.user
            if cd["file"]:
                if type_file(cd["file"].name) == "image":
                    message.image = request.FILES['file']
                else:
                    message.file = request.FILES['file']
            message.save()
            chat.message_set.add(message)
        return redirect(reverse('chat:chat', kwargs={'chat_id': chat_id}))

    def get_context_data_(self, *, object_list=None, **kwargs):
        # context = super(MessagesView, self).get_context_data(**kwargs)
        message = {'ans': '', 'type': 'danger', 'support': 'white', 'chat': self.messages}
        message['page'] = {'home': 'white', 'support': 'white', 'chat': 'secondary', 'about': 'white', 'games': 'white',
                           'hz': 'white'}
        message['form'] = MultiForm()
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
        self.messages = self.chat.message_set.order_by('-id')
        # print(self.messages.all()[0].text)
        context = self.get_context_data_()
        check = user_auth_check(request)
        if check:
            return check
        return render(request, 'chat/index.html', self.get_context_data_())


def createDialog(request):
    u_name = request.GET.get('u_name')
    second_user = None
    try:
        second_user = User.objects.get(username=u_name)
    finally:
        if not second_user:
            message = {'ans': 'This user doesn`t exist', 'type': 'danger',
                       'chats': Chat.objects.filter(members=request.user),
                       'page': {'home': 'white', 'support': 'white', 'chat': 'secondary', 'about': 'white',
                                'games': 'white', 'hz': 'white'}}
            return render(request, 'chat/index.html', message)
        model = Chat()
        model.save()
        model.members.add(second_user)
        model.members.add(request.user)
        model.type = 'dialog'
        return redirect('/chat')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


def search(request):
    if is_ajax(request):
        q = request.GET.get('term', '')
        results = []
        if len(q):
            results = list(User.objects.filter(username__istartswith=q).values_list(Lower('username'), flat=True))
        return JsonResponse(results, safe=False)
    else:
        return createDialog(request)


class GetMessagesInfoView(APIView):

    def get(self, request):
        queryset = Message.objects.all()
        serializer_for_queryset = MessageSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)


class GetChatsInfoView(APIView):

    def get(self, request):
        queryset = None
        #if request.user.is_authenticated:
        queryset = Chat.objects.filter(members=request.user)
        serializer_for_queryset = ChatSerializer(
            instance=queryset,  # Передаём набор записей
            many=True  # Указываем, что на вход подаётся именно набор записей
        )
        return Response(serializer_for_queryset.data)



