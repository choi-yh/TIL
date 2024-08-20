package go_concurrency

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

func Test_GenerateDeadlock(t *testing.T) {
	type value struct {
		mu    sync.Mutex
		value int
	}

	var wg sync.WaitGroup
	printSum := func(v1, v2 *value) {
		defer wg.Done()
		v1.mu.Lock()
		defer v1.mu.Unlock()

		time.Sleep(2 * time.Second)

		v2.mu.Lock()
		defer v2.mu.Unlock()

		fmt.Printf("sum = %v\n", v1.value+v2.value)
	}

	var a, b value
	wg.Add(2)
	go printSum(&a, &b) // a를 잠그고 b를 대기
	go printSum(&b, &a) // b를 잠그고 a를 대기
	wg.Wait()
}
