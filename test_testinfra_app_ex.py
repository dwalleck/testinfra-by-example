def test_postgres_checks(host):
    
    # Check that the package is installed and its version
    nginx = host.package("postgresql")
    assert nginx.is_installed
    assert nginx.version.startswith("9.5")

    # Verify the ngnix service is started
    # There is a `service` module, but it requires systemd to be
    # running, which it won't be inside a container. However, we can
    # run any arbitrary command and check its response
    output = host.check_output('service postgresql status')
    assert '9.5/main (port 5432): online' in output

    # Verify the socket is listening for HTTP traffic
    assert host.socket("unix:///var/run/postgresql/.s.PGSQL.5432").is_listening



def test_nginx_checks(host):
    # Check that the package is installed and its version
    nginx = host.package("nginx")
    assert nginx.is_installed
    assert nginx.version.startswith("1.10")

    # Verify the ngnix service is started
    # There is a `service` module, but it requires systemd to be
    # running, which it won't be inside a container. However, we can
    # run any arbitrary command and check its response
    output = host.check_output('service nginx status')
    assert 'nginx is running' in output

    # Verify worker procs are running
    master = host.process.get(user="root", comm="nginx")
    workers = host.process.filter(ppid=master.pid)
    assert len(workers) > 0

    # Verify the socket is listening for HTTP traffic
    assert host.socket("tcp://0.0.0.0:80").is_listening
    assert host.socket("tcp://:::80").is_listening