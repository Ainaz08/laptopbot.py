from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, LabeledPrice
from aiogram.utils import executor

API_TOKEN = '7129173571:AAGM1EBRdWKWQQObDKw2r2-UvM_kRYt1fS0'
PROVIDER_TOKEN = '381764678:TEST:38051'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

start_buttons = [
    types.KeyboardButton('О нас'),
    types.KeyboardButton('Каталог'),
    types.KeyboardButton('Адрес'),
    types.KeyboardButton('Контакты'),
    types.KeyboardButton('Помощь'),
    types.KeyboardButton('Акции'),
    types.KeyboardButton('Оставить отзыв'),
    types.KeyboardButton('Оплатить')
]

start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer(f'Здравствуйте, {message.from_user.full_name}!', reply_markup=start_keyboard)

@dp.message_handler(text='О нас')
async def about_us(message: types.Message):
    await message.reply("Добро пожаловать в наш магазин ноутбуков! Мы предлагаем широкий выбор ноутбуков для любых задач.")

@dp.message_handler(text='Адрес')
async def send_adress(message: types.Message):
    await message.reply("Наш адрес: Город Ош, ул Масалиева, 100")
    await message.reply_location(42.874621, 74.612587)

@dp.message_handler(text='Контакты')
async def contact(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, вот наши контакты:')
    await message.answer_contact("+996708424268", "Айназ", "Маматиса кызы")
    await message.answer_contact("+996706894095", "Маматиса", "Акматов")

catalog_buttons = [
    types.KeyboardButton("Ноутбуки"),
    types.KeyboardButton("Аксессуары"),
    types.KeyboardButton("Оставить заявку"),
    types.KeyboardButton("Назад")
]

catalog_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*catalog_buttons)

@dp.message_handler(text='Каталог')
async def catalog(message: types.Message):
    await message.answer("Вот наш каталог ноутбуков и аксессуаров:", reply_markup=catalog_keyboard)

@dp.message_handler(text='Ноутбуки')
async def laptops(message: types.Message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo='https://www.google.com/imgres?q=%D0%9C%D0%BE%D1%89%D0%BD%D1%8B%D0%B9%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%20%D0%B4%D0%BB%D1%8F%20%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B%20%D0%B8%20%D0%B8%D0%B3%D1%80.%20%D0%A6%D0%B5%D0%BD%D0%B0%2060%2C000%20%D1%81%D0%BE%D0%BC&imgurl=https%3A%2F%2Fimg5.lalafo.com%2Fi%2Fposters%2Foriginal%2F8f%2F71%2F69%2Fnoutbuk-asus-16-gb-ozu-intel-core-i5-156-dla-raboty-uceby-pamat-ssd-id-37194753-794469839.jpeg&imgrefurl=https%3A%2F%2Flalafo.kg%2Fkant%2Fads%2Fnoutbuk-asus-16-gb-ozu-intel-core-i5-156-dla-raboty-uceby-pamat-ssd-id-37194753&docid=YYmhtNSyyGjd5M&tbnid=HuGNuRpRv8A3yM&vet=12ahUKEwjekOu7ya6IAxURIhAIHU1dKt8QM3oECBYQAA..i&w=1024&h=768&hcb=2&itg=1&ved=2ahUKEwjekOu7ya6IAxURIhAIHU1dKt8QM3oECBYQAA',
        caption="Мощный ноутбук для работы и игр. Цена 60,000 сом."
    )

@dp.message_handler(text='Аксессуары')
async def accessories(message: types.Message):
    await bot.send_photo(
        chat_id=message.chat.id,
        photo='https://www.google.com/imgres?q=%D0%9F%D0%BE%D0%BB%D0%B5%D0%B7%D0%BD%D1%8B%D0%B5%20%D0%B0%D0%BA%D1%81%D0%B5%D1%81%D1%81%D1%83%D0%B0%D1%80%D1%8B%20%D0%B4%D0%BB%D1%8F%20%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%D0%BE%D0%B2.%20%D0%A6%D0%B5%D0%BD%D0%B0%20%D0%BE%D1%82%201%2C500%20%D1%81%D0%BE%D0%BC&imgurl=https%3A%2F%2Fnotebookoff.uz%2Fupload%2Fresize_cache%2Fiblock%2F595%2F550_500_1%2Ffkwhdajmlmfb8m8pl1n6xhzni5ya7pf1.jpg&imgrefurl=https%3A%2F%2Fnotebookoff.uz%2Fblog%2Fpoleznie_aksessuari_dlya_noutbukov_chto_stoit_kupit%2F&docid=QQ5p6FZ18hyNjM&tbnid=oH6ijJ4lvzQi4M&vet=12ahUKEwiYnavx1K6IAxVoFBAIHTsYC04QM3oECBkQAA..i&w=550&h=373&hcb=2&ved=2ahUKEwiYnavx1K6IAxVoFBAIHTsYC04QM3oECBkQAA',
        caption="Полезные аксессуары для ноутбуков. Цена от 1,500 сом."
    )

@dp.message_handler(text="Назад")
async def back_start(message: types.Message):
    await start(message)

@dp.message_handler(text="Оставить заявку")
async def application(message: types.Message):
    button = types.KeyboardButton("Отправить контакт", request_contact=True)
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(button)
    await message.answer("Пожалуйста, отправьте свой контакт для оформления заказа.", reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(message: types.Message):
    await bot.send_message(
        chat_id=-4267715696,
        text=f'Новый заказ:\nИмя: {message.contact.first_name}\nФамилия: {message.contact.last_name}\nUsername пользователя: {message.from_user.username}\nТелефон: {message.contact.phone_number}'
    )
    await message.answer("Спасибо за ваш заказ! Мы свяжемся с вами в ближайшее время.")
    await start(message)

@dp.message_handler(text='Помощь')
async def help(message: types.Message):
    await message.reply("Если у вас есть вопросы, вы можете обратиться к нашему менеджеру или посмотреть раздел FAQ.")

@dp.message_handler(text='Акции')
async def promotions(message: types.Message):
    await message.reply("У нас есть специальные предложения и скидки! Подпишитесь на нашу рассылку, чтобы не пропустить ни одной акции.")


@dp.message_handler(text='Оставить отзыв')
async def leave_review(message: types.Message):
    await message.reply("Пожалуйста, отправьте свой отзыв. Мы ценим ваше мнение!")

@dp.message_handler(text='Оплатить')
async def process_payment(message: types.Message):
    prices = [LabeledPrice(label='Мощный ноутбук', amount=60000 * 100)] 

    await bot.send_invoice(
        chat_id=message.chat.id,
        title="Покупка ноутбука",
        description="Мощный ноутбук для любых задач",
        payload="payment-payload",
        provider_token=PROVIDER_TOKEN,
        currency="KGS",
        prices=prices,
        start_parameter="payment_example",
        photo_url="https://www.google.com/imgres?q=%D0%BD%D0%BE%D1%83%D1%82%D0%B1%D1%83%D0%BA%20%D1%81%D0%B0%D0%BC%D1%8B%D0%B9%20%D0%B4%D0%BE%D1%80%D0%BE%D0%B3%D0%BE%D0%B9&imgurl=https%3A%2F%2Fwww.ixbt.com%2Fimg%2Fn1%2Fnews%2F2023%2F2%2F2%2Frog-zephyrus-duo-16-2023-asus.com_-1020x600_large.png&imgrefurl=https%3A%2F%2Fwww.ixbt.com%2Fnews%2F2023%2F03%2F14%2F8000-asus-geforce-rtx-4090-mobile.html&docid=R_9wNd0zglhpoM&tbnid=zeHK4ryKgPE6eM&vet=12ahUKEwjYyLPhz66IAxVDHRAIHTO9A3oQM3oECHYQAA..i&w=924&h=544&hcb=2&ved=2ahUKEwjYyLPhz66IAxVDHRAIHTO9A3oQM3oECHYQAA",
        photo_size=512,
        photo_width=512,
        photo_height=512,
    )

@dp.pre_checkout_query_handler(lambda query: True)
async def pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)

@dp.message_handler(content_types=types.ContentType.SUCCESSFUL_PAYMENT)
async def successful_payment(message: types.Message):
    await message.answer("Спасибо за покупку! Мы скоро свяжемся с вами для подтверждения заказа.")

if __name__ == '__main__':
    from logging import basicConfig, INFO
    basicConfig(level=INFO)
    executor.start_polling(dp, skip_updates=True)
