def parse_filed(s: str):
    fields = {"skill_damage", "damage", "attack", "attribute", "fight"}
    words = set(s.split())
    if len(fields & words) != 1:
        return

    param = fields & words
    return param


def parse_fight_info(s: str) -> dict:
    s = s.replace("[", "").replace("]", "")
    result = {
        "Hero1": "Hero1",
        "Hero2": "Hero2",
        "Res": "Res"
    }
    for word in s.split():
        if word.startswith("Hero1="):
            result["Hero1"] = word[len("Hero1="):]
        if word.startswith("Hero2="):
            result["Hero2"] = word[len("Hero2="):]
        if word.startswith("Res="):
            result["Res"] = word[len("Res="):]

    return result
