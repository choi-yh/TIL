package go_concurrency

import (
	"fmt"
	"sync"
	"testing"
	"time"
)

/*
레이스 컨디션의 대표적인 예시
 1. the value is 0.
 2. the value is 1. (if 문 진입시 고루틴에서 data 가 증가되어 출력됨)
 3. 아무 일도 일어나지 않음. (data == 1)
*/
func Test_RaceCondition(t *testing.T) {
	var data int

	go func() {
		data++
	}()

	if data == 0 {
		fmt.Printf("the value is %v. \n", data)
	}
}

func Test_RaceCondition_Sleep(t *testing.T) {
	var data int

	go func() {
		data++
	}()

	// sleep 으로 인해 괜찮아보인다고 생각하지만 오산이다.
	// 논리의 정확성을 추구하라.
	time.Sleep(time.Second)

	if data == 0 {
		fmt.Printf("the value is %v. \n", data)
	}
}

func Test_RaceCondition_Sync(t *testing.T) {
	var memoryAccess sync.Mutex
	var value int

	go func() {
		memoryAccess.Lock()
		value++
		memoryAccess.Unlock()
	}()

	memoryAccess.Lock()
	if value == 0 {
		fmt.Printf("the value is %v. \n", value)
	} else {
		fmt.Printf("the value is %v. \n", value)
	}
	memoryAccess.Unlock()
}
