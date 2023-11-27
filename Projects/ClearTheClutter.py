import glob
import os
a = glob.glob('C:\\Users\\Administrator\\Desktop\Projects\\Projects\\ClearTheClutter\\*.png')

asb = 0

for an in a:
    os.rename(an,f"C:\\Users\\Administrator\\Desktop\Projects\\Projects\\ClearTheClutter\\{str(asb+1)}.png" )
    asb = asb + 1

print("Done!")