# audiobook
Read and translate pdf book

## License
[MIT](https://en.wikipedia.org/wiki/MIT_License)
 
## Usage
'''bash
./main.py [-h] [--start START] [--end END] [--lang LANG] bookName  
  
Read PDF ebook  
  
positional arguments:  
  bookName       Name of the book to read  
  
optional arguments:  
  -h, --help     show this help message and exit  
  --start START  Page to start reading (default to start of document)  
  --end END      Page to end reading (default to end of document)  
  --lang LANG    Language for translation (default to no translation)  
                 choices are:  
                 '' : no tranlation  
                 'af' : afrikaans  
                 'sq' : albanian  
                 'am' : amharic  
                 'ar' : arabic  
                 'hy' : armenian  
                 'az' : azerbaijani  
                 'eu' : basque  
                 'be' : belarusian  
                 'bn' : bengali  
                 'bs' : bosnian  
                 'bg' : bulgarian  
                 'ca' : catalan  
                 'ceb' : cebuano  
                 'ny' : chichewa  
                 'zh-cn' : chinese (simplified)  
                 'zh-tw' : chinese (traditional)  
                 'co' : corsican  
                 'hr' : croatian  
                 'cs' : czech  
                 'da' : danish  
                 'nl' : dutch  
                 'en' : english  
                 'eo' : esperanto  
                 'et' : estonian  
                 'tl' : filipino  
                 'fi' : finnish  
                 'fr' : french  
                 'fy' : frisian  
                 'gl' : galician  
                 'ka' : georgian  
                 'de' : german  
                 'el' : greek  
                 'gu' : gujarati  
                 'ht' : haitian creole  
                 'ha' : hausa  
                 'haw' : hawaiian  
                 'iw' : hebrew  
                 'he' : hebrew  
                 'hi' : hindi  
                 'hmn' : hmong  
                 'hu' : hungarian  
                 'is' : icelandic  
                 'ig' : igbo  
                 'id' : indonesian  
                 'ga' : irish  
                 'it' : italian  
                 'ja' : japanese  
                 'jw' : javanese  
                 'kn' : kannada  
                 'kk' : kazakh  
                 'km' : khmer  
                 'ko' : korean  
                 'ku' : kurdish (kurmanji)  
                 'ky' : kyrgyz  
                 'lo' : lao  
                 'la' : latin  
                 'lv' : latvian  
                 'lt' : lithuanian  
                 'lb' : luxembourgish  
                 'mk' : macedonian  
                 'mg' : malagasy  
                 'ms' : malay  
                 'ml' : malayalam  
                 'mt' : maltese  
                 'mi' : maori  
                 'mr' : marathi  
                 'mn' : mongolian  
                 'my' : myanmar (burmese)  
                 'ne' : nepali  
                 'no' : norwegian  
                 'or' : odia  
                 'ps' : pashto  
                 'fa' : persian  
                 'pl' : polish  
                 'pt' : portuguese  
                 'pa' : punjabi  
                 'ro' : romanian  
                 'ru' : russian  
                 'sm' : samoan  
                 'gd' : scots gaelic  
                 'sr' : serbian  
                 'st' : sesotho  
                 'sn' : shona  
                 'sd' : sindhi  
                 'si' : sinhala  
                 'sk' : slovak  
                 'sl' : slovenian  
                 'so' : somali  
                 'es' : spanish  
                 'su' : sundanese  
                 'sw' : swahili  
                 'sv' : swedish  
                 'tg' : tajik  
                 'ta' : tamil  
                 'te' : telugu  
                 'th' : thai  
                 'tr' : turkish  
                 'uk' : ukrainian  
                 'ur' : urdu  
                 'ug' : uyghur  
                 'uz' : uzbek  
                 'vi' : vietnamese  
                 'cy' : welsh  
                 'xh' : xhosa  
                 'yi' : yiddish  
                 'yo' : yoruba  
                 'zu' : zulu  
'''

## Requirements
pip3 install pyttsx3
pip3 install PyPDF2
pip3 install googletrans

## Run application in virtual environment
### Requirements
sudo apt-get install python3-venv  

### Prepare and run
python3 -m venv audiobook-env  
source audiobook-env/bin/activate  
(audiobook-env)$ pip3 install pyttsx3 PyPDF2 goggletrans  
(audiobook-env)$ git clone https://github.com/ProgrammingHero1/audiobook.git  
(audiobook-env)$ wget https://ptgmedia.pearsoncmg.com/images/9780132350884/samplepages/9780132350884.pdf -O ~/Downloads  
(audiobook-env)$ cd audiobook  
(audiobook-env/audiobook)$ ./main.py bookName ~/Downloads/9780132350884.pdf --start 19 --end 23 --lang eo  
(audiobook-env/audiobook)$ deactivate  

