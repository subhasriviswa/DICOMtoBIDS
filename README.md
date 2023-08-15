# DICOMtoBIDS
Step by Step process for DICOM to BIDS conversion using Heudiconv package


## Intial Steps

1. Look at the protocol of the MRI acquisition to get an idea of the MRI parameters like different types of acquisitons, TR, TE, sequence names etc from the DICOM headers or json files.

## Installing [Heudiconv Package](https://heudiconv.readthedocs.io/en/latest/)
The heudiconv package is a DICOM to BIDS conversion tool which uses a heuristics based approach by matching the MRI acqusition parameters based on the heurstic rules custom written to match the DICOMS to make BIDS compatable folders. It uses the dcm2niix under the hood so that the resulting output is in NIFTI format. 
# [Installation](https://heudiconv.readthedocs.io/en/latest/installation.html)
We can download the heudiconv by pip installling or using docker containers.


## Creating the custom Heurstics file 

Heudiconv requires us to specify a heurestics file which it will use to match the DICOMS to its corresponding accquistions. 
There are two options here to first either create a base heurestics file, and then edit the heurstics file from that ( best for begining with heudiconv as it comes with pre-defined functions that need not be modifed) or making the heuristics file from scratch. 

This repo contains a bash script file which actually runs the heudiconv commands and a python script which is the heurstics file, which is called in during the heudiconv execution. 


This is how a BIDS valid folder to should like. 
![Screenshot 2023-08-15 at 5 08 42 PM](https://github.com/subhasriviswa/DICOMtoBIDS/assets/62513668/f24d508f-c5ee-4b67-8d16-746e74401dc6)



