__author__ = "reza0310"

import socket
import select
import os
import threading


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP


HEADER_LENGTH = 10
IP = get_ip()
print("IP:", IP)
PORT = 9999


def serveur():
    envoye = False
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list)
    for notified_socket in read_sockets:
        if notified_socket == server_socket:
            client_socket, client_address = server_socket.accept()
            sockets_list.append(client_socket)
            clients[client_socket] = {'header': len(client_address), 'adresse': client_address}
        else:
            message = receive_message(notified_socket)
            if message is False:
                print('Closed connection from: {}'.format(clients[notified_socket]['adresse']))
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket]
            print("User:", user)
            reponse = traiter(message["data"].decode("utf-8"), user)
            reponses = reponse.encode('utf-8')
            message_header = f"{len(reponses):<{HEADER_LENGTH}}".encode('utf-8')
            notified_socket.send(message_header + reponses)


def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH)
        if not len(message_header):
            print("Ho no...")
            return False
        print("Header:", message_header)
        message_length = int(message_header.decode('utf-8').strip())
        data = client_socket.recv(message_length)
        return {'header': message_header, 'data': data}
    except Exception as e:
        print("Error:", e)
        return False


def envoyer(fichier, client_socket):
    message = fichier.split(os.sep)[-1].encode('utf-8')
    client_socket.send(message)
    a = client_socket.recv(2).decode('utf-8')
    if not a == "ok":
        print("Erreur")
    taille = os.path.getsize(fichier)
    message = str(taille).encode('utf-8')
    client_socket.send(message)
    a = client_socket.recv(2).decode('utf-8')
    if not a == "ok":
        print("Erreur")
    num = 1
    with open(fichier, "rb") as f:
        while num <= taille:
            if taille-num > 10000000:
                octet = f.read(10000000)
                client_socket.send(octet)
                num += 10000000
            elif taille-num > 1000000:
                octet = f.read(1000000)
                client_socket.send(octet)
                num += 1000000
            elif taille-num > 100000:
                octet = f.read(100000)
                client_socket.send(octet)
                num += 100000
            elif taille-num > 10000:
                octet = f.read(10000)
                client_socket.send(octet)
                num += 10000
            elif taille - num > 1000:
                octet = f.read(1000)
                client_socket.send(octet)
                num += 1000
            elif taille-num > 100:
                octet = f.read(100)
                client_socket.send(octet)
                num += 100
            else:
                octet = f.read(1)
                client_socket.send(octet)
                num += 1
            print("Paquet numéro", num - 1, "/", taille, "envoyé. Progression:", str(((num - 1) / taille) * 100), "%")
            a = client_socket.recv(2).decode('utf-8')
            if not a == "ok":
                print("Erreur")


def traiter(requete):
    requete = requete.replace("'", "&apos;").replace("＇", "&apos;").replace("`", "&apos;").replace('"', '&quot;').replace('＂', '&quot;').split("\0")
    if requete[0] == "premier_mot_de_la_requête":
    	return "La réponse"
    else:
        return "Mauvaise requête"


# Initialisation du serveur
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((IP, PORT))
server_socket.listen()
sockets_list = [server_socket]
clients = {}

# Serveur:
while True:
    thread = threading.Thread(target=serveur)
    thread.start()
    thread.join()
