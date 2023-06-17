import os
import subprocess as sp
from colorama import Fore
import json5

config: dict = {}
missing_packs = []
already_packs = []

check_path = ["/etc/redhat-release"]

warning_prompt = '[W]'
error_prompt = '[E]'
info_prompt = '[I]'


must_packs = []
def _base_grep(cmd=[]):
    builtin_packs = config['check_packs']['builtin']['general']
    general_packs = config['check_packs']['must']['general']
    total_packs = general_packs + builtin_packs + must_packs

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
                ((Fore.YELLOW + warning_prompt) if pib else (Fore.RED + error_prompt)) +
                (" '%s' is missing" % pack) +
                ex_prompt
            )
        else:
            print(Fore.CYAN + info_prompt + " '%s' is " % pack + Fore.GREEN + "OK")


def do_as_debian():
    cmd = ['dpkg', '--list']
    _base_grep(cmd)


def do_as_redhat():
    cmd = ['rpm', '-qa']
    _base_grep(cmd)


def check_os(sign_file=""):
    global check_path
    if check_path[0] == sign_file:
        return "RedHat"
    elif check_path[1] == sign_file:
        return "Debian"
    return None


def check_packs(sys=""):
    global must_packs
    match sys:
        case 'Debian':
            must_packs = ['check_packs']['must']['debians']
            do_as_debian()
        case 'RedHat':
            must_packs = ['check_packs']['must']['redhats']
            do_as_redhat()


def main():
    global check_path
    what_system = ""
    for p in check_path:
        ve_res = os.path.exists(p)
        if ve_res is True:
            what_system = check_os(p)
            print(info_prompt + " Current os is series of " + what_system)
            break

    # sys_type = sp.Popen(['cat', check_path], stdout=sp.PIPE)
    # stdout, stderr = sys_type.communicate()
    # what_system = stdout.decode('utf-8').split(' ')[0].lower()

    # check packs
    global config
    with open("../config.json", "r") as f:
        config = f.read()
    config = json5.loads(config)
    check_packs(what_system)

    for i in config['php_options']['compile_configs']:
        print("%s" % i, end=' ')

    print()


if __name__ == "__main__":
    main()
