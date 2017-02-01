from skf import settings

def security_headers():
    """This decorator passes multiple security headers"""
    if settings.FLASK_SERVER_NAME == 'localhost:8888':
        return {'X-Frame-Options': 'deny',
                'X-XSS-Protection': '1',
                'X-Content-Type-Options': 'nosniff',
                'Cache-Control': 'no-store, no-cache',
                'Server': 'Security Knowledge Framework API'}
    else:
        return {'X-Frame-Options': 'deny',
                'X-XSS-Protection': '1',
                'X-Content-Type-Options': 'nosniff',
                'Cache-Control': 'no-store, no-cache',
                'Strict-Transport-Security': 'max-age=16070400; includeSubDomains',
                'Server': 'Security Knowledge Framework API'}

def log(message, value, threat):
    """Create log file and write events triggerd by the user
    The variables: message can be everything, value contains FAIL or SUCCESS and threat LOW MEDIUM HIGH"""
    now = datetime.datetime.now()
    dateLog = now.strftime("%Y-%m")
    dateTime = now.strftime("%Y-%m-%d %H:%M")
    ip = request.remote_addr
    try:
        file = open('logs/'+dateLog+'.txt', 'a+')
    except IOError:
        # If not exists, create the file
        file = open('logs/'+dateLog+'.txt', 'w+')
    file.write(dateTime +' '+ message +' ' + ' ' + value + ' ' + threat + ' ' +ip + "\r\n")
    file.close()


def valAlphaNum(value, countLevel):
    match = re.findall(r"[a-zA-Z0-9_.-]", value)
    if match:
        log("User supplied not an a-zA-Z0-9 value", "FAIL", "MEDIUM")
        countAttempts(countLevel)
        abort(406)
        return False
    else:
        return True


def valNum(value, countLevel):
    match = re.findall(r'[a-zA-Z_]', str(value))
    if match:
        log("malicious input found", "FAIL", "MEDIUM")
        countAttempts(countLevel)
        abort(406)
        return False
    else:
        return True
