from datetime import datetime

from edupage_api import Edupage

edupage = Edupage()
edupage.login_auto("Username (or e-mail)", "Password")

today = datetime.now()
lunch = edupage.get_lunches(today)

if lunch is None:
    print(f"No lunch choices for today ({today.date()}) yet!")
else:
    for menu_index_str in lunch.chooseable_menus:
        menu_index = int(menu_index_str)
        print(f"[{menu_index_str}] {lunch.menus[menu_index].name}")

    lunch_n = input("Which lunch do you want? ")
    while lunch_n not in lunch.chooseable_menus:
        lunch_n = input("Which lunch do you want? ")

    lunch.choose(edupage, int(lunch_n))
    print("Done!")
