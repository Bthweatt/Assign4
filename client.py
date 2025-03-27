# Program Name: Assignment4.py (use the name the program is saved as)
# Course: IT3883/Section 430
# Student Name: Brandon Thweatt
# Assignment Number: Lab4
# Due Date: 03/24/ 2025
# Purpose: What does the program do (in a few sentences)?
# This program prompts the user for input that will be sent to the server, and printed out by the console
# List Specific resources used to complete the assignment.
# N/A
import socket


def client_program():
    host = '127.0.0.1'  # Server IP (localhost)
    port = 40001  # Port number

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input("Enter a message: ")  # User input
    client_socket.send(message.encode())  # Send to server

    response = client_socket.recv(1024).decode()  # Receive response
    print(f"Response from server: {response}")

    client_socket.close()


if __name__ == '__main__':
    client_program()