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
