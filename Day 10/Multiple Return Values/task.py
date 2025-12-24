def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))

def is_leap_year(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)