import subprocess

# 第三引数にアプリケーション名をつける
subprocess.Popen(["open", "-a", "Visual Studio Code"])
subprocess.Popen(["open", "-a", "Adobe Illustrator"])
subprocess.Popen(["open", "-a", "Cyberduck"])
subprocess.Popen(["open", "-a", "Google Chrome"])
subprocess.Popen(["open", "-a", "Mail"])
subprocess.Popen(["open", "-a", "Adobe Illustrator"])

# ファイルを指定したいとき
# subprocess.Popen(["open", "-a", "Microsoft Excel",  "./data/output.xlsx"])