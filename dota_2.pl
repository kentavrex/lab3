% База знаний персонажей Dota 2

% hero(name, health, attack, Attack speed, attribute)
%
% Персонажи с атрибутом - Сила, Ловкость, Интелект
hero(axe, 670, 57, 0.71, strength).
hero(bristleback, 604, 58,0.71,strength).
hero(kunkka, 648, 55, 0.67,strength).
hero(slardar, 582, 54, 0.69,strength).
hero(pudge, 670, 73, 0.67,strength).
hero(omniknight, 626, 58, 0.68,strength).
hero(tiny, 780, 63, 0.59,strength).

hero(slark, 560, 57, 0.83, agility).
hero(ursa, 670, 45, 0.69, agility).
hero(razor, 604, 48, 0.73, agility).
hero(luna, 670, 53, 0.73, agility).
hero(juggernaut, 560, 55, 0.79,agility).
hero(weaver, 472, 56, 0.69,agility).
hero(sniper, 538, 48, 0.75,agility).

hero(disruptor, 582, 48, 0.68, intelligence).
hero(jakiro, 670, 57, 0.68,intelligence).
hero(lich, 560, 53, 0.69, intelligence).
hero(lina, 560, 54, 0.72, intelligence).
hero(lion, 560, 42, 0.76,intelligence).
hero(oracle, 560, 42, 0.68,intelligence).
hero(zeus, 538, 60, 0.65,intelligence).

% У каждого персонажа есть своя способность, помимо обычных аттак
% каждая способность уникально - поэтому в skill() будем следить
% за ее итоговым результатом

% skill(name, damage)

skill(axe, 120).
skill(bristleback, 400).
skill(kunkka, 60).
skill(slardar, 340).
skill(pudge, 150).
skill(omniknight, 360).
skill(slark, 550).
skill(ursa, 700).
skill(razor, 600).
skill(luna, 200).
skill(juggernaut, 250).
skill(weaver, 250).
skill(sniper, 150).
skill(disruptor, 110).
skill(jakiro, 150).
skill(lich, 80).
skill(lina, 400).
skill(lion, 390).
skill(oracle, 100).
skill(zeus, 380).

% Добавим минимальные правила для существования игры
is_alive(HP) :- HP > 0.
is_not_alive(HP) :- \+ is_alive(HP).
hero_attack(Name, DMG * AS) :- hero(Name, _, DMG, AS, _).
skill_dmg(Name, SkillDMG - AttackDmg) :- skill(Name, SkillDMG), hero_attack(Name, AttackDmg).

cast_skills(Name1, Name2, HP1_left, HP2_left) :-
    skill_dmg(Name1, SkillDmg1),
    skill_dmg(Name2, SkillDmg2),
    hero(Name1, HP1, _, _, _),
    hero(Name2, HP2, _, _, _),
    hero_attack(Name1, HA1),
	hero_attack(Name2, HA2),
    HP1_left is HP1 - HA2 - SkillDmg2,
    HP2_left is HP2 - HA1 - SkillDmg1.

do_hits(H1, H2, D1, D2, Res) :-
    (
    is_not_alive(H1), is_not_alive(H2) ->  Res is 0;
    is_not_alive(H1) ->  Res is 2;
   	is_not_alive(H2) ->  Res is 1;
    do_hits(H1 - D2, H2 - D1, D1, D2, Res)
    ).

fight(Name1, Name2, Fight_Res) :-
    cast_skills(Name1, Name2, HP1_left, HP2_left),
    hero_attack(Name1, AT1),
    hero_attack(Name2, AT2),
    do_hits(HP1_left, HP2_left, AT1, AT2, Fight_Res).

