使用chatgpt
from itertools import product

def solve_sat(variables, formula):
    print("===== SAT 真值表 =====")

    # 產生所有 TRUE / FALSE 組合
    for values in product([False, True], repeat=len(variables)):

        # 建立變數對應
        assignment = dict(zip(variables, values))

        # 計算公式
        result = formula(assignment)

        # 顯示目前組合
        text = ""

        for var in variables:
            text = text + var + "=" + str(assignment[var]) + "  "

        print(text + "=> " + str(result))

        # 找到解
        if result:
            print("")
            print("===== SAT =====")
            print("找到滿足條件的解：")

            for var in variables:
                print(var + " = " + str(assignment[var]))

            return True

    print("")
    print("===== UNSAT =====")
    print("沒有任何滿足條件的解")

    return False


# =====================================
# 測試公式：
# (A OR B) AND (NOT A OR C)
# =====================================

variables = ["A", "B", "C"]

formula = lambda x: (
    (x["A"] or x["B"])
    and
    ((not x["A"]) or x["C"])
)

solve_sat(variables, formula)
