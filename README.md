# Remote-Procedure-Call
## Recursionのソケット通信の課題
<p>サーバー側はPythonで実装し、クライアント側はNode.jsで実装</p>
<p>サーバは、以下の関数を RPC としてクライアントに提供します。</p>
<ul>
  <li>
  floor(double x): 10 進数 x を最も近い整数に切り捨て、その結果を整数で返す。
</li>
<li>
  nroot(int n, int x): 方程式 rn = x における、r の値を計算する。
</li>
<li>  
  reverse(string s): 文字列 s を入力として受け取り、入力文字列の逆である新しい文字列を返す。
</li>
<li>  
  validAnagram(string str1, string str2): 2 つの文字列を入力として受け取り，2 つの入力文字列が互いにアナグラムであるかどうかを示すブール値を返す。
</li>
<li>
  sort(string[] strArr): 文字列の配列を入力として受け取り、その配列をソートして、ソート後の文字列の配列を返す。
</li>
</ul>





