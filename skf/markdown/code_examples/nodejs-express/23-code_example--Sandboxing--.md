# Iframe Sandboxing

- [General](#general)
- [Example](#example)
- [Considerations](#considerations)

## General
Sandboxing applies a set of restrictions to the iframes in order to tighten security. It can be declared as follows:
```html
<iframe sandbox="value">
```

Full list of permitted values is available in [MDN iframe documentation](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe#attr-sandbox).

## Example
To enable full sandbox mode please use the following code:
```html
<iframe sandbox>...</iframe>
``` 

Desired restriction can be lifted as shown below: 
```html
<iframe sandbox="allow-forms allow-scripts">...</iframe>
```

## Considerations
TBA
