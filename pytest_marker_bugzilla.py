import bugzilla
import ConfigParser
import pytest


class BugzillaHooks(object):
    def __init__(self, config, bugzilla):
        self.config = config
        self.bugzilla = bugzilla

    def pytest_runtest_setup(self, item):
        
        if 'bugzilla' in item.keywords:
            marker = item.keywords['bugzilla']
            if len(marker.args) != 1:
                raise TypeError('Bugzilla marker must have exactly 1 argument')
        
            
        bug_id = item.keywords['bugzilla'].args[0]
    
        bug = self.bugzilla.getbugsimple(bug_id)
        status = str(bug).split(None, 2)[1]
        
        if status in ['NEW', 'ASSIGNED', 'ON_DEV']:
            pytest.skip("https://bugzilla.redhat.com/show_bug.cgi?id=%s" % bug_id)

"""        
    def pytest_report_teststatus(self, report):
        bug_id = getattr(report, "bug_id", None)
        status = getattr(report, "status", None)
        
        if bug_id is not None:
            #if report.failed:
            #    return "failed", "P", "PENDINGFIX"
            if status in ['NEW', 'ASSIGNED', 'ON_DEV']:
                pytest.skip("%s" % bug_id)
                #return "skipped", "S", "SKIPPED_BUG"

"""
def pytest_addoption(parser):
    """
    Add a options section to py.test --help for bugzilla integration.
    Parse configuration file, bugzilla.cfg and / or the command line options
    passed.
    """
    
    config = ConfigParser.ConfigParser()
    config.read('bugzilla.cfg')
    
    group = parser.getgroup('Bugzilla integration')
    group.addoption('--bugzilla', 
                    action='store_true', 
                    default=False,
                    dest='bugzilla',
                    help='Enable Bugzilla support.')
    group.addoption('--bugzilla-url',
                    action='store',
                    dest='bugzilla_url',
                    default=config.get('DEFAULT', 'bugzilla_url'),
                    metavar='url',
                    help='Overrides the xmlrpc url for bugzilla found in bugzilla.cfg.')
    group.addoption('--bugzilla-user',
                    action='store',
                    dest='bugzilla_username',
                    default=config.get('DEFAULT', 'bugzilla_username'),
                    metavar='username',
                    help='Overrides the bugzilla username in bugzilla.cfg.')
    group.addoption('--bugzilla-password',
                    action='store',
                    dest='bugzilla_password',
                    default=config.get('DEFAULT', 'bugzilla_password'),
                    metavar='password',
                    help='Overrides the bugzilla password in bugzilla.cfg.')
    
def pytest_configure(config):
    """
    If bugzilla is neabled, setup a session
    with bugzilla_url.
    """
    if config.getvalue("bugzilla"):
        url = config.getvalue('bugzilla_url')
        user = config.getvalue('bugzilla_username')
        password = config.getvalue('bugzilla_password')
        
        bz = bugzilla.Bugzilla(url=url)
        bz.login(user,password)
        
        my = BugzillaHooks(config, bz)
        ok = config.pluginmanager.register(my, "bugzilla_helper")
        assert ok
