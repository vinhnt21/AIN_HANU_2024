import markdown
import pdfkit
import os

def convert_md_to_pdf(md_file_path, pdf_file_path):
  # Check if the Markdown file exists
  if not os.path.isfile(md_file_path):
      print(f"Markdown file '{md_file_path}' not found.")
      return

  # Read the Markdown file
  with open(md_file_path, 'r', encoding='utf-8') as md_file:
      md_content = md_file.read()

  # Convert Markdown to HTML
  html_content = markdown.markdown(md_content, output_format='html5')

  # Optional: Add basic HTML structure
  html = f'''
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <title>{os.path.splitext(os.path.basename(md_file_path))[0]}</title>
  </head>
  <body>
      {html_content}
  </body>
  </html>
  '''

  # Configure pdfkit to use wkhtmltopdf
  # If wkhtmltopdf is not in your PATH, specify the full path:
  # config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
  # If wkhtmltopdf is in PATH, you can omit the configuration parameter
  try:
      pdfkit.from_string(html, pdf_file_path)
      print(f"Successfully converted '{md_file_path}' to '{pdf_file_path}'.")
  except OSError:
      print("Error: wkhtmltopdf not found. Ensure wkhtmltopdf is installed and added to your system PATH.")
      # If wkhtmltopdf is not in PATH, specify the path directly:
      # config = pdfkit.configuration(wkhtmltopdf=r'path_to_wkhtmltopdf')
      # pdfkit.from_string(html, pdf_file_path, configuration=config)

# Convert 'Knowledge.md' to 'Knowledge.pdf'
convert_md_to_pdf('Knowlegde.md', 'Knowlegde.md')