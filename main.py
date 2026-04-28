import random
import time

products = [
    "мини пылесос для клавиатуры",
    "умная розетка",
    "держатель телефона в авто",
    "LED подсветка для комнаты",
    "портативный блендер"
]

hooks = [
    "Ты не поверишь, что это делает...",
    "ТОП находка с маркетплейса",
    "Вещь, которая изменила мою жизнь",
    "Почему я не знал об этом раньше?"
]

def generate_idea():
    product = random.choice(products)
    hook = random.choice(hooks)

    script = f"""
Хук: {hook}
Продукт: {product}
Сюжет: показывает проблему → решение через товар
CTA: ссылка в описании
"""

    return script


while True:
    idea = generate_idea()

    print("=== НОВАЯ ИДЕЯ ===")
    print(idea)

    with open("ideas.txt", "a") as f:
        f.write(idea + "\n\n")

    time.sleep(60)
