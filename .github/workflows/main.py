# Flipper-IRDB orderer
# (c) DarkBrines, All Rights Reserved

import sys
import os
import shutil


def createdir(p):
    if not os.path.exists(p):
        os.makedirs(p)


def handlebranddir(p, newdir, irtype, irbrand):
    letter = irbrand[0].capitalize()
    createdir(f"{newdir}/{letter}/{irbrand}/{irtype}")

    for f in os.listdir(p):
        if os.path.isdir(f"{p}/{f}"):
            handlebranddir(p + "/" + f, newdir, irtype + "_" + irbrand, f)
        else:
            shutil.copy2(
                f"{p}/{f}",
                f"{newdir}/{letter}/{irbrand}/{irtype}/{f}",
            )


def main(olddir, newdir):
    createdir(newdir)

    for irtype in os.listdir(olddir):
        if not os.path.isdir(f"{olddir}/{irtype}"):
            continue
        if irtype.startswith(".") or irtype.startswith("_"):
            continue

        for irbrand in os.listdir(f"{olddir}/{irtype}"):
            if not os.path.isdir(f"{olddir}/{irtype}/{irbrand}"):
                continue
            if irbrand.startswith(".") or irbrand.startswith("_"):
                continue

            handlebranddir(f"{olddir}/{irtype}/{irbrand}", newdir, irtype, irbrand)

        print("Done", irtype)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} irdb-location filtered-dir")
        exit(1)

    main(sys.argv[1], sys.argv[2])
