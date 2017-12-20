
"""
The `host` parameter for each of these functions is something that
is injected into each test function by the testinfra pytest plugin.
"""


def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644


def test_package_checks(host):
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.10")


def test_oc_tool_on_path(host):
    assert host.exists("oc")


def test_exec_command_and_verify_output(host):
    cmd = host.run("ls -la")
    
    # Check outcome directly
    assert cmd.rc == 0
    assert cmd.stderr == ''

    # Run and check specific status codes in one step
    host.run_expect([0], "hostname")
    
    # Or if you just want to implicitly check for an exit code of 0 or 1
    host.run_test("hostname")

    # Or execute, check for a successful exit status, and get output in one step
    output = host.check_output("ls -la")
    assert 'requirements.txt' in output


def test_system_info(host):
    assert host.system_info.type == 'linux'
    assert host.system_info.distribution == 'ubuntu'
    assert host.system_info.release == '16.04'
    assert host.system_info.codename == 'xenial'


def test_socket_statuses(host):
    assert not host.socket("unix:///var/run/docker.sock").is_listening


def test_service_statuses(host):
    host.service('ssh').is_enabled
    host.service('ssh').is_running


def test_file_checks(host):
    # (TODO): implement
    pass


def test_file_checks(host):
    # (TODO): implement
    pass


def test_process_checks(host):
    # (TODO): implement
    pass


def test_socket_checks(host):
    # (TODO): implement
    pass