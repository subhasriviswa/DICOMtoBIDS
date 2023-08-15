def create_key(template, outtype=('nii.gz',), annotation_classes=None):
    if template is None or not template:
        raise ValueError('Template must be a valid format string')
    return template, outtype, annotation_classes

def infotodict(seqinfo):
    """Heuristic evaluator for determining which runs belong where

    allowed template fields - follow python string module:

    item: index within category
    subject: participant id
    seqitem: run number during scanning
    subindex: sub index within group
    """

    ##### list keys for t1w,dwi, rs-fMRI, task -fMRI ###########

  
    t1w = create_key('sub-{subject}/{session}/anat/sub-{subject}_{session}_T1w')
    func_rest = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-rest_bold')
    func_task_STOP = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-STOP_bold')
    func_task_MIDT = create_key('sub-{subject}/{session}/func/sub-{subject}_{session}_task-MIDT_bold')
    dwi = create_key('sub-{subject}/{session}/dwi/sub-{subject}_{session}_dwi')
    
    
   

    info = {t1w: [], func_rest: [], func_task_STOP: [], func_task_MIDT: [], dwi : []}

    for s in seqinfo:
        """
        The namedtuple `s` contains the following fields:

        * total_files_till_now
        * example_dcm_file
        * series_id
        * dcm_dir_name
        * unspecified2
        * unspecified3
        * dim1
        * dim2
        * dim3
        * dim4
        * TR
        * TE
        * protocol_name
        * is_motion_corrected
        * is_derived
        * patient_id
        * study_description
        * referring_physician_name
        * series_description
        * image_type
        """
        # T1w
        if s.protocol_name == 'T1 SAG MPRAGE grappa2':
            info[t1w].append(s.series_id)

        # rs-fMRI
        if s.protocol_name == 'BOLD MOSAIC 64_REST':    
            info[func_rest].append(s.series_id)

        #if ('BOLD_REST1_PA' in s.dcm_dir_name) and (s.dim4 >= 200) :    
        #    info[func_rest_PA].append(s.series_id)
        #if ('BOLD_REST1_AP' in s.dcm_dir_name) and (s.dim4 >= 200) :    
        #    info[func_rest_AP].append(s.series_id)

        # task-fMRI
        if s.protocol_name == 'BOLD MOSAIC 64_STOP':
            info[func_task_STOP].append(s.series_id)
        if s.protocol_name == 'BOLD MOSAIC 64_MIDT':
            info[func_task_MIDT].append(s.series_id)
            
        # DWI
        if s.protocol_name == 'DTI AX EP2D grappa2 ':    
            info[dwi].append(s.series_id)

        #if ('DWI_PA' in s.dcm_dir_name) and (s.dim4 >= 30):    
        #    info[dwi_PA].append(s.series_id)
        #if ('DWI_AP' in s.dcm_dir_name) and (s.dim4 >= 30):    
        #    info[dwi_AP].append(s.series_id)
        #info[data].append(s.series_id)
    return info
