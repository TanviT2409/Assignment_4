try:
    with open("D:\VS Code\Tute_Dude\Python 4 (Tute Dude)\sample.txt","r") as file:
        print("Reading the contents of the file:")
        i=1
        for lines in file:
            print(f"Line {i}: ",end=" ")
            print(lines,end="")
            i+=1
except FileNotFoundError:
    print("No such file as sample.txt")