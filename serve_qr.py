#!/usr/bin/env python3
"""
QR Code Web Server

This script starts a simple HTTP server to display the QR code HTML page.
Usage: python serve_qr.py [port]
"""

import sys
import os
import webbrowser
import http.server
import socketserver
import threading
import time

def start_server(port=8000):
    """
    Start a simple HTTP server to serve the QR code HTML page.
    
    Args:
        port (int): Port number to use for the server
    """
    # Change to the directory containing this script
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Check if the HTML file exists
    if not os.path.exists("qr_display.html"):
        print("Error: qr_display.html not found.")
        return False
    
    # Check if the QR code image exists
    if not os.path.exists("survey_qr.png"):
        print("Warning: survey_qr.png not found. The QR code will not display correctly.")
        print("Generate a QR code first with: python generate_qr.py \"YOUR_FORM_URL\"")
    
    # Set up the server
    handler = http.server.SimpleHTTPRequestHandler
    httpd = socketserver.TCPServer(("", port), handler)
    
    print(f"Server started at http://localhost:{port}")
    print("Press Ctrl+C to stop the server")
    
    # Open the browser
    threading.Timer(1.0, lambda: webbrowser.open(f"http://localhost:{port}/qr_display.html")).start()
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    finally:
        httpd.server_close()
    
    return True

def main():
    """Main function to handle command line arguments."""
    port = 8000
    
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            print(f"Invalid port number: {sys.argv[1]}")
            print("Using default port 8000")
    
    start_server(port)

if __name__ == "__main__":
    main() 