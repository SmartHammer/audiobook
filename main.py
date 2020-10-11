#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__license__ = "MIT"

import pyttsx3
import PyPDF2
import argparse
from googletrans import Translator

def read(bookName, start=0, end=0, dest=''):
  '''
  '''
  assert isinstance(bookName, str)
  assert isinstance(start, int)
  assert isinstance(end, int)
  assert isinstance(dest, str)
  book = open(bookName, 'rb')
  pdfReader = PyPDF2.PdfFileReader(book)

  speaker = pyttsx3.init()
  translator = Translator()

  firstPage=1 if start==0 else start
  lastPage=pdfReader.numPages if end==0 else end

  for num in range(firstPage, lastPage):
    page = pdfReader.getPage(num)
    text = page.extractText()
    if dest != "original":
      translated = translator.translate(text, src='auto', dest=dest)
      tts = translated.text
    else:
      tts = text
    speaker.say(tts)
    speaker.runAndWait()

if __name__ == "__main__":
  from googletrans import LANGUAGES
  languages = "'' : no tranlation\n"
  for key, value in LANGUAGES.items():
    languages = languages + "'" + key + "' : " + value + '\n'
  parser = argparse.ArgumentParser(description='Read PDF ebook', formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument('bookName', type=str, help='Name of the book to read')
  parser.add_argument('--start', type=int, default=0, help='Page to start reading (default to start of document)')
  parser.add_argument('--end', type=int, default=0, help='Page to end reading (default to end of document)')
  parser.add_argument('--lang', type=str, default='', help='Language for translation (default to no translation)\n' +
  'choices are:\n' + languages)
  args = parser.parse_args()
  read(args.bookName, args.start, args.end, args.lang)
