Name
====

Functionality
----

Install
----

### Install java
How to [Install java]()

### Install sikuli
How to [Install sikuli]()

### Install vk.civilwar.skl
Just download [vk.civilwar.skl 2.1]()

Run
----

```bash
java -jar <PATH_TO_SIKULIX>/sikulix.jar -r <PATH_TO_SKL>/vk.civilwar.skl --args buy-items
```

Help
----

### About program

```bash
java -jar ~/Applications/sikulix/sikulix.jar -r vk.civilwar.skl --args  -h
```

```
usage: vk.civilwar.sikuli [-h] [--version] [-v] [-d]
                          {sent-presents,buy-items} ...

Automation of the game `vk.civilwar`

positional arguments:
  {sent-presents,buy-items}
                        Sub command help:
    sent-presents       Sent presents to fiends.
    buy-items           Buy items in shop.

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -v, --verbose         increase output verbosity.
  -d, --debug           print lots of debugging statements.

Home page: <https://github.com/banadiga/vk.civilwar.sikuli/>
Documentation pade: <https://github.com/banadiga/vk.civilwar.sikuli/README.md>
Report bugs to <banadiga@users.noreply.github.com> or <https://github.com/banadiga/vk.civilwar.sikuli/issues>

```

### About `buy-items`
```bash
java -jar ~/Applications/sikulix/sikulix.jar -r vk.civilwar.skl --args  buy-items -h
```

```
usage: vk.civilwar.sikuli buy-items [-h] [-c COUNT] [-l {0,1,2,3,4,5}]

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        amount of items. Default is 100.
  -l {0,1,2,3,4,5}, --level {0,1,2,3,4,5}
                        level of item. Default is 0.
```
