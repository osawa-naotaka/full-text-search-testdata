# full-text-search-testdata
testdatas from wikipedia

% cd mediawiki-services-parsoid
% composer install
% cd ..
% cd html2md
% npm install
% npm run build
% cd ..
% python extract_wikipedia.py --input jawiki-20241120-pages-articles-multistream.xml.bz2 --number 100 --language ja --output wikipedia_ja_extracted_100.json
% node html2md/dist/main.js wikipedia_ja_extracted_100.json md
