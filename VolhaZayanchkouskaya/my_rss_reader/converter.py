from args_parameters import ArgParser
from fpdf import FPDF
import pandas as pd
import json
import requests
import logging

arg_parser = ArgParser()
config = arg_parser.get_args()


def convert_to_html():
	"""Convert to HTML-format (html-table)"""
	s = ['<HTML>']
	s.append('\n<HEAD>\n<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\n'
			 '<TITLE>\nNews</TITLE>\n</HEAD>\n')
	s.append('<BODY>\n')
	try:
		with open("cache.json", "r", encoding="utf-8") as f:
			d = json.load(f)
			for i in d.values():
				for value in i[:config.limit]:
					df = pd.DataFrame.from_dict(value, orient='index')
					s.append(df.to_html())
			s.append('</BODY>\n</HTML>')
			html = ''.join(s)
	except Exception as ex:
		logging.warning(f"File is invalid")
		raise ex

	try:
		with open("html_format.html", 'w', encoding="utf-8") as html_file:
			html_file.write(html)
		logging.info(f"HTML is ready")
	except Exception as ex:
		logging.warning(f"File is invalid")
		raise ex


def convert_to_pdf():
	"""Convert to PDF-format"""
	pdf = FPDF()
	pdf.add_font("DejaVu", '', 'DejaVuSansCondensed.ttf', uni=True)
	pdf.set_font("DejaVu", size=14)
	count = 0
	with open("cache.json", "r", encoding="utf-8") as ff:
		d = json.load(ff)
		for i in d.values():
			for value in i[:config.limit]:
				pdf.add_page()
				title = value["Title"]
				date = value["Date"]
				description = value["Description"]
				source = value["Source"]
				link = value["Link"]
				media = value["Media"]
				pdf.multi_cell(200, 10, "Title: "+title, 0, 1)
				pdf.multi_cell(200, 10, "Date: "+date, 0, 1)
				pdf.multi_cell(200, 10, "Description: "+description, 0, 1)
				pdf.multi_cell(200, 10, "Source: "+source, 0, 1)
				pdf.multi_cell(200, 10, "Link: "+link, 0, 1)
				img_list = []
				for item in media:
					if item.endswith(('.jpg', '.jpeg', '.bmp')):
						req = requests.get(item)
						responce = req.content
						with open(f"media/{count}.jpg", "wb") as file:
							file.write(responce)
							img_list.append(f"media/{count}.jpg")
					count += 1
				for img in img_list:
					pdf.image(img, x=None, y=None, w=60, h=50)
				img_list.clear()
	pdf.output("pdf_format.pdf")


