"""
50_匹配命令配置文件 - 

Author: kayotin
Date 2024/4/14
"""

s_com = {"reset": "reset what"}
l_com = {"reset board": "board fault",
         "board add": "where to add",
         "board delete": "no board at all",
         "reboot backplane": "impossible",
         "backplane abort": "install first"
         }


def check_command(command: str):
    is_l = False
    if " " in command:
        is_l = True
    if is_l:
        command_list = command.split(" ")
        if len(command_list) > 2:
            return False
        com1, com2 = command_list

        res1 = []
        # 匹配命令1
        for key in l_com.keys():
            if com1 == key[:len(com1)]:
                res1.append(key)
        if not res1:
            return False
        res2 = []
        for key in res1:
            if com2 == key.split(" ")[1][:len(com2)]:
                res2.append(key)
        if len(res2) == 1:
            return res2[0]
        else:
            return False
    else:
        if command == "reset"[: len(command)]:
            return "reset"
        else:
            return False


while True:
    try:
        int_comm = str(input())
        checked_com = check_command(int_comm)
        if checked_com:
            if " " in checked_com:
                print(l_com[checked_com])
            else:
                print(s_com[checked_com])
        else:
            print("unknown command")
    except EOFError:
        break
