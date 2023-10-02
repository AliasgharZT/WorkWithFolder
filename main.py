import os
import shutil
import pyAesCrypt

def create_folder(address,name):
    try:
        os.mkdir(os.path.join(address,name))
        print('ok')
    except:
        print('Error')

def delete_folder(address):
    try:
        os.rmdir(address)
        print('ok')
    except:
        print('Error')

def rename_folder(old_name,new_name):
    try:
        os.rename(old_name,new_name)
        print('ok')
    except:
        print('Error')

def folder_to_zip(address,name_address):
    try:
        shutil.make_archive(name_address,'zip',address)
        print('ok')
    except:
        print('Error') 

def lock_folder(name_address_input,name_address_output,password):
    try:
        pyAesCrypt.encryptFile(name_address_input,name_address_output,password,64*1024)
        print('ok')
    except:
        print('Error')

# ///////////////////////////////////////////////////
# create_folder('D:\\FileCode\\Python\\az','az2')
# delete_folder('D:\\FileCode\\Python\\az\\az2')
# rename_folder('D:\\FileCode\\Python\\azt','az')
# folder_to_zip('D:\\FileCode\\Python\\az\\az0','D:\\FileCode\\Python\\az\\az_zip2')
lock_folder('D:\\FileCode\\Python\\az\\az1\\kali.pdf','D:\\FileCode\\Python\\az\\kali.pdf.aes','1234')


