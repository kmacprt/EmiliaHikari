from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 1131653685  # my telegram ID
    OWNER_USERNAME = "kavinduaj"  # my telegram username
    API_KEY = "1422942998:AAE270WdtC_vqLWHfIzBNWVwsm_LfJQqlwo"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost:5432/database'  # sample db credentials
    MESSAGE_DUMP = '-1001367838165' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [1131653685]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
