# Program Name: Assignment4.py (use the name the program is saved as)
# Course: IT3883/Section 430
# Student Name: Brandon Thweatt
# Assignment Number: Lab4
# Due Date: 03/24/ 2025
# Purpose: What does the program do (in a few sentences)?
# This program  creates a server port to listen for input from the client
# List Specific resources used to complete the assignment.
# N/A

import socket


def server_program():
    host = '127.0.0.1'  # Server IP (localhost)
    port = 40001  # Port number

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server listening...")

    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    message = conn.recv(1024).decode()
    print(f"Received from client: {message}")

    response = message.upper()
    conn.send(response.encode())

    conn.close()


if __name__ == '__main__':
    server_program()