def user_data(f_name, l_name, dob, city, email, phone):
    return f_name + " " + l_name + " " + dob + " " + city + " " + email + " " + phone


first_name = input("first name: ")
last_name = input("last name: ")
birth_date_str = input("date of birth: ")
city_living = input("city: ")
email_str = input("email: ")
phone_str = input("phone: ")

res_str = user_data(phone=phone_str, email=email_str, city=city_living, dob=birth_date_str, l_name=last_name,
                    f_name=first_name)

print(res_str)
