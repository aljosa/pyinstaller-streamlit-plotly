import os
import sys
from streamlit import cli as stcli

if __name__ == '__main__':

    launchdir = os.path.dirname(sys.argv[0])

    if launchdir == '':
        launchdir = '.'

    print('Launch dir ', launchdir)
    sys.argv = ["streamlit", "run", f"{launchdir}/app.py", "--server.port=10000", "--server.headless=true", "--global.developmentMode=false"]
    sys.exit(stcli.main())
