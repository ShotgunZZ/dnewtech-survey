# Survey Project

This project contains tools to create a survey and generate a QR code for easy access.

## Survey Questions

1. What demo topics would you be most interested in?
   - AI
   - Finance
   - Crypto
   - Commerce/Marketplace
   - Service apps or websites
   - Knowledge transfer (guest speakers)
   - Other

2. How could we enhance networking beyond the demos?
   - Structured mentor matching
   - Industry-specific discussion groups
   - Investor speed meetings
   - Matching with incubator programs

3. What features or huddle topics would you like to have in our slack channel?

4. Would prefer other events besides our monthly meet-up? If yes, what type?

5. Any other feedback?

## Step 1: Create Your Google Form

Follow the detailed instructions in `google_form_guide.md` to create your survey using Google Forms.

## Step 2: Generate a QR Code

Once you have created your Google Form, generate a QR code for it:

```bash
python3 generate_qr.py "YOUR_GOOGLE_FORM_URL"
```

This will create a file called `survey_qr.png` in the current directory.

## Step 3: View or Share the QR Code

You have several options to view or share the QR code:

### Option 1: View the QR code directly

```bash
python3 view_qr.py
```

This will open the QR code image in your default image viewer.

### Option 2: Start a local web server to display the QR code

```bash
python3 serve_qr.py
```

This will start a local web server and open a browser window displaying the QR code with instructions. This is useful if you want to display the QR code on a screen for people to scan.

### Option 3: Print the QR code

You can print the `survey_qr.png` file or include it in any document.

## Step 4: Collect and Analyze Responses

1. Responses will be automatically collected in your Google Form
2. You can view responses in the "Responses" tab of your Google Form
3. You can export responses to a Google Sheet for further analysis by clicking the Google Sheets icon in the Responses tab

## Files in this Project

- `generate_qr.py` - Script to generate a QR code for your survey
- `view_qr.py` - Script to view the generated QR code
- `serve_qr.py` - Script to start a local web server to display the QR code
- `qr_display.html` - HTML template for displaying the QR code
- `google_form_guide.md` - Detailed guide for creating your Google Form
- `README.md` - This file

## Requirements

- Python 3.6+
- qrcode[pil]
- pillow

## Troubleshooting

- If the QR code doesn't display correctly, make sure you have generated it first with `generate_qr.py`
- If the web server doesn't start, make sure port 8000 is available or specify a different port: `python3 serve_qr.py 8080`
- If you can't scan the QR code, make sure your device's camera is working and try increasing the size of the QR code by adjusting the `box_size` parameter in `generate_qr.py` 