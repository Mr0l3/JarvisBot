<p align="center">
    <img src="jarvisBot-image.png" width="180">
    <h3 align="center">JarvisBot</h3>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project 

With the new WhatsApp Terms, a lot of people decided to move to Telegram. And since most of them will probably create groups and stuff I decided to create a JarvisBot to help them manage their groups.

### Built With
* [Python](https://www.python.org/)
* [Python Telegram Bot Framework](https://python-telegram-bot.org/)

<!-- GETTING STARTED -->
## Getting Started
### Prerequisites
* Install pipenv if you don't have it installed
    ```sh
    sudo apt update && sudo apt install pipenv -y
    ```
### Installation
1. [Get your free Telegram API Token](https://www.siteguarding.com/en/how-to-get-telegram-bot-api-token)
2. Clone the repo
    ```sh
    git clone https://github.com/Mr0l3/JarvisBot.git
    ```
3. Install dependencies
    ```sh
    pipenv install
    ```
4. Enter your Telegram API token in `Bot.py`
    ```PY
    __TOKEN = 'TOKEN HERE'
    ```

<!-- USAGE EXAMPLES -->
## Usage
To run the bot, do the following:

1. Go to JarvisBot directory
    ```sh
    cd path/to/JarvisBot
    ```
2. Run JarvisBot
    ```sh
    pipenv run python jarvisBot/main.py
    ```

To stop the bot, just press Ctrl+C in the terminal and wait a few seconds until the bot stop execution

## Contributing
1. Fork the Project
2. Create your Feature Branch
    ```sh
    git checkout -b feature/AmazingFeature
    ```
3. Commit your Changes 
    ```sh
    git commit -m '[FEAT] Add some AmazingFeature'
    ```
4. Push to the Branch
    ```sh
    git push origin feature/AmazingFeature
    ```
5. Open a Pull Request
