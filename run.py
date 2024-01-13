from utilities.Social import instagram
import utilities.constants as const

def fully_human_like(auto):
    interact_number = auto.get_and_remove_random_word(const.interact_human_like)
    interact_comment_number = auto.get_and_remove_random_word(const.comment_number)
    interact_follow_number = auto.get_and_remove_random_word(const.follow_number)
    interact_counter = 0

    try:
        auto.searching()
        auto.click_first_pic()
    except:
        pass

    for i in range(interact_number):
        try:
            auto.wait_short()
            auto.like()
            for c in range(interact_comment_number):
                auto.wait_short()
                auto.comment()
                break
            for f in range(interact_follow_number):
                auto.wait_short()
                auto.follow()
                break
            auto.go_to_next_page()
            interact_counter += 1
            print(f"{interact_counter} process done.")
            print("------------------------------------------------")
        except:
            pass
        print(f"{interact_counter} process of {const.search} done.")
        print("------------------------------------------------")
    auto.close_windows()
    auto.go_main_page()

    if interact_counter > 0:
        print(f"{interact_counter} like processes of {auto.search_randomly} done successfully!")
        print("------------------------------------------------")
    else:
        print("No likes were performed.")
        print("------------------------------------------------")

    auto.wait_middle()

def like(auto):
    random_number = auto.get_and_remove_random_word(const.like_number)
    try:
        auto.searching()
        auto.click_first_pic()
    except:
        pass

    like_counter = 0
    for _ in range(random_number):
        try:
            auto.like()
            auto.go_to_next_page()
            like_counter += 1
            print(f"{like_counter} process done.")
            print("------------------------------------------------")
        except:
            print(f"Error")
    auto.close_windows()
    auto.go_main_page()

    if like_counter > 0:
        print(f"{like_counter} like processes of {auto.search_randomly} done successfully!")
        print("------------------------------------------------")
    else:
        print("No likes were performed.")
        print("------------------------------------------------")

    auto.wait_middle()

def follow(auto):
    num_processes = 0
    random_follow_number = auto.get_and_remove_random_word(const.follow_number)
    try:
        auto.searching()
        auto.click_first_pic()
    except:
        pass
    for _ in range(0, random_follow_number):
        print(f"Starting new with follow of {const.search} ...")
        auto.wait_short()
        auto.follow()
        auto.wait_short()
        auto.go_to_next_page()
        num_processes += 1
        print(f"{num_processes} process of {const.search} done.")
        print("------------------------------------------------")
    print("Follow successfully!")
    print("------------------------------------------------")
    auto.wait_middle()

def unfollow(auto):
    num_processes = 0
    random_number_unfollow = auto.get_and_remove_random_word(const.unfollow_number)
    auto.go_to_profile()
    for i in range(0, random_number_unfollow):
        print("Starting with unfollow...")
        auto.unfollow()
        num_processes += 1
        print(f"{num_processes} process of unfollow done.")
        print("------------------------------------------------")
        auto.wait_short()
    print("unfollow was successfully!")
    auto.close_windows()
    auto.go_main_page()
    auto.wait_middle()

def comment(auto):
    num_processes = 0
    random_follow_number = auto.get_and_remove_random_word(const.comment_number)
    auto.searching()
    auto.click_first_pic()
    for _ in range(0, random_follow_number):
        print(f"Starting new with comment of {const.search} ...")
        auto.wait_short()
        auto.comment()
        auto.wait_short()
        auto.go_to_next_page()
        num_processes += 1
        print(f"{num_processes} process of {const.search} done.")
        print("------------------------------------------------")
    print("Comment successfully!")
    print("------------------------------------------------")
    auto.wait_middle()
