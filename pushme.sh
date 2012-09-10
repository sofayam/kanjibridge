./hg add .
comment=no_comment
./hg ci -m ${1:-$comment}
./hg push http://bitbucket.org/sofayam/kanjibridge
