// go is much faster at guessing the secret becauase it has better threading than python


package main

import (
	"fmt"
	"sync"
	"time"
)

// var secret string = "9384756230918273"
var secret string = "86753299189"
var halfLength int = len(secret) / 2
var aliceShare string = secret[:halfLength]
var bobShare string = secret[halfLength:]
var wg sync.WaitGroup
var done = make(chan bool)
var isSecretFound = false

func main() {
	fmt.Println("Alice's share: ", aliceShare)
	fmt.Println("Bob's share: ", bobShare)

	fmt.Println("Problem 1: Lack of Security")

	max := 1
	for i := 0; i < len(bobShare); i++ {
		max *= 10
	}

	start := time.Now()

	for i := 0; i < max; i++ {
		wg.Add(1)
		go tryKey(i)
		if isSecretFound {
			break
		}
	}

	go func() {
		wg.Wait()
		close(done)
	}()

	<-done

	duration := time.Since(start)
	fmt.Printf("Duration: %s\n", duration)
}

func tryKey(i int) {
	defer wg.Done()

	if isSecretFound {
		return
	}

	possibleShare := fmt.Sprintf("%0*d", len(bobShare), i)
	attempt := aliceShare + possibleShare
	if attempt == secret {
		fmt.Printf("Attacker has guessed the secret: %s\n", attempt)
		isSecretFound = true
	}
	if i%10000 == 0 {
		fmt.Printf("Trying %d...\n", i)
	}
}
