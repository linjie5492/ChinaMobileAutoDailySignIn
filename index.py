import main

def main_handler(event: dict, context: dict):
    msg = main.main()
    main.ftqq(msg)
    print("中国移动和你自动签到！")
    return 0