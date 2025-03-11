#!/usr/bin/env python3
"""
QR Code Generator for Survey

This script generates a QR code for a given URL (typically a Google Form).
Usage: python generate_qr.py "YOUR_GOOGLE_FORM_URL"
"""

import sys
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def generate_qr_code(url, output_file="survey_qr.png", add_text=True):
    """
    Generate a QR code for the given URL and save it to a file.
    
    Args:
        url (str): The URL to encode in the QR code
        output_file (str): The filename to save the QR code to
        add_text (bool): Whether to add text below the QR code
    
    Returns:
        str: The path to the saved QR code image
    """
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    if add_text:
        # Convert to RGB mode if it's not already
        if qr_img.mode != 'RGB':
            qr_img = qr_img.convert('RGB')
            
        # Get the size of the QR code image
        width, height = qr_img.size
        
        # Create a larger image to accommodate the QR code and text
        new_img = Image.new('RGB', (width, height + 50), color='white')
        
        # Paste the QR code onto the new image
        new_img.paste(qr_img, (0, 0))
        
        # Add text below the QR code
        draw = ImageDraw.Draw(new_img)
        
        # Try to use a system font, or fall back to default
        try:
            font = ImageFont.truetype("Arial", 20)
        except IOError:
            font = ImageFont.load_default()
            
        text = "Scan to take our survey!"
        
        # Handle different PIL versions for text width calculation
        try:
            # For newer PIL versions
            text_width = draw.textlength(text, font=font)
        except AttributeError:
            # For older PIL versions
            text_width = font.getlength(text)
        
        # Draw the text
        try:
            draw.text(((width - text_width) // 2, height + 15), text, fill="black", font=font)
        except TypeError:
            # Fallback for older PIL versions
            draw.text(((width - text_width) // 2, height + 15), text, fill="black")
        
        # Save the image
        new_img.save(output_file)
    else:
        # Save the QR code directly
        qr_img.save(output_file)
    
    print(f"QR code saved to {output_file}")
    return output_file

def main():
    """Main function to handle command line arguments."""
    if len(sys.argv) < 2:
        print("Usage: python generate_qr.py \"YOUR_GOOGLE_FORM_URL\"")
        print("Example: python generate_qr.py \"https://forms.gle/example\"")
        sys.exit(1)
    
    url = sys.argv[1]
    output_file = "survey_qr.png"
    
    if len(sys.argv) > 2:
        output_file = sys.argv[2]
    
    generate_qr_code(url, output_file)
    
    # Print instructions
    print("\nInstructions:")
    print("1. Print this QR code or display it on a screen")
    print("2. People can scan it with their smartphone camera to access the survey")
    print("3. Responses will be collected in your Google Form")
    print("4. You can view and export responses from the Google Form dashboard")

if __name__ == "__main__":
    main() 