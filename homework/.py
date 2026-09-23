使用chatgpt
from itertools import product

# SAT Solver：使用真值表暴力搜尋
def solve_sat(variables, formula):
    print("===== SAT 真值表 =====")

    # 產生所有可能的 TRUE / FALSE 組合
    for values in product([False, True], repeat=len(variables)):

        # 建立變數與真值的對應
        assignment = dict(zip(variables, values))

        # 計算公式
        result = formula(assignment)

        # 顯示真值表
        for var in variables:
            print(f"{var}={assignment[var]}", end="  ")
        print("=>", result)

        # 找到一組滿足條件的解
        if result:
            print("\n===== SAT =====")
            print("找到滿足條件的解：")

            for var in variables:
                print(f"{var} = {assignment[var]}")

            return True

    # 所有組合都不符合
    print("\n===== UNSAT =====")
    print("沒有任何滿足條件的解")

    return False


# ==========================================
# 測試 SAT 問題
#
# (A OR B) AND (NOT A OR C)
# ==========================================

variables = ["A", "B", "C"]

formula = lambda x: (
    (x["A"] or x["B"])
    and
    ((not x["A"]) or x["C"])
)

solve_sat(variables, formula)
