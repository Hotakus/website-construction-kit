import os
import subprocess as sp
from colorama import Fore
import json5

config: dict = {}
missing_packs = []
already_packs = []


def _base_grep(cmd=[]):
    builtin_packs = config['check_packs']['builtin']
    must_packs = config['check_packs']['must']
    total_packs = builtin_packs + must_packs

    builtin_prompt = " (Program will automatically install it by builtin packs. Don't mind it.)"

    # packs must be installed
    for pack in total_packs:
        if pack == "":
            continue

        std = sp.Popen(cmd, stdout=sp.PIPE)
        try:
            sp.check_output(('grep', pack), stdin=std.stdout).decode('utf-8')
        except sp.CalledProcessError:
            pib = (pack in builtin_packs)
            ex_prompt = "" if not pib else builtin_prompt
            already_packs.append(pack) if pib else missing_packs.append(pack)
            print(
                ((Fore.YELLOW + "[W]") if pib else (Fore.RED + "[E]")) +
                (" '%s' is missing" % pack) +
                ex_prompt
            )
        else:
            print(Fore.CYAN + "[I] '%s' is " % pack + Fore.GREEN + "OK")


def do_as_ubuntu():
    cmd = ['dpkg', '--list']
    res = _base_grep(cmd)


def check_packs(sys=""):
    match sys:
        case 'ubuntu':
            do_as_ubuntu()


def main():
    check_path = "/proc/version_signature"
    ve_res = os.path.exists(check_path)
    if not ve_res:
        check_path = '/proc/version'

    sys_type = sp.Popen(['cat', check_path], stdout=sp.PIPE)
    stdout, stderr = sys_type.communicate()
    what_system = stdout.decode('utf-8').split(' ')[0].lower()

    # check packs
    global config
    with open("../config.json", "r") as f:
        config = f.read()
    config = json5.loads(config)
    check_packs(what_system)

    for i in config['php_options']['compile_configs']:
        print("%s" % i, sep=' ')


if __name__ == "__main__":
    main()
