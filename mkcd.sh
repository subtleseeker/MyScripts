fun='
mkcd ()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}'

echo "$fun" >> ~/.bashrc
