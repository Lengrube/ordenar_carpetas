import os
import shutil

# Aquí colocas tu ruta de descargas
route_downloads = 'C:\\Users\\Elias\\Downloads\\'

# Si quieres puedes agregar mas extensiones, como .bat, .ttf, .py, etx
text_extensions = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf')
video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac')
photo_extensions = ('.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg')
compressed_extensions = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executable_extensions = ('.exe', '.msi')

# Cree las carpetas antes de ejecutar, si no, puede usar el módulo mkdir(), de os
def order(file, extension):

    for etx in text_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Texto')

    for etx in video_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Videos')

    for etx in audio_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Audios')

    for etx in photo_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Imagenes')

    for etx in compressed_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Comprimidos')

    for etx in executable_extensions:

        if extension == etx:
            shutil.move(route_downloads + file, route_downloads + 'Ejecutables')

    if extension != '':
        try:
            shutil.move(route_downloads + file, route_downloads + 'Otros')

        except:
            pass

    
def main():

    print('Iniciando\n')

    for file in os.listdir(route_downloads):

        try:
            etx = os.path.splitext(file)[1]

            order(file, etx)

        except:
            print('No se puedo mover el archivo {}\n'.format(file))

    print('Proceso terminado')


if __name__ == '__main__':
    main()