import sys, subprocess, time

try:
    sys.stdout.write("\x1b[8;34;89t")


except ValueError:
    pass

finally:
    print("Hello WORLD MOTHA FUCKAS!!!!!")
    time.sleep(2)
