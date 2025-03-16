import math
import webbrowser

# تخزين القيم المتغيرة
variables = {}
geometry_mode = False  # وضع الرسومات الهندسية

def evaluate_expression(expression):
    """ تنفيذ العمليات الحسابية والمنطقية """
    try:
        return eval(expression, {"__builtins__": None}, {**math.__dict__, **variables})
    except Exception as e:
        return f"error Production: {e}"

def execute_commands(commands):
    """ تنفيذ مجموعة من الأوامر """
    global geometry_mode

    for command in commands:
        parts = command.split()
        if not parts:
            continue

        if parts[0] == "@import" and parts[1] == "=>":
            if parts[2] == "m.geometrique":
                geometry_mode = True
                print("\033[96mGeometry mode enabled!\033[0m")

        elif geometry_mode and parts[0] == "square" and len(parts) > 1:
            try:
                size = int(parts[1])
                url = f"data:text/html,<html><body style='background:black;display:flex;justify-content:center;align-items:center;height:100vh;'><div style='width:{size * 10}px;height:{size * 10}px;background:white;'></div></body></html>"
                webbrowser.open(url)
            except ValueError:
                print("Error: size must be an integer.")

        elif parts[0] == "exit":  # إنهاء البرنامج
            print("Closing M.scripte...")
            exit()
        else:
            print(f"Syntax error: {command}")

# تشغيل المفسر في الـ Terminal
print('Welcome to M.scripte! Type "exit" to quit, or "end" to execute the script.')

commands_buffer = []  # قائمة لتخزين الأوامر

while True:
    user_input = input("M.scripte> ").strip()
    
    if user_input.lower() == "exit":  # إنهاء البرنامج
        print("Closing M.scripte...")
        break
    
    elif user_input.lower() == "end":  # تنفيذ الأوامر المخزنة
        execute_commands(commands_buffer)
        commands_buffer = []  # تفريغ القائمة بعد التنفيذ

    else:
        commands_buffer.append(user_input)  # تخزين الأمر في القائمة
