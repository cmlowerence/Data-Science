import os
dirs = [dir for dir in os.listdir() if os.path.isdir(dir)]

for dir in dirs:
  os.system(f"touch ./{dir}/__init__.py")