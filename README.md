## TL;DR

 This is a really very limited Item Store (*no payment method accepted*)

This project aim to be a programming exercise made in a very little free time, providing a first basic solution to

https://github.com/xpeppers/sales-taxes-problem

In spite of what the previous link advice
>You may use whatever programming language/platform you prefer. Use something that you know well

I started this development with a language I did not know before a week ago:
**python!!**

I did it for several reason,
### How To

```
> python repository/consolepurchaseclient.py "all*"
```
or single purchase input
```
python repository/consolepurchaseclient.py "user_input1*"
```

### Software Domain
* Client - sh console user
* Item - to purchase (e.g imported book, national food, ...)
* Origin - of Item (national, imported)
* Type - of Item (category like book, food, ...)
* Store - where a Client can purchase a set of items
* Tax handler - handling taxes strategies related to the Store
* Tax strategy - real tax behaviour (basic, imported, ...)
* Repository - a csv repository containing items to sell into store

### Roadmap
* A good purchase receipt as requested (actually just few raw data are printed)
* Better DDD
* Deeper OOP/SOLID principles
* Externalize every configurable aspect via Dep Inj.
* a mocked payment method ;)
* Better unit test coverage
* (2) point of the next quote


> 1. First, you write the software to prove to yourself (or a client) that the solution is possible. Others may not recognize that this is just a proof-of-concept, but you do.
2. The second time, you make it work.
3. The third time, you make it work right.
