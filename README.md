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

### current_user.update_profile(options)
Update the current user’s profile.

__Arguments__

| Argument | Type | Opt/Required |Notes|
|---|---|---|---|
|__`options`__|_Object_|Required|Object with the following optional keys: `username`, `first_name`, `last_name`, `email`, `url`, `location`, `bio`, `instagram_username`|

__Example__
```python
unsplash.current_user.update_profile({
    'username'           : 'john_doe',
    'first_name'         : 'John',
    'last_name'          : 'Doe',
    'email'              : 'john.doe@unkn.own',
    'url'                : 'https://www.superbox.one',
    'location'           : 'Unknown',
    'bio'                : '',
    'instagram_username' : 'john_doe'
})
```
---

<div id="users" />

### users.profile(username)
Retrieve public details on a given user.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`username`__|_string_|Required|

__Example__
```python
users_profile = unsplash.users.profile(
    username = 'naoufal'
)
```
---

### users.photos(username, page, per_page, order_by)
Get a list of photos uploaded by a user.

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`username`__|_string_|Required||
|__`page`__|_number_|Optional||
|__`per_page`__|_number_|Optional||
|__`order_by`__|_string_|Optional|`latest`, `popular` or `oldest`|

__Example__
```python
users_photos = unsplash.users.photos(
    username = 'naoufal',
    order_by = 'popular'
)
```
---

### users.likes(username, page, per_page, order_by)
Get a list of photos liked by a user.

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`username`__|_string_|Required||
|__`page`__|_number_|Optional||
|__`per_page`__|_number_|Optional||
|__`order_by`__|_string_|Optional|`latest`, `popular` or `oldest`|

__Example__
```python
unsplash.users.likes(
    username = 'naoufal',
    page     = 2,
    per_page = 15,
    order_by = 'popular'
)
```
---

### users.collections(username, page, per_page)
Get a list of collections created by the user.

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`username`__|_string_|Required||
|__`page`__|_number_|Optional||
|__`per_page`__|_number_|Optional||

__Example__
```python
unsplash.users.collections(
    username = 'naoufal',
    page     = 2,
    per_page = 15
)
```
---
