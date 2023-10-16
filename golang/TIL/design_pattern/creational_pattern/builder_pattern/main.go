package main

import (
	"context"

	"github.com/elastic/go-elasticsearch/v8"
	"github.com/elastic/go-elasticsearch/v8/typedapi/core/search"
	"github.com/elastic/go-elasticsearch/v8/typedapi/types"
	"google.golang.org/appengine/log"
)

func main() {
	ctx := context.Background()

	es8, _ := elasticsearch.NewTypedClient(elasticsearch.Config{})

	query := types.NewQuery()
	query.MatchAll = types.NewMatchAllQuery()

	// builder pattern 으로 구현
	resp, err := es8.Search().
		Index("my_index").
		Request(&search.Request{
			Query: query,
		}).
		Do(ctx)
	if err != nil {
		log.Errorf(ctx, "search query error = %v", err.Error())
	}

	log.Debugf(ctx, "search response = %v", resp)
}
