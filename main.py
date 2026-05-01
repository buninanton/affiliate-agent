import random
import time
import json

# Загружаем товары
with open("products.json", "r", encoding="utf-8") as f:
    products = json.load(f)

hooks = [
    "Ты делаешь это неправильно...",
    "99% людей не знают об этом",
    "Вот почему у тебя не получается",
    "Эта вещь решает проблему за 10 секунд"
]

def pick_best_product(products):
    sorted_products = sorted(products, key=lambda x: x["score"], reverse=True)
    top = sorted_products[:2]
    return random.choice(top)

def generate_post(product, hook):
    return f"""
🎬 СЦЕНАРИЙ:

{hook}

У тебя тоже {product['pain']}?

Я нашёл решение 👇

{product['name']} — реально спасает

✔ удобно
✔ быстро
✔ работает сразу

💰 Цена: {product['price']}

👉 Ссылка в профиле

#товары #находки #обзор #лайфхак
"""

def generate_idea():
    product = pick_best_product(products)
    hook = random.choice(hooks)

    return generate_post(product, hook)


while True:
    idea = generate_idea()

    print("=== ГОТОВЫЙ ПОСТ ===")
    print(idea)

    time.sleep(60)
