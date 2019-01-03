from argparse import ArgumentParser

'''
start instance with command args
'''

parser = ArgumentParser()

parser.add_argument("-n", "--node", dest="filename",
                    help="write report to FILE", metavar="FILE")