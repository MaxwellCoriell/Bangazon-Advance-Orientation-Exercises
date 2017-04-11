# Orientation Exercises For Python
This is a suggested order for completing the exercises in orientation:

## Advanced exercises
1. [Advanced Challenge: Matching Makes and Models](./cars.py)
1. Persist data with a [Bag of Loot](./bag-of-loot/)
1. Persist data with a [Mary Margaret](./memories/)

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Advanced Challenge: Matching Makes & Models

## Setup

```
mkdir -p ~/workspace/python/exercises/car-challenge && cd $_
touch cars.py
```

Place the following code into **cars.py**.

```
makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7), 
  (2, 1), (2, 3), (2, 7), 
  (3, 2), (3, 3), (3, 7), 
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8), 
  (6, 2), (6, 6), (6, 7), 
  (7, 1), (7, 3), (7, 7), 
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7), 
  (10, 2), (10, 5), (10, 7), 
  (11, 3), (11, 6), (11, 8), 
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8), 
  (14, 2), (14, 5), (14, 8), 
  (15, 1), (15, 4), (15, 7)
)
```

## Overview

This is an advanced challenge because it requires multiple layers of iteration. It is also an introduction to database relationships because there are four unique collections that are all related to each other.

In the `makes` and `colors` collections, each item has a numeric identifier, and then a string representation.

##### Example

```
(1, "Toyota")
```

In the `models` collection, each item also has a numeric identifier, but also stores the numeric identifier of a model

##### Example

```
(5, "Prius", 1)
# 5 is the numeric identifier for a Prius
# 1 is the numeric identifier to a foreign collection item... Toyota
```

Finally, the `available_car_colors` collection is storing the relationships between items in two foreign collections. The first number represents the corresponding model, and the second number represents the corresponding color.

##### Example
```
(1, 7)
# This represents a relationship between "Altima" and "White"
```

## Instructions

### Part I: Reporting Object

You must first build a new dictionary that follows the format below. 

1. Each key in the dictionary should be the name of a make, and its value will be a dictionary.
1. The keys in the make dictionary will be the models, and the value will be a list of colors in which that the model is available.

```
{
    'Toyota': {
      'Prius': ['Charcoal', 'Brick', 'Ivory'],
      'Camry': ['Black', 'Red', 'White']
    },
    'Nissan': {
      'Sentra': ['Charcoal', 'Blue', 'Ivory'], 
      'Altima': ['Black', 'Charcoal', 'White'], 
      'Xterra': ['Charcoal', 'Navy', 'Ivory']
    },
    'Mini': {
      'Countryman': ['Charcoal', 'Navy', 'White'],
      'Cooper': ['Red', 'Navy', 'Ivory']
    }, 
    'Ford': {
      'F150': ['Black', 'Blue', 'Ivory'],
      'Thunderbird': ['Black', 'Red', 'White']
    }, 
    'Honda': {
      'Civic': ['Black', 'Navy', 'White'], 
      'Pilot': ['Black', 'Brick', 'White'], 
      'Accord': ['Red', 'Blue', 'Ivory']
    }, 
    'Dodge': {
      'Ram': ['Charcoal', 'Blue', 'White'], 
      'Charger': ['Black', 'Brick', 'White'], 
      'Dart': ['Charcoal', 'Red', 'White']
    }
}
```

### Part II - Command Line Report

Output a report on the command line that looks like this.

```
Ford
------------------
F150 available in Black, Blue, Ivory
Thunderbird available in Black, Red, White

etc...
```

# Black Hat Hacker Challenge

Rewrite your nested `for` loops as nested comprehensions.

|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---

# Bag o' Loot

This exercises will help with your comprehension of [command line parameters](http://www.pythonforbeginners.com/argv/more-fun-with-sys-argv).

## Setup

```
mkdir -p ~/workspace/python/exercises/cli && cd $_
touch lootbag.py
```

## Instructions

You have an acquaintance whose job is to, once a year, delivery presents to the best kids around the world. They have a problem, though. There are so many good boys and girls in the world now, that their old paper accounting systems just don't cut it anymore. They want you to write a program that will let them do the following tasks.

1. Add a toy to the bag o' loot, and label it with the child's name who will receive it. The first argument must be the word `add`. The second argument is the gift to be delivered. The third argument is the name of the child.

    ```bash
    python lootbag.py add kite suzy
    python lootbag.py add baseball michael
    ```

1. Remove a toy from the bag o' loot in case a child's status changes before delivery starts.

    ```bash
    python lootbag.py remove suzy kite
    python lootbag.py remove michael baseball
    ```

1. Produce a list of children currently receiving presents.

    ```bash
    python lootbag.py ls
    ```

1. List toys in the bag o' loot for a specific child.

    ```bash
    python lootbag.py ls suzy
    ```

1. Specify when a child's toys have been delivered.

    ```bash
    python lootbag.py delivered suzy
    ```


## Requirements

**Write a test before you write implementation code**

```python
# This is only an example. If I find this code in your project
#  I will make you go back and delete it and write your own test.
def test_toys_for_child_can_be_added_to_bag ()
{
    lootBag = Bag()
    lootBag.add_toy_for_child("kite", "suzy");
    self.assertEqual("kite", lootBag.child_items("suzy")[0]);
}
```

1. Items can be added to bag, and assigned to a child.
1. Items can be removed from bag, per child. Removing `ball` from the bag should not be allowed. A child's name must be specified.
1. Must be able to list all children who are getting a toy.
1. Must be able to list all toys for a given child's name.
1. Must be able to set the *delivered* property of a child, which defaults to `false` to `true`.

## Bonus Features

1. Write a response for the argument `python lootbag.py help` that lists all of the possible arguments, and what they do.
1. Create a shortcut combination of arguments that can remove *all* toys from the bag for a child who has been deemed naughty.




|----|----|----|----|----|----|----|----|----|----|----|----|----|----|----|---
# Mary Margaret

In this exercise, you're going to use object serialization to allow two distinct Python modules pass a dictionary back and forth, while they are running independently of each other.

You will execute each module seperately, and each one will augment a dictionary, and then serialize it to a file.

## Setup

```
mkdir -p ~/workspace/python/exercises/memories && cd $_
touch mary.py
touch margaret.py
```

## Requirements

1. Create a `mary.py` module that contains a `Mary` class.
1. Create a `margaret.py` module that contains a `Margaret` class.
1. Each module must accept one command line argument that is a message to add to a list *(see example below)*.
1. Each module must be able to serialize a dictionary to a file named `messages`.
1. Each module must be able to deserialize the dictionary stored in `messages`.
1. Each module, after the object is deserialized from the file, must add the message to the appropriate list in the dictionary.
1. Each module must [handle exceptions](../FND_10_EXCEPTION_HANDLING.md) properly. You may encounter the following while testing your logic.
    1. `FileNotFoundError`
    1. `EOFError`
    1. `KeyError`

> **Tip:** Make sure you import `sys` for the command line arguments, and `pickle` for serialization.


###### Dictionary structure

```python
{
    "Mary": ["Hi, I'm Mary", "I like jet planes"],
    "Margaret": ["Hi, I'm Margaret", "I like cookies"]
}
```

###### Command line syntax

```bash
python mary.py "Hi, I'm Mary"
```








