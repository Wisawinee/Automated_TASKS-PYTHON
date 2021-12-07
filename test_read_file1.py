import os
for path_file , dris , files in os.walk("documents"):
    for file in files:
        if file.startswith("doc") and file.endswith(".docx"):
            full_file_path = os.path.join(path_file,file)
            print(full_file_path)
        '''
        full_file_path = os.path.join(path_file,file)
        print(full_file_path)
        '''
        #if "ple" in file: