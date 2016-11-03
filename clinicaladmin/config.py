try:
    import ConfigParser as cp
except:
    from six.moves import configparser as cp 

import os
import glob

clinical_adminrc=glob.glob(os.path.expanduser('~/.clinical_adminrc'))[0]
config = cp.SafeConfigParser()
config.readfp(open(clinical_adminrc))

DEMULTIPLEX_DATABASE_URI = config.get('admin data', 'SQLALCHEMY_DATABASE_URI').rstrip()


