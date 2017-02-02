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
- [Authorization](https://github.com/michael-hacker/unsplash-python#authorization)
- [Current User](https://github.com/michael-hacker/unsplash-python#current-user)
- [Users](https://github.com/michael-hacker/unsplash-python#users)
- [Photos](https://github.com/michael-hacker/unsplash-python#photos)
- [Categories](https://github.com/michael-hacker/unsplash-python#categories)
- [Collections](https://github.com/michael-hacker/unsplash-python#collections)
- [Search](https://github.com/michael-hacker/unsplash-python#searchallkeyword-page)
- [Stats](https://github.com/michael-hacker/unsplash-python#stats)

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

### auth.user_authentication(code)
Retrieve a user's access token.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`code`__|_string_|Required|

__Example__
```python
access_token = unsplash.auth.user_authentication(code = '{OAUTH_CODE}')
```
---

<div id="current-user" />

### current_user.profile()
Get the user’s profile.

__Arguments__

_N/A_

__Example__
```python
current_user_profile = unsplash.current_user.profile()
```
---
