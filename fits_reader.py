from astropy.io import fits
from os import path, walk
import matplotlib.pyplot as plt


direct = path.abspath("")

tess_folder_path = path.abspath(r"mastDownload/TESS/")
paths = []
for fold in walk(tess_folder_path):
    if not fold[2]:
        pass
    else:
        paths.append(path.abspath(fold[0] + "\\" + fold[2][0]))
print(paths)


def find_path(f_name):
    global direct
    for root, dirs, files in walk(direct):
        for name in files:
            if name == f_name:
                return path.abspath(path.join(root, name))
    return "False"


def get_star_data(f_path):
    file = fits.open(f_path)
    data = file[1].data
    times = data.field(0)
    flux = data.field(3)
    file.close()
    return times, flux


data_set = []

for n, fp in enumerate(paths):
    data_set.append(get_star_data(fp))
    plt.plot(data_set[-1][0], data_set[-1][1], "b+", markersize=0.01, label=str(n))
plt.show()
