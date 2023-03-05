import os, time

class UpdateBackup():
    def __init__(self):
        pass
    def update_backup(self,p):
        #print(p)

        self.backup_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), p)
        if os.path.isdir(self.backup_path):
            print(f"{self.backup_path} is a directory: ")
            time.sleep(2)
            print('Starting backup...')
            #rsync -avz --progress --exclude '*.config/' --ex    clude '*.cache/' --exclude ' *.iso' --max-size=2g  /home/jerr    ipat/ /media/jerripat/SeagateOne1/rsync_backup
            # if os.path.exists(self.backup_path):
            #     print("Backup already exists...Continue backup? (y/n): ")
            #     time.sleep(2)
            #     print('Starting backup...')
            #     #rsync -avz --progress --exclude '*.config/' --ex    clude '*.cache/' --exclude ' *.iso' --max-size=2g  /home/jerr    ipat/ /media/jerripat/SeagateOne1/rsync_backup
        else:
            #os.makedirs(self.backup_path)
            print(f"{self.backup_path} is a file: ")

ub = UpdateBackup()
#ub.update_backup('/media/jerripat/SeagateOne')
ub.update_backup('/media/jerripat/SeagateOne')
