import os
import shutil
from_dir = "C:/Users/nitgu/Downloads"
to_dir = "C:/Users/nitgu/Desktop"
list_of_files = os.listdir(from_dir)
#print(list_of_files)
for x in list_of_files:
 a,b = os.path.splitext(x)
 if (b=='.pdf' or b=='.doc' or b=='.txt' or b=='.docx') : 
  path1= from_dir+'/'+x
  path2=to_dir+'/'+'document_files'
  path3=to_dir + '/' + "Document_Files" + '/' + x
  if os.path.exists(path2):
    shutil.move(path1, path3)
  else:
    os.makedirs(path2)
    shutil.move(path1, path3)