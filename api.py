import requests
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
# from io import BytesIO

def create_pdf(endpoint):
    # Set the URL of the endpoint
    url = endpoint

    # Set the filename for the PDF file
    filename = 'Cohort1.pdf'

    # Create a new PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter)

    # Set up some styles for the text
    styles = getSampleStyleSheet()
    style_normal = styles['Normal']

    # Create an empty list to hold the content
    content = []

    # Send a GET request to the endpoint
    response = requests.get(url)

   
    # Parse the JSON data from the response
    data = response.json()
        
    # Adds the questions to the content and numbers them
    for i, question in enumerate(data['items']):
            
             # Check if we have already processed 50 questions
            if i >= 50:
                break
            print(" ")

            # Add the question title
            title_text = f"{i+1}. {question['title']}"
            print(title_text)
            title_para = Paragraph(title_text, style_normal)
            content.append(title_para)
            
            # Add the total number of views
            views_text = f"Views: {question['view_count']}"
            print(views_text)
            views_para = Paragraph(views_text, style_normal)
            content.append(views_para)
            
            # Add the link to the question
            link_text = f"Link: {question['link']}"
            print(link_text + '\n')
            link_para = Paragraph(link_text, style_normal)
            content.append(link_para)
            
        
            # # Add the picture of the question
            # picture_data = question['owner']['profile_images']
            # byte_string = picture_data.encode()
            # picture_image = Image(BytesIO(byte_string))
            # content.append(picture_image)
   

    # Build the PDF document
    doc.build(content)

# Prompt the User for the endpoint and calling the function:
endpoint = input('Enter your endpoint: ')
create_pdf(endpoint)
