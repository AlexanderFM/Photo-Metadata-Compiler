import os
import pandas as pd
from glob import glob
import timeit
import exifread
from collections import OrderedDict

data_dir = './'

intro = "0"
while intro == "0":
    print("Do you analyse current folder? \n [1] Yes, use same folder as this .py \n [2] No, I wish to input directory \n [3] Help")
    rename = input()
    if rename == "1":



        intro = "1"
    elif rename == "2":
        print("Paste your desired file directory here:")
        data_dir = input()
        intro = "1"
    elif rename == "3":
        print("This is defining which folder you want to analyse, program will ony analise .jpg... for now \n")

start = timeit.default_timer()
Files = [OrderedDict([("Name", "Name"),
("Size", "Size"),
('Image Model', "(0x0110) ASCII=Canon EOS 760D @ 164"),
('Image DateTime', "(0x0132) ASCII=2015:06:15 11:31:05 @ 212"),
('EXIF ExposureTime', "(0x829A) Ratio=1/60 @ 822"),
('EXIF FNumber', "(0x829D) Ratio=16 @ 830"),
('EXIF ExposureProgram', "(0x8822) Short=Aperture Priority @ 394"),
('EXIF ISOSpeedRatings', "(0x8827) Short=200 @ 406"),
('EXIF DateTimeOriginal', "(0x9003) ASCII=2015:06:15 11:31:05 @ 838"),
('EXIF ShutterSpeedValue', "(0x9201) Signed Ratio=6 @ 878"),
('EXIF ApertureValue', "(0x9202) Ratio=8 @ 886"),
('EXIF MeteringMode', "(0x9207) Short=Pattern @ 526"),
('EXIF Flash', "(0x9209) Short=Flash did not fire"),
('EXIF FocalLength', "(0x920A) Ratio=18 @ 902"),
('EXIF ColorSpace', '(0xA001) Short=sRGB @ 634'),
('EXIF ExposureMode', "(0xA402) Short=Auto Exposure @ 730"),
('EXIF WhiteBalance', "(0xA403) Short=Auto @ 742"),
('EXIF SceneCaptureType', "(0xA406) Short=Standard @ 754"),
('EXIF BodySerialNumber', "(0xA431) ASCII=033032000898 @ 9898"),
('EXIF LensSpecification', "(0xA432) Ratio=[18, 55, 0, 0, @ 9930"),
('EXIF LensModel', "(0xA434) ASCII=EF-S18-55mm f/3.5-5.6 IS @ 9962"),
('EXIF LensSerialNumber', "(0xA435) ASCII=0000300cd7 @ 10036")])]
df = pd.DataFrame(Files)#, 'r')
df.to_csv("Files.csv", header = False, index = True)

print("\033[32;mUpdateing: Files.csv ")

audio_files = glob(data_dir + "/*.jpg")

len_audio_files = len(audio_files)
print("Number of Audio Files:", len_audio_files)
print("Files to be Processed", audio_files)

for current in audio_files:
    size = os.path.getsize(current)
    bsize = round(size/1000000, 1)
    msize = str(bsize)+" mb"
    File_Name = os.path.basename(current)
    print("\033[30;mFile Name = " + File_Name)
    print("File Size = ", msize)
    print("CURRENT IS:", current)
    with open(current, 'rb') as f:
        raw_tags = exifread.process_file(f, details=False)
        raw_tags["Name"] = File_Name
        raw_tags["Size"] = msize
        tags = OrderedDict()
        for key in Files[0].keys():
            tags[key] = raw_tags.get(key, 'Nul')
        print(repr(raw_tags))
    print("Format = ", format)

    df2 = pd.DataFrame([tags])
    df2.to_csv('Files.csv', mode='a', header=False)

end = timeit.default_timer()
print("\033[32;mTook", end - start, "seconds")