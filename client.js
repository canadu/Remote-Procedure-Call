const net = require('net');
const port = '50080';
const host = '127.0.0.1';

const req = {
   "method": "floor", 
   "params": [42, 23], 
   "id": 1
};

//サーバーに接続
client = connect();
client.setEncoding('utf-8');
client.write(JSON.stringify(req));

//接続
function connect() {
    const client = new net.Socket();
    client.connect(port, host);
    return client;
}

//サーバーからのデータを受信したときのコールバック
client.on('data', (data) => {
    console.log(`Received data from server: ${data}`);
});

//エラー発生時のコールバック
client.on('error', (err) => {
    console.log(`Error:${err}`);
});

//接続が切れたときのコールバック
client.on('close', () => {
    console.log('Connection closed');
})