#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Item:
	def __init__(self, row):
		self.item_id = row[0]
		self.count = 1
		self.warehouse = 0
		self.pict_id = row[1]
		self.name = row[3]
		self.type = row[4]
		self.price = row[5]
		self.weight = row[6]
		self.capa = row[7]
		self.stock = row[16]
		self.durability_max = row[20]
		self.eventid = row[24]
		self.hp = row[39]
		self.mp = row[40]
		self.sp = row[41]
		self.speed = row[44]
		self.str = row[45]
		self.mag = row[46]
		self.vit = row[47]
		self.dex = row[48]
		self.agi = row[49]
		self.int = row[50]
		self.luk = row[51]
		self.cha = row[52]
		self.atk1 = row[53]
		self.atk2 = row[54]
		self.atk3 = row[55]
		self.matk = row[56]
		self.DEF = row[57]
		self.mdef = row[58]
		self.s_hit = row[59]
		self.l_hit = row[60]
		self.magic_hit = row[61]
		self.s_avoid = row[62]
		self.l_avoid = row[63]
		self.magic_avoid = row[64]
		self.critical_hit = row[65]
		self.critical_avoid = row[66]
		self.heal_hp = row[67]
		self.heal_mp = row[68]
		self.energy = row[69]
		self.fire = row[70]
		self.water = row[71]
		self.wind = row[72]
		self.earth = row[73]
		self.light = row[74]
		self.dark = row[75]
		self.poison = row[76]
		self.stone = row[77]
		self.paralyze = row[78]
		self.sleep = row[79]
		self.silence = row[80]
		self.slow = row[81]
		self.confuse = row[82]
		self.freeze = row[83]
		self.stan = row[84]
		self.petid = row[167]
	
	def __str__(self):
		return "%s<%s, %s, %d>"%(
			repr(self),
			self.item_id,
			self.name.decode("utf-8").encode(sys.getfilesystemencoding()),
			self.count)