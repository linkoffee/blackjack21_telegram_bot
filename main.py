"""
Here is main path of bot.

This project - is my debut, it was made entirely by me,
so i cant vouch for the fact that errors or bugs
may occur while the bot is running,
if you write anything, I will definitely fix it.

I wish each of you to enjoy playing "21"
as much as possible with my clumsy bot =)
"""

from random import choice
import os

import telebot  # type: ignore
from telebot import types
from dotenv import load_dotenv

from pyblackjack import Constants as Const
from pyblackjack import Game


load_dotenv()
dealer_bot = telebot.TeleBot(os.getenv('TOKEN'))


@dealer_bot.message_handler(commands=['start'])
def start_bot(message):
    """
    Start bot, send greeting.

    start_message -> str type object, here is greeting message,
    where message.from_user.first_name -> first part of user nickname.
    """
    start_message = (
        'Здравствуйте, добро пожаловать в Двадцать Одно, '
        f'<b>{message.from_user.first_name}!</b>\n'
        'Чтобы посмотреть список доступных действий, введите: <u>/help</u>'
    )
    dealer_bot.send_message(message.chat.id, start_message, parse_mode='html')


@dealer_bot.message_handler(commands=['help'])
def help(message):
    """Send all commands available to the bot."""
    dealer_bot.send_message(message.chat.id, Const.HELP, parse_mode='html')


@dealer_bot.message_handler(commands=['play'])
def play_command(message):
    """
    Start game, request to the Game class.

    Creating and displaying game buttons.
    """
    dealer_bot.send_message(message.chat.id, 'Игра начинается!!!')
    Game.play(self=Game, letter=message, bot_name=dealer_bot,
              random_module=choice, dict_name=Const.CARDS,
              bot_module=types)


@dealer_bot.message_handler(commands=['rules'])
def rules(message):
    """Send rules of a game as a str type."""
    dealer_bot.send_message(
        message.chat.id, Const.RULES, parse_mode='html')


@dealer_bot.message_handler(content_types=['text'])
def buttons(message):
    """Draws another card if the button is pressed."""
    if message.text == 'Взять ещё':
        Game.more(self=Game, letter=message, bot_name=dealer_bot,
                  random_module=choice, dict_name=Const.CARDS,
                  bot_module=types)
    if message.text == 'Достаточно':
        bot_player_name = dealer_bot.get_me().username
        dealer_bot.send_message(message.chat.id,
                                'Вы пасуете, ваш ход окончен.\n'
                                f'Ход делает <b>{bot_player_name}</b>',
                                parse_mode='html',
                                reply_markup=types.ReplyKeyboardRemove())
        Game.enough(self=Game, letter=message, bot_name=dealer_bot,
                    random_module=choice, dict_name=Const.CARDS,
                    bot_username=bot_player_name)


dealer_bot.polling(non_stop=True)
