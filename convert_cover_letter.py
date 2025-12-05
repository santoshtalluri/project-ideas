import markdown
from xhtml2pdf import pisa

def convert_md_to_pdf(source_md_file, output_pdf_file):
    with open(source_md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    # Convert Markdown to HTML
    html_content = markdown.markdown(md_content)

    # Add some basic styling
    styled_html = f"""
    <html>
    <head>
    <style>
        body {{
            font-family: Helvetica, Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.5;
            margin: 2cm;
        }}
        h1 {{
            font-size: 18pt;
            text-align: center;
            margin-bottom: 1cm;
        }}
        h2 {{
            font-size: 14pt;
            margin-top: 0.5cm;
            margin-bottom: 0.3cm;
            border-bottom: 1px solid #ccc;
        }}
        p {{
            margin-bottom: 0.3cm;
            text-align: justify;
        }}
        ul {{
            margin-bottom: 0.3cm;
        }}
        li {{
            margin-bottom: 0.1cm;
        }}
    </style>
    </head>
    <body>
    {html_content}
    </body>
    </html>
    """

    # Write PDF
    with open(output_pdf_file, "wb") as result_file:
        pisa_status = pisa.CreatePDF(
            styled_html,                # the HTML to convert
            dest=result_file            # file handle to recieve result
        )

    if pisa_status.err:
        print(f"Error converting file: {pisa_status.err}")
    else:
        print(f"Successfully created PDF: {output_pdf_file}")

if __name__ == "__main__":
    convert_md_to_pdf("COVER_LETTER.md", "COVER_LETTER.pdf")

