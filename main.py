import parser
import utils
from entities import Hero, Skill

print("% hero(name, health, attack, Attack speed, attribute)")
print("% skill(name, damage)")
print("% fight(Name1, Name2, Fight_Result)")
print()

hero_names = utils.get_all_hero_names()
print(f"Коллекция героев: {', '.join(hero_names)}")
hero_name1, hero_name2 = input("Введи имена двух героев через пробел\n").split()

hero1 = Hero(hero_name1)
skill1 = Skill(hero_name1)

hero2 = Hero(hero_name2)
skill2 = Skill(hero_name2)

print("Можешь узнать: skill_damage, damage, attack, attribute")
print("А можешь начать сражение: fight [Hero1=...] [Hero2=...] [Res=...]")

s = input()
parsed = parser.parse_filed(s) or {}
while "fight" not in parsed:
    if not parsed:
        if len(parsed) == 0:
            print("Введи без ошибок!")
        else:
            print("Введи один параметр")
    else:
        attr = parsed.pop()
        print(f"{hero1.name} | {attr}: {hero1.__dict__.get(attr) or skill1.__dict__.get(attr)}")
        print(f"{hero2.name} | {attr}: {hero2.__dict__.get(attr) or skill2.__dict__.get(attr)}")

    s = input()
    parsed = parser.parse_filed(s) or {}

fight_results = utils.fight(s)

print(f"всего результатов найдено: {len(fight_results)}")
for index, res in enumerate(fight_results):
    hero1, hero2, fight_res = res
    print(f"hero1: {hero1}, hero2: {hero2}, winner: {fight_res}")
    if index == 5:
        print("...")
        break
