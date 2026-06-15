# ============================================================
#  頑扣 FunnyCoding｜Python 魔法夏令營 — 下午實作 Demo
#  Day 2：職業選擇與劇情分支
#  對應上午觀念：比較運算子 / if / if-else / elif / and · or
#  ──────────────────────────────────────────────
#  ⚠️ 教師示範版（解答），請勿直接發給學生。
#  ▶ 本日在 Day1 角色卡的基礎上「加上選擇」：
#     讓玩家選職業、走岔路，程式用 if/elif/else 給不同結果。
#  ▶ 本日學生應完成的進度：程式會依玩家選擇走向不同劇情與屬性
# ============================================================

print("=" * 40)
print("🏰 《魔法地下城》第二章：選擇你的道路")
print("=" * 40)

name = input("勇者，請報上你的名字：")

# ── 1) 職業選擇：用 if / elif / else 三選一 ──
print()
print("請選擇你的職業：")
print("   1) 戰士 ⚔️    2) 法師 🔮    3) 弓箭手 🏹")
job = input("輸入 1 / 2 / 3：")

if job == "1":
    role = "戰士"
    hp = 120
    attack = 15
    line = "「以我之劍，破敵之盾！」"
elif job == "2":
    role = "法師"
    hp = 80
    attack = 25
    line = "「知識，就是最強的魔法。」"
elif job == "3":
    role = "弓箭手"
    hp = 100
    attack = 20
    line = "「百步穿楊，箭無虛發。」"
else:
    # 輸入不是 1/2/3 時的保底分支
    role = "見習冒險者"
    hp = 100
    attack = 10
    line = "「呃……我還在找我的武器。」"

print()
print(f"你成為了「{role}」！　HP={hp}，攻擊力={attack}")
print(line)

# ── 2) 劇情分支：用 if / elif / else 改變狀態 ──
print()
print("前方出現岔路……")
choice = input("要走 (左) 明亮通道，還是 (右) 黑暗密道？輸入 左 或 右：")

if choice == "左":
    print("你走進明亮通道，遇見老法師，獲得治療藥水 🧪（HP +20）")
    hp = hp + 20
elif choice == "右":
    print("你潛入黑暗密道，發現寶箱，卻觸動陷阱！（HP −20）")
    hp = hp - 20
else:
    print("你猶豫不決，站在原地……什麼都沒發生。")

# ── 3) 綜合判斷：用 and / or 一次看多個條件 ──
print()
print(f"目前狀態 → {role}，HP={hp}，攻擊力={attack}")
if hp >= 100 and attack >= 15:
    print("🟢 體力充沛、攻擊強勁，你已準備好迎戰哥布林！")
elif hp < 60 or attack < 12:
    print("🔴 狀態偏弱，建議先補給再前進……")
else:
    print("🟡 狀態普通，小心前進。")
