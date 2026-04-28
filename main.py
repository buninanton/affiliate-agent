import random
import time

products = [
    {"name": "мини пылесос для клавиатуры", "pain": "грязная клавиатура"},
    {"name": "умная розетка", "pain": "забываешь выключать приборы"},
    {"name": "держатель телефона в авто", "pain": "неудобно смотреть навигатор"},
    {"name": "LED подсветка", "pain": "скучный интерьер"},
    {"name": "портативный блендер", "pain": "нет времени готовить"}
]

hooks = [
    "Ты делаешь это неправильно...",
    "99% людей не знают об этом",
    "Вот почему у тебя не получается",
    "Эта вещь решает проблему за 10 секунд"
]

def generate_idea():
    product = random.choice(products)
    hook = random.choice(hooks)

    script = f"""
🎬 СЦЕНАРИЙ ВИДЕО:

Хук: {hook}

Проблема: {product['pain']}

Решение: используем {product['name']}

Сцены:
1. показать проблему
2. показать товар
3. эффект "вау"

CTA: ссылка в профиле
"""

    return script


while True:
    idea = generate_idea()

    print("=== ВИРУСНАЯ ИДЕЯ ===")
    print(idea)

    with open("ideas.txt", "a") as f:
        f.write(idea + "\n\n")

    time.sleep(60)
