import sys
from setup import HackerModeInstaller

help_msg = """
\033[1mUSAGE:\033[0m
  python3 -B HackerMode/ <command>

\033[1mCOMMANDS:\033[0m
 update   Update HackerMode                \033[0;92m(Update).\033[0m
 install  Install HackerMode               \033[0;92m(Setup Tool Files).\033[0m
 check    Check all Modules And Packages   \033[0;92m(Check For Newer Version Of Modules and Packages).\033[0m
 delete   Delete HackerMode                \033[0;92m(Delete HackerMode, Warning: This Option Cannot Be Undone).\033[0m
""".strip()

if __name__ == "__main__":
    HackerMode = HackerModeInstaller()
    if len(sys.argv) > 1:
        try:
            HackerMode.__getattribute__(sys.argv[1])()
        except AttributeError:
            print(help_msg)
        except Exception as e:
            print(e)
    else:
        print(help_msg)
