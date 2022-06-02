
import json
from ur

from channels import Group
from channels.sessions import channel_session



@channel_session
def ws_add(msg,room):
    Group("chat").add(msg.reply_channel)
    msg.channel_session['room'] = room


@channel_session
def ws_echo(msg):
    room = msg.channel_session['room']

    Group("chat-%s" % room ).send({
        "text": msg.content['text'],
    })
    #msg.reply_channel.send({
    #    'text': msg.content['text'],
    #})