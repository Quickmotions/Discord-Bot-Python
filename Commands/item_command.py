from Mobs.mob_loot import loot_table

item_list = [
    # Materials
    [{'TrainingPoints': 'Used to get player xp'}, 'None', {}],
    [{'WorkPoints': 'Used to get job promotions'}, 'None', {}],
    [{'RemovalSigil': 'Used to remove cards'}, 'None', {}],
    [{'ResetSigil': 'Used to reset player stats'}, 'None', {}],
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
    [{'Ectoplasm': 'Material used for crafting'}, 'None', {}],
    [{'DarkShard': 'Material used for crafting'}, 'None', {}],
    [{'Crystalium': 'Material used for crafting bought from the shop'}, 'None', {}],
    [{'Coal': 'Material used for crafting bought from the shop'}, 'None', {}],


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

    [{'GolemHelmet': 'Gives +40 Defense Skill, +8 healing Skill'}, 'Head', {'Defense': 40, 'Healing': 8}],
    [{'GolemChestplate': 'Gives +40 Defense Skill, +8 healing Skill'}, 'Chest', {'Defense': 40, 'Healing': 8}],
    [{'GolemLeggings': 'Gives +40 Defense Skill, +8 healing Skill'}, 'Legs', {'Defense': 40, 'Healing': 8}],
    [{'GolemBoots': 'Gives +40 Defense Skill, +8 healing Skill'}, 'Feet', {'Defense': 40, 'Healing': 8}],

    [{'GriffinHelmet': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Head', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinChestplate': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Chest', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinLeggings': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Legs', {'Defense': 24, 'Healing': 5, 'Agility': 5}],
    [{'GriffinBoots': 'Gives +24 Defense Skill, +5 healing Skill, +5 Agility Skill'}, 'Feet', {'Defense': 24, 'Healing': 5, 'Agility': 5}],

    [{'BasaltHelmet': 'Gives +32 Defense Skill, -7 Health Skill'}, 'Head', {'Defense': 32, 'Health': -7}],

    [{'EternalHelmet': 'Gives +12 Defense Skill, +10 Health Skill'}, 'Head', {'Defense': 12, 'Health': 10}],
    [{'EternalChestplate': 'Gives +16 Defense Skill, +10 Health Skill'}, 'Chest', {'Defense': 16, 'Health': 10}],
    [{'EternalLeggings': 'Gives +13 Defense Skill, +10 Health Skill'}, 'Legs', {'Defense': 13, 'Health': 10}],
    [{'EternalBoots': 'Gives +16 Defense Skill, +10 Health Skill'}, 'Feet', {'Defense': 16, 'Health': 10}],

    [{'TinBoots': 'Gives +5 Defense Skill'}, 'Feet', {'Defense': 5}],
    [{'TinLeggings': 'Gives +5 Defense Skill'}, 'Legs', {'Defense': 5}],
    [{'TinChestplate': 'Gives +5 Defense Skill'}, 'Chest', {'Defense': 5}],
    [{'TinHelmet': 'Gives +5 Defense Skill'}, 'Head', {'Defense': 5}],

    [{'HallowedHelmet': 'Gives +30 Defense Skill, +6 Luck Skill'}, 'Head', {'Defense': 30, 'Luck': 6}],
    [{'HallowedChestplate': 'Gives +30 Defense Skill, +6 Luck Skill'}, 'Chest', {'Defense': 30, 'Luck': 6}],
    [{'HallowedLeggings': 'Gives +30 Defense Skill, +6 Luck Skill'}, 'Legs', {'Defense': 30, 'Luck': 6}],
    [{'HallowedBoots': 'Gives +30 Defense Skill, +6 Luck Skill'}, 'Feet', {'Defense': 30, 'Luck': 6}],
    [{'HallowedSpear': 'Gives +30 Defense Skill, +5 Combat Skill'}, 'Hand', {'Defense': 30, 'Combat': 5}],

    [{'Shield': 'Grants 5 shield each turn'}, 'Hand', {}],
    [{'EternalGuardianShield': 'Gives +30 Defense Skill'}, 'Hand', {'Defense': 30}],
    [{'BasaltShield': 'Gives +15 Defense Skill'}, 'Hand', {'Defense': 15}],
    [{'OldIronChestplate': 'Gives +6 Defense Skill'}, 'Chest', {'Defense': 6}],


    # combat
    [{'HellHoundHelmet': 'Gives +41 Combat Skill, -7 healing Skill, +5 Defense Skill'}, 'Head', {'Combat': 41, 'Healing': -7, 'Defense': 5}],
    [{'HellHoundChestplate': 'Gives +41 Combat Skill, -9 healing Skill, +5 Defense Skill'}, 'Chest', {'Combat': 41, 'Healing': -9, 'Defense': 5}],
    [{'HellHoundLeggings': 'Gives +41 Combat Skill, -8 healing Skill, +5 Defense Skill'}, 'Legs', {'Combat': 41, 'Healing': -8, 'Defense': 5}],
    [{'HellHoundBoots': 'Gives +41 Combat Skill, -6 healing Skill, +5 Defense Skill'}, 'Feet', {'Combat': 41, 'Healing': -6, 'Defense': 5}],

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
    [{'LavaSword': 'Gives +52 Combat Skill'}, 'Hand', {'Combat': 52}],
    [{'PunySword': 'Gives +6 Combat Skill'}, 'Hand', {'Combat': 6}],
    [{'SteelGreatSword': 'Gives +20 Combat Skill'}, 'Hand', {'Combat': 20}],
    [{'Katana': 'Gives +12 Combat Skill, +12 Agility Skill'}, 'Hand', {'Combat': 12, 'Agility': 12}],

    [{'FangRing': 'Gives +15 Combat Skill'}, 'Ring', {'Combat': 15}],
    [{'FuryRageRing': 'Gives +21 Combat Skill, -12 Defense Skill'}, 'Ring', {'Combat': 21, 'Defense': -12}],
    [{'RavenEyeRing': 'Gives +52 Combat Skill, -11 Dodge Skill, +5 Health Skill'}, 'Ring', {'Combat': 52, 'Dodge': -11, 'Health': 5}],

    # agility
    # not added yet:
    [{'ShadowScaleHelmet': 'Gives +28 Agility Skill, -5 Health Skill'}, 'Head', {'Agility': 28, 'Health': -5}],
    [{'ShadowScaleChestplate': 'Gives +28 Agility Skill, -8 Health Skill'}, 'Chest', {'Agility': 28, 'Health': -8}],
    [{'ShadowScaleLeggings': 'Gives +28 Agility Skill, -4 Health Skill'}, 'Legs', {'Agility': 28, 'Health': -4}],
    [{'ShadowScaleBoots': 'Gives +28 Agility Skill, -6 Health Skill'}, 'Feet', {'Agility': 28, 'Health': -6}],

    [{'ThiefHelmet': 'Gives +8 Stealing, +10 Agility Skill'}, 'Head', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefChestplate': 'Gives +8 Stealing, +10 Agility Skill'}, 'Chest', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefLeggings': 'Gives +8 Stealing, +10 Agility Skill'}, 'Legs', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefBoots': 'Gives +8 Stealing, +10 Agility Skill'}, 'Feet', {'Stealing': 8, 'Agility': 10}],
    [{'ThiefRing': 'Gives +10 Stealing, +10 Agility Skill'}, 'Ring', {'Stealing': 10, 'Agility': 10}],

    [{'HelixHelmet': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Head', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixChestplate': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Chest', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixLeggings': 'Gives +10 Dodge, +10 Agility, +10 Health Skill'}, 'Legs', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixBoots': 'Gives +10 Dodge, +10 Agility, +10 Health Skill, '}, 'Feet', {'Dodge': 10, 'Agility': 10, 'Health': 10}],
    [{'HelixCoreSword': '+18 Agility, +5 Health Skill, '}, 'Hand', {'Agility': 18, 'Health': 5}],

    [{'AssassinsHelmet': 'Gives +13 Agility Skill'}, 'Head', {'Agility': 13}],
    [{'AssassinsChestplate': 'Gives +13 Agility Skill'}, 'Chest', {'Agility': 13}],
    [{'AssassinsLeggings': 'Gives +13 Agility Skill'}, 'Legs', {'Agility': 13}],
    [{'AssassinsBoots': 'Gives +13 Agility Skill'}, 'Feet', {'Agility': 13}],

    [{'SkyDarkHelmet': 'Gives +12 Dodge Skill'}, 'Head', {'Dodge': 12}],
    [{'SkyDarkChestplate': 'Gives +12 Dodge Skill'}, 'Chest', {'Dodge': 12}],
    [{'SkyDarkLeggings': 'Gives +12 Dodge Skill'}, 'Legs', {'Dodge': 12}],
    [{'SkyDarkBoots': 'Gives +15 Dodge Skill'}, 'Feet', {'Dodge': 15}],

    [{'SkeletalChestplate': 'Gives +19 Agility Skill'}, 'Chest', {'Agility': 19}],
    [{'DarkBoots': 'Gives +18 Agility Skill'}, 'Feet', {'Agility': 18}],

    [{'AbyssalDagger': 'Gives +6 Agility Skill, +4 Defense Skill'}, 'Hand', {'Agility': 6, 'Defense': 4}],
    [{'BonerSword': 'Gives +10 Agility Skill, +10 Dodge Skill'}, 'Hand', {'Agility': 10, 'Dodge': 10}],
    [{'WraithDagger': 'Gives +6 Agility Skill, +17 Dodge Skill'}, 'Hand', {'Agility': 6, 'Dodge': 17}],


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


    # Magic

    [{'MagicChestplate': 'Gives +5 Magic Skill'}, 'Chest', {'Magic': 5}],
    [{'ElementalChestplate': 'Gives +15 Magic Skill'}, 'Chest', {'Magic': 15}],
    [{'ArchMageChestplate': 'Gives +27 Magic Skill'}, 'Chest', {'Magic': 27}],

    [{'ArcaneHelmet': 'Gives +22 Magic Skill'}, 'Head', {'Magic': 22}],
    [{'ArcaneChestplate': 'Gives +21 Magic Skill'}, 'Chest', {'Magic': 21}],
    [{'ArcaneLeggings': 'Gives +24 Magic Skill'}, 'Legs', {'Magic': 24}],
    [{'ArcaneBoots': 'Gives +20 Magic Skill'}, 'Feet', {'Magic': 20}],

    [{'NecromancerHelmet': 'Gives +20 Magic Skill, -9 health skill'}, 'Head', {'Magic': 20, 'Health': -9}],
    [{'NecromancerChestplate': 'Gives +32 Magic Skill, -9 health skill'}, 'Chest', {'Magic': 32, 'Health': -9}],
    [{'NecromancerLeggings': 'Gives +27 Magic Skill, -9 health skill'}, 'Legs', {'Magic': 27, 'Health': -9}],
    [{'NecromancerBoots': 'Gives +24 Magic Skill, -9 health skill'}, 'Feet', {'Magic': 24, 'Health': -9}],

    [{'DarkPhoenixHelmet': 'Gives +31 Magic Skill, -10 Defense skill'}, 'Head', {'Magic': 31, 'Defense': -10}],
    [{'DarkPhoenixChestplate': 'Gives +31 Magic Skill, -10 Defense skill'}, 'Chest', {'Magic': 31, 'Defense': -10}],
    [{'DarkPhoenixLeggings': 'Gives +31 Magic Skill, -10 Defense skill'}, 'Legs', {'Magic': 31, 'Defense': -10}],
    [{'DarkPhoenixBoots': 'Gives +31 Magic Skill, -10 Defense skill'}, 'Feet', {'Magic': 31, 'Defense': -10}],

    [{'InfinityBoots': 'Gives +30 Magic Skill'}, 'Feet', {'Magic': 30}],
    [{'SpectralHelmet': 'Gives +19 Magic, +9 Critical Skill'}, 'Head', {'Magic': 19, 'Critical': 9}],
    [{'SpectralChestplate': 'Gives +19 Magic, +9 Critical Skill'}, 'Chest', {'Magic': 19, 'Critical': 9}],
    [{'SpectralLeggings': 'Gives +19 Magic, +9 Critical Skill'}, 'Legs', {'Magic': 19, 'Critical': 9}],
    [{'CursedMask': 'Gives -10 Defense Skill, -5 Luck Skill, +23 Magic Skill'}, 'Head', {'Magic': 23, 'Luck': -5, 'Defense': -10}],
    [{'SpectralBoots': 'Gives +19 Magic, +9 Critical Skill'}, 'Feet', {'Magic': 19, 'Critical': 9}],

    [{'WarlockLeggings': 'Gives +15 Magic Skill, -3 Healing Skill'}, 'Legs', {'Magic': 15, 'Healing': -3}],
    [{'WarlockBoots': 'Gives +15 Magic Skill, -3 Healing Skill'}, 'Feet', {'Magic': 15, 'Healing': -3}],

    [{'MagicStaff': 'Gives +9 Magic Skill'}, 'Hand', {'Magic': 9}],
    [{'ElectrumWand': 'Gives +17 Magic Skill'}, 'Hand', {'Magic': 17}],
    [{'SorcererWand': 'Gives +14 Magic Skill, +2 Defense Skill'}, 'Hand', {'Magic': 14, 'Defense': 2}],
    [{'MagicDagger': 'Gives +7 Magic Skill, +4 Agility Skill'}, 'Hand', {'Magic': 7, 'Agility': 4}],
    [{'DiabloRing': 'Gives +49 Magic Skill'}, 'Ring', {'Magic': 49}],
    [{'StaffOfAegis': 'Gives +63 Magic Skill'}, 'Hand', {'Magic': 63}],
    [{'TormentShard': 'Gives +12 Magic Skill, +8 Healing Skill'}, 'Hand', {'Magic': 12, 'Healing': 8}],
    [{'SlimeRing': 'Gives +4 Magic Skill, +4 Healing Skill'}, 'Ring', {'Magic': 4, 'Healing': 4}],
    [{'MagicRing': 'Gives +6 Magic Skill'}, 'Ring', {'Magic': 6}],
    [{'ArchmageRing': 'Gives +20 Magic Skill'}, 'Ring', {'Magic': 20}],
    [{'ChaosRing': 'Gives +43 Magic Skill, -10 Health Skill, -5 Defense Skill'}, 'Ring', {'Magic': 43, 'Health': -10, 'Defense': -5}],
    [{'FrostRing': 'Gives +21 Magic Skill, +2 Dodge Skill'}, 'Ring', {'Magic': 21, 'Dodge': 2}],

    # other
    [{'LuckyStick': 'Gives +18 Luck Skill'}, 'Hand', {'Luck': 18}],




    # health
    [{'AncientChestplate': 'Gives +16 Health Skill'}, 'Chest', {'Health': 16}],
    [{'PurityChestplate': 'Gives +30 Health Skill'}, 'Chest', {'Health': 30}],

    # healing

    [{'RestoreWand': 'Gives +2 Healing Skill, +2 Magic'}, 'Hand', {'Healing': 2, 'Magic': 2}],
    [{'UnholyStaff': 'Gives +12 Healing Skill, +7 Health'}, 'Hand', {'Healing': 12, 'Health': 7}],
    [{'DemonScythe': 'Gives +15 Healing Skill, +6 Magic, +6 Dodge'}, 'Hand', {'Healing': 15, 'Magic': 6, 'Dodge': 6}],
    [{'WandOfHealing': 'Gives +20 Healing Skill'}, 'Hand', {'Healing': 20}],
    [{'Spellbinder': 'Gives +9 Healing Skill, +9 Defense'}, 'Hand', {'Healing': 9, 'Defense': 9}],
    [{'ProtectorsCurse': 'Gives +10 Healing Skill, +8 Defense, -6 Health'}, 'Hand', {'Healing': 10, 'Defense': 8, 'Health': -6}],


    [{'AngelHelmet': 'Gives +60 Healing Skill'}, 'Head', {'Healing': 60}],
    [{'AngelChestplate': 'Gives +60 Healing Skill'}, 'Chest', {'Healing': 60}],
    [{'AngelLeggings': 'Gives +60 Healing Skill'}, 'Legs', {'Healing': 60}],
    [{'AngelBoots': 'Gives +60 Healing Skill'}, 'Feet', {'Healing': 60}],

    [{'CrystalHelmet': 'Gives +6 Healing Skill'}, 'Head', {'Healing': 6}],
    [{'CrystalChestplate': 'Gives +6 Healing Skill'}, 'Chest', {'Healing': 6}],
    [{'CrystalLeggings': 'Gives +6 Healing Skill'}, 'Legs', {'Healing': 6}],
    [{'CrystalBoots': 'Gives +6 Healing Skill'}, 'Feet', {'Healing': 6}],

    [{'TrueSteelHelmet': 'Gives +9 Healing Skill, +2 Magic Skill'}, 'Head', {'Healing': 9, 'Magic': 2}],
    [{'TrueSteelChestplate': 'Gives +12 Healing Skill, +4 Magic Skill'}, 'Chest', {'Healing': 12, 'Magic': 4}],
    [{'TrueSteelLeggings': 'Gives +14 Healing Skill, +8 Magic Skill'}, 'Legs', {'Healing': 14, 'Magic': 8}],
    [{'TrueSteelBoots': 'Gives +9 Healing Skill, +4 Magic Skill'}, 'Feet', {'Healing': 9, 'Magic': 4}],

    [{'EbonHelmet': 'Gives +18 Healing Skill'}, 'Head', {'Healing': 18}],
    [{'EbonChestplate': 'Gives +18 Healing Skill'}, 'Chest', {'Healing': 18}],
    [{'EbonLeggings': 'Gives +18 Healing Skill'}, 'Legs', {'Healing': 18}],
    [{'EbonBoots': 'Gives +18 Healing Skill'}, 'Feet', {'Healing': 18}],

    [{'AberrantHelmet': 'Gives +24 Healing Skill, +16 Dodge'}, 'Head', {'Healing': 24, 'Dodge': 16}],
    [{'AberrantChestplate': 'Gives +18 Healing Skill, +8 Dodge'}, 'Chest', {'Healing': 18, 'Dodge': 8}],
    [{'AberrantLeggings': 'Gives +24 Healing Skill, +16 Dodge'}, 'Legs', {'Healing': 24, 'Dodge': 16}],
    [{'AberrantBoots': 'Gives +18 Healing Skill, +8 Dodge'}, 'Feet', {'Healing': 18, 'Dodge': 8}],




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
    [{'Onepunch': "(combat) Damage - 18"}, 'Card', {'Combat': 18}],
    [{'Slam': "(combat) Damage - 5, Shield - 5, Heal - 4"}, 'Card', {'Combat': 5, 'Defense': 5, 'Healing': 4}],
    [{'Smash': "(combat) Damage - 3, Heal - 10"}, 'Card', {'Combat': 3, 'Healing': 4}],
    [{'DarkCharge': "(combat) Damage - 12, Extra Card Draw"}, 'Card', {'Combat': 12, 'Draw': 1}],
    [{'Shatter': "(combat) Damage - 9, Heal - 5"}, 'Card', {'Combat': 9, 'Healing': 5}],
    [{'RagingFury': "(combat) Damage - 6, Heal - 6"}, 'Card', {'Combat': 6, 'Healing': 6}],
    [{'JumpKick':  "Damage - 10, Lose Defense - 5"}, 'Card', {'Combat': 10, 'Reduce Shield': 5}],


    # healing
    [{'Recharge': "Heal - 8"}, 'Card', {'Healing': 8}],
    [{'Regeneration': "Heal - 18"}, 'Card', {'Healing': 18}],
    [{'Restoration': "Heal - 14, Extra Card Draw"}, 'Card', {'Healing': 14, 'Draw': 1}],
    [{'HeavenlyGuard': "Heal - 20, Shield - 10"}, 'Card', {'Healing': 20, 'Shield': 10}],
    [{'LifeTap': "Heal - 45, self - 45"}, 'Card', {'Healing': 45, 'Self': 100}],

    # defense
    [{'Defend': "Shield - 5"}, 'Card', {'Defense': 5}],
    [{'Towershield': "Shield - 12"}, 'Card', {'Defense': 12}],
    [{'LeechingWard': "Shield - 28, Self Damage - 20"}, 'Card', {'Defense': 30, 'Self': 80}],
    [{'GoddessProtection': "Shield - 14, Healing - 10"}, 'Card', {'Defense': 14, 'Healing': 10}],
    [{'HolyShield': "Shield - 15, , Extra Card Draw"}, 'Card', {'Defense': 15, 'Draw': 1}],

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
