def sum_max_two(val_1, val_2, val_3):
    m_list = [val_1, val_2, val_3]
    max_1 = max(m_list)
    m_list.remove(max_1)
    max_2 = max(m_list)
    return max_1 + max_2


print(sum_max_two(1, 2, 3))
