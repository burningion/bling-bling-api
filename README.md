# Bling Bling API

An Example Flask API to add GIF *Bling* to Your Images

There's an example base64 encoded image to get you started:

```bash
$ curl -X POST -H "Content-Type: application/json" -d @example-bling.json http://localhost:5000/place-bling
```

Set the number of "spots" for "bling" in your request JSON, and get back out something like this:

![Output Bling Image](https://github.com/burningion/bling-bling-api/raw/master/images/test.gif)
