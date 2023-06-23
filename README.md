# tinygo

```go
var a int64
a = 42

c := a + 1
c = c + 1

fmt.Println("Hello world!") // fmt module is already in the current scope

func f(x string) {
	a := 53
	fmt.Printf("x=%v, a=%v\n", x, a)
}

for i := 0; i < 10; i += 1 {
  f("zoo")
}
```
