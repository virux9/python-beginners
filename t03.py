m_dict = {1: "winter", 2: "winter", 3: "spring", 4: "spring", 5: "spring", 6: "summer", 7: "summer", 8: "summer",
          9: "autumn", 10: "autumn", 11: "autumn", 12: "winter"}
m_list = ["winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn",
          "winter"]
month = int(input("Enter month number:"))
if (month > 0) and (month <= 12):
    print(f"month name (through dict) : {m_dict[month]}")
    print(f"month name (through list) : {m_list[month - 1]}")
else:
    print("invalid month number")
