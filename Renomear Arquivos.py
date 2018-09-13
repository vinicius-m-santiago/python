import os

def rename_files():
    # (1) recuperar o nome dos arquivos da pasta
    file_list = os.listdir(r"/Users/viniciussantiago/Desktop/Python")
    saved_path = os.getcwd()
    print("O diretorio é " +saved_path)
    os.chdir(r"/Users/viniciussantiago/Desktop/Python")
    
    # (2) para cada arquivo, renomear, retirando os numeros
    for file_name in file_list:
         print("Nome anterior - "+file_name)
         table = str.maketrans(dict.fromkeys('0123456789'))
         os.rename(file_name, file_name.translate(table))
         print("Nome novo     - "+file_name.translate(table))
    os.chdir(saved_path)
rename_files()
