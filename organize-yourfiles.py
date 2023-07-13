import sys
import os
import time

src = "src-folder-path"
dst = "dst-folder-path"
# src = input("please input your source: ")
# dst = input("please input your destination:")
    
files_dict = {}
count = 0
for root, dirs, files in os.walk(src):
    for file in files:
        if "." in file:
            suffix = file.split(".")[-1].lower()
            file_root = os.path.join(root, file)
            second = os.path.getmtime(file_root)
            year = time.ctime(second).split()[-1]
            files_dict[f"{file}"] = year
           
            # year_dst = os.path.join(dst , year)
            # image_dest = os.path.join(year_dst, "photos")
            # video_dest = os.path.join(year_dst, "videos")
            #-----------for file in files---------
            if suffix in ("png", "jpeg", "jpg"):
                year_dst = os.path.join(dst , year)
                image_dest = os.path.join(year_dst, "photos")
                os.makedirs(image_dest, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "photos", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
                    
            elif suffix in ("mp4", "avi", "3gp", "mpeg", "mkv", "wmv", "mov"):
                year_dst = os.path.join(dst , year)
                video_dest = os.path.join(year_dst, "videos")
                os.makedirs(video_dest, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "videos", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
                    
            elif suffix in ("dll"):
                year_dst = os.path.join(dst , year)
                dll_file = os.path.join(year_dst, "DLL files")
                os.makedirs(dll_file, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "DLL files", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
                    
            elif suffix in ("mp3" , "aac", "WAV", "OGG", "FLAC","m4a"):
                year_dst = os.path.join(dst , year)
                music_dest = os.path.join(year_dst, "music files")
                os.makedirs(music_dest, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "music files", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
                    
            elif suffix in ("rtf", "doc","docx", "odt", "pdf", 'md', "html"):
                year_dst = os.path.join(dst , year)
                doc_dst = os.path.join(year_dst, "Documents")
                os.makedirs(doc_dst, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "Documents", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
                    
            elif suffix in ("xls" , "xlxs" , "xltx"):
                year_dst = os.path.join(dst , year)
                excel_dest = os.path.join(year_dst, "excel files")
                os.makedirs(excel_dest, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "excel files", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)
            else:
                year_dst = os.path.join(dst , year)
                others_dest = os.path.join(year_dst, "others file")
                os.makedirs(others_dest, exist_ok=True)
                os.makedirs(year_dst, exist_ok=True)
                file_dst = os.path.join(year_dst, "others file", file)
                with open(file_root , "rb") as src_file, open(file_dst, "wb") as dst_file:
                    data = src_file.read()
                    dst_file.write(data)        
            