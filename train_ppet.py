import pydicom as dicom
import os
import pandas as pd
import glob
from nipype.interfaces.dcm2nii import Dcm2nii


scans_path = "dataset\ADNI\*\Talairach_Warped\*\*"
patients = glob.glob(scans_path)

converter = Dcm2nii()
for patient in patients:
    print(patient)
    PET_imgs = glob.glob(patient+"/*")
    converter.inputs.source_names = PET_imgs
    converter.inputs.gzip_output = True
    converter.inputs.output_dir = '../../..'
    converter.cmdline
    exit()

