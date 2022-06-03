# Usage:
#
# timetrack.py add <project>:<task> <start>:<end>
# timetrack.py view <day>
# timetrack.py view <id>
# timetrack.py edit <id> <start>:<end>
# timetrack.py delete <id>
# Projects or tasks that have not been defined will be created
#
# Start and end times should be to the minute, in 24hr time,
# consist of 4 digits and no separators
# e.g. 1100 2330 0821 1215
#
# Days should be yyyy-mm-dd

import sys

arg_rules = {
        1: ['add', 'a', 'delete', 'd', 'edit', 'view', 'v']
        }

def validate_args(args):
    message = ''
    valid = True
    for i in range(1, len(args)):
        if args[i] not in arg_rules[i]:
            return False, 'Argument {} is not valid'.format(i)
    return True, ''

def main():
    args_are_valid, message = validate_args(sys.argv)
    if args_are_valid:
        pass
    else:
        print(message)

if __name__ == '__main__':
    main()
