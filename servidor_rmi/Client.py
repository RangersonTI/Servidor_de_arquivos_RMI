import Pyro5.api as Pyro5

ns = Pyro5.locate_ns()
url = ns.lookup('obj')
o = Pyro5.Proxy(url)

print(o.saludar())




#def main():
#    # Conecta ao serviço de arquivo no servidor Pyro
#    file_service = Pyro5.api.Proxy("PYRO:Pyro.NameServer@localhost:9090")
#
#    # Lista arquivos no diretório especificado
#    directory_path = "/Downloads/"
#    try:
#        files = file_service.list_files(directory_path)
#        print("Files:", files)
#    except Exception as e:
#        print("Error listing files:", e)
#
#    # Lê o conteúdo de um arquivo especificado
#    file_path = "/Downloads/"
#    try:
#        content = file_service.read_file(file_path)
#        print("File Content:", content)
#    except Exception as e:
#        print("Error reading file:", e)
#
#    # Baixa um arquivo em partes
#    try:
#        download_path = "/some/directory/file.txt"
#        file_size = file_service.get_file_size(download_path)
#        chunk_size = 1024 * 1024  # 1 MB
#        with open("downloaded_file.txt", "wb") as f:
#            for start in range(0, file_size, chunk_size):
#                data = file_service.download_file(download_path, start, chunk_size)
#                f.write(data)
#        print("File downloaded successfully!")
#    except Exception as e:
#        print("Error downloading file:", e)
#
#if __name__ == "__main__":
#    main()