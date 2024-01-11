import docx

def create_file(text):
    doc = docx.Document()
    doc.add_paragraph(text)
    doc.save('output.docx')

if __name__ == '__main__':
    a = input('Введите текст:')
    create_file(a)