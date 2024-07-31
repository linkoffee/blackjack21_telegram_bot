### blackjack21_telegram_bot

`The bot is designed to play "blackjack" a.k.a "21" - a game known all over the world.`

> [!NOTE]
> This is the first demo version of this bot -> `0.0.1`

---

### Аt the moment the bot can
- Play, draws cards for himself (so far AI is weak and he almost always loses)
- Show the rules of the game

### In the future it is planned to add
- Rating system
- The ability to play not only against a bot, but also against other players
- The ability to change the game language(at the moment only **Russian** is available)
- More interactive buttons

---

### Stack
- python 3.9
- pyTelegramBotAPI 4.15.2

---

### How to install and use:
1. Clone the remote repository and go to it:
```console
git clone 
```
```console
cd blackjack21_telegram_bot 
```
2. Create and activate a virtual environment:
```console
python3 -m venv env
```
```console
source env/bin/activate
```
3. Install all required dependencies:
```console
python3 -m pip install --upgrade pip
```
```console
pip install -r requirements.txt
```
4. Create your telegram bot [`here`](https://t.me/BotFather)
5. Copy your bot's API key, you can do it right here using `@BotFather`
6. In the root dir, create a file `.env`, and fill it in according to the example from the file `.env.example`
7. Run the bot:
```console
python main.py
```

---

Author: [Mikhail Kopochinskiy](https://github.com/linkoffee)
