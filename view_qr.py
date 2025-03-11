#!/usr/bin/env python3
"""
QR Code Viewer

This script opens the generated QR code image for viewing.
Usage: python view_qr.py [qr_code_file]
"""

import sys
import os
import webbrowser
from pathlib import Path

def view_qr_code(qr_file="survey_qr.png"):
    """
    Open the QR code image for viewing.
    
    Args:
        qr_file (str): Path to the QR code image file
    """
    if not os.path.exists(qr_file):
        print(f"Error: QR code file '{qr_file}' not found.")
        return False
    
    # Get the absolute path to the file
    file_path = os.path.abspath(qr_file)
    
    # Convert to file:// URL format
    if sys.platform == 'win32':
        file_url = f"file:///{file_path.replace(os.sep, '/')}"
    else:
        file_url = f"file://{file_path}"
    
    print(f"Opening QR code: {file_path}")
    webbrowser.open(file_url)
    return True

def main():
    """Main function to handle command line arguments."""
    qr_file = "survey_qr.png"
    
    if len(sys.argv) > 1:
        qr_file = sys.argv[1]
    
    if view_qr_code(qr_file):
        print("\nIf the QR code doesn't open automatically, you can find it at:")
        print(os.path.abspath(qr_file))

if __name__ == "__main__":
    main() 