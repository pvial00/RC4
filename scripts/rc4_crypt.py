from rc4 import RC4
import sys, select, getpass, time, hashlib

if select.select([sys.stdin,],[],[],0.0)[0]:
    data = sys.stdin.read()
else:
    sys.exit(1)

try:
    key = sys.argv[1]
except IndexError as ier:
    key = getpass.getpass("Enter key: ")
key = hashlib.pbkdf2_hmac('md5', key, ')sVg&efG2X55*@1Di`', 100000)

start = time.time()

sys.stdout.write(RC4(key).crypt(data))

end = time.time() - start
bps = len(data) / end
sys.stderr.write("Completed in "+str(end)+" seconds\n")
sys.stderr.write(str(bps)+" bytes per second.\n")
