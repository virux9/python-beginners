import json

firm_dic = {}
num_firms_with_revenue = 0
total_revenue = 0
with open("file_t07.txt", encoding="utf-8") as f_obj:
    for line in f_obj:
        firm_name, firm_form, firm_profit_str, firm_loss_str = line.split()
        firm_profit = int(firm_profit_str)
        firm_loss = int(firm_loss_str)
        firm_revenue = firm_profit - firm_loss
        firm_dic[firm_name] = firm_revenue
        if firm_revenue > 0:
            num_firms_with_revenue += 1
            total_revenue += firm_revenue

my_list = [firm_dic, {"average_profit": total_revenue / num_firms_with_revenue}]

with open("file_t07_out.json", "w", encoding="utf-8") as write_f:
    json.dump(my_list, write_f)
