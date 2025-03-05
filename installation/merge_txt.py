fileList = ["requirements1.txt", "requirements2.txt", "requirements3.txt"]
pkgList = []

for file in fileList:
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            pkg = line.strip()
            # 忽略空行和注释
            if not pkg or pkg.startswith("#"):
                continue
            if pkg not in pkgList:
                pkgList.append(pkg)

with open("pkgList.txt", "w", encoding="utf-8") as f:
    for pkg in pkgList:
        f.write(pkg + "\n")
