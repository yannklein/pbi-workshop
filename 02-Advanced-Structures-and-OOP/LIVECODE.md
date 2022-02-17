# Livecode

Let's model a [Multimedia Library](https://www.google.com/search?q=multimedia+library). Here are our hypothesis:

The library contains **4 types of media**:

- **BOOKS**
- **MOVIES**
- **CDS**
- **COMICS**

The library has a storage software allowing a few basic actions:

- To add a new media
- To borrow a media
- To return a media

The library use a dictionary to store its medias and an `interface` function allows to perform the actions.

Try to use functions for atomic actions, it's best practice.

Optional:

_Note: Some of those options can imply a change in the functions' signatures and other data structures._

- Handle the quantity of objects
- Associate a borrow to an user
- Specify a date of retrieval and fines on returns

## Scenarios

```python
# Library's storage
medias = {'BOOKS': {}, 'MOVIES': {'SW - Empire strikes back': True}, 'CDS': {}, 'COMICS': {}}

# Can add a new media
interface(medias, 'add', 'Harry Potter 1', 'BOOKS')
# => "Add completed"
# If the media type exists, else a message should be printed
interface(medias, 'add', 'Harry Potter 1', 'MANGAS')
# => "We do not have any MANGAS."

# Can borrow a media
interface(medias, 'borrow', 'Harry Potter 1', 'BOOKS')
# => "Borrow completed"
# If the media type exists, the title exists and is not already borrowed else a message should be printed
interface(medias, 'borrow', 'Harry Potter 1', 'BOOKS')
# => "The BOOK is already borrowed."
interface(medias, 'borrow', 'Harry Potter 2', 'BOOKS')
# => "The BOOKS you're looking for is not in our BOOKS."

# Can return a media
interface(medias, 'return', 'Harry Potter 1', 'BOOKS')
# => "Return completed"
# If the media type exists, the title exists and is borrowed else a message should be printed
interface(medias, 'return', 'Harry Potter 1', 'BOOKS')
# => "The BOOK was not borrowed."

```

## Solution

Please do not peek _before_ the livecode session!

<details><summary markdown='span'>View solution
</summary>

```python
def add(bib, title, media_type):
    if media_type in bib:
        bib[media_type][title] = True
        return 1
    else:
        return 2

def handle_media(bib, title, media_type, back=False):
    # Can split 2 functions (return_media and borrow_media)
    if media_type in bib:
        if title in bib[media_type]:
            if (bib[media_type][title] and not back) or (not bib[media_type][title] and back):
                bib[media_type][title] = back
                return 1
            elif back:
                return 5
            else:
                return 4
        else:
            return 3
    else:
        return 2

def interface(bib, action, title, media_type):
    # Occasion to use higher order functions
    if action == 'add':
        code = add(bib, title, media_type)
    elif action == 'borrow':
        code = handle_media(bib, title, media_type)
    elif action == 'return':
        code = handle_media(bib, title, media_type, True)
    else:
        print("The action entered doesn't exist.")

    # Occasion to use dict as switch
    if code == 1:
        print(f"{action.capitalize()} completed")
    elif code == 2:
        print(f"We do not have any {media_type.lower()}.")
    elif code == 3:
        print(f"The {media_type[:-1].lower()} you're looking for is not in our {media_type.lower()}.")
    elif code == 4:
        print(f'The {media_type[:-1].lower()} is already borrowed.')
    elif code == 5:
        print(f'The {media_type[:-1].lower()} was not borrowed.')

```

</details>
