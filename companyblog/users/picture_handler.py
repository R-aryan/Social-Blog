# inside users/picture_handler

import os
from PIL import Image
from flask import url_for,current_app


def add_profile_picture(pic_upload,username):

    filename= pic_upload.filename
    ## eg if filename is mypict.jpg  then split it into mypict and jpg
    ext_type= filename.split('.')[-1]
    storage_filename= str(username)+ '.'+ext_type

    filepath= os.path.join(current_app.root_path,'static\profile_pics',storage_filename)

    output_size=(400,400)
    pic= Image.open(pic_upload)
    pic.thumbnail(output_size)
    pic.save(filepath)

    return storage_filename
    
