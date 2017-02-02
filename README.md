# unsplash-python
A unofficial Python client for the [Unsplash API](https://unsplash.com/developers).


## Usage
### Creating an instance
To create an instance, simply provide an _Object_ with your `application_id`, `secret` and `callback_url`.

```python
from unsplash import Unsplash

unsplash = Unsplash({
    'application_id' : '{APP_ID}',
    'secret'         : '{APP_SECRET}',
    'callback_url'   : '{CALLBACK_URL}'
})
```

===

### User


---

## Instance Methods
- [Authorization](https://github.com/unsplash/unsplash-js#authorization)
- [Current User](https://github.com/unsplash/unsplash-js#current-user)
- [Users](https://github.com/unsplash/unsplash-js#users)
- [Photos](https://github.com/unsplash/unsplash-js#photos)
- [Categories](https://github.com/unsplash/unsplash-js#categories)
- [Collections](https://github.com/unsplash/unsplash-js#collections)
- [Search](https://github.com/unsplash/unsplash-js#searchallkeyword-page)
- [Stats](https://github.com/unsplash/unsplash-js#stats)

<div id="authorization" />

### auth.get_authentication_url(scopes)
Build an OAuth url with requested scopes.

__Arguments__

| Argument | Type | Opt/Required | Default |
|---|---|---|---|
|__`scopes`__|_Array<string>_|Optional| `['public']` |

__Example__
```python
authentication_url = unsplash.auth().get_authentication_url([
    'public',
    'read_user',
    'write_user',
    'read_photos',
    'write_photos'
])
```
---
