.. image:: https://pypip.in/v/$REPO/badge.png
    :target: https://crate.io/packages/$REPO/
    :alt: Latest PyPI version

|Latest Version| |Build Status|

unsplash-python
===============

A unofficial Python client for the `Unsplash
API <https://unsplash.com/developers>`__.

Installation
------------

::

    $ pip install unsplash-python

Dependencies
------------

::

    $ pip install requests

Usage
-----

Creating an instance
~~~~~~~~~~~~~~~~~~~~

To create an instance, simply provide an *Object* with your
``application_id``, ``secret`` and ``callback_url``.

.. code:: python

    import unsplash

    unsplash = Unsplash({
        'application_id' : '{APP_ID}',
        'secret'         : '{APP_SECRET}',
        'callback_url'   : '{CALLBACK_URL}'
    })

===

User
~~~~

--------------

Instance Methods
----------------

-  `Authorization <https://github.com/michael-hacker/unsplash-python#authorization>`__
-  `Current
   User <https://github.com/michael-hacker/unsplash-python#current-user>`__
-  `Users <https://github.com/michael-hacker/unsplash-python#users>`__
-  `Photos <https://github.com/michael-hacker/unsplash-python#photos>`__
-  `Collections <https://github.com/michael-hacker/unsplash-python#collections>`__
-  `Search <https://github.com/michael-hacker/unsplash-python#searchallkeyword-page>`__
-  `Stats <https://github.com/michael-hacker/unsplash-python#stats>`__

.. raw:: html

   <div id="authorization" />

auth().get\_authentication\_url(scopes)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Build an OAuth url with requested scopes.

**Arguments**

+------------------+-----------+----------------+------------------+
| Argument         | Type      | Opt/Required   | Default          |
+==================+===========+================+==================+
| **``scopes``**   | *Array*   | Optional       | ``['public']``   |
+------------------+-----------+----------------+------------------+

**Example**

.. code:: python

    authentication_url = unsplash.auth().get_authentication_url([
        'public',
        'read_user',
        'write_user',
        'read_photos',
        'write_photos'
    ])

--------------

auth().user\_authentication(code)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a user's access token.

**Arguments**

+----------------+------------+----------------+
| Argument       | Type       | Opt/Required   |
+================+============+================+
| **``code``**   | *string*   | Required       |
+----------------+------------+----------------+

**Example**

.. code:: python

    access_token = unsplash.auth().user_authentication(code = '{OAUTH_CODE}')

--------------

.. raw:: html

   <div id="current-user" />

current\_user().profile()
~~~~~~~~~~~~~~~~~~~~~~~~~

Get the user’s profile.

**Arguments**

*N/A*

**Example**

.. code:: python

    current_user_profile = unsplash.current_user().profile()

--------------

current\_user().update\_profile(options)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update the current user’s profile.

**Arguments**

+------+------+------+------+
| Argu | Type | Opt/ | Note |
| ment |      | Requ | s    |
|      |      | ired |      |
+======+======+======+======+
| **`` | *Obj | Requ | Obje |
| opti | ect* | ired | ct   |
| ons` |      |      | with |
| `**  |      |      | the  |
|      |      |      | foll |
|      |      |      | owin |
|      |      |      | g    |
|      |      |      | opti |
|      |      |      | onal |
|      |      |      | keys |
|      |      |      | :    |
|      |      |      | ``us |
|      |      |      | erna |
|      |      |      | me`` |
|      |      |      | ,    |
|      |      |      | ``fi |
|      |      |      | rst_ |
|      |      |      | name |
|      |      |      | ``,  |
|      |      |      | ``la |
|      |      |      | st_n |
|      |      |      | ame` |
|      |      |      | `,   |
|      |      |      | ``em |
|      |      |      | ail` |
|      |      |      | `,   |
|      |      |      | ``ur |
|      |      |      | l``, |
|      |      |      | ``lo |
|      |      |      | cati |
|      |      |      | on`` |
|      |      |      | ,    |
|      |      |      | ``bi |
|      |      |      | o``, |
|      |      |      | ``in |
|      |      |      | stag |
|      |      |      | ram_ |
|      |      |      | user |
|      |      |      | name |
|      |      |      | ``   |
+------+------+------+------+

**Example**

.. code:: python

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

--------------

.. raw:: html

   <div id="users" />

users().profile(username)
~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve public details on a given user.

**Arguments**

+--------------------+------------+----------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+
| **``username``**   | *string*   | Required       |
+--------------------+------------+----------------+

**Example**

.. code:: python

    users_profile = unsplash.users().profile(
        username = 'michael_hacker'
    )

--------------

users().photos(username, page, per\_page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of photos uploaded by a user.

**Arguments**

+--------------------+------------+----------------+-----------------------------------------+
| Argument           | Type       | Opt/Required   | Notes                                   |
+====================+============+================+=========================================+
| **``username``**   | *string*   | Required       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``page``**       | *number*   | Optional       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``per_page``**   | *number*   | Optional       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``order_by``**   | *string*   | Optional       | ``latest``, ``popular`` or ``oldest``   |
+--------------------+------------+----------------+-----------------------------------------+

**Example**

.. code:: python

    users_photos = unsplash.users().photos(
        username = 'naoufal',
        order_by = 'popular'
    )

--------------

users().likes(username, page, per\_page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of photos liked by a user.

**Arguments**

+--------------------+------------+----------------+-----------------------------------------+
| Argument           | Type       | Opt/Required   | Notes                                   |
+====================+============+================+=========================================+
| **``username``**   | *string*   | Required       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``page``**       | *number*   | Optional       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``per_page``**   | *number*   | Optional       |                                         |
+--------------------+------------+----------------+-----------------------------------------+
| **``order_by``**   | *string*   | Optional       | ``latest``, ``popular`` or ``oldest``   |
+--------------------+------------+----------------+-----------------------------------------+

**Example**

.. code:: python

    users_likes = unsplash.users().likes(
        username = 'naoufal',
        page     = 2,
        per_page = 15,
        order_by = 'popular'
    )

--------------

users().collections(username, page, per\_page)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a list of collections created by the user.

**Arguments**

+--------------------+------------+----------------+---------+
| Argument           | Type       | Opt/Required   | Notes   |
+====================+============+================+=========+
| **``username``**   | *string*   | Required       |         |
+--------------------+------------+----------------+---------+
| **``page``**       | *number*   | Optional       |         |
+--------------------+------------+----------------+---------+
| **``per_page``**   | *number*   | Optional       |         |
+--------------------+------------+----------------+---------+

**Example**

.. code:: python

    users_collections = unsplash.users().collections(
        username = 'naoufal',
        page     = 2,
        per_page = 15
    )

--------------

.. raw:: html

   <div id="photos" />

photos().list\_photos(page, per\_page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from the list of all photos.

**Arguments**

+--------------------+------------+----------------+-----------------------------------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+=========================================+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+-----------------------------------------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+-----------------------------------------+
| **``order_by``**   | *string*   | Optional       | ``latest``, ``popular`` or ``oldest``   |
+--------------------+------------+----------------+-----------------------------------------+

**Example**

.. code:: python

    photos = unsplash.photos().list_photos(
        page     = 2,
        per_page = 15,
        order_by = 'popular'
    )

--------------

photos().list\_curated\_photos(page, per\_page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from the list of the curated photos.

**Arguments**

+--------------------+------------+----------------+-----------------------------------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+=========================================+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+-----------------------------------------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+-----------------------------------------+
| **``order_by``**   | *string*   | Optional       | ``latest``, ``popular`` or ``oldest``   |
+--------------------+------------+----------------+-----------------------------------------+

**Example**

.. code:: python

    curated_photos = unsplash.photos().list_curated_photos(
        page     = 2,
        per_page = 15,
        order_by = 'popular'
    )

--------------

photos().search\_photos(query, category, page, per\_page)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from a photo search. Optionally limit your search to a
set of categories by supplying the category ID’s.

**Arguments**

+--------------------+------------+----------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+
| **``query``**      | *string*   | Optional       |
+--------------------+------------+----------------+
| **``category``**   | *Array*    | Optional       |
+--------------------+------------+----------------+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+

**Example**

.. code:: python

    photos = unsplash.photos().search_photos(
        query    = 'cats',
        category = [11, 88],
        page     = 1
        per_page = 15
    )

--------------

photos().get\_photo(id, width, height, rectangle)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a single photo.

**Arguments**

+---------------------+------------+----------------+
| Argument            | Type       | Opt/Required   |
+=====================+============+================+
| **``id``**          | *string*   | Required       |
+---------------------+------------+----------------+
| **``width``**       | *number*   | Optional       |
+---------------------+------------+----------------+
| **``height``**      | *number*   | Optional       |
+---------------------+------------+----------------+
| **``rectangle``**   | *Array*    | Optional       |
+---------------------+------------+----------------+

**Example**

.. code:: python

    photo = unsplash.photos().get_photo(
        id        = '6r1_ZnnI5m8',
        width     = 500,
        height    = 500,
        rectangle = [0, 0, 200, 200]
    )

--------------

photos().get\_photo\_stats(id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a single photo's stats.

**Arguments**

+--------------+------------+----------------+
| Argument     | Type       | Opt/Required   |
+==============+============+================+
| **``id``**   | *string*   | Required       |
+--------------+------------+----------------+

**Example**

.. code:: python

    photo_stats = unsplash.photos().get_photo_stats(
        id = '6r1_ZnnI5m8'
    )

--------------

photos().get\_random\_photo(width, height, query, username, featured, collections)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a single random photo, given optional filters.

**Arguments**

+-----------------------+-------------+----------------+
| Argument              | Type        | Opt/Required   |
+=======================+=============+================+
| **``width``**         | *number*    | Optional       |
+-----------------------+-------------+----------------+
| **``height``**        | *number*    | Optional       |
+-----------------------+-------------+----------------+
| **``query``**         | *string*    | Optional       |
+-----------------------+-------------+----------------+
| **``username``**      | *string*    | Optional       |
+-----------------------+-------------+----------------+
| **``featured``**      | *boolean*   | Optional       |
+-----------------------+-------------+----------------+
| **``collections``**   | *Array*     | Optional       |
+-----------------------+-------------+----------------+

**Example**

.. code:: python

    random_photo = unsplash.photos().get_random_photo(
        width    = 500,
        height   = 500,
        username = 'michael_hacker'
    )

--------------

photos().upload\_photo(photo)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload a photo on behalf of the logged-in user. This requires the
``write_photos`` scope.

Work in progress!

--------------

photos().like\_photo(id)
~~~~~~~~~~~~~~~~~~~~~~~~

Like a photo on behalf of the logged-in user. This requires the
``write_likes`` scope.

Work in progress!

--------------

photos().unlike\_photo(id)
~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove a user’s like of a photo.

Work in progress!

--------------

.. raw:: html

   <div id="collections" />

collections().list\_collections(page, per\_page)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from the list of all collections.

**Arguments**

+--------------------+------------+----------------+---------+
| Argument           | Type       | Opt/Required   | Notes   |
+====================+============+================+=========+
| **``page``**       | *number*   | Optional       |         |
+--------------------+------------+----------------+---------+
| **``per_page``**   | *number*   | Optional       |         |
+--------------------+------------+----------------+---------+

**Example**

.. code:: python

    list_collections = unsplash.collections().list_collections(
        page     = 1,
        per_page = 10,
        order_by = 'popular'
    )

--------------

collections().list\_curated\_collections(page, per\_page)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from the list of curated collections.

**Arguments**

+--------------------+------------+----------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+

**Example**

.. code:: python

    list_curated_collections = unsplash.collections().list_curated_collections(
        page     = 1,
        per_page = 10,
    )

--------------

collections().list\_featured\_collections(page, per\_page)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get a single page from the list of featured collections.

**Arguments**

+--------------------+------------+----------------+
| Argument           | Type       | Opt/Required   |
+====================+============+================+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+

**Example**

.. code:: python

    list_featured_collections = unsplash.collections().list_featured_collections(
        page     = 1,
        per_page = 10,
    )

--------------

collections().get\_collection(id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a single collection. To view a user’s private collections, the
``read_collections`` scope is required.

**Arguments**

+--------------+------------+----------------+
| Argument     | Type       | Opt/Required   |
+==============+============+================+
| **``id``**   | *number*   | Required       |
+--------------+------------+----------------+

**Example**

.. code:: python

    collection = unsplas()h.collections().get_collection(
        id = 123456
    )

--------------

collections().get\_curated\_collection(id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Or, for a curated collection:

**Arguments**

+--------------+------------+----------------+
| Argument     | Type       | Opt/Required   |
+==============+============+================+
| **``id``**   | *number*   | Required       |
+--------------+------------+----------------+

**Example**

.. code:: python

    curated_collection = unsplash().collections().get_curated_collection(
        id = 134
    )

--------------

collections().get\_collection\_photos(id, page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Retrieve a collection’s photos.

**Arguments**

+--------------------+------------+----------------+---------+
| Argument           | Type       | Opt/Required   | Notes   |
+====================+============+================+=========+
| **``id``**         | *number*   | Required       |         |
+--------------------+------------+----------------+---------+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+---------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+---------+

**Example**

.. code:: python

    collection_photos = unsplash().collections().get_collection_photos(
        id       = 123456,
        page     = 1,
        per_page = 10
    )

--------------

collections().get\_curated\_collection\_photos(id, page, order\_by)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Or, for a curated collection:

**Arguments**

+--------------------+------------+----------------+---------+
| Argument           | Type       | Opt/Required   | Notes   |
+====================+============+================+=========+
| **``id``**         | *number*   | Required       |         |
+--------------------+------------+----------------+---------+
| **``page``**       | *number*   | Optional       |
+--------------------+------------+----------------+---------+
| **``per_page``**   | *number*   | Optional       |
+--------------------+------------+----------------+---------+

**Example**

.. code:: python

    unsplash().collections().get_curated_collection_photos(
        id       = 88,
        page     = 1,
        per_page = 10
    )

--------------

collections().create\_collection(title, description, private)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a new collection. This requires the ``write_collections`` scope.

Work in progress!

--------------

collections().update\_collection(id, title, description, private)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Update an existing collection belonging to the logged-in user. This
requires the ``write_collections`` scope.

Work in progress!

--------------

collections().delete\_collection(id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Delete a collection belonging to the logged-in user. This requires the
``write_collections`` scope.

Work in progress!

--------------

collections().add\_photo\_to\_collection(collection\_id, photo\_id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Add a photo to one of the logged-in user’s collections. Requires the
``write_collections`` scope.

Work in progress!

--------------

collections().remove\_photo\_from\_collection(collection\_id, photo\_id)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Remove a photo from one of the logged-in user’s collections. Requires
the ``write_collections`` scope.

Work in progress!

--------------

.. raw:: html

   <div id="search" />

.. |Latest Version| image:: https://pypip.in/version/unsplash-python/badge.svg
   :target: https://pypi.python.org/pypi/unsplash-python/
.. |Build Status| image:: https://travis-ci.org/michael-hacker/unsplash-python.svg?branch=master
   :target: https://travis-ci.org/michael-hacker/unsplash-python
