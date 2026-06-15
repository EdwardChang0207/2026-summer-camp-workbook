# ============================================================
#  頑扣 FunnyCoding｜Python 魔法夏令營 — 下午實作 Demo
#  Day 4：完整文字 RPG（期末成果整合版）
#  對應上午觀念：def / 參數 / return / list / .append() / len()
#                / random（randint、choice）＋ 前三天全部觀念
#  ──────────────────────────────────────────────
#  ⚠️ 教師示範版（解答），請勿直接發給學生。
#  ▶ 本日把前三天拆開的零件「組裝成一支完整遊戲」：
#     函式封裝戰鬥、list 管理敵人與背包、random 製造隨機性。
#  ▶ 本日學生應完成的進度：一支可從頭玩到尾、會打三場 BOSS 的文字 RPG
# ============================================================

import random


# ── 函式 1：建立角色（def + return）──
def create_hero():
    name = input("勇者，請報上你的名字：")
    return name


# ── 函式 2：一場戰鬥（def + 參數 + while + random + return）──
#    回傳「戰鬥後勇者剩餘 HP」；> 0 代表獲勝，<= 0 代表落敗
def battle(name, hero_hp, hero_atk, enemy_name, enemy_hp):
    print()
    print(f"⚔️ {name} 遭遇了 {enemy_name}（HP {enemy_hp}）！")
    while hero_hp > 0 and enemy_hp > 0:
        print(f"   你 HP={hero_hp}　｜　{enemy_name} HP={enemy_hp}")
        input("   （按 Enter 攻擊）")
        # random：每次攻擊傷害在 攻擊力±5 之間浮動
        dmg = random.randint(hero_atk - 5, hero_atk + 5)
        enemy_hp = enemy_hp - dmg
        print(f"   🗡️ 造成 {dmg} 點傷害！")
        if enemy_hp <= 0:
            print(f"   💥 {enemy_name} 被擊敗！")
            return hero_hp
        # 敵人反擊，傷害也是亂數
        edmg = random.randint(5, 15)
        hero_hp = hero_hp - edmg
        print(f"   👹 {enemy_name} 反擊，你失去 {edmg} HP！")
    return hero_hp


# ── 主程式 ──
print("=" * 44)
print("🐉 《魔法地下城》最終章：通往火龍王座")
print("=" * 44)

name = create_hero()
hero_hp = 100
hero_atk = 20

# list：用清單管理「要依序挑戰的敵人」，每個敵人是 [名稱, HP]
enemies = [["哥布林", 40], ["骸骨戰士", 60], ["火龍王", 100]]
loot_bag = []   # 背包：用 list + .append() 收集戰利品

# for：依序走訪敵人清單，一場一場打
for enemy in enemies:
    enemy_name = enemy[0]
    enemy_hp = enemy[1]
    hero_hp = battle(name, hero_hp, hero_atk, enemy_name, enemy_hp)

    if hero_hp <= 0:
        print(f"\n☠️ {name} 在 {enemy_name} 面前倒下了……冒險到此為止。")
        break

    # random.choice：從清單隨機掉落一件戰利品
    loot = random.choice(["金幣 💰", "藥水 🧪", "魔法卷軸 📜"])
    loot_bag.append(loot)
    print(f"   🎁 獲得戰利品：{loot}")

    hero_hp = hero_hp + 10   # 戰後稍作休息
    print(f"   ❤️ 你回復了一些體力，HP 來到 {hero_hp}")

# ── 結算（len 統計背包）──
print()
print("=" * 44)
if hero_hp > 0:
    print(f"🏆 恭喜！{name} 一路擊敗火龍王，成功通關地下城！")
print(f"📦 背包戰利品：{loot_bag}")
print(f"🎒 本次冒險共蒐集 {len(loot_bag)} 件寶物。")
print("=" * 44)
