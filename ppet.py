import os
import matplotlib.pyplot as plt
import pydicom as dicom
import numpy as np

import glob

path = r"C:\Users\Stefanos Stoikos\p-ai\dataset\ADNI\003_S_1057\Talairach_Warped\2007-02-16_13_01_23.0\I95836"
PET_imgs = os.listdir(path)

slices = [dicom.read_file(path + '/' + s, force=True) for s in PET_imgs]
slices = sorted(slices, key=lambda x: x.ImagePositionPatient[2])

pixel_spacing = slices[0].PixelSpacing
slice_thickness = slices[0].SliceThickness

axial_aspect_ratio = pixel_spacing[1] / pixel_spacing[0]
sagital_aspect_ratio = pixel_spacing[1] / slice_thickness
coronal_aspect_ratio = slice_thickness / pixel_spacing[0]

print(pixel_spacing)
print(slice_thickness)

print("1:",axial_aspect_ratio)
print("2:",sagital_aspect_ratio)
print("3:",coronal_aspect_ratio)

image_shape = list(slices[0].pixel_array.shape)
image_shape.append(len(slices))
volume3d = np.zeros(image_shape)

for i, s in enumerate(slices):
    array2d = s.pixel_array
    volume3d[:, :, i] = array2d

print(array2d.shape)
print(volume3d.shape)
axial = plt.subplot(2, 2, 1)
plt.title("Axial")
plt.imshow(volume3d[:, :, image_shape[2] // 2])
axial.set_aspect(axial_aspect_ratio)

sagital = plt.subplot(2, 2, 2)
plt.plot("Sagital")
plt.imshow(volume3d[:, image_shape[2] // 2, :])
sagital.set_aspect(sagital_aspect_ratio)


coronal = plt.subplot(2, 2, 3)
plt.plot("Coronal")
plt.imshow(volume3d[image_shape[2]//2, :, :].T)
coronal.set_aspect(coronal_aspect_ratio)

plt.show()
