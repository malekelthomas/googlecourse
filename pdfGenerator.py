#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(attachment, title, paragraph):  
  report = SimpleDocTemplate(attachment)
  styles = getSampleStyleSheet()  
  report_title = Paragraph(title, styles["h1"])
  report_paragraph = Paragraph(paragraph, styles['Normal'])
  report.build([report_title, report_paragraph])
