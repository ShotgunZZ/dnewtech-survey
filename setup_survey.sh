#!/bin/bash
# Survey Setup Script
# This script guides you through the process of setting up your survey

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check for Python
if command_exists python3; then
    PYTHON=python3
elif command_exists python; then
    PYTHON=python
else
    echo "Error: Python is not installed. Please install Python 3.6 or higher."
    exit 1
fi

# Print welcome message
echo "====================================="
echo "Welcome to the Survey Setup Assistant"
echo "====================================="
echo ""
echo "This script will help you set up your survey and generate a QR code."
echo ""

# Check if the required packages are installed
$PYTHON -c "import qrcode, PIL" >/dev/null 2>&1
if [ $? -ne 0 ]; then
    echo "Installing required packages..."
    pip install "qrcode[pil]" pillow
    if [ $? -ne 0 ]; then
        echo "Error: Failed to install required packages."
        echo "Please run: pip install \"qrcode[pil]\" pillow"
        exit 1
    fi
fi

# Step 1: Create Google Form
echo "Step 1: Create your Google Form"
echo "------------------------------"
echo "Please follow the instructions in google_form_guide.md to create your survey."
echo "Once you have created your form, you will need the URL to generate a QR code."
echo ""
read -p "Have you created your Google Form? (y/n): " created_form

if [ "$created_form" != "y" ] && [ "$created_form" != "Y" ]; then
    echo "Please create your Google Form first. You can find instructions in google_form_guide.md."
    exit 0
fi

# Step 2: Generate QR code
echo ""
echo "Step 2: Generate QR Code"
echo "----------------------"
read -p "Enter your Google Form URL: " form_url

if [ -z "$form_url" ]; then
    echo "Error: No URL provided."
    exit 1
fi

echo "Generating QR code..."
$PYTHON generate_qr.py "$form_url"

if [ $? -ne 0 ]; then
    echo "Error: Failed to generate QR code."
    exit 1
fi

# Step 3: View options
echo ""
echo "Step 3: View or Share QR Code"
echo "---------------------------"
echo "How would you like to view or share your QR code?"
echo "1. View the QR code directly"
echo "2. Start a local web server to display the QR code"
echo "3. Exit (I'll handle it myself)"
read -p "Enter your choice (1-3): " view_option

case $view_option in
    1)
        echo "Opening QR code..."
        $PYTHON view_qr.py
        ;;
    2)
        echo "Starting web server..."
        $PYTHON serve_qr.py
        ;;
    3)
        echo "Exiting. Your QR code has been saved as survey_qr.png."
        ;;
    *)
        echo "Invalid option. Your QR code has been saved as survey_qr.png."
        ;;
esac

echo ""
echo "Thank you for using the Survey Setup Assistant!"
echo "Remember to check your Google Form for responses." 