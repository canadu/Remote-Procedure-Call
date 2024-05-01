import socket
import os
import json

def floor(*param):
    data = {
        'results': 19,
        'id': 1,
    }
    json_data = json.dumps(data).encode('utf-8')
    return json_data


#モードで切り替える 0=Unixドメインソケット 1=IPv4インターネットプロトコル
MODE = 1

IPADDR = "127.0.0.1"
PORT = 50080

if MODE == 0:
    #Unixドメインソケット
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    # ソケットファイルのファイル名を指定
    server_address = '/tmp/app_socket_file'
else:
    # IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = IPADDR
try:
    os.unlink(server_address)
except FileNotFoundError:
    pass

print(f'接続開始します。{server_address}')

# バインド
if MODE == 0:
    sock.bind(server_address)
else:
    # 同じポートを共有して使用できるようになります。
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((server_address, PORT))

# 接続を待ち受け
sock.listen(1)

try:
    # 接続に対し、新しいソケットを作成
    connection, client_address = sock.accept()
    while True:
        try:
            # クライアントからのデータを確認
            data = connection.recv(1024)
            from_client = data.decode()
            dec = json.loads(from_client)

            if str(dec['method']) == 'floor':
                result = floor(dec['params'])
                connection.send(result)
                break
            
            # if from_client == 'exit' or from_client == 'bye':
            #     print('接続を切ります')
            #     break
            # else:
            #     print(f"受信したメッセージ >>> {from_client}")
            #     to_client = fake.sentence()
            #     connection.sendall(to_client.encode("UTF-8"))

        except Exception as e:
            print('エラー > ' + str(e))
            break
except Exception as e:
    print(e)
finally:
    connection.close()
    sock.close()


