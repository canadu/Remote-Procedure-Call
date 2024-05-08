const { request } = require('http');
const net = require('net');
const port = '50080';
const host = '127.0.0.1';

const req = {
    "method": "",
    "params": "",
    "id": ""
};

function readUserInput(question) {

    process.stdin.resume();
    process.stdin.setEncoding('utf8');

    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    return new Promise((resolve, reject) => {
        readline.question(question, (answer) => {
            resolve(answer);
            readline.close();
        });
    });

}

(async function main() {

    method = await readUserInput('Input Method --> ');
    params = await readUserInput('Input params --> ');
    id = await readUserInput('Input Id --> ');

    req.method = method == ""? req.method : method;
    req.params = params == ""? req.params : params;
    req.id = id == ""? req.id : id;

    req.method = method;    
    req.params = params;
    req.id = id;

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
        console.log(`${client.remoteAddress}:${client.remotePort} Connected`);
        const response = JSON.parse(data);
        console.log(`Received data from server ====================`);
        console.log(`id: ${response['id']}`);
        console.log(`results: ${response['results']}`);
        console.log(`==============================================`);
        client.destroy();
    });

    //エラー発生時のコールバック
    client.on('error', (err) => {
        console.log(`${client.remoteAddress}:${client.remotePort} Error:${err}`);
    });

    //接続が切れたときのコールバック
    client.on('close', () => {
        console.log(`${client.remoteAddress}:${client.remotePort} Connection closed`);
    })

})();

