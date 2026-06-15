# ============================================================
#  頑扣 FunnyCoding｜Python 魔法夏令營 — 下午實作 Demo
#  Day 3：回合制戰鬥系統
#  對應上午觀念：for + range() / 累加 / while / break / continue
#  ──────────────────────────────────────────────
#  ⚠️ 教師示範版（解答），請勿直接發給學生。
#  ▶ 本日重點：用 while 迴圈讓「戰鬥一回合接一回合」自動進行，
#     直到一方 HP 歸零；用 break 結束戰鬥、continue 跳過攻擊。
#  ▶ 本日學生應完成的進度：能和怪物進行多回合戰鬥並分出勝負
# ============================================================

print("=" * 40)
print("⚔️ 《魔法地下城》第三章：哥布林來襲")
print("=" * 40)

name = input("勇者，請報上你的名字：")
hero_hp = 100   # 勇者生命值
hero_atk = 20   # 勇者攻擊力
goblin_hp = 60  # 哥布林生命值

# ── 1) 戰鬥倒數：用 for + range() 跑固定次數 ──
print()
print("戰鬥即將開始！")
for i in range(3, 0, -1):   # 3, 2, 1
    print(f"   {i}...")
print("   開始！")

print()
print(f"{name}（HP {hero_hp}）遭遇了哥布林（HP {goblin_hp}）！")
print("每回合輸入指令 → a：攻擊　　h：喝藥水回血")
print("-" * 40)

# ── 2) 回合迴圈：用 while，兩邊都還活著就繼續打 ──
turn = 1
while hero_hp > 0 and goblin_hp > 0:
    print(f"【第 {turn} 回合】你 HP={hero_hp}　哥布林 HP={goblin_hp}")
    cmd = input("你的行動 (a/h)：")

    # ── continue：喝藥水這回合不攻擊，直接進下一回合 ──
    if cmd == "h":
        hero_hp = hero_hp + 15   # 累加回血
        print("🧪 你喝下藥水，HP +15！（這回合沒有攻擊）")
        turn = turn + 1
        continue

    if cmd != "a":
        print("❓ 看不懂的指令，這回合白白浪費了……")
        turn = turn + 1
        continue

    # ── 玩家攻擊（累減敵人 HP）──
    goblin_hp = goblin_hp - hero_atk
    print(f"🗡️ 你攻擊哥布林，造成 {hero_atk} 點傷害！")

    # ── break：敵人倒下，立刻跳出戰鬥迴圈 ──
    if goblin_hp <= 0:
        print("💥 哥布林被擊倒了！")
        break

    # ── 哥布林反擊 ──
    hero_hp = hero_hp - 10
    print("👹 哥布林反咬一口，你失去 10 點 HP！")
    turn = turn + 1

# ── 3) 戰鬥結算 ──
print("-" * 40)
if hero_hp > 0:
    print(f"🏆 勝利！{name} 在第 {turn} 回合擊敗了哥布林！")
else:
    print(f"☠️ {name} 倒下了……休息一下，下次再挑戰吧。")
