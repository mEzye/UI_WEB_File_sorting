IMAGES = ('JPEG', 'PNG', 'JPG', 'SVG')
VIDEO = ('AVI', 'MP4', 'MOV', 'MKV')
DOCS = ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX')
MUSIC = ('MP3', 'OGG', 'WAV', 'AMR')
ARCHIVES = ('ZIP', 'GZ', 'TAR')
SUMB = """ !"#$%&'()*+№,-/:;<=>?@[\]^_`{|}~"""
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = (
    "a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
"f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g"
)
TRANS = {ord(c): l for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION)}
