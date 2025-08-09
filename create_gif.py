import imageio.v3 as iio

filenames = ['team (1).jpeg', 'team (2).jpeg','team (3).jpeg', 'team (4).jpeg']
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite('created_gif.gif',images, duration=0.5,loop =0)
  