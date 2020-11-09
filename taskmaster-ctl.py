from optparse import OptionParser
from manager import manage_configuration_file
import sys



parser = OptionParser()

parser.add_option('--create', dest='create', action='store_true', default=False)


(options, args) = parser.parse_args(sys.argv[0:2])

if options.create:
    manage_configuration_file(standalone='create')