import requests
import json
import collections
# disable insecure warnings
requests.packages.urllib3.disable_warnings()


PROXY = demisto.params().get('proxy')
INSECURE = demisto.params().get('insecure')
BASE_URL = demisto.params().get('url')
API_KEY = demisto.params().get('apikey')
URL_SUFFIX = 'yoda'
if not demisto.params().get('proxy', False):
    del os.environ['HTTP_PROXY']
    del os.environ['HTTPS_PROXY']
    del os.environ['http_proxy']
    del os.environ['https_proxy']


'''HELPER FUNCTIONS'''
def http_request(method, URL_SUFFIX, json=None):
    if method == 'GET':
        headers = {}
    elif method == 'POST':
        if not API_KEY:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        else:
            headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'X-FunTranslations-Api-Secret': API_KEY
            }
    r = requests.request(
        method,
        BASE_URL + URL_SUFFIX,
        data=json,
        headers=headers,
        verify=INSECURE
    )
    if r.status_code != 200:
        return_error('Error in API call [%d] - %s' % (r.status_code, r.reason))
    return r.json()


# Allows nested keys to be accesible
def makehash():
    return collections.defaultdict(makehash)


'''MAIN FUNCTIONS'''
def translate(text):
    query = { 'text': text }
    search = json.dumps(query)
    r = http_request('POST', URL_SUFFIX, search)
    return r


def translate_command():
    text = demisto.args().get('text')
    contxt = makehash()
    human_readable = makehash()
    res = translate(text)
    contents = res['contents']
    if 'translated' in contents:
        human_readable['Original'] = text
        human_readable['Translation'] = contents['translated']
        contxt['Original'] = text
        contxt['Translation'] = contents['translated']
    ec = {'YodaSpeak.TheForce(val.Original && val.Original == obj.Original)': contxt}
    demisto.results({
        'Type': entryTypes['note'],
        'ContentsFormat': formats['markdown'],
        'Contents': res,
        'HumanReadable': tableToMarkdown('Yoda Says...', human_readable),
        'EntryContext': ec
    })


''' EXECUTION '''
LOG('command is %s' % (demisto.command(), ))
try:
    if demisto.command() == 'yoda-speak-translate':
        translate_command()
    elif demisto.command() == 'test-module':
        text = 'I have the high ground!'
        translate(text)
        demisto.results('ok')
except getopt.GetoptError as e:
    demisto.debug('The Senate? I am the Senate!')
    LOG(e.message)
    LOG.print_log()
    return_error(e.message)
