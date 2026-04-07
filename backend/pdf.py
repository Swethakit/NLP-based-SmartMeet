from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
import os
import uuid   # 🔥 to create unique file names

def generate_pdf(transcript, topics, summary):

    # ✅ Ensure files folder exists
    os.makedirs("files", exist_ok=True)

    # ✅ Unique file name (important if multiple users)
    file_name = f"files/report_{uuid.uuid4().hex}.pdf"

    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("SmartMeet Report", styles['Title']))

    story.append(Paragraph("Summary:", styles['Heading2']))
    story.append(Paragraph(summary, styles['Normal']))

    story.append(Paragraph("Topics:", styles['Heading2']))
    for t in topics:
        story.append(Paragraph(t, styles['Normal']))

    story.append(Paragraph("Transcript:", styles['Heading2']))
    for line in transcript:
        story.append(Paragraph(line, styles['Normal']))

    doc = SimpleDocTemplate(file_name)
    doc.build(story)

    # ✅ return ONLY filename (not full path)
    return file_name.replace("files/", "")