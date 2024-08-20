package go_concurrency

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

// 기아 상태: 어떤 동시 프로세스가 작업을 수행하는데 필요한 모든 리소스를 얻을 수 없는 모든 상황
func Test_Starvation(t *testing.T) {
	var wg sync.WaitGroup
	var sharedLock sync.Mutex
	const runtime = time.Second

	greedyWorker := func() {
		defer wg.Done()

		var count int
		for begin := time.Now(); time.Since(begin) < runtime; {
			sharedLock.Lock()
			time.Sleep(3 * time.Nanosecond) // 불필요하게 임계 영역을 오래 가지고 있기 때문에 기아 상태 발생 가능
			sharedLock.Unlock()
			count++
		}

		fmt.Printf("Greedy worker was able to execute %v work loops\n", count)
	}

	politeWorker := func() {
		defer wg.Done()

		var count int
		for begin := time.Now(); time.Since(begin) < runtime; {
			sharedLock.Lock()
			time.Sleep(1 * time.Nanosecond)
			sharedLock.Unlock()

			sharedLock.Lock()
			time.Sleep(1 * time.Nanosecond)
			sharedLock.Unlock()

			sharedLock.Lock()
			time.Sleep(1 * time.Nanosecond)
			sharedLock.Unlock()

			count++
		}

		fmt.Printf("Polite worker was able to execute %v work loops\n", count)
	}

	wg.Add(2)
	go greedyWorker()
	go politeWorker()

	wg.Wait()
}
