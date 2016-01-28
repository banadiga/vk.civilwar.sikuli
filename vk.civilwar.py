import argparse
from argparse import RawTextHelpFormatter
import logging

SLEEP_ON_LOAD = 1
LONG_SLEEP = 10
SLEEP_ON_BUY = 1

LIST_OF_DONE_ITEM = [
"done_11.png", "done_21.png", "done_31.png", "done_41.png", "done_15.png",
"done_12.png", "done_22.png", "done_32.png", "done_42.png", "done_25.png",
"done_13.png", "done_23.png", "done_33.png", "done_43.png", "done_35.png",
"done_14.png", "done_24.png", "done_34.png", "done_44.png", "done_45.png",
]

LIST_OF_NEXT = [
[ "item_11.png", "item_21.png", "item_31.png", "item_41.png", "item_15.png"],
[ "item_12.png", "item_22.png", "item_32.png", "item_42.png", "item_25.png"],
[ "item_13.png", "item_23.png", "item_33.png", "item_43.png", "item_35.png"],
[ "item_14.png", "item_24.png", "item_34.png", "item_44.png", "item_45.png"],
]

def get_sleep_time(level):
    return SLEEP_ON_LOAD + LONG_SLEEP * level + SLEEP_ON_BUY * level

def check_is_item_redy() :
    for i, v in enumerate(LIST_OF_DONE_ITEM):
        top = exists(v)
        if top:
            print top
            return top

def get_netx_item(level):
    for j, q in enumerate(LIST_OF_NEXT[level]):
        next_item = exists(q)
        if next_item:
            print next_item
            return next_item

def buy_next_item(top, level):
    logging.debug("buy_next_item {0} and level {1}".format(top, level))
    click(top)
    shop = capture(top.getX(), top.getY() + 100, 20, 20)
    logging.debug("shop {0}".format(shop))
    print shop

    sleep(SLEEP_ON_BUY)
    click(shop)
    sleep(SLEEP_ON_BUY)
    click("buy.png")
    next_item = get_netx_item(level)
    if next_item:
        print "click on:"
        print next_item
        click(next_item)
    sleep(SLEEP_ON_BUY)
    click("close.png")


def buyitems(args):
    logging.debug("buy_next_item level {0}".format(args.level))
    sleep(SLEEP_ON_LOAD)
    i = 0
    while i < args.count:
        top = check_is_item_redy()
        if top :
            logging.debug("buy item #{0}".format(i))
            buy_next_item(top, args.level)
            i = i +1
        sleep(get_sleep_time(args.level))

#------------------------------------------------------------------------------------------------------------------------
def sentpresents(args):
    print "Not implemented yet."

#------------------------------------------------------------------------------------------------------------------------
def get_parser():
    parser = argparse.ArgumentParser(description='Automation of the game `vk.civilwar`', epilog=(
    'Home page: <https://github.com/banadiga/vk.civilwar.sikuli/>\n'
    'Documentation pade: <https://github.com/banadiga/vk.civilwar.sikuli/README.md>\n'
    'Report bugs to <banadiga@users.noreply.github.com> or <https://github.com/banadiga/vk.civilwar.sikuli/issues>\n'
    ), formatter_class=RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest='run', help='Sub command help:')
    parser_sent_presents = subparsers.add_parser('sent-presents',
        help='Sent presents to fiends.')
    parser_sent_presents.set_defaults(func=sentpresents)
    parser_buy_items = subparsers.add_parser('buy-items',
        help='Buy items in shop.')
    parser_buy_items.add_argument('-c', '--count',
        type=int, default=100,
        help='amount of items. Default is 100.')
    parser_buy_items.add_argument('-l', '--level', 
        type=int, default=0, choices=xrange(0, 6),
        help='level of item. Default is 0.')
    parser_buy_items.set_defaults(func=buyitems)

    parser.add_argument('--version', action='version', version='%(prog)s 2.1')

    parser.add_argument('-v', '--verbose',
        action="store_const", dest="Set log level to INFO.", const=logging.INFO,
        help="increase output verbosity.")
    parser.add_argument('-d', '--debug',
        action="store_const", dest="Set log level to DEBUG.", const=logging.DEBUG, default=logging.WARNING,
        help="print lots of debugging statements.")
    return parser

#------------------------------------------------------------------------------------------------------------------------
def main(args):
    logging.debug("Parser{0}".format(args))
    logging.info("Run command `{0}`".format(args.run))
    args.func(args)

args = get_parser().parse_args()
logging.basicConfig(level=args.loglevel)
if __name__ == '__main__':
    main(args)
