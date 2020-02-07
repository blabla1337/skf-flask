# Directory Path traversal

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example
First, we want to filter the filenames for expected values. For this example the filenames should consist of only alphanumeric characters, which we validate with the following regex - `/^[a-zA-Z0-9]+$/`.
```js
const isValidPath = path => {
    const filenamesRegex = /^[a-zA-Z0-9]+$/;
    return filenamesRegex.test(path);
};
```

Then we whitelist the path to only the allowed locations using the [path](https://nodejs.org/api/path.html) library. `dirWhitelist` is an array of directory pathnames (such as `/foo/bar/baz`) the application is allowed to load resources from:
```js
const isAllowedLocation = path =>
    dirWhitelist.includes(path.dirname(path));
```

Together the methods shown above can be used as follows:
```js
app.get('/read-file', (req, res) => {
    const filePath = req.query.filename;
    if(isValidPath(filePath) && isAllowedLocation(filePath)) {
        // serve request
    } else {
        // return error
    }
});
```

## Considerations
TBA
