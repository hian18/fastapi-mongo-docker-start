import enum


class StateEnum(enum.Enum):
    WAIT_PAYMENT = "wait_payment"


class OrderEnum(enum.Enum):
    MENOR_VALOR = 1
    MAIOR_VALOR = 2
    DATA = 3

