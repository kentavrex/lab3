from pyswip import Prolog
from parser import parse_fight_info

prolog = Prolog()
prolog.consult("dota_2.pl")


def run_query(msg: str) -> iter:
    query = prolog.query(msg)
    try:
        return query
    except Exception:
        raise IOError("Incorrect input")


def check_hero_name(name: str, names: set) -> None:
    if name not in names:
        raise IOError("Incorrect input")


def get_all_hero_names() -> set:
    query = prolog.query("hero(Name, _, _, _, _)")
    res = set()
    for hero in query:
        res.add(hero["Name"])
    return res


def fight(s: str) -> list:
    parsed = parse_fight_info(s)
    hero1 = parsed["Hero1"]
    hero2 = parsed["Hero2"]
    res = parsed["Res"]

    query_result = list(prolog.query(f'fight({hero1}, {hero2}, {res})'))

    ans = []
    for result in query_result:
        hero1 = result.get("Hero1", hero1)
        hero2 = result.get("Hero2", hero2)
        res = result.get("Res", res)
        ans.append((hero1, hero2, res))

    return ans
