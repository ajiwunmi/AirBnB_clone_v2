from fabric import Connection
con = Connection.run('ubuntu@3.83.227.12')
def process_list(c, process=''):
    return c.run(f"ps aux | grep -i '{process}'", hide=True).stdout.strip()

process_list(con,"python" )