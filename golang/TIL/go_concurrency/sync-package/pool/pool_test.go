package pool

import (
	"io/ioutil"
	"net"
	"testing"
)

func Test_example1(t *testing.T) {
	example1()
}

func Test_memoryExample(t *testing.T) {
	memoryExample()
}

func init() {
	//daemonStarted := startNetworkDaemon()
	daemonStarted := startNetworkDaemonUsingPool()

	daemonStarted.Wait()
}

func BenchmarkNetworkRequest(b *testing.B) {
	for i := 0; i < b.N; i++ {
		conn, err := net.Dial("tcp", "localhost:8080")
		if err != nil {
			b.Fatalf("cannot dial host: %v", err)
		}

		if _, err = ioutil.ReadAll(conn); err != nil {
			b.Fatalf("cannot read: %v", err)
		}

		conn.Close()
	}
}
