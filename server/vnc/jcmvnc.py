#import memcache
#import simplejson
import imp

class TokenMemc(object):
    def __init__(self, src):
        self._server = src

    def lookup(self, token):
        #client = memcache.Client([self._server], debug=0)
        #stuff = client.get(token)
        #combo = simplejson.loads(stuff)
        #pair = "unix_socket:/run/jcm/qemu/vnc/tmp.vnc"
        #os.system("pwd")
        sh = "../../../server/vnc/api.py"
        sh = imp.load_source(sh,sh)
        return sh.soket(token)