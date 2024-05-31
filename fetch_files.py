import argparse
import shutil
import glob
import os
parser = argparse.ArgumentParser()
parser.add_argument("lines_txt")
args = parser.parse_args()
lines = []
with open(args.lines_txt) as ls:
    for l in ls:
        lines.append(int(l))

#print(lines)

with open("../made_from_testset.lst") as f:
    ja = [l.rstrip() for l in f.readlines()]

with open("../test_caption_en.txt") as f:
    en = [l.rstrip() for l in f.readlines()]

with open("../deepl_translation/translate_test_en.txt") as f:
    trans = [l.rstrip() for l in f.readlines()]

LENGTH = 128
for n in lines:
    i = n - 1
    fname = ja[i].split("|")[0]
    #print(fname)
    shutil.copy("../base_test/" + fname, "ans/" + fname)
    shutil.copy("../inference_test/" + fname, "ja/" + fname)
    shutil.copy(glob.glob("../dev/output/generation/*" + en[i][:LENGTH] + "*.wav")[0],
                "en/" + os.path.splitext(fname)[0] + ".wav")
    shutil.copy(glob.glob("../deepl_translation/output/generation/*" + trans[i][:LENGTH] + "*.wav")[0],
                "trans/" + os.path.splitext(fname)[0] + ".wav")
    with open("caption/" + os.path.splitext(fname)[0] + ".txt", "w") as f:
        f.write(ja[i].split("|")[1] + "\n")
        f.write(en[i] + "\n")
        f.write(trans[i] + "\n")