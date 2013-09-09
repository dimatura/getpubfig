
getpubfig
=========

Just a quick hack to download the pictures of the
[Pubfig](http://www.cs.columbia.edu/CAVE/databases/pubfig/) face database. You
will need 

- Python
- ``wget`` and it should be in the path
- The files ``dev_urls.txt`` and ``eval_urls.txt`` from
  [here](http://www.cs.columbia.edu/CAVE/databases/pubfig/download/) in the
  same directory you run the script from.


Then run ``./getpubfig.py dev`` or ``./getpubfig.py eval`` depending on which
of the databases you want to download. It will start downloading files (using
md5 as the ID) into the current working directory. It will also save various
logfiles.

Afterwards run ``./verifypubfig.py dev`` or ``./verifypubfig.py eval`` to check
the downloaded files using the MD5 checksum. "Bad" files will be moved into
``bad_dev`` or ``bad_eval`` respectively, where you can delete them. Note that
many files with "bad" MD5s actually seem okay; perhaps they were resized or
something like that. 

Daniel Maturana - dimatura@cmu.edu
