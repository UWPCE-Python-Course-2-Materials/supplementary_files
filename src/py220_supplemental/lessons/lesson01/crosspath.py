import pathlib

cwd = pathlib.Path.cwd()

print('cwd = ', cwd)
# in windows returns C:\workspace
# in unix returns /mnt/c/workspace

print('cwd parent', cwd.parent)

# on windows use raw strings to prevent esc issues with \

new_file = r'c:\workspace\andy.txt'


myfile = pathlib.Path.home() / 'test' / 'test.txt'
print("myfile is ", myfile)

# windows myfile is  C:\Users\chq-andym\test\test.txt
# unix myfile is  /home/andy/test/test.txt

print('path ', myfile)
print('stem ', myfile.stem)
print('suffix ', myfile.suffix)
print('parent ', myfile.parent)
print("parent's parent ", myfile.parent.parent)
print('parent ', myfile.parent)
print('anchor ', myfile.anchor)

# unix:
# path  /home/andy/test/test.txt
# stem  test
# suffix  .txt
# parent  /home/andy/test
# parent's parent  /home/andy
# parent  /home/andy/test
# anchor  /

# cwd =  C:\workspace
# cwd parent C:\
# myfile is  C:\Users\chq-andym\test\test.txt
# path  C:\Users\chq-andym\test\test.txt
# stem  test
# suffix  .txt
# parent  C:\Users\chq-andym\test
# parent's parent  C:\Users\chq-andym
# parent  C:\Users\chq-andym\test
# anchor C:\
