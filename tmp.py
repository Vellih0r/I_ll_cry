# ------------------------------------------------------------------------------------------
#      IT IS THE SMALL SCRITP TO DECIDE PATH TO FILE WITH PHRASES FOR GENERATING
#-------------------------------------------------------------------------------------------
#   add  '#' at start of a line to NOT USE this path 
#   and remove '#' to use line
#   Only 1 path can be used!

import os

if __name__ == "__main__":
    with open("./config.py", "w") as f:
        f.write(f"FILE_PATH='{os.getcwd()}/helpru.txt'")   #russian
        #f.write(f"FILE_PATH='{os.getcwd()}/helpukr.txt'")  #ukrainian
        #f.write(f"FILE_PATH='{os.getcwd()}/helpeng.txt'")   #english
