#!/usr/bin/env bash
import socket

# Create a socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket options to allow reusing address
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Close the socket
sock.close()

