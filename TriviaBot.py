#!/usr/bin/env python

import discord
from discord.ext import commands
import re
import json
import random
import time

token = <token>
client = discord.Client()
IN_TRIVIA = False
QPATH = <path/to/question/file>
qs = json.loads(open(QPATH, 'r').read())
q = None

random.seed(time.time())

class question:
    def __init__(self):
        global qs
        _q = random.choice(qs)
        self.question = _q['question']
        self.answer = _q['answer']
                    
    def check(self, message):
        if (re.search(message, self.answer, re.IGNORECASE) and 
            len(message) >= 3):
            return True
        else:
            return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    global IN_TRIVIA
    global q
    
    if (not IN_TRIVIA and message.content.upper().startswith('!TRIVIA')):
        IN_TRIVIA = True
        q = question()
        await client.send_message(message.channel, 'Trivia has begun!')
        await client.send_message(message.channel, q.question)
        i = 0
        while(True):
            msg = await client.wait_for_message(timeout=15)
            if (msg is None):
                await client.send_message(message.channel, 
                                          'Too slow! The answer was %s.' % 
                                          (q.answer))
                q = question()
                await client.send_message(message.channel, q.question)
            elif (msg.author == client.user):
                continue
            elif (q.check(msg.content)):
                await client.send_message(msg.channel, 'Correct, %s! %s.' % 
                                          (msg.author, q.answer))
                q = question()
                await client.send_message(msg.channel,q.question)
                i+=1
            elif (msg.content.upper() == '!KILL'):
                break
            if (i >= 25):
                break
        
client.run(token)
