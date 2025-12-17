
file= open ("D:\VS Code\Tute_Dude\Python 4 (Tute Dude)\output.txt","a")
text= input("Enter text to write to the file:")
file.write(text)
file.close()

file= open ("D:\VS Code\Tute_Dude\Python 4 (Tute Dude)\output.txt","a")
text= input("Enter additional text to append to the file:")
file.write(text)
file.close()
