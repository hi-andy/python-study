import paramiko


transport = paramiko.Transport(('hostname', 22))
transport.connect(username='name', password='pass')

sftp = paramiko.SFTPClient.from_transport(transport)

sftp.put('/tmp/location.py', '/tmp/test.py')
sftp.get('remote_path', 'local_path')


transport.close()