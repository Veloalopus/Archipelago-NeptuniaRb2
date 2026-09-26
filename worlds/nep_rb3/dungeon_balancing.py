#ef hasNeptune(state, player):
#   return state.has("Character - Neptune", player)
#
#ef hasNepgear(state, player):
#   return state.has("Character - Nepgear", player)
#
#ef hasVert(state, player):
#   return state.has("Character - Vert", player)
#
#ef hasBlanc(state, player):
#   return state.has("Character - Blanc", player)
#
#ef hasNoire(state, player):
#   return state.has("Character - Noire", player)
#
#ef hasPlutia(state, player):
#   return state.has("Character - Plutia", player)
#
#ef hasPeashy(state, player):
#   return state.has("Character - Peashy", player)
#
#ef hasRom(state, player):
#   return state.has("Character - Rom", player)
#
#ef hasRam(state, player):
#   return state.has("Character - Ram", player)
#
#ef hasUni(state, player):
#   return state.has("Character - Uni", player)
#
#ef ch3Armor(state, player):
#   return state.has("Progressive Armor", player, 1)
#
#ef ch6Armor(state, player):
#   return state.has("Progressive Armor", player, 2)
#
#ef ch9Armor(state, player):
#   return state.has("Progressive Armor", player, 3)
#
#This tier is finally better than base candidate armor
#ef charArmor(state, player):
#   return state.has("Progressive Armor", player, 4)
#
#ef eventArmor(state, player):
#   return state.has("Progressive Armor", player, 5)
#
#ef postgameArmor(state, player):
#   return state.has("Progressive Armor", player, 6)
#
#ef neptuneT1(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 1)
#
#ef neptuneT2(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 2)
#
#ef neptuneT3(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 3)
#This tier is better than base candidate weapons
#ef neptuneT4(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 4)
#
#ef neptuneT5(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 5)
#
#ef neptuneT6(state, player):
#   return state.has("Neptune - Progressive Weapons", player, 6)
#
#ef noireT1(state, player):
#   return state.has("Noire - Progressive Weapons", player, 1)
#
#ef noireT2(state, player):
#   return state.has("Noire - Progressive Weapons", player, 2)
#
#ef noireT3(state, player):
#   return state.has("Noire - Progressive Weapons", player, 3)
#
#ef noireT4(state, player):
#   return state.has("Noire - Progressive Weapons", player, 4)
#
#ef noireT5(state, player):
#   return state.has("Noire - Progressive Weapons", player, 5)
#
#ef plutiaT1(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 1)
#
#ef plutiaT2(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 2)
#
#ef plutiaT3(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 3)
#
#ef plutiaT4(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 4)
#
#ef plutiaT5(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 5)
#
#ef plutiaT6(state, player):
#   return state.has("Plutia - Progressive Weapons", player, 6)
#
#
#
#ef VirtuaForestSafeZone(state, player):
#   return True
#
#ef StationArea(state, player):
#   return True
#
#ef ZecaRuinsNo1(state, player):
#   viable_members = 0
#   if hasRam(state, player):
#       return True
#
#   if hasUni(state, player):
#       return True
#
#   if hasRom(state, player):
#       return True
#
#   if hasPeashy(state, player):
#       return True
#
#   if hasBlanc(state, player):
#       return True
#
#   if hasVert(state, player):
#       return True
#
#   if hasNepgear(state, player):
#       return True
#
#   if hasNeptune(state, player):
#       if neptuneT1(state, player) and ch3Armor(state, player):
#           viable_members += 1
#
#   if hasNoire(state, player):
#       if noireT1(state, player) and ch3Armor(state, player):
#           viable_members += 1
#
#   if hasPlutia(state, player):
#       if plutiaT1(state, player) and ch3Armor(state, player):
#           viable_members += 1
#
#   if viable_members >= 2:
#       return True