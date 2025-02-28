#!/usr/bin/env python
# -*- coding: utf-8 -*-
from general import NULL

def dbstr(s): 
	return str(s)

def dbint(i):
	if i in ("", "."):
		return 0
	return int(i)

def dbfloat(i):
	if i in ("", "."):
		return 0.0
	return float(i)

DATABASE_PATH = {
	"item": "./data/item.csv",
	"job": "./data/job.csv",
	"map": "./data/map.csv",
	"monster": "./data/monster.csv",
	"npc": "./data/npc.csv",
	"partner": "./data/partner_info.csv",
	"pet": "./data/pet.csv",
	"shop": "./data/shop.csv",
	"skill": "./data/skill.csv",
}

DATABASE_ROW_MAP_RAW = {
	"item": {
		"#ItemID": (dbint, "item_id"),
		"PictID": (dbint, "pict_id"),
		"IconID": NULL,
		"アイテム名": (dbstr, "name"),
		"振り仮名（アイテム名）": NULL,
		"種別ID": (dbstr, "type"),
		"値段": (dbint, "price"),
		"重量": (dbint, "weight"), #payl
		"容量": (dbint, "capa"),
		"装備時容量": NULL,
		"憑依重量（未使用）": NULL,
		"修理": NULL,
		"強化ID（未使用）": NULL,
		"処理フラグ0": NULL,
		"イベントアイテムフラグ": NULL,
		"レシピ表示": NULL,
		"染色": NULL,
		"ストック": (dbint, "stock"),
		"両手装備フラグ": NULL,
		"使用時消滅": (dbint, "disposable"),
		"色": (dbint, "color"),
		"耐久度": (dbint, "durability_max"),
		"ジョイントジョブＩＤ": NULL,
		"初期イリスカードスロット数": NULL,
		"アイテムチェンジ可否フラグ": NULL,
		"イベントＩＤ": (dbint, "event_id"),
		"エフェクトＩＤ": NULL,
		"発動Skill": (dbint, "skill_id"),
		"使用可能Skill": (dbint, "skill_id_add"),
		"パッシブスキル": NULL,
		"憑依時可能Skill": NULL,
		"憑依パッシブSkill": NULL,
		"ターゲットタイプ": NULL,
		"発動タイプ": NULL,
		"射程": NULL,
		"効果時間": NULL,
		"効果範囲": NULL,
		"効果値": NULL,
		"キャスト": NULL,
		"ディレイ": NULL,
		"HP上昇": (dbint, "hp"),
		"MP上昇": (dbint, "mp"),
		"SP上昇": (dbint, "sp"),
		"最大重量上昇": (dbint, "payl_add"),
		"最大容量上昇": (dbint, "capa_add"),
		"移動力上昇": (dbint, "speed"),
		"STR": (dbint, "str"),
		"MAG": (dbint, "mag"),
		"VIT": (dbint, "vit"),
		"DEX": (dbint, "dex"),
		"AGI": (dbint, "agi"),
		"INT": (dbint, "int"),
		"LUK": (dbint, "luk"),
		"CHA": (dbint, "cha"),
		"物理攻撃力(叩)": (dbint, "atk1"),
		"物理攻撃力(斬)": (dbint, "atk2"),
		"物理攻撃力(突)": (dbint, "atk3"),
		"魔法攻撃力": (dbint, "matk"),
		"物理防御力": (dbint, "DEF"),
		"魔法防御力": (dbint, "mdef"),
		"近命中力": (dbint, "s_hit"),
		"遠命中力": (dbint, "l_hit"),
		"魔法命中力": (dbint, "magic_hit"),
		"近回避力": (dbint, "s_avoid"),
		"遠回避力": (dbint, "l_avoid"),
		"魔回避力": (dbint, "magic_avoid"),
		"クリ力": (dbint, "critical_hit"),
		"クリ回避": (dbint, "critical_avoid"),
		"回復力": (dbint, "heal_hp"),
		"魔法回復力": (dbint, "heal_mp"),
		"無": (dbint, "energy"),
		"火": (dbint, "fire"),
		"水": (dbint, "water"),
		"風": (dbint, "wind"),
		"土": (dbint, "earth"),
		"光": (dbint, "light"),
		"闇": (dbint, "dark"),
		"毒": (dbint, "poison"),
		"石化": (dbint, "stone"),
		"麻痺": (dbint, "paralyze"),
		"睡眠": (dbint, "sleep"),
		"沈黙": (dbint, "silence"),
		"鈍足": (dbint, "slow"),
		"混乱": (dbint, "confuse"),
		"凍結": (dbint, "freeze"),
		"気絶": (dbint, "stan"),
		"エミル種族": NULL,
		"タイタニア種族": NULL,
		"ドミニオン種族": NULL,
		"DEM種族": NULL,
		"男": NULL,
		"女": NULL,
		"LV": NULL,
		"転生時のみ装備可": NULL,
		"装備可STR": NULL,
		"装備可MAG": NULL,
		"装備可VIT": NULL,
		"装備可DEX": NULL,
		"装備可AGI": NULL,
		"装備可INT": NULL,
		"装備可LUK": NULL,
		"装備可CHA": NULL,
		"ノービス": NULL,
		"ソードマン": NULL,
		"ブレマス": NULL,
		"バウンテ": NULL,
		"フェンサ": NULL,
		"ナイト": NULL,
		"ダークスト": NULL,
		"スカウト": NULL,
		"アサシン": NULL,
		"コマンド": NULL,
		"アーチャ": NULL,
		"ストライ": NULL,
		"ガンナー": NULL,
		"ウィザ": NULL,
		"ソーサラ": NULL,
		"セージ": NULL,
		"シャーマン": NULL,
		"エレメン": NULL,
		"エンチャン": NULL,
		"ウァテス": NULL,
		"ドルイド": NULL,
		"バード": NULL,
		"ウォーロ": NULL,
		"カバリ": NULL,
		"ネクロマ": NULL,
		"タタラベ": NULL,
		"ブラスミ": NULL,
		"マシンナ": NULL,
		"ファーマ": NULL,
		"アルケミ": NULL,
		"マリオネ": NULL,
		"レンジャ": NULL,
		"エクスプ": NULL,
		"トレジャ": NULL,
		"マーチャ": NULL,
		"トレーダ": NULL,
		"ギャンブラー": NULL,
		"グラディエイター": NULL,
		"ガーディアン": NULL,
		"イレイザー": NULL,
		"ホークアイ": NULL,
		"フォースマスター": NULL,
		"アストラリスト": NULL,
		"カーディナル": NULL,
		"ソウルテイカー": NULL,
		"マエストロ": NULL,
		"ハーヴェスト": NULL,
		"ストライダー": NULL,
		"ロイヤルディーラー": NULL,
		"ジョーカー": NULL,
		"東軍": NULL,
		"西軍": NULL,
		"南軍": NULL,
		"北軍": NULL,
		"所属５（未使用）": NULL,
		"所属６（未使用）": NULL,
		"所属７（未使用）": NULL,
		"所属８（未使用）": NULL,
		"ブリーダー": NULL,
		"ガーデナー": NULL,
		"フラグ３（未使用）": NULL,
		"フラグ４（未使用）": NULL,
		"フラグ５（未使用）": NULL,
		"フラグ６（未使用）": NULL,
		"フラグ７（未使用）": NULL,
		"マリオネットＩＤ": NULL,
		"封印モンＩＤ": (dbint, "pet_id"),
		"片手モーションID": (dbint, "s_motion"),
		"両手モーションID": (dbint, "d_motion"),
		"右手憑依者モーション": NULL,
		"左手憑依者モーション": NULL,
		"胸アクセ憑依者モーション": NULL,
		"鎧憑依者モーション": NULL,
		"アイテム説明": NULL,
		"国内専用アイテムフラグ": NULL,
		"課金アイテムフラグ": NULL,
		"ゴーレムカタログアイテム検索フラグ": NULL,
		"ワールド用リサイクルポイント": NULL,
	},
	"job": {
		"#job_id": (dbint, "job_id"),
		"job_name": (dbstr, "name"),
		"hp_rate": (dbfloat, "hp_rate"),
		"mp_rate": (dbfloat, "mp_rate"),
		"sp_rate": (dbfloat, "sp_rate"),
		"payl_rate": (dbfloat, "payl_rate"),
		"capa_rate": (dbfloat, "capa_rate"),
	},
	"map": {
		"#マップＩＤ": (dbint, "map_id"),
		"マップ名": (dbstr, "name"),
		"中心座標ｘ": (dbfloat, "centerx"),
		"中心座標ｙ": (dbfloat, "centery"),
	},
	"monster": {
		"#ID": (dbint, "monster_id"),
		"EXP": (dbint, "base_exp"),
		"JOB": (dbint, "job_exp"),
	},
	"npc": {
		"#NPCID": (dbint, "npc_id"),
		"NAME": (dbstr, "name"),
	},
	"partner": {
		"#パートナーID": (dbint, "pet_id"),
		"パートナー名": (dbstr, "name"),
		"PICTID": (dbint, "pict_id"),
		"モーションセット番号": (dbint, "motion_set"),
		"種別ID": (dbstr, "pet_type"),
	},
	"pet": {
		"#PETID": (dbint, "pet_id"),
		"ペット名": (dbstr, "name"),
		"PICTID": (dbint, "pict_id"),
		"モーションセット番号": (dbint, "motion_set"),
		"種別ID": (dbstr, "pet_type"),
	},
	"shop": {
		"#ショップID": (dbint, "shop_id"),
		"商品ID1": (dbint, 1),
		"商品ID2": (dbint, 2),
		"商品ID3": (dbint, 3),
		"商品ID4": (dbint, 4),
		"商品ID5": (dbint, 5),
		"商品ID6": (dbint, 6),
		"商品ID7": (dbint, 7),
		"商品ID8": (dbint, 8),
		"商品ID9": (dbint, 9),
		"商品ID10": (dbint, 10),
		"商品ID11": (dbint, 11),
		"商品ID12": (dbint, 12),
		"商品ID13": (dbint, 13),
	},
	"skill": {
		'"ID"': (dbint, "skill_id"),
		'"Name"': (dbstr, "name"),
		'"説明"': NULL,
		'"Active"': NULL,
		'"MaxLv"': (dbint, "maxlv"),
		'"Lv"': NULL,
		'"MP"': NULL,
		'"SP"': NULL,
		'"HP"': NULL,
		'"射程"': NULL,
		'"ターゲット"': NULL,
		'"ターゲット2"': NULL,
		'"範囲"': NULL,
		'"適応"': NULL,
		'"Zero"': NULL,
		'"Flag"': NULL,
		'"?"': NULL,
		'"nTarget2"': NULL,
		'"射程"': NULL,
		'"0"': NULL,
		'"MarkTarget"': NULL,
		'"MarkTarget"': NULL,
		'"MarkCaster"': NULL,
		'"icon"': NULL,
		'"MarkTarget"': NULL,
		'"0"': NULL,
		'"mark?"': NULL,
		'"MarkRound"': NULL,
		'"MarknewObj"': NULL,
		'"AnimStart"': NULL,
		'"AnimLoop"': NULL,
		'"AnimAttack"': NULL,
	},
}

DATABASE_ROW_MAP_EXT = {
	"hair_info": {},
	"item": {
		#3: (dbstr, "name"),
	},
	"job": {},
	"map": {},
	"monster": {
		1: (dbstr, "name"),
	},
	"npc": {},
	"partner": {
		9: (dbint, "speed"),
	},
	"pet": {
	},
	"shop": {},
	"skill": {},
}