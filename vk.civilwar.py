import argparse
import java.awt.Robot as JRobot
from argparse import RawTextHelpFormatter
import logging

SLEEP_ON_LOAD = 1
LONG_SLEEP = 10
SLEEP_ON_BUY = 1
SIMILAR_FOR_NEW = 0.8
SIMILAR_FOR_DONE = 0.58

LIST_OF_DONE_ITEM = [
    "done_11.png", "done_21.png", "done_31.png", "done_41.png", "done_15.png",
    "done_12.png", "done_22.png", "done_32.png", "done_42.png", "done_25.png",
    "done_13.png", "done_23.png", "done_33.png", "done_43.png", "done_35.png",
    "done_14.png", "done_24.png", "done_34.png", "done_44.png", "done_45.png",
]

LIST_OF_NEXT = [
    ["item_11.png", "item_21.png", "item_31.png", "item_41.png"],
    ["item_12.png", "item_22.png", "item_32.png", "item_42.png"],
    ["item_13.png", "item_23.png", "item_33.png", "item_43.png"],
    ["item_14.png", "item_24.png", "item_34.png", "item_44.png"],
    ["item_15.png", "item_25.png", "item_35.png", "item_45.png"]
]

# ------------------------------------------------------------------------------------------------------------------------
# buy items
# ------------------------------------------------------------------------------------------------------------------------
def get_sleep_time(level):
    return SLEEP_ON_LOAD + LONG_SLEEP * level + SLEEP_ON_BUY * level


def check_is_item_redy():
    for i, v in enumerate(LIST_OF_DONE_ITEM):
        pattern = Pattern(v)
        pattern.similar(SIMILAR_FOR_DONE)
        top = exists(v)
        if top:
            print v
            print top
            return top


def get_netx_item(level):
    for j, q in enumerate(LIST_OF_NEXT[level - 1]):
        pattern = Pattern(q)
        pattern.similar(SIMILAR_FOR_NEW)
        next_item = exists(pattern)
        if next_item:
            print q
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
    sleep(SLEEP_ON_BUY)
    x = find("close.png")
    mouseMove(x)
    next_item = get_netx_item(level)
    if next_item:
        print "click on:"
        print next_item
        click(next_item)
        sleep(SLEEP_ON_BUY)
    click(x)


def buyitems(args):
    logging.debug("buy_next_item level {0}".format(args.level))
    i = 0
    while i < args.count:
        sleep(SLEEP_ON_LOAD)
        top = check_is_item_redy()
        if top:
            logging.debug("buy item #{0}".format(i))
            buy_next_item(top, args.level)
            i = i + 1

# ------------------------------------------------------------------------------------------------------------------------
# sent presents
# ------------------------------------------------------------------------------------------------------------------------
def is_last():
    p = find("previous.png").getCenter()
    c = JRobot().getPixelColor(p.x, p.y)
    crgb = (c.getRed(), c.getGreen(), c.getBlue())
    gris = (183, 123, 35)
    return crgb == gris


def send_present_to(person):
    sleep(SLEEP_ON_LOAD)
    click(person)

    sleep(SLEEP_ON_LOAD)
    if exists("present.png"):
        click("present.png")
        sleep(SLEEP_ON_LOAD)

        check = find("checked.png")
        click(check)
        present = capture(check.getX() + 50, check.getY() - 50, 20, 20)

        sleep(SLEEP_ON_LOAD)
        click(present)

        sleep(SLEEP_ON_LOAD)
        click("close.png")


def send_present_to_all_in_scrin(top):
    step = 75
    y = top.getY() - 25
    x = top.getX() + 6 * step + 10
    for i in range(0, 6):
        person = capture(x - i * step, y, 50, 50)
        send_present_to(person)


def sentpresents(args):
    sleep(SLEEP_ON_LOAD)
    top = find("users.png").getCenter()
    if not top:
        logging.info("Open list of users")
        return
    while True:
        send_present_to_all_in_scrin(top)
        if is_last():
            break
        click("previous.png")
        sleep(SLEEP_ON_LOAD)


# ------------------------------------------------------------------------------------------------------------------------
def get_parser():
    parser = argparse.ArgumentParser(description='Automation of the game `vk.civilwar`', epilog=(
        'Home page: <https://github.com/banadiga/vk.civilwar.sikuli/>\n'
        'Documentation pade: <https://github.com/banadiga/vk.civilwar.sikuli/blob/master/README.md>\n'
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
                                  type=int, default=1, choices=xrange(1, 6),
                                  help='level of item. Default is 0.')
    parser_buy_items.set_defaults(func=buyitems)

    parser.add_argument('--version', action='version', version='%(prog)s 2.2')

    parser.add_argument('-v', '--verbose',
                        action="store_const", dest="loglevel", const=logging.INFO,
                        help="increase output verbosity.")
    parser.add_argument('-d', '--debug',
                        action="store_const", dest="loglevel", const=logging.DEBUG,
                        default=logging.WARNING,
                        help="print lots of debugging statements.")
    return parser


# ------------------------------------------------------------------------------------------------------------------------
def main(args):
    logging.debug("Parser{0}".format(args))
    logging.info("Run command `{0}`".format(args.run))
    args.func(args)


args = get_parser().parse_args()
logging.basicConfig(level=args.loglevel)
if __name__ == '__main__':
    main(args)
