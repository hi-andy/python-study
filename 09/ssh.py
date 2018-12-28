import paramiko

ssh = paramiko.SSHClient()

# Allow to connect host that name not in know_hosts file
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

private_key = paramiko.RSAKey.from_private_key_file('/home/user/.ssh/id_rsa')

# ssh.connect(hostname='202.182.116.80', port=22, username='root', pkey=private_key)
ssh.connect(hostname='202.182.116.80', port=22, username='root', password='_gC8zgx)ptUw-MF%')

stdin, stdout, stderr = ssh.exec_command('df -lh')

result = stdout.read()

print(result.decode())

ssh.close()


