import utils


class Hero:
    def __init__(
            self,
            name,
            health="Health",
            attack="Attack",
            attack_speed="AttackSpeed",
            attribute="Attribute"
    ):
        utils.check_hero_name(name, utils.get_all_hero_names())

        message = f"hero({name}, {health}, {attack}, {attack_speed}, {attribute})"
        res = next(utils.run_query(message))
        if not isinstance(res, dict):
            raise Exception

        self.name = name
        self.health = res.get(health, health)
        self.attack = res.get(attack, attack)
        self.attack_speed = res.get(attack_speed, attack_speed)
        self.attribute = res.get(attribute, attribute)


class Skill:
    def __init__(
            self,
            name,
            damage="Damage"
    ):
        utils.check_hero_name(name, utils.get_all_hero_names())

        message = f"skill({name}, {damage})"
        res = next(utils.run_query(message))
        if not isinstance(res, dict):
            raise Exception

        self.name = name
        self.damage = res.get(damage, damage)
