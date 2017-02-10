[![Latest Version](https://pypip.in/version/unsplash-python/badge.svg)](https://pypi.python.org/pypi/unsplash-python/)[![Build Status](https://travis-ci.org/michael-hacker/unsplash-python.svg?branch=master)](https://travis-ci.org/michael-hacker/unsplash-python)

# unsplash-python
A unofficial Python client for the [Unsplash API](https://unsplash.com/developers).

## Installation

    $ pip install unsplash-python


## Dependencies

    $ pip install requests

## Usage
### Creating an instance
To create an instance, simply provide an _Object_ with your `application_id`, `secret` and `callback_url`.

```python
import unsplash

unsplash = Unsplash({
    'application_id': '{application_id}',
    'secret': '{secret}',
    'callback_url': '{callback_url}'
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
- [Collections](https://github.com/michael-hacker/unsplash-python#collections)
- [Search](https://github.com/michael-hacker/unsplash-python#searchallkeyword-page)
- [Stats](https://github.com/michael-hacker/unsplash-python#stats)

<div id="authorization" />

### auth().get_authentication_url(scopes)
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

### auth().user_authentication(code)
Retrieve a user's access token.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`code`__|_string_|Required|

__Example__
```python
access_token = unsplash.auth().user_authentication(code = '{OAUTH_CODE}')
```
---

<div id="current-user" />

### current_user().profile()
Get the user’s profile.

__Arguments__

_N/A_

__Example__
```python
current_user_profile = unsplash.current_user().profile()
```
---

### current_user().update_profile(options)
Update the current user’s profile.

__Arguments__

| Argument | Type | Opt/Required |Notes|
|---|---|---|---|
|__`options`__|_Object_|Required|Object with the following optional keys: `username`, `first_name`, `last_name`, `email`, `url`, `location`, `bio`, `instagram_username`|

__Example__
```python
unsplash.current_user().update_profile({
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

### users().profile(username)
Retrieve public details on a given user.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`username`__|_string_|Required|

__Example__
```python
unsplash.users().profile(
    username='michael_hacker'
)
```
---

### users().photos(username, page, per_page, order_by)
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
unsplash.users().photos(
    username='naoufal',
    order_by = 'popular'
)
```
---

### users().likes(username, page, per_page, order_by)
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
users_likes = unsplash.users().likes(
    username = 'naoufal',
    page     = 2,
    per_page = 15,
    order_by = 'popular'
)
```
---

### users().collections(username, page, per_page)
Get a list of collections created by the user.

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`username`__|_string_|Required||
|__`page`__|_number_|Optional||
|__`per_page`__|_number_|Optional||

__Example__
```python
users_collections = unsplash.users().collections(
    username = 'naoufal',
    page     = 2,
    per_page = 15
)
```
---

<div id="photos" />

### photos().list_photos(page, per_page, order_by)
Get a single page from the list of all photos.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|
|__`order_by`__|_string_|Optional|`latest`, `popular` or `oldest`|

__Example__
```python
unsplash.photos().list_photos(
    page=2,
    per_page=15,
    order_by='popular'
)
```
---

### photos().list_curated_photos(page, per_page, order_by)
Get a single page from the list of the curated photos.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|
|__`order_by`__|_string_|Optional|`latest`, `popular` or `oldest`|

__Example__
```python
unsplash.photos().list_curated_photos(
    page=2,
    per_page=15,
    order_by='popular'
)
```
---

### photos().search_photos(query, category, page, per_page)
Get a single page from a photo search. Optionally limit your search to a set of categories by supplying the category ID’s.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`query`__|_string_|Optional|
|__`category`__|_Array<number>_|Optional|
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|

__Example__
```python
unsplash.photos().search_photos(
    query='lisboa',
    category=[11, 88],
    page=1
    per_page=15
)
```
---

### photos().get_photo(id, width, height, rectangle)
Retrieve a single photo.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`id`__|_string_|Required|
|__`width`__|_number_|Optional|
|__`height`__|_number_|Optional|
|__`rectangle`__|_Array<number>_|Optional|

__Example__
```python
unsplash.photos().get_photo(
    id='3PmwYw2uErY',
    width=500,
    height=500,
    rectangle=[0, 0, 200, 200]
)
```
---

### photos().get_photo_stats(id)
Retrieve a single photo's stats.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`id`__|_string_|Required|

__Example__
```python
unsplash.photos().get_photo_stats(
    id='3PmwYw2uErY'
)
```
---

### photos().get_random_photo(width, height, query, username, featured, collections)
Retrieve a single random photo, given optional filters.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|

|__`collections`__|_Array<number>_|Optional|
|__`featured`__|_boolean_|Optional|
|__`username`__|_string_|Optional|
|__`query`__|_string_|Optional|
|__`width`__|_number_|Optional|
|__`height`__|_number_|Optional|

__Example__
```python
unsplash.photos().get_random_photo(
    username='michael_hacker',
    width=500
)
```
---

### photos().upload_photo(photo)
Upload a photo on behalf of the logged-in user. This requires the `write_photos` scope.

Work in progress!

---

### photos().like_photo(id)
Like a photo on behalf of the logged-in user. This requires the `write_likes` scope.

Work in progress!

---

### photos().unlike_photo(id)
Remove a user’s like of a photo.

Work in progress!

---

<div id="collections" />

### collections().list_collections(page, per_page)
Get a single page from the list of all collections.

__Arguments__

| Argument | Type | Opt/Required |Notes|
|---|---|---|---|
|__`page`__|_number_|Optional||
|__`per_page`__|_number_|Optional||

__Example__
```python
list_collections = unsplash.collections().list_collections(
    page     = 1,
    per_page = 10,
    order_by = 'popular'
)
```
---

### collections().list_curated_collections(page, per_page)
Get a single page from the list of curated collections.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|

__Example__
```python
list_curated_collections = unsplash.collections().list_curated_collections(
    page     = 1,
    per_page = 10,
)
```
---

### collections().list_featured_collections(page, per_page)
Get a single page from the list of featured collections.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|

__Example__
```python
list_featured_collections = unsplash.collections().list_featured_collections(
    page     = 1,
    per_page = 10,
)
```
---

### collections().get_collection(id)
Retrieve a single collection. To view a user’s private collections, the `read_collections` scope is required.

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`id`__|_number_|Required|


__Example__
```python
collection = unsplas()h.collections().get_collection(
    id = 123456
)
```
---

### collections().get_curated_collection(id)
Or, for a curated collection:

__Arguments__

| Argument | Type | Opt/Required |
|---|---|---|
|__`id`__|_number_|Required|


__Example__
```python
curated_collection = unsplash().collections().get_curated_collection(
    id = 134
)
```
---

### collections().get_collection_photos(id, page, order_by)
Retrieve a collection’s photos.

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`id`__|_number_|Required||
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|


__Example__
```python
collection_photos = unsplash().collections().get_collection_photos(
    id       = 123456,
    page     = 1,
    per_page = 10
)
```
---

### collections().get_curated_collection_photos(id, page, order_by)
Or, for a curated collection:

__Arguments__

| Argument | Type | Opt/Required | Notes |
|---|---|---|---|
|__`id`__|_number_|Required||
|__`page`__|_number_|Optional|
|__`per_page`__|_number_|Optional|


__Example__
```python
unsplash().collections().get_curated_collection_photos(
    id       = 88,
    page     = 1,
    per_page = 10
)
```
---

### collections().create_collection(title, description, private)
Create a new collection. This requires the `write_collections` scope.

Work in progress!

---

### collections().update_collection(id, title, description, private)
Update an existing collection belonging to the logged-in user. This requires the `write_collections` scope.

Work in progress!

---

### collections().delete_collection(id)
Delete a collection belonging to the logged-in user. This requires the `write_collections` scope.

Work in progress!

---

### collections().add_photo_to_collection(collection_id, photo_id)
Add a photo to one of the logged-in user’s collections. Requires the `write_collections` scope.

Work in progress!

---

### collections().remove_photo_from_collection(collection_id, photo_id)
Remove a photo from one of the logged-in user’s collections. Requires the `write_collections` scope.

Work in progress!

---

<div id="search" />
