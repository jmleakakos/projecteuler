I run most of my programs directly through `ghci`, although I am putting a `main` in each file. This will let you compile the file easily, which will make all of the problems run faster. Some of the problems will need to be compiled to get an answer in a reasonable amount of time.

```
$ ghci
Prelude> :l 001.hs
*main> main
233168
```

```
$ ghc 001.hs
$ ./001
233168
```

Packages (install with `cabal install primes`)
* primes
* hunit
