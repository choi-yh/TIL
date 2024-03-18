package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/elastic/go-elasticsearch/v8"
)

var (
	typedES *elasticsearch.TypedClient
	err     error
)

func main() {
	ctx := context.Background()

	config := elasticsearch.Config{
		Addresses:              []string{os.Getenv("ELASTIC_HOST")},
		Username:               os.Getenv("ELASTIC_USER"),
		Password:               os.Getenv("ELASTIC_PASSWORD"),
		CertificateFingerprint: "",
	}
	typedES, err = elasticsearch.NewTypedClient(config)
	if err != nil {
		panic(err)
	}

	resp, err := typedES.Search().Do(ctx)
	fmt.Println(resp, err)

	//_ = createIndex(ctx, "article")
}

func createIndex(ctx context.Context, index string) error {
	if !checkIndex(ctx, index) {
		return nil
	}

	_, err := typedES.Indices.Create(index).Do(ctx)
	if err != nil {
		return err
	}

	return nil
}

func checkIndex(ctx context.Context, index string) bool {
	res, err := typedES.Cat.Indices().Index(index).Do(ctx)
	if err != nil {
		log.Println(err)

		return false
	}

	if len(res) == 0 {
		return false
	}

	if *res[0].Index == index {
		return true
	}

	return false
}
