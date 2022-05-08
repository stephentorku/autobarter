from unicodedata import name
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Chat, Message
from django.http import HttpResponse, JsonResponse
import sweetify
# Create your views here.


def chat(request, id):
    chat_id =id
    chat = Chat.objects.get(id=chat_id)
    context={'chat_id': chat_id, 'chat': chat}
    return render(request, 'chat/chat.html', context)

def checkChat(request):
    username = request.POST['username']
    vendor = User.objects.get(username=username)
    buyer = request.user

    if Chat.objects.filter(vendor=vendor, buyer=buyer ).exists():
        chat = Chat.objects.get(vendor=vendor, buyer=buyer)
        sweetify.success(request, 'Redirecting to chat')
        return redirect('chat/'+str(chat.id))
    else:
        new_chat = Chat.objects.create(vendor=vendor, buyer=buyer)
        new_chat.save()
        sweetify.success(request, 'Redirecting to chat')
        return redirect('chat/'+ str(new_chat.id))



def send(request):
    text = request.POST['message']
    chat_id = request.POST['chat_id']
    chat = Chat.objects.get(id=chat_id)
    sender = request.user
    sender_name = request.user.first_name + " " + request.user.last_name

    new_message = Message.objects.create(text=text, chat=chat, sender=sender, sender_name = sender_name)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, chat_id):
    chat = Chat.objects.get(id=chat_id)

    messages = Message.objects.filter(chat=chat)
    return JsonResponse({"messages":list(messages.values())})

def getChats(request):
    user = request.user

    if user.groups.filter(name="vendor"):
        chats = Chat.objects.filter(vendor=user)
        #last_message = Message.objects.filter(sender=user).last().text
        context={'chats': chats}
        return render(request, 'chat/all_chats.html', context)
    else:
        chats = Chat.objects.filter(buyer=user)
        #last_message = Message.objects.filter(sender=user).last().text
        context={'chats': chats}
        return render(request, 'chat/all_chats.html', context)
