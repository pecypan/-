received = 'ack'
for i in range(5):
    if received == 'ack':
        print('----------------retry--------------------')
        # self.dmc.clearBuffer(self.devName)
        # time.sleep(1)
        # received = self.send_and_recv(cmd, timeout)
        continue
    elif received != 'ack':
        print('write successful')
        break
    print('return write message error!!!!! none ack!!!')
