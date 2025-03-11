# Google Form Setup Guide

Follow these steps to create your survey using Google Forms:

## Step 1: Create a New Google Form

1. Go to [Google Forms](https://forms.google.com/)
2. Click on the "+" icon to create a new form
3. Sign in with your Google account if prompted

## Step 2: Set Up Form Title and Description

1. Click on "Untitled form" to rename it (e.g., "Event Feedback Survey")
2. Add a description explaining the purpose of the survey (e.g., "Help us improve our events by sharing your feedback")

## Step 3: Add the Survey Questions

### Question 1: Multiple Choice with Checkboxes

1. Type "What demo topics would you be most interested in?" as the question
2. Click the dropdown menu on the right and select "Checkboxes"
3. Add the following options:
   - AI
   - Finance
   - Crypto
   - Commerce/Marketplace
   - Service apps or websites
   - Knowledge transfer (guest speakers)
4. Click "Add 'Other'" to allow respondents to enter their own options

### Question 2: Multiple Choice with Checkboxes

1. Click the "+" icon on the right to add a new question
2. Type "How could we enhance networking beyond the demos?" as the question
3. Select "Checkboxes" from the dropdown menu
4. Add the following options:
   - Structured mentor matching
   - Industry-specific discussion groups
   - Investor speed meetings
   - Matching with incubator programs

### Question 3: Paragraph

1. Click the "+" icon to add a new question
2. Type "What features or huddle topics would you like to have in our slack channel?" as the question
3. Select "Paragraph" from the dropdown menu

### Question 4: Paragraph

1. Click the "+" icon to add a new question
2. Type "Would prefer other events besides our monthly meet-up? If yes, what type?" as the question
3. Select "Paragraph" from the dropdown menu

### Question 5: Paragraph

1. Click the "+" icon to add a new question
2. Type "Any other feedback?" as the question
3. Select "Paragraph" from the dropdown menu

## Step 4: Configure Form Settings

1. Click the Settings gear icon at the top
2. Under the "General" tab:
   - Decide whether to collect email addresses
   - Choose whether respondents can submit only once
3. Under the "Presentation" tab:
   - Add a confirmation message (e.g., "Thank you for your feedback!")
   - Choose whether to show a progress bar

## Step 5: Get the Form URL

1. Click the "Send" button at the top right
2. In the popup, click the link icon
3. Copy the URL provided
4. (Optional) Click "Shorten URL" if you want a shorter link

## Step 6: Generate QR Code

1. Use the provided Python script to generate a QR code:
   ```
   python generate_qr.py "YOUR_COPIED_FORM_URL"
   ```

## Step 7: View and Analyze Responses

1. Open your form in Google Forms
2. Click the "Responses" tab at the top
3. You can view:
   - Summary of responses
   - Individual responses
4. Click the Google Sheets icon to create a spreadsheet of responses for more detailed analysis 