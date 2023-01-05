import os
dirfiles = os.listdir()
def isbinod(file):
    with open (file) as f:
        str = f.read()
        str = str.lower()
        if "binod" in str:
            return True
if __name__ == '__main__':
    num = 0
    for file in dirfiles:
        if file.endswith('.txt'):
            # print(f"Detcting 'binod' in {file}")
            if (isbinod(file)):
                print(f"Binod detected in {file}")
                num+=1
            else:
                print(f"Binod not detected in {file}")
print("*****Summary*****")
print(f"{num} files found with binod")