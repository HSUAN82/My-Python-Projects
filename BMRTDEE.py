import datetime  # 放在程式最上方

def save_record(content):
    # 取得現在的時間
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # 開啟檔案，"a" 代表附加模式
    with open("record.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] {content}\n")
    print(">> 數據已自動同步至紀錄檔 (record.txt)")

def cal_bmi(weight, height):
    if height <= 0:
        return 0  # 避免除以零的錯誤
    return weight / (height ** 2)
def cal_bmr(sex,weight,height,age):
    if sex == "1":
        return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)
    else:
        return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
print("="*30)
print("  歡迎使用健康數據大管家")
print("="*30)
while True:
    print("請選擇要計算的類型")
    print("1.計算BMI")
    print("2.計算BMR")
    print("3.計算TDEE")
    print("'q'離開系統")
    cho = input("請選擇 1 or 2 or 3 oe r q ").lower()
    if cho == "q":
        print("感謝使用，祝您身體健康！")
        break
    try:
        h_raw = float(input("請輸入身高cm"))
        w_raw = float(input("請輸入體重kg"))
        h_m = h_raw/100 if h_raw >3 else h_raw
        h_cm = h_raw if h_raw>3 else h_raw*100

        if cho == "1":
            bmi = cal_bmi(w_raw,h_m)
            msg = f"BMI 計算結果:{bmi:.2f}"
            print(f"您的BMI為{bmi:.2f}")
            save_record(msg)

        elif cho == "2" or "3":
            gen = input ("請輸入性別1男性 2女性:")
            age = int(input("請輸入年齡"))
            bmr = cal_bmr(gen,w_raw,h_cm,age)

            if cho == "2":
                print(f"您的BMR為{bmr:.2f}大卡")
                msg = f"BMR 計算結果: {bmr:.2f} 大卡"
                save_record(msg)
            else:
                print("\n活動量：1.久坐(1.2) 2.輕度(1.375) 3.中度(1.55) 4.高度(1.725) 5.強度(1.9)")
                gym_lv = input("請選擇活動量編號: ")
                # 活動係數對照表 (用簡單的 if/elif)
                if gym_lv == "1":
                    factor = 1.2
                elif gym_lv == "2":
                    factor = 1.375
                elif gym_lv == "3":
                    factor = 1.55
                elif gym_lv == "4":
                    factor = 1.725
                else:
                    factor = 1.9
                tdee= bmr*factor
                msg = f"TDEE 計算結果: {tdee:.2f} 大卡"
                save_record(msg)
                print(f"您的TDEE為{tdee:.2f}大卡")
    except ValueError:
        print("請輸入正確數字格式")
    print("-" * 30)
    input("\n計算完成，按 Enter 鍵結束程式...")