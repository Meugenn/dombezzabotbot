import telebot.types as types
from const import imgs
import os

# def get_imgs(n):
#     images = []
#     if n in imgs:
#         i = 1
#         ims = []
#         while i <= imgs[n]:
#             try:
#                 ims.append(types.InputMediaPhoto(open(f'img\\{n}\\{i}.jpg', 'rb')))
#             except Exception as e:
#                 break
#             if i % 10 == 0:
#                 images.append(ims)
#                 ims = []
#             i += 1
#         if ims:
#             images.append(ims)
#     return images


def get_imgs(n):
    directory = f'img\\{n}'
    images = []
    addresses = sorted(filter(lambda x: x.endswith('.jpg') or
                                 x.endswith('.png') or
                                 x.endswith('.jpeg'),os.listdir(directory)))
    i = 1
    ims = []
    for addr in addresses:
        try:
            ims.append(types.InputMediaPhoto(open(f'img\\{n}\\{addr}', 'rb')))
        except Exception as e:
            break
        if i % 10 == 0:
            images.append(ims)
            ims = []
        i += 1
    if ims:
        images.append(ims)
    return images


def back_markup(ids=[]):
    markup = types.InlineKeyboardMarkup()
    back_data = 'back'
    for i in ids:
        back_data += f'_{i}'
    markup.add(types.InlineKeyboardButton('Назад', callback_data=back_data))
    return markup


def main_markup():
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(
        '1. Как зарегистрироваться в приложении?',
        callback_data='1'))
    markup.add(types.InlineKeyboardButton(
        '2. Как пополнить баланс?',
        callback_data='2'))

    markup.add(types.InlineKeyboardButton(
        '3. Как принять заявку?',
        callback_data='3'))

    markup.add(types.InlineKeyboardButton(
        '4. Как отказаться от заявки и в каких случаях происходит возврат комиссии? ',
        callback_data='4'))

    markup.add(types.InlineKeyboardButton(
        '5. Как найти и закрыть заявку после выполнения работ? ',
        callback_data='5'))

    markup.add(types.InlineKeyboardButton(
        '6. Для чего нам необходим скан/фото Вашего паспорта? ',
        callback_data='6'))

    markup.add(types.InlineKeyboardButton(
        '7. Кто отвечает за качество проведённых работ ',
        callback_data='7'))

    markup.add(types.InlineKeyboardButton(
        '8. Сколько стоит использование сервиса «Дом Без Забот»?',
        callback_data='8'))

    markup.add(types.InlineKeyboardButton(
        '9. Как быть если выполнение принятой/оплаченной заявки сорвалось? ',
        callback_data='9'))

    markup.add(types.InlineKeyboardButton(
        '10. Как вывести средства с баланса? ',
        callback_data='10'))

    return markup
