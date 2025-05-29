#!/usr/bin/env python3
"""
QR Code Generator for Slack Invitation

This script generates a QR code for the DNewTech Slack invitation link.
"""

import qrcode
from PIL import Image

def generate_slack_qr():
    # Slack invitation link
    slack_url = "https://join.slack.com/t/dnewtech/shared_invite/zt-31lrcp9f8-19x13TsoulWs~titpTUL0A"
    
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(slack_url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    output_file = "slack_qr.png"
    qr_img.save(output_file)
    
    print(f"Slack QR code saved to {output_file}")
    return output_file

if __name__ == "__main__":
    generate_slack_qr() 