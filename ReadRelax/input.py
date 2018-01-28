import os

def main():
    while True:
        f = open("input.txt",'r+');
        val = raw_input("0 -> PAUSE\n1 -> RESUME\n2 -> SPEED UP\n3 -> SLOW DOWN\n:")
        if val != '':
            f.seek(0);
            f.truncate();
            f.write(val);
            f.close();
        os.system('cls')

main()
