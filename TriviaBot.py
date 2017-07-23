#!/usr/bin/env python3

import discord
import re
import json
import random
import time
import operator
import string

token = ''
client = discord.Client()
IN_TRIVIA = False
QPATH = './JEOPARDY_QUESTIONS1.json'
qs = json.loads(open(QPATH, 'r').read())
q = None
ignore = {ord(c): None for c in string.punctuation}

random.seed(time.time())


class question(object):
    def __init__(self):
        global qs
        _q = random.choice(qs)
        self.question = _q['question']
        self.answer = _q['answer']
        self.category = _q['category']

    def check(self, message):
        msg = message.content.translate(ignore)
        if(re.search(msg, self.answer, re.IGNORECASE) and
           len(msg) >= int(0.5 * len(self.answer) - 1)):
            return True
        else:
            return False


def get_trivia_num(message):
    integer = re.compile(r'(\d+)')
    i = integer.search(message)
    if(i):
        return int(i.group())
    else:
        return 25


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
     
    if(not IN_TRIVIA and message.content.upper().startswith('!TRIVIA')):
        IN_TRIVIA = True
        players = {}
        q = question()
        await client.send_message(message.channel, 'Trivia has begun!')
        x = get_trivia_num(message.content)
        await client.send_message(message.channel, '%d to win.' % x)
        await client.send_message(message.channel,
                                  'Category is %s' % q.category)
        await client.send_message(message.channel, q.question)
        i = 0
        while(IN_TRIVIA):
            msg = await client.wait_for_message(timeout=30)
            if(msg is None):
                await client.send_message(message.channel,
                                          'Too slow! The answer was %s.' %
                                          (q.answer))
                q = question()
                await client.send_message(message.channel,
                                          'Category is %s' % q.category)
                await client.send_message(message.channel, q.question)
            elif(msg.author == client.user):
                continue
            elif(q.check(msg)):
                await client.send_message(msg.channel, 'Correct, %s! %s.' %
                                          (msg.author.nick, q.answer))
                try:
                    players[msg.author.nick] += 1
                except KeyError:
                    players[msg.author.nick] = 1
                scores = sorted(players.items(), key=operator.itemgetter(1))
                q = question()
                await client.send_message(message.channel,
                                          'Category is %s' % q.category)
                await client.send_message(msg.channel, q.question)
                i += 1
            elif(msg.content.upper().startswith('!PASS')):
                await client.send_message(msg.channel,
                                          'Passed. The answer was %s.'
                                          % (q.answer))
                q = question()
                await client.send_message(message.channel,
                                          'Category is %s' % q.category)
                await client.send_message(msg.channel, q.question)
            elif(msg.content.upper() == '!KILL'):
                IN_TRIVIA = False
                break
            elif(msg.content.upper().startswith('!TRIVIA') and
                 IN_TRIVIA and i > 0):
                await client.send_message(msg.channel,
                                          '%d to win. Leader is %s with %d.'
                                          % (x, scores[-1][0], scores[-1][1]))
            if(i > 0):
                if(scores[-1][1] >= x):
                    await client.send_message(msg.channel,
                                              'We got a winrar! Congrats @%s'
                                              % scores[-1][0])
                    IN_TRIVIA = False
                    break

client.run(token)
