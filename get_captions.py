import argparse
parser = argparse.ArgumentParser()
parser.add_argument("src")
parser.add_argument("dst")
args = parser.parse_args()
lines = []
with open(args.src) as f:
    lines = [int(l) for l in f]

with open("../made_from_testset.lst") as f, open(args.dst, "w") as g:
    test_set = f.readlines()
    for l in lines:
        i = l - 1
        g.write(str(l) + "|" + test_set[i])