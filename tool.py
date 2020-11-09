from check import is_key_exists, is_valid_environment, is_valid_return_codes

def surround_exit(func, *args, exitcode=2):
    try:
        func(*args)
    except ValueError as error:
        print(error)
        exit(exitcode)

def clean_options(options):
    configuration = vars(options)
    surround_exit(is_key_exists, configuration, 'configurationfile', '-c configurationfile')
    surround_exit(is_valid_return_codes, options.returncodes)
    options.returncodes = options.returncodes.split(',')
    if options.environment:
        surround_exit(is_valid_environment, options.environment)
        environment = options.environment.split(',')
        options.environment = environment
    file = options.configurationfile
    show = options.show
    configuration['configurationfile'] = None
    configuration['show'] = None
    configuration['standalone'] = None
    keys = list(configuration.keys())
    for e in keys:
        if not configuration[e]:
            del configuration[e]
    return file, show, configuration