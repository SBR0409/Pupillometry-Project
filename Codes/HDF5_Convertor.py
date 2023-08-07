#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from __future__ import unicode_literals   
import pandas as pd
import os
path=input(str("Enter the path to HDF5 file"))

filename_input=input(str("Enter the file name with extension"))
    ## File name
filename=os.path.join(path,filename_input)

    ## File export path
    #filepath_bino = os.path.join(path,"binocular_data.csv")
filepath_mono = os.path.join(path,"monocular_data.csv")
print(filepath_mono)
    ####Reading File
recording_hdf5 = pd.HDFStore(filename,"r")

    #binocular_data = recording_hdf5["/data_collection/events/eyetracker/BinocularEyeSampleEvent"]

monocular_data = recording_hdf5["/data_collection/events/eyetracker/MonocularEyeSampleEvent"]
print("Sample Data",monocular_data)
    
    #binocular_data.to_csv(filepath_bino,'r')
monocular_data.to_csv(filepath_mono)

quit()






# In[ ]:




