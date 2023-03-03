import os

class UpdateBackup():
    def __init__(self):
        pass

    def update_backup(self):
        self.backup_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'backup')
        self.backup_path = os.path.join(self.backup_path, 'backup')
        if not os.path.exists(self.backup_path):
            os.makedirs(self.backup_path)