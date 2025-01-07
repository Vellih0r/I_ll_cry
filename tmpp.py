import os

if __name__ == "__main__":
    with open("./config.py", "w") as f:
        f.write(f"FILE_PATH='{os.getcwd()}/helptext.txt'")
