find . -name "*.xml" -print0 | xargs -0 sed -i 's/mis="on"/mis="off"/g'   #修改mis(从on-->off)
find . -name "*.xml" -print0 | xargs -0 sed -i 's/err="on"/err="off"/g'   #修改mis(从on-->off)
find . -name "*.xml" -print0 | xargs -0 sed -i 's/ans="on"/ans="off"/g'   #修改mis(从on-->off)
