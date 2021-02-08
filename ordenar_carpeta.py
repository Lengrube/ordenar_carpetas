import os
import shutil

# Aquí colocas tu ruta de descargas
route_downloads = '/home/elias-lengrube/Descargas/'

# Si quieres puedes agregar mas extensiones, como .bat, .ttf, .py, etx
text_extensions = ('.txt', '.doc', '.docx', 'pptx', '.odf', '.docm', '.pdf')
video_extensions = ('.mov', '.mp4', '.avi', '.mkv', '.mkv', '.flv', '.wmv')
audio_extensions = ('.mp3', '.wma', '.wav', '.flac')
photo_extensions = ('.jpg', '.png', 'jpeg', '.gif', '.tiff', '.psd', '.bmp', '.ico', '.svg')
compressed_extensions = ('.zip', '.rar', '.rar5', '.7z', '.ace', '.gz')
executable_extensions = ('.exe', '.msi')

def get_option():
    print('¿Deseas que el programa cree las carpetas faltantes?')
    option = input('S/N >>').strip().lower()

    attemps = 0

    while option != 's' and option != 'n':

        if attemps == 4:
            print('')
            print('Máximos intentos realizados.')
            exit()

        print('' )
        print('Opción no válida, inserte una "S" o una "N" respectivamente')
        option = input('>> ').strip().lower()

        attemps += 1

    return option

def check_folders():
    necessary = (
            'Texto','Videos', 'Audios',
            'Imagenes', 'Comprimidos', 'Ejecutables',
            'Otros'
            )

    all_files = os.listdir(route_downloads)
    missing_folders = []

    for n in necessary:

        len_files = len(all_files)
        progress = 0
        
        for f in all_files:
            if f != n:
                progress += 1

            else:
                pass

        if progress == len_files:
            missing_folders.append(n)

    if len(missing_folders) == 0:
        pass

    else:
        print('Oh a ocurrido un error, en su directorio {} - faltan las siguientes carpetas: '.format(route_downloads))

        for c in missing_folders:
            print('* {}'.format(c))

        print('')

        option = get_option()
        
        if option == 'n':
            print('')
            exit()

        else:
            try:
                for mf in missing_folders:
                    # OJO AQUÍ CON LA SITAXIS DE LA RUTA
                    os.mkdir(route_downloads + mf)
                    
                print('')
                print('Carpetas creadas satisfactoriamente.')

            except:
                print('')
                print('Oh, ah ocurrido un error inesperado.')


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

    check_folders()

    for file in os.listdir(route_downloads):

        try:
            etx = os.path.splitext(file)[1]

            order(file, etx)

        except:
            print('No se puedo mover el archivo {}\n'.format(file))

    print('Proceso terminado')


if __name__ == '__main__':
    main()
