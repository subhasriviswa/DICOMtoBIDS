

# replace your subject number with a placeholder {subject} in the heuristics file, as you will be declaring the subject and session again as a seperate argument
# Modify the path to the DICOM directory on the -d argument and add or remove sub directories as needed 
heudiconv -d /'path to your DICOM folder'/{subject}/DICOM/*/*/*/* \ 
    -f /path to your heuristics_file'/heuristics_file_final.py \
    -s \
    --ses none \
    -c dcm2niix \
    --bids \
    -o /'path to your Output folder where you want to save the BIDS valid dataset'




