spellbook1 = {
    "Elemental Magic": ["Fireball", "Lightning Bolt", "Earthquake"],
    "Healing Magic": ["Heal", "Greater Heal"],
    "Dark Magic": ["Curse"]
}

spellbook2 = {
    "Elemental Magic": ["Fireball", "Ice Storm"],
    "Healing Magic": ["Heal"],
    "Necromancy": ["Raise Undead", "Life Drain"]
}

#spellbook3 (merge both spellbooks together)
merged_spellbook = spellbook1.copy()

for i in spellbook2:

    for j in spellbook2[i]:
        if i not in merged_spellbook:
            merged_spellbook[i] = [j]
        if j not in merged_spellbook[i]:
            merged_spellbook[i].append(j)

print(merged_spellbook)

