import PyPDF2
import ebooklib
from ebooklib import epub
import pyttsx3
import os
from HTMLFilter import HTMLFilter


def read_pdf_aloud(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        engine = pyttsx3.init()

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            engine.say(text)
            engine.runAndWait()


def read_epub_aloud(epub_path):
    book = epub.read_epub(epub_path)
    engine = pyttsx3.init()

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            print('==================================')
            print('NAME : ', item.get_name())
            
            engine.say('NAME : ', item.get_name())
            engine.runAndWait()
            
            print('----------------------------------')
            
            bodyContent = item.get_body_content().decode('utf-8')
            f = HTMLFilter()
            f.feed(bodyContent)
            print(f.text)
            
            engine.say(f.text)
            engine.runAndWait()
        
    return




if __name__ == "__main__":
 
    file_path = "D:\Continguts\Side Hustle_ From Idea to Income in 27 Days by Chris Guillebeau EPUB\Side Hustle_ From Idea to Income in 27 Days by Chris Guillebeau.epub"
    
    ext = os.path.splitext(file_path)[1].lower()
    
    if   (ext==".pdf"):  read_pdf_aloud(file_path)
    elif (ext==".epub"): read_epub_aloud(file_path)
