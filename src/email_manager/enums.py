from enum import Enum


class MessageType(Enum):
    PASSWORD_RESET = 'PASSWORD_RESET'
    CONFIRM = 'CONFIRM'
    ACCOUNT_CREATION = 'ACCOUNT_CREATION'
