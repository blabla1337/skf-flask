# Session timeout 

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
TBA

## Example:
```
app.use(express.session({
             secret : 'your_cookie_secret',
             cookie:{_expires : (10 * 60 * 1000)}, // time im ms, this is 10 minutes
             })
        ); 
     
```

## Considerations
TBA
