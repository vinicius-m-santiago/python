import time
import webbrowser

count = 0

print("o programa começou em " +time.ctime())
while count < 3:
    time.sleep(10)
    webbrowser.open("https://www.youtube.com/watch?v=TWACe_5KEBo")
    count +=1
