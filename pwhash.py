# A simple module to make iPython hashes without needing to have iPython available
import hashlib
import random

salt_len = 12

def passwd(passphrase=None, algorithm='sha1'):
    h.hashlib.new(algorithm)
    salt = ('%0' + str(salt_len) + 'x') % random.getrandbits(4 * salt_len)
    h.update(passphrase + salt)
    return ':'.join(algorithm, salt, h.hexdigest())
