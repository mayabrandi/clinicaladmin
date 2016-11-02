import ConfigParser
import os
import glob

clinical_adminrc=glob.glob(os.path.expanduser('~/.clinical_adminrc'))[0]
config = ConfigParser.SafeConfigParser()
config.readfp(open(clinical_adminrc))

DEMULTIPLEX_DATABASE_URI = config.get('admin data', 'SQLALCHEMY_DATABASE_URI').rstrip()


