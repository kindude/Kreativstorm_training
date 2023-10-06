import os
import time
from ftplib import FTP

import schedule
from dotenv import load_dotenv
import logging

load_dotenv()

def configure_logging():
    logging.basicConfig(level=logging.INFO, filename="ftp_transfer.log", filemode="a+",
                        format="%(asctime)s %(levelname)s %(message)s")

def connect_ftp():
    host = os.getenv('host')
    port = int(os.getenv('port'))
    login = os.getenv('login')
    passwd = os.getenv('passwd')
    ftp = FTP()
    ftp.connect(host, port)
    logging.info(msg=f"Connected to {host}:{port}")
    ftp.login(user=login, passwd=passwd)
    logging.info(msg=f"Authenticated")
    ftp.set_pasv(True)
    return ftp

def download_files_from_ftp(ftp, remote_directory, local_directory):
    try:
        ftp.cwd(remote_directory)
        logging.info(msg=f"Current directory: {ftp.pwd()}")
        files = ftp.nlst()

        for file in files:
            local_path = os.path.join(local_directory, file)
            with open(local_path, 'wb') as local_file:
                ftp.retrbinary(f"RETR {file}", local_file.write)
                logging.info(f"Downloaded: {file}")

        logging.info(msg=f"Downloaded {len(files)} files from FTP")
    except Exception as e:
        print("An error occurred:", str(e))
        logging.error(f"An error occurred: {str(e)}")

def upload_files_to_ftp(ftp, remote_directory, local_directory):
    try:
        ftp.cwd(remote_directory)
        logging.info(msg=f"Current directory: {ftp.pwd()}")

        files = os.listdir(local_directory)
        for file in files:
            local_path = os.path.join(local_directory, file)
            if os.path.isfile(local_path):
                with open(local_path, 'rb') as local_file:
                    ftp.storbinary(f"STOR {file}", local_file)
                logging.info(f"Uploaded: {file}")

        logging.info(msg=f"Uploaded {len(files)} files to FTP")
    except Exception as e:
        print("An error occurred:", str(e))
        logging.error(f"An error occurred: {str(e)}")

def main():
    try:
        configure_logging()
        local_directory_to_download = 'storage'
        local_directory_to_upload = 'upload'
        remote_directory = '/pub/example'

        ftp = connect_ftp()

        if os.path.exists('storage') and os.path.exists('upload'):
            download_files_from_ftp(ftp, remote_directory, local_directory_to_download)
            upload_files_to_ftp(ftp, remote_directory, local_directory_to_upload)
        else:
            raise Exception("Directory to store not found")

        print("Files transferred to/from FTP")
    except Exception as e:
        print("An error occurred:", str(e))
        logging.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    schedule.every().day.at("21:48").do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
