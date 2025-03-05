pkgList = []

with open("test1.txt", "r", encoding="utf-8") as f:
    for line in f:
        pkg = line.strip()
        # 忽略空行和注释
        if not pkg or pkg.startswith("#"):
            continue
        pkgList.append(pkg)
print(pkgList)


with open("test2.txt", "r", encoding="utf-8") as f:
    for line in f:
        pkg = line.strip()
        if not pkg or pkg.startswith("#"):
            continue
        if pkg not in pkgList:
            pkgList.append(pkg)
print(pkgList)
