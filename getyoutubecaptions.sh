# Copied from SO
cap()(cd /tmp;rm -f *.vtt;youtube-dl --skip-download --write-auto-sub "$1";sed '1,/^$/d' *.vtt|sed 's/<[^>]*>//g'|awk -F. 'NR%8==1{printf"%s ",$1}NR%8==3'|tee cap)

# Just del first files from the piped files
del_lines()(
    for file in ./captions/*.txt; do
        sed -i -e 1,4d $file
    done

    rm ./captions/*-e
)