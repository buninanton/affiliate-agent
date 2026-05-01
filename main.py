import random
import time
import json

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
    top = sorted_products[:2]  # берём топ 2
    return random.choice(top)

def generate_idea():
    product = pick_best_product(products)
    hook = random.choice(hooks)

    script = f"""
🎬 СЦЕНАРИЙ ВИДЕО:

Хук: {hook}

🔥 ТОВАР С ПОТЕНЦИАЛОМ:
{product['name']}

Цена: {product['price']}

Проблема: {product['pain']}

Сюжет:
1. показать боль
2. усилить проблему
3. решение через товар
4. вау-эффект

Ссылка: {product['link']}
"""

    return script


while True:
    idea = generate_idea()

    print("=== ЛУЧШИЙ ТОВАР ===")
    print(idea)

    time.sleep(60)
