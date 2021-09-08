from Mobs.mob_loot import loot_table

item_list = [
    # Materials
    [{'Leather': 'Material used for crafting'}, 'None', {}],
    [{'SpruceLog': 'Material used for crafting'}, 'None', {}],
    [{'OakLog': 'Material used for crafting'}, 'None', {}],
    [{'PineLog': 'Material used for crafting'}, 'None', {}],
    [{'BeechLog': 'Material used for crafting'}, 'None', {}],
    [{'MapleLog': 'Material used for crafting'}, 'None', {}],
    [{'AshLog': 'Material used for crafting'}, 'None', {}],
    [{'WaterRune': 'Material used for crafting'}, 'None', {}],
    [{'Cod': 'Material used for crafting'}, 'None', {}],
    [{'Mackerel': 'Material used for crafting'}, 'None', {}],
    [{'Carp': 'Material used for crafting'}, 'None', {}],
    [{'Trout': 'Material used for crafting'}, 'None', {}],
    [{'Salmon': 'Material used for crafting'}, 'None', {}],
    [{'Catfish': 'Material used for crafting'}, 'None', {}],
    [{'Tuna': 'Material used for crafting'}, 'None', {}],
    [{'Bone': 'Material used for crafting'}, 'None', {}],
    [{'Paper': 'Material used for crafting'}, 'None', {}],
    [{'IceRune': 'Material used for crafting'}, 'None', {}],
    [{'SandRune': 'Material used for crafting'}, 'None', {}],
    [{'GunPart': 'Material used for crafting'}, 'None', {}],
    [{'EarthRune': 'Material used for crafting'}, 'None', {}],
    [{'FireRune': 'Material used for crafting'}, 'None', {}],
    [{'DeathLily': 'Material used for crafting'}, 'None', {}],
    [{'AncientRune': 'Material used for crafting'}, 'None', {}],
    [{'DevilsHorn': 'Material used for crafting'}, 'None', {}],
    [{'Blood': 'Material used for crafting'}, 'None', {}],
    [{'Stone': 'Material used for crafting'}, 'None', {}],
    [{'Limestone': 'Material used for crafting'}, 'None', {}],
    [{'Basalt': 'Material used for crafting'}, 'None', {}],
    [{'Ironore': 'Material used for crafting'}, 'None', {}],
    [{'Goldore': 'Material used for crafting'}, 'None', {}],
    [{'Tinore': 'Material used for crafting'}, 'None', {}],
    [{'Ruby': 'Material used for crafting'}, 'None', {}],
    [{'Sapphire': 'Material used for crafting'}, 'None', {}],
    [{'Diamond': 'Material used for crafting'}, 'None', {}],
    [{'Mithrilore': 'Material used for crafting'}, 'None', {}],
    [{'Obsidian': 'Material used for crafting'}, 'None', {}],
    [{'Titaniumore': 'Material used for crafting'}, 'None', {}],
    [{'GemIngot': 'Material used for crafting'}, 'None', {}],
    [{'IronIngot': 'Material used for crafting'}, 'None', {}],
    [{'TinIngot': 'Material used for crafting'}, 'None', {}],
    [{'GoldIngot': 'Material used for crafting'}, 'None', {}],
    [{'MithrilIngot': 'Material used for crafting'}, 'None', {}],
    [{'TitaniumIngot': 'Material used for crafting'}, 'None', {}],
    [{'FishIngot': 'Material used for crafting'}, 'None', {}],
    [{'CutStone': 'Material used for crafting'}, 'None', {}],
    [{'CutLimestone': 'Material used for crafting'}, 'None', {}],
    [{'CutBasalt': 'Material used for crafting'}, 'None', {}],
    [{'Paper': 'Material used for crafting'}, 'None', {}],
    [{'BloodInfusedStone': 'Material used for crafting'}, 'None', {}],
    [{'BloodInfusedIngot': 'Material used for crafting'}, 'None', {}],
    [{'BloodInfusedDiamond': 'Material used for crafting'}, 'None', {}],
    [{'DevilIngot': 'Material used for crafting'}, 'None', {}],
    [{'BlackLeather': 'Material used for crafting'}, 'None', {}],
    [{'ShadeWoodLog': 'Material used for crafting'}, 'None', {}],
    [{'HelixCore': 'Material used for crafting'}, 'None', {}],

    # misc
    [{'pickaxe': 'Used to mine rocks'}, 'None', {}],
    [{'fishingrod': 'Used to fish'}, 'None', {}],
    [{'HunterRing': 'Gives +5 Combat Skill, +4 Agility Skill, +5 Magic Skill'}, 'Ring', {'Agility': 4, 'Magic': 5, 'Combat': 5}],

    # defense
    [{'KnightHelmet': 'Gives +5 Defense Skill, +3 Combat Skill'}, 'Head', {'Defense': 5, 'Combat': 3}],
    [{'KnightChestplate': 'Gives +5 Defense Skill, +3 Combat Skill'}, 'Chest', {'Defense': 5, 'Combat': 3}],
    [{'KnightLeggings': 'Gives +5 Defense Skill, +3 Combat Skill'}, 'Legs', {'Defense': 5, 'Combat': 3}],
    [{'KnightBoots': 'Gives +5 Defense Skill, +3 Combat Skill'}, 'Feet', {'Defense': 5, 'Combat': 3}],

    [{'DarkKnightHelmet': 'Gives +11 Defense Skill, +7 Combat Skill'}, 'Head', {'Defense': 11, 'Combat': 7}],
    [{'DarkKnightChestplate': 'Gives +11 Defense Skill, +7 Combat Skill'}, 'Chest', {'Defense': 11, 'Combat': 7}],
    [{'DarkKnightLeggings': 'Gives +11 Defense Skill, +7 Combat Skill'}, 'Legs', {'Defense': 11, 'Combat': 7}],
    [{'DarkKnightBoots': 'Gives +11 Defense Skill, +7 Combat Skill'}, 'Feet', {'Defense': 11, 'Combat': 7}],

    [{'GolemHelmet': 'Gives +15 Defense Skill, +8 healing Skill'}, 'Head', {'Defense': 15, 'Healing': 8}],
    [{'GolemChestplate': 'Gives +15 Defense Skill, +8 healing Skill'}, 'Chest', {'Defense': 15, 'Healing': 8}],
    [{'GolemLeggings': 'Gives +15 Defense Skill, +8 healing Skill'}, 'Legs', {'Defense': 15, 'Healing': 8}],
    [{'GolemBoots': 'Gives +15 Defense Skill, +8 healing Skill'}, 'Feet', {'Defense': 15, 'Healing': 8}],

    [{'GriffinHelmet': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Head', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinChestplate': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Chest', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinLeggings': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Legs', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinBoots': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Feet', {'Defense': 24, 'Healing': 5, 'Agility': 5}],

    [{'BasaltHelmet': 'Gives +16 Defense Skill, -7 Health Skill'}, 'Head', {'Defense': 16, 'Health': -7}],

    [{'EternalHelmet': 'Gives +20 Defense Skill, +10 Health Skill'}, 'Head', {'Defense': 20, 'Health': 10}],
    [{'EternalChestplate': 'Gives +20 Defense Skill, +10 Health Skill'}, 'Chest', {'Defense': 20, 'Health': 10}],
    [{'EternalLeggings': 'Gives +20 Defense Skill, +10 Health Skill'}, 'Legs', {'Defense': 20, 'Health': 10}],
    [{'EternalBoots': 'Gives +20 Defense Skill, +10 Health Skill'}, 'Feet', {'Defense': 20, 'Health': 10}],

    [{'TinBoots': 'Gives +5 Defense Skill'}, 'Feet', {'Defense': 5}],
    [{'TinLeggings': 'Gives +5 Defense Skill'}, 'Legs', {'Defense': 5}],
    [{'TinChestplate': 'Gives +5 Defense Skill'}, 'Chest', {'Defense': 5}],
    [{'TinHelmet': 'Gives +5 Defense Skill'}, 'Head', {'Defense': 5}],

    [{'HallowedHelmet': 'Gives +12 Defense Skill, +6 Luck Skill'}, 'Head', {'Defense': 12, 'Luck': 6}],
    [{'HallowedChestplate': 'Gives +12 Defense Skill, +6 Luck Skill'}, 'Chest', {'Defense': 12, 'Luck': 6}],
    [{'HallowedLeggings': 'Gives +12 Defense Skill, +6 Luck Skill'}, 'Legs', {'Defense': 12, 'Luck': 6}],
    [{'HallowedBoots': 'Gives +12 Defense Skill, +6 Luck Skill'}, 'Feet', {'Defense': 12, 'Luck': 6}],
    [{'HallowedSpear': 'Gives +10 Defense Skill, +10 Combat Skill'}, 'Hand', {'Defense': 10, 'Combat': 10}],

    [{'Shield': 'Grants 5 shield each turn'}, 'Hand', {}],
    [{'EternalGuardianShield': 'Gives +30 Defense Skill'}, 'Hand', {'Defense': 30}],
    [{'BasaltShield': 'Gives +15 Defense Skill'}, 'Hand', {'Defense': 15}],
    [{'OldIronChestplate': 'Gives +6 Defense Skill'}, 'Chest', {'Defense': 6}],


    # combat
    [{'HellHoundHelmet': 'Gives +21 Combat Skill, -7 healing Skill, +5 Defense Skill'}, 'Head', {'Combat': 21, 'Healing': -7, 'Defense': 5}],
    [{'HellHoundChestplate': 'Gives +21 Combat Skill, -9 healing Skill, +5 Defense Skill'}, 'Chest', {'Combat': 21, 'Healing': -9, 'Defense': 5}],
    [{'HellHoundLeggings': 'Gives +21 Combat Skill, -8 healing Skill, +5 Defense Skill'}, 'Legs', {'Combat': 21, 'Healing': -8, 'Defense': 5}],
    [{'HellHoundBoots': 'Gives +21 Combat Skill, -6 healing Skill, +5 Defense Skill'}, 'Feet', {'Combat': 21, 'Healing': -6, 'Defense': 5}],

    [{'WarriorBoots': 'Gives +9 Combat Skill'}, 'Feet', {'Combat': 9}],
    [{'WarriorLeggings': 'Gives +9 Combat Skill'}, 'Legs', {'Combat': 9}],
    [{'WarriorChestplate': 'Gives +9 Combat Skill'}, 'Chest', {'Combat': 9}],
    [{'WarriorHelmet': 'Gives +9 Combat Skill'}, 'Head', {'Combat': 9}],

    [{'SteelHelmet': 'Gives +14 Combat Skill'}, 'Head', {'Combat': 14}],
    [{'SteelChestplate': 'Gives +14 Combat Skill'}, 'Chest', {'Combat': 14}],
    [{'SteelLeggings': 'Gives +14 Combat Skill'}, 'Legs', {'Combat': 14}],
    [{'SteelBoots': 'Gives +14 Combat Skill'}, 'Feet', {'Combat': 14}],

    [{'CombatChestplate': 'Gives +5 Combat Skill'}, 'Chest', {'Combat': 7}],
    [{'ChampionChestplate': 'Gives +15 Combat Skill'}, 'Chest', {'Combat': 15}],
    [{'WarBornChestplate': 'Gives +27 Combat Skill'}, 'Chest', {'Combat': 27}],

    [{'IronSword': 'Gives +8 Combat Skill'}, 'Hand', {'Combat': 8}],
    [{'LavaSword': 'Gives +27 Combat Skill'}, 'Hand', {'Combat': 27}],
    [{'PunySword': 'Gives +4 Combat Skill'}, 'Hand', {'Combat': 4}],
    [{'SteelGreatSword': 'Gives +14 Combat Skill'}, 'Hand', {'Combat': 14}],
    [{'Katana': 'Gives +7 Combat Skill, +7 Agility Skill'}, 'Hand', {'Combat': 7, 'Agility': 7}],



    # agility
    [{'ShadowScaleHelmet': 'Gives +28 Agility Skill, -5 Health Skill'}, 'Head', {'Agility': 28, 'Health': -5}],
    [{'ShadowScaleChestplate': 'Gives +28 Agility Skill, -8 Health Skill'}, 'Chest', {'Agility': 28, 'Health': -8}],
    [{'ShadowScaleLeggings': 'Gives +28 Agility Skill, -4 Health Skill'}, 'Legs', {'Agility': 28, 'Health': -4}],
    [{'ShadowScaleBoots': 'Gives +28 Agility Skill, -6 Health Skill'}, 'Feet', {'Agility': 28, 'Health': -6}],

    [{'ThiefHelmet': 'Gives +8 Stealing, +10 Agility Skill'}, 'Head', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefChestplate': 'Gives +8 Stealing, +10 Agility Skill'}, 'Chest', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefLeggings': 'Gives +8 Stealing, +10 Agility Skill'}, 'Legs', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefBoots': 'Gives +8 Stealing, +10 Agility Skill'}, 'Feet', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefRing': 'Gives +15 Stealing, +10 Agility Skill'}, 'Ring', {'Stealing': 15, 'Agility': 10}],

    [{'HelixHelmet': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Head', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixChestplate': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Chest', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixLeggings': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Legs', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixBoots': 'Gives +10 Dodge, +10 Agility, +10 Health Skill, '}, 'Feet', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixCoreSword': '+18 Agility, +5 Health Skill, '}, 'Hand', {'Agility': 18, 'Health': 5}],

    [{'AssassinsHelmet': 'Gives +13 Agility Skill'}, 'Head', {'Agility': 13}],
    [{'AssassinsChestplate': 'Gives +13 Agility Skill'}, 'Chest', {'Agility': 13}],
    [{'AssassinsLeggings': 'Gives +13 Agility Skill'}, 'Legs', {'Agility': 13}],
    [{'AssassinsBoots': 'Gives +13 Agility Skill'}, 'Feet', {'Agility': 13}],

    [{'SkyDarkHelmet': 'Gives +16 Dodge Skill'}, 'Head', {'Dodge': 16}],
    [{'SkyDarkChestplate': 'Gives +16 Dodge Skill'}, 'Chest', {'Dodge': 16}],
    [{'SkyDarkLeggings': 'Gives +16 Dodge Skill'}, 'Legs', {'Dodge': 16}],
    [{'SkyDarkBoots': 'Gives +16 Dodge Skill'}, 'Feet', {'Dodge': 16}],

    [{'SkeletalChestplate': 'Gives +19 Agility Skill'}, 'Chest', {'Agility': 19}],
    [{'DarkBoots': 'Gives +18 Agility Skill'}, 'Feet', {'Agility': 18}],

    [{'AbyssalDagger': 'Gives +15 Agility Skill, +10 Defense Skill'}, 'Hand', {'Agility': 15, 'Defense': 10}],
    [{'BonerSword': 'Gives +10 Agility Skill, +10 Dodge Skill'}, 'Hand', {'Agility': 10, 'Dodge': 10}],
    [{'WraithDagger': 'Gives +6 Agility Skill, +20 Dodge Skill'}, 'Hand', {'Agility': 6, 'Dodge': 20}],


    # gathering

    [{'FishBoots': 'Gives +2 Fishing Skill'}, 'Feet', {'Fishing': 2}],
    [{'FishChestplate': 'Gives +2 Fishing Skill'}, 'Chest', {'Fishing': 2}],
    [{'FishLeggings': 'Gives +2 Fishing Skill'}, 'Legs', {'Fishing': 2}],
    [{'FishHelmet': 'Gives +2 Fishing Skill'}, 'Head', {'Fishing': 2}],
    [{'MinerBoots': 'Gives +2 Mining Skill'}, 'Feet', {'Mining': 2}],
    [{'MinerHelmet': 'Gives +2 Mining Skill'}, 'Head', {'Mining': 2}],
    [{'MinerChestplate': 'Gives +2 Mining Skill'}, 'Chest', {'Mining': 2}],
    [{'MinerLeggings': 'Gives +2 Mining Skill'}, 'Legs', {'Mining': 2}],

    [{'GemFishingRod': 'Gives +5 Fishing Skill'}, 'Hand', {'Fishing': 5}],


    # magic (done)

    [{'MagicChestplate': 'Gives +5 Magic Skill'}, 'Chest', {'Magic': 5}],
    [{'ElementalChestplate': 'Gives +15 Magic Skill'}, 'Chest', {'Magic': 15}],
    [{'ArchMageChestplate': 'Gives +27 Magic Skill'}, 'Chest', {'Magic': 27}],

    [{'ArcaneHelmet': 'Gives +17 magic Skill'}, 'Head', {'magic': 17}],
    [{'ArcaneChestplate': 'Gives +17 magic Skill'}, 'Chest', {'magic': 17}],
    [{'ArcaneLeggings': 'Gives +17 magic Skill'}, 'Legs', {'magic': 17}],
    [{'ArcaneBoots': 'Gives +17 magic Skill'}, 'Feet', {'magic': 17}],

    [{'NecromancerHelmet': 'Gives +24 magic Skill, -9 health skill'}, 'Head', {'magic': 24, 'Health': -9}],
    [{'NecromancerChestplate': 'Gives +24 magic Skill, -9 health skill'}, 'Chest', {'magic': 24, 'Health': -9}],
    [{'NecromancerLeggings': 'Gives +24 magic Skill, -9 health skill'}, 'Legs', {'magic': 24, 'Health': -9}],
    [{'NecromancerBoots': 'Gives +24 magic Skill, -9 health skill'}, 'Feet', {'magic': 24, 'Health': -9}],

    [{'DarkPhoenixHelmet': 'Gives +31 magic Skill, -10 Defense skill'}, 'Head', {'magic': 31, 'Defense': -10}],
    [{'DarkPhoenixChestplate': 'Gives +31 magic Skill, -10 Defense skill'}, 'Chest', {'magic': 31, 'Defense': -10}],
    [{'DarkPhoenixLeggings': 'Gives +31 magic Skill, -10 Defense skill'}, 'Legs', {'magic': 31, 'Defense': -10}],
    [{'DarkPhoenixBoots': 'Gives +31 magic Skill, -10 Defense skill'}, 'Feet', {'magic': 31, 'Defense': -10}],

    [{'InfinityBoots': 'Gives +20 Magic Skill'}, 'Feet', {'Magic': 20}],
    [{'SpectralHelmet': 'Gives +15 Magic Skill'}, 'Head', {'Magic': 15}],
    [{'SpectralChestplate': 'Gives +15 Magic Skill'}, 'Chest', {'Magic': 15}],
    [{'SpectralLeggings': 'Gives +15 Magic Skill'}, 'Legs', {'Magic': 15}],
    [{'CursedMask': 'Gives -10 Defense Skill, -5 Luck Skill, +23 Magic Skill'}, 'Head', {'Magic': 23, 'Luck': -5, 'Defense': -10}],
    [{'SpectralBoots': 'Gives +15 Magic Skill'}, 'Feet', {'Magic': 15}],

    [{'WarlockLeggings': 'Gives +8 Magic Skill, -3 Healing Skill'}, 'Legs', {'Magic': 8, 'Healing': -3}],
    [{'WarlockBoots': 'Gives +8 Magic Skill, -3 Healing Skill'}, 'Feet', {'Magic': 8, 'Healing': -3}],

    [{'MagicStaff': 'Gives +9 Magic Skill'}, 'Hand', {'Magic': 9}],
    [{'ElectrumWand': 'Gives +8 Magic Skill'}, 'Hand', {'Magic': 8}],
    [{'SorcererWand': 'Gives +14 Magic Skill, +2 Defense Skill'}, 'Hand', {'Magic': 14, 'Defense': 2}],
    [{'MagicDagger': 'Gives +7 Magic Skill, +4 Agility Skill'}, 'Hand', {'Magic': 7, 'Agility': 4}],
    [{'DiabloRing': 'Gives +14 Magic Skill'}, 'Ring', {'Magic': 14}],
    [{'StaffOfAegis': 'Gives +38 Magic Skill'}, 'Hand', {'Magic': 38}],
    [{'TormentShard': 'Gives +12 Magic Skill, +8 Healing Skill'}, 'Hand', {'Magic': 12, 'Healing': 8}],
    [{'SlimeRing': 'Gives +7 Magic Skill, +7 Healing Skill'}, 'Ring', {'Magic': 7, 'Healing': 7}],
    [{'MagicRing': 'Gives +6 Magic Skill'}, 'Ring', {'Magic': 6}],


    # other
    [{'LuckyStick': 'Gives +18 Luck Skill'}, 'Hand', {'Luck': 18}],




    # health
    [{'AncientChestplate': 'Gives +9 Health Skill'}, 'Chest', {'Health': 9}],
    [{'PurityChestplate': 'Gives +16 Health Skill'}, 'Chest', {'Health': 16}],

    # healing

    [{'RestoreWand': 'Gives +6 Healing Skill, +4 Magic'}, 'Hand', {'Healing': 6, 'Magic': 4}],
    [{'UnholyStaff': 'Gives +12 Healing Skill, +6 Health'}, 'Hand', {'Healing': 12, 'Health': 6}],
    [{'DemonScythe': 'Gives +15 Healing Skill, +6 Magic, +6 Dodge'}, 'Hand', {'Healing': 15, 'Magic': 6, 'Dodge': 6}],
    [{'WandOfHealing': 'Gives +10 Healing Skill'}, 'Hand', {'Healing': 10}],
    [{'Spellbinder': 'Gives +9 Healing Skill, +9 Defense'}, 'Hand', {'Healing': 9, 'Defense': 9}],
    [{'ProtectorsCurse': 'Gives +10 Healing Skill, +16 Defense, -6 Health'}, 'Hand', {'Healing': 10, 'Defense': 16, 'Health': -6}],


    [{'AngelHelmet': 'Gives +30 Healing Skill'}, 'Head', {'Healing': 30}],
    [{'AngelChestplate': 'Gives +30 Healing Skill'}, 'Chest', {'Healing': 30}],
    [{'AngelLeggings': 'Gives +30 Healing Skill'}, 'Legs', {'Healing': 30}],
    [{'AngelBoots': 'Gives +30 Healing Skill'}, 'Feet', {'Healing': 30}],

    [{'CrystalHelmet': 'Gives +6 Healing Skill'}, 'Head', {'Healing': 6}],
    [{'CrystalChestplate': 'Gives +6 Healing Skill'}, 'Chest', {'Healing': 6}],
    [{'CrystalLeggings': 'Gives +6 Healing Skill'}, 'Legs', {'Healing': 6}],
    [{'CrystalBoots': 'Gives +6 Healing Skill'}, 'Feet', {'Healing': 6}],

    [{'TrueSteelHelmet': 'Gives +9 Healing Skill, +6 Magic Skill'}, 'Head', {'Healing': 9, 'Magic': 6}],
    [{'TrueSteelChestplate': 'Gives +9 Healing Skill, +6 Magic Skill'}, 'Chest', {'Healing': 9, 'Magic': 6}],
    [{'TrueSteelLeggings': 'Gives +9 Healing Skill, +6 Magic Skill'}, 'Legs', {'Healing': 9, 'Magic': 6}],
    [{'TrueSteelBoots': 'Gives +9 Healing Skill, +6 Magic Skill'}, 'Feet', {'Healing': 9, 'Magic': 6}],

    [{'EbonHelmet': 'Gives +18 Healing Skill'}, 'Head', {'Healing': 18}],
    [{'EbonChestplate': 'Gives +18 Healing Skill'}, 'Chest', {'Healing': 18}],
    [{'EbonLeggings': 'Gives +18 Healing Skill'}, 'Legs', {'Healing': 18}],
    [{'EbonBoots': 'Gives +18 Healing Skill'}, 'Feet', {'Healing': 18}],

    [{'AberrantHelmet': 'Gives +20 Healing Skill, +8 Dodge'}, 'Head', {'Healing': 20, 'Dodge': 8}],
    [{'AberrantChestplate': 'Gives +20 Healing Skill, +8 Dodge'}, 'Chest', {'Healing': 20, 'Dodge': 8}],
    [{'AberrantLeggings': 'Gives +20 Healing Skill, +8 Dodge'}, 'Legs', {'Healing': 20, 'Dodge': 8}],
    [{'AberrantBoots': 'Gives +20 Healing Skill, +8 Dodge'}, 'Feet', {'Healing': 20, 'Dodge': 8}],




    # cards -------------------

    # magic
    [{'Snipe': "(magic) Damage - 7"}, 'Card', {'Magic': 7}],
    [{'Trickshot': "(magic) Damage - 5, Shield - 3"}, 'Card', {'Magic': 5, 'Defense': 3}],
    [{'Incinerate': "(magic) Damage - 11"}, 'Card', {'Magic': 11}],
    [{'Devastate': "(magic) Damage - 8, Shield - 2"}, 'Card', {'Magic': 8, 'Defense': 2}],
    [{'Venom': "(magic) Damage - 3, Shield - 8"}, 'Card', {'Magic': 3, 'Defense': 8}],
    [{'SkyShard': "(magic) Damage - 9, Extra Card Draw"}, 'Card', {'Magic': 9, 'Draw': 1}],
    [{'ShadowBeam': "(magic) Damage - 6, Shield - 7"}, 'Card', {'Magic': 6, 'Defense': 7}],
    [{'ShadowStep': "(magic) Damage - 1, Shield - 4"}, 'Card', {'Magic': 1, 'Defense': 4}],
    [{'Wrath': "(magic) Damage - 15"}, 'Card', {'Magic': 15}],
    [{'Corruption': "(magic) Damage - 20, Self Damage - 30"}, 'Card', {'Magic': 20, 'Self': 30}],

    # agility
    [{'Charge': "(agility) Damage - 2, Extra Card Draw"}, 'Card', {'Agility': 2, 'Draw': 1}],
    [{'Punch': "(agility) Damage - 4"}, 'Card', {'Agility': 4}],
    [{'Slice': "(agility) Damage - 4, Heal - 4"}, 'Card', {'Agility': 4, 'Healing': 4}],
    [{'Bomb': "(agility) Damage - 30, Bonus - Gets permanently destroyed"}, 'Card', {'Agility': 30, 'Destroy': 1}],
    [{'Bite': "(agility) Damage - 10"}, 'Card', {'Agility': 10}],
    [{'Assassinate': "(agility) Damage - 9, + 3 if target below 40%"}, 'Card', {'Agility': 9, 'Finisher': 3}],
    [{'Stab': "(agility) Damage - 5, Extra Card Draw"}, 'Card', {'Agility': 5, 'Draw': 1}],
    [{'ShadowSlice': "(agility) Damage - 4, (magic) Damage - 2"}, 'Card', {'Agility': 4, 'Magic': 2}],
    [{'FrostArrow': "(agility) Damage - 8, + 15 if target below 40%"}, 'Card', {'Agility': 8, 'Finisher': 15}],
    [{'Shockwave': "(agility) Damage - 16, 2 - Healing, Self Damage - 15"}, 'Card', {'Agility': 16, 'Healing': 2, 'Self': 15}],
    [{'Evasion': "(agility) Damage - 8, Dodge - +15% "}, 'Card', {'Agility': 8, 'Dodge': 30}],
    [{'QuickStab': "(agility) Damage - 13"}, 'Card', {'Agility': 13}],
    [{'FirstAid': "(agility) Damage - 6, Healing - 8"}, 'Card', {'Agility': 6, 'Healing': 8}],
    [{'MultiShot': "(agility) Damage - 12, Dodge - +5%"}, 'Card', {'Agility': 12, 'Dodge': 10}],
    [{'DarkSlice': "(agility) Damage - 10, Healing - 5"}, 'Card', {'Agility': 10, 'Healing': 5}],

    # combat
    [{'Slash': "(combat) Damage - 3"}, 'Card', {'Combat': 3}],
    [{'Shieldbash': "(combat) Damage - 5"}, 'Card', {'Combat': 5}],
    [{'Bash': "(combat) Damage - 2, Shield - 4"}, 'Card', {'Combat': 2, 'Defense': 4}],
    [{'Whirlwind': "(combat) Damage - 5, Extra Card Draw"}, 'Card', {'Combat': 5, 'Draw': 1}],
    [{'Onepunch': "(combat) Damage - 30"}, 'Card', {'Combat': 30}],
    [{'Slam': "(combat) Damage - 5, Shield - 5, Heal - 4"}, 'Card', {'Combat': 5, 'Defense': 5, 'Healing': 4}],
    [{'Smash': "(combat) Damage - 3, Heal - 10"}, 'Card', {'Agility': 4, 'Healing': 4}],
    [{'DarkCharge': "(combat) Damage - 12, Extra Card Draw"}, 'Card', {'Magic': 6, 'Defense': 7}],
    [{'Shatter': "(combat) Damage - 9, Heal - 5"}, 'Card', {'Combat': 9, 'Healing': 5}],
    [{'RagingFury': "(combat) Damage - 6, Heal - 6"}, 'Card', {'Combat': 6, 'Healing': 6}],

    # healing
    [{'Recharge': "Heal - 8"}, 'Card', {'Healing': 8}],
    [{'Regeneration': "Heal - 25"}, 'Card', {'Healing': 25}],

    # defense
    [{'Defend': "Shield - 5"}, 'Card', {'Defense': 5}],
    [{'Towershield': "Shield - 12"}, 'Card', {'Defense': 12}],

]


def item_c(*args):  # 0 = this user_data, 1 = Command Class, 2 = all user data, 3 = extra args in list
    if len(args[3]) > 0:
        for item, slot, stats in item_list:
            for item_name, desc in item.items():
                if args[3][0] == item_name.lower():
                    response = f"Info for  {item_name}: {slot}\n{desc}"

                    for loot in loot_table:
                        if loot[1] == item_name:
                            response += f"\nMob Drop:"
                            break
                    for difficulty, name, amount, chance in loot_table:
                        if item_name == name:
                            response += f"\n{chance / 10}% drop in hunt ({difficulty})"
                    return response

    else:
        return f"Incorrect use of item:\ntry 'item (item-name)'"
