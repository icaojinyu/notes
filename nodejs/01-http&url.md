## http和url模块

#### http模块
```js
let http = require('http');

let port = 3000, host = '127.0.0.1';
let app = http.createServer((req, res) => {
  // 指定状态码、文件类型、字符集
  res.writeHead(200, {'content-type': 'text/html;charset=utf-8'});
  res.write('hello nodejs');
  res.end(`我买了一个iPhone${1+2+3}s`);
});

app.listen(port, host, () => {
  console.log('ok');
}); 
```

#### url模块
```js
let url  = require('url');

// 可以通过req.url获取url地址
let res = url.parse('https://www.google.com?name=cjy&age=17',true);
console.log(res);
/*
Url {
  protocol: 'https:',
  slashes: true,
  auth: null,
  host: 'www.google.com',
  port: null,
  hostname: 'www.google.com',
  hash: null,
  search: '?name=cjy&age=17',
  query: [Object: null prototype] { name: 'cjy', age: '17' },
  pathname: '/',
  path: '/?name=cjy&age=17',
  href: 'https://www.google.com/?name=cjy&age=17'
}
*/
```