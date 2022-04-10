# youtubeFoldersPreparation
youtubeFoldersPreparation.py is a Python script to prepare some folders and txt files to edit a Youtube's video in Windows. 
<h2> How to use </h2>
To use the script you only have to execute it with Python (developed in Python 3.9) and pass the correct arguments. The script will create a main folder named as the first parameter. If we pass "exampleFolder" as first parameter, the script will create a folder called "exampleFolder". Inside this folder the script will create the next subfolders: "Images, Movs, Music, Project, Sound, Source, Spam and Stock", and the next .txt files: "Cards, Description, Keywords, Title". 

<h3> Example of use </h3>

> python3 youtubeFoldersPreparation.py "New Youtube Video" 

<img width="315" alt="folderPreparation" src="https://user-images.githubusercontent.com/48330849/147373665-ed40af52-0a22-4076-b66e-34d542ae074a.png">

<img width="325" alt="creation1" src="https://user-images.githubusercontent.com/48330849/147373519-0cc184ce-35eb-49a4-a459-a81c62e12abf.png">

<img width="337" alt="creation2" src="https://user-images.githubusercontent.com/48330849/147373522-faeee66b-b098-4444-b0ec-b308b7f80e3d.png">

<h2> Arguments </h2>
The script only needs one argument, a string that will be the name of the root folder, and accept additionally all the files that we want to appear in the 'Source' directory.
<ul>
  <li><b>First Parameter</b>. A string that will be the name of the root folder. </li>
  <li><b>Additional parameters</b>. The files that we want to move to the 'Source' directory. For example, the input video files. </li>
</ul>

<h3> Example of use </h3>
> python3 youtubeFoldersPreparation.py "New Youtube Video" originalVideo.mp4 example.png

<img width="486" alt="preparation" src="https://user-images.githubusercontent.com/48330849/147373648-f88983ce-3404-4218-b9fa-a2ffb2fb17e9.png">

<img width="192" alt="source" src="https://user-images.githubusercontent.com/48330849/147373576-67003efc-1ccd-4b7b-8236-6d03fcc3943b.png">


