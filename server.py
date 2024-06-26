import socket
import os
import json
import math

IPADDR = "127.0.0.1"
PORT = 50080

class Func:

    # floor(double x): 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
    # nroot(int n, int x): 方程式 rn = x における、r の値を計算する。
    # reverse(string s): 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
    # validAnagram(string str1, string str2): 2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
    # sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。
 
    def floor(x):
        r = math.floor(x[0])
        return r

    def nroot(params):
        x = params[0]
        n  = params[1]
        r = x ** (1/n)
        return r

    def reverse(s):
        r = s[0][::-1]
        return r
    
    def validAnagram(params):
        s1 = params[0]
        s2 = params[1]
        print(s1)
        print(s2)
        sorted_str1 = ''.join(sorted(set(s1.lower())))
        sorted_str2 = ''.join(sorted(set(s2.lower())))
        return sorted_str1 == sorted_str2

    def sort(params):
        r = sorted(params[0])
        return r

def changeType(method, params):

    params = params.split(',')

    if method == 'floor':
        return [float(x) for x in params]
    elif method == 'nroot':
        return [int(x) for x in params]
    elif method == 'reverse':
        return [str(x) for x in params]
    elif method == 'validAnagram' or method == 'sort':
        return list(params)
    
def main():

    FuncHashMap = {
        "floor": Func.floor,
        "nroot": Func.nroot,
        "reverse": Func.reverse,
        "validAnagram": Func.validAnagram,
        "sort": Func.sort
    }

    # IPv4
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = IPADDR

    try:
        os.unlink(server_address)
    except FileNotFoundError:
        pass
    
    print(f'接続開始します。{server_address}')

    # バインド
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

                #クライアントからのデータを確認
                data = connection.recv(1024)
                from_client = data.decode()
                
                #jsonを取得
                client_json = json.loads(from_client)

                # パラメーターを取得
                method = str(client_json['method'])
                params = client_json['params']
                id = client_json['id']

                if method in FuncHashMap:
                    
                    param = changeType(method, params)

                    # メソッドを実行
                    result = FuncHashMap[method](param)
                    
                    data = {
                        'results': result,
                        'id': id,
                    }

                else:
                    # エラー
                    data = {
                        'results': 'そんなメソッドありません。',
                        'id': id,
                    }

                json_data = json.dumps(data).encode('utf-8')
        
                # 戻り値をクライアントに返す
                connection.send(json_data)

                break
            
            except Exception as e:
                print('エラー > ' + str(e))
                break
    except Exception as e:
        print(e)
    finally:
        connection.close()
        sock.close()

main()