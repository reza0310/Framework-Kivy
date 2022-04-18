__author__ = "reza0310"

import globals


def echanger(message):  # Code pour envoyer un msg
    message = message.encode('utf-8')
    message_header = f"{len(message):<{globals.HEADER_LENGTH}}".encode('utf-8')
    globals.client_socket.send(message_header + message)
    message_header = globals.client_socket.recv(globals.HEADER_LENGTH)
    if not len(message_header):
        print('Connection perdue.')
    message_length = int(message_header.decode('utf-8').strip())
    message = globals.client_socket.recv(message_length).decode('utf-8')
    return message.replace("&apos;", "'").replace('&quot;', '"')


def recevoir(client_socket):
    Nom_du_fichier = b''
    while Nom_du_fichier == b'':
        Nom_du_fichier = client_socket.recv(100).strip().decode('utf-8')
    msg = "ok".encode('utf-8')
    client_socket.send(msg)
    Taille_du_fichier = b''
    while Taille_du_fichier == b'':
        Taille_du_fichier = int(client_socket.recv(100).strip().decode('utf-8'))
    msg = "ok".encode('utf-8')
    client_socket.send(msg)
    print(Taille_du_fichier)
    fichier = Nom_du_fichier
    num = 1
    donnees = b''
    while num <= Taille_du_fichier:
        if Taille_du_fichier-num > 10000000:
            octet = client_socket.recv(10000000)
            num += 10000000
        elif Taille_du_fichier-num > 1000000:
            octet = client_socket.recv(1000000)
            num += 1000000
        elif Taille_du_fichier-num > 100000:
            octet = client_socket.recv(100000)
            num += 100000
        elif Taille_du_fichier-num > 10000:
            octet = client_socket.recv(10000)
            num += 10000
        elif Taille_du_fichier - num > 1000:
            octet = client_socket.recv(1000)
            num += 1000
        elif Taille_du_fichier - num > 100:
            octet = client_socket.recv(100)
            num += 100
        else:
            octet = client_socket.recv(1)
            num += 1
        donnees += octet
        print("Paquet numéro", num - 1, "/", Taille_du_fichier, "reçu. Progression:", str(((num - 1) / Taille_du_fichier) * 100), "%")
        msg = "ok".encode('utf-8')
        client_socket.send(msg)
    with open("DLS/"+fichier, "wb") as f:
        f.write(donnees)
    print("Opération terminée")