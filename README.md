# DSRipper

A simple recursive ripper of .DS_Store files left by developers on websites. It will iterate over provided URL with .DS_Store file, parse out files mentioned there and will try to find nested .DS_Store files and so on.

Internal help is self-explanatory:

```
$ python3 dsripper.py -h                                                                                                                                                                                                              2 ⨯
usage: dsripper.py [-h] -u url [-iu]

Recursive .DS_Store ripper

options:
  -h, --help          show this help message and exit
  -u url, --url url   Full URI to .DS_Store file or its directory
  -iu, --include-url  Set to print full URL
```

But here's an example call, just in case:

```
$ python3 dsripper.py -u "https://example.com/files/.DS_Store"
directory1
directory2
directory2/subdirectory1
directory3
directory3/subdirectory1
directory3/subdirectory2
directory3/subdirectory2/subsubdirectory1
directory4
```
