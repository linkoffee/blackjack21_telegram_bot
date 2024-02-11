"""Here is all the basic logic of the game in '21'."""


class Game:
    """Class contains methods of game in '21'."""

    # Global variables:
    # Belongs: Attributes of class.
    sum_of_player_points: int = 0
    sum_of_bot_points: int = 0

    # Global dictionaries:
    # Belongs: Attributes of class.
    all_using_player_cards: dict = {}
    all_using_bot_cards: dict = {}

    # Class constructor.
    def __init__(self) -> None:
        """Class constructor."""
        self.all_using_player_cards = Game.all_using_player_cards
        self.all_using_bot_cards = Game.all_using_bot_cards
        self.sum_of_player_points = Game.sum_of_player_points
        self.sum_of_bot_points = Game.sum_of_bot_points

    # Class method play().
    def play(self, letter, bot_name, random_module, dict_name, bot_module):
        """First step of game. Initial deal of cards to a player."""
        self.reset(Game)
        random_card = random_module(list(dict_name.keys()))
        random_card_value = dict_name[random_card]
        self.all_using_player_cards[random_card] = random_card_value
        for card_value in self.all_using_player_cards.values():
            self.sum_of_player_points += card_value
        keyboard1 = bot_module.ReplyKeyboardMarkup(resize_keyboard=True)
        button_more = bot_module.KeyboardButton('Взять ещё')
        button_pass = bot_module.KeyboardButton('Достаточно')
        keyboard1.add(button_more, button_pass)
        bot_name.send_message(letter.chat.id, 'У вас на руках карта: '
                              f'{random_card} '
                              f'(всего {self.sum_of_player_points} очк.)',
                              reply_markup=keyboard1)

    # Class method reset().
    def reset(self):
        """When the game ends, all settings are reset to default."""
        self.all_using_player_cards.clear()
        self.all_using_bot_cards.clear()
        self.sum_of_player_points = 0
        self.sum_of_bot_points = 0

    # Class method more().
    def more(self, letter, bot_name, random_module, dict_name, bot_module):
        """Run when player push button 'Взять ещё'."""
        self.sum_of_player_points = 0
        random_card = random_module(list(dict_name.keys()))
        random_card_value = dict_name[random_card]
        self.all_using_player_cards[random_card] = random_card_value
        for card_value in self.all_using_player_cards.values():
            self.sum_of_player_points += card_value
        all_cards_str = ' '.join(list(self.all_using_player_cards.keys()))
        bot_name.send_message(letter.chat.id, 'Ваша новая карта: '
                              f'{random_card}\n'
                              f'Все карты: {all_cards_str} '
                              f'(всего {self.sum_of_player_points} очк.)')
        if self.sum_of_player_points > 21:
            bot_name.send_message(letter.chat.id,
                                  'Перебор, вы проиграли :('
                                  ' Сыграем ещё раз? -> /play',
                                  reply_markup=bot_module.ReplyKeyboardRemove()
                                  )

    # Class method enough().
    def enough(self, letter, bot_name, random_module,
               dict_name, bot_username):
        """Run when player push button 'Достаточно'."""
        while self.sum_of_bot_points < 21:
            if self.sum_of_bot_points < self.sum_of_player_points:
                self.sum_of_bot_points = 0
                random_card = random_module(list(dict_name.keys()))
                random_card_value = dict_name[random_card]
                self.all_using_bot_cards[random_card] = random_card_value
                for card_value in self.all_using_bot_cards.values():
                    self.sum_of_bot_points += card_value
                all_cards_str = ' '.join(list(self.all_using_bot_cards.keys()))
                bot_name.send_message(letter.chat.id,
                                      f'Карты {bot_username}: '
                                      f'{all_cards_str} '
                                      f'(всего {self.sum_of_bot_points} очк.)')
            else:
                break
        self.check_win(self, letter=letter, bot_name=bot_name,
                       bot_username=bot_username)

    # Class method check_win().
    def check_win(self, letter, bot_name, bot_username):
        """Check who win a game."""
        player_name = letter.from_user.first_name
        if (self.sum_of_player_points > self.sum_of_bot_points or
                self.sum_of_bot_points > 21):
            bot_name.send_message(letter.chat.id,
                                  f'Поздравляю, {player_name}, ты победил!'
                                  ' Сыграем ещё раз? -> /play')
        elif (self.sum_of_player_points < self.sum_of_bot_points or
              self.sum_of_player_points > 21):
            bot_name.send_message(letter.chat.id,
                                  f'Эх, не повезло, победил {bot_username} :('
                                  ' Сыграем ещё раз? -> /play')
        else:
            bot_name.send_message(letter.chat.id,
                                  'Ого, кажется у нас...... ничья -_-'
                                  ' Сыграем ещё раз? -> /play')
