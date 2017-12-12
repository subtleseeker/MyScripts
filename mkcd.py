import os
path=os.path.expanduser(r'~/.bashrc')
f=open(path,"a+")
f.write("""
mkcd ()
{
    mkdir -p -- "$1" && cd -P -- "$1"
}""")
f.close()
