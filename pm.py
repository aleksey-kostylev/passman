from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None
        self.password_file = None
        self.password_dict = {}
    
    def create_key(self, path):
        self.key = Fernet.generate_key()
        with open(path, 'wb') as f:
            f.write(self.key)
            print(f'Ключ для хранилища({path}) создан')
    
    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key = f.read()
    
    def create_password_file(self, path, initial_values=None):
        self.password_file = path

        done = None
        while not done:
            try:
                open(path, 'x')
                print(f'Файл хранилища {path} создан')
                done = True
            except FileExistsError:
                print('Файл с таким именем уже существует!')

        if initial_values is not None:
            for k, v in initial_values.items():
                self.add_password(k, v)

    def load_password_file(self, path):
        self.password_file = path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted_data = line.split(':')
                self.password_dict[site] = Fernet(self.key).decrypt(encrypted_data.encode()).decode().split()
    
    def add_password(self, site, login, password):
        data = [login, password]
        self.password_dict[site] = data
        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted_data = Fernet(self.key).encrypt(' '.join(data).encode())
                f.write(site + ':' + encrypted_data.decode() + '\n')
    
    def get_password(self, site):
        return self.password_dict[site]